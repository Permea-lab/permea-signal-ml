"""Run existing baseline models under a leakage-aware split manifest.

This script writes sensitivity outputs only. It does not overwrite canonical
random-stratified benchmark outputs.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.eval.metrics import compute_binary_metrics
from permea_signal_ml.models.baselines import build_baseline_model


FEATURE_COLUMNS = ["length", "charge", "gravy", "pI", "aromaticity"]
MODEL_CONFIG_PATHS = {
    "dummy": "configs/models/dummy.yaml",
    "logistic_regression": "configs/models/logistic_regression.yaml",
    "random_forest": "configs/models/random_forest.yaml",
}
SPLIT_POLICY = "leakage_aware_group_stratified"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run existing baseline models under leakage-aware split manifest."
    )
    parser.add_argument(
        "--input",
        default="data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv",
        help="Input dataset CSV path.",
    )
    parser.add_argument(
        "--split-manifest",
        default="results/sensitivity/combined_group_stratified_split_manifest.csv",
        help="Leakage-aware split manifest CSV path.",
    )
    parser.add_argument("--output-dir", default="results/sensitivity")
    return parser.parse_args()


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML config file."""
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_inputs(
    dataset: pd.DataFrame,
    split_manifest: pd.DataFrame,
    label_col: str = "label",
    sequence_id_col: str = "sequence_id",
) -> pd.DataFrame:
    """Validate dataset/manifest alignment and return merged frame."""
    required_dataset = set(FEATURE_COLUMNS + [label_col, sequence_id_col])
    missing_dataset = sorted(required_dataset - set(dataset.columns))
    if missing_dataset:
        raise ValueError(f"Missing dataset columns: {missing_dataset}")

    required_manifest = {"row_index", sequence_id_col, "label", "group_id", "fold_id", "split_policy"}
    missing_manifest = sorted(required_manifest - set(split_manifest.columns))
    if missing_manifest:
        raise ValueError(f"Missing split manifest columns: {missing_manifest}")
    if split_manifest["row_index"].duplicated().any():
        raise ValueError("Split manifest contains duplicate row_index values")

    indexed = dataset.reset_index(drop=True).reset_index().rename(columns={"index": "row_index"})
    merged = split_manifest.merge(
        indexed[["row_index", sequence_id_col, label_col] + FEATURE_COLUMNS],
        on="row_index",
        how="left",
        suffixes=("_manifest", "_dataset"),
        validate="one_to_one",
    )
    if len(merged) != len(dataset):
        raise ValueError("Split manifest row count does not match dataset row count")
    if merged[FEATURE_COLUMNS + [f"{label_col}_dataset"]].isna().any().any():
        raise ValueError("Missing dataset values after joining split manifest")
    if not (merged[f"{sequence_id_col}_manifest"] == merged[f"{sequence_id_col}_dataset"]).all():
        raise ValueError("Sequence IDs do not align between dataset and split manifest")
    if not (merged[f"{label_col}_manifest"].astype(int) == merged[f"{label_col}_dataset"].astype(int)).all():
        raise ValueError("Labels do not align between dataset and split manifest")
    if split_manifest.groupby("group_id")["fold_id"].nunique().max() > 1:
        raise ValueError("At least one group crosses folds in the split manifest")
    return merged.rename(
        columns={
            f"{sequence_id_col}_dataset": sequence_id_col,
            f"{label_col}_dataset": label_col,
        }
    )


def get_binary_predictions(model: object, x_test: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Return predicted labels and positive-class scores."""
    if hasattr(model, "predict_proba"):
        scores = model.predict_proba(x_test)[:, 1]
    elif hasattr(model, "decision_function"):
        import numpy as np

        raw_scores = np.asarray(model.decision_function(x_test), dtype=float)
        scores = 1.0 / (1.0 + np.exp(-raw_scores))
    else:
        scores = model.predict(x_test)

    score_series = pd.Series(scores, index=x_test.index, dtype=float)
    predicted = (score_series >= 0.5).astype(int)
    return predicted, score_series


def _mean(values: list[float]) -> float:
    valid = [value for value in values if not math.isnan(value)]
    return float(sum(valid) / len(valid)) if valid else math.nan


def _std(values: list[float]) -> float:
    valid = [value for value in values if not math.isnan(value)]
    if len(valid) <= 1:
        return 0.0
    mean = _mean(valid)
    variance = sum((value - mean) ** 2 for value in valid) / (len(valid) - 1)
    return float(math.sqrt(variance))


def summarize_model_metrics(model_name: str, fold_metrics: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate per-fold metrics for one model."""
    metric_names = ["roc_auc", "pr_auc", "precision", "recall", "f1", "mcc"]
    summary: dict[str, Any] = {
        "model": model_name,
        "split_policy": SPLIT_POLICY,
        "folds": int(len(fold_metrics)),
    }
    for metric_name in metric_names:
        values = [float(row[metric_name]) for row in fold_metrics]
        summary[metric_name] = _mean(values)
        summary[f"{metric_name}_std"] = _std(values)
    summary["test_rows_total"] = int(sum(int(row["test_rows"]) for row in fold_metrics))
    summary["test_positive_total"] = int(sum(int(row["test_positives"]) for row in fold_metrics))
    summary["test_negative_total"] = int(sum(int(row["test_negatives"]) for row in fold_metrics))
    return summary


def run_leakage_aware_baselines(
    input_path: str | Path,
    split_manifest_path: str | Path,
    output_dir: str | Path,
) -> dict[str, Any]:
    """Run existing baseline model families under manifest-defined folds."""
    dataset = pd.read_csv(input_path)
    split_manifest = pd.read_csv(split_manifest_path)
    merged = validate_inputs(dataset, split_manifest)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    per_fold_rows: list[dict[str, Any]] = []
    prediction_rows: list[pd.DataFrame] = []
    summary_rows: list[dict[str, Any]] = []

    labels = merged["label"].astype(int)
    features = merged[FEATURE_COLUMNS].copy()
    folds = sorted(int(fold_id) for fold_id in merged["fold_id"].unique())

    for model_name, config_path in MODEL_CONFIG_PATHS.items():
        model_config = load_yaml(ROOT / config_path)
        fold_metrics: list[dict[str, Any]] = []
        for fold_id in folds:
            test_mask = merged["fold_id"].astype(int) == fold_id
            train_mask = ~test_mask
            x_train = features.loc[train_mask]
            x_test = features.loc[test_mask]
            y_train = labels.loc[train_mask]
            y_test = labels.loc[test_mask]

            model = build_baseline_model(model_config)
            model.fit(x_train, y_train)
            predicted_label, predicted_score = get_binary_predictions(model, x_test)
            metrics = compute_binary_metrics(y_test, predicted_label, predicted_score)
            fold_row = {
                "model": model_name,
                "fold_id": int(fold_id),
                "split_policy": SPLIT_POLICY,
                "test_rows": int(len(y_test)),
                "test_positives": int((y_test == 1).sum()),
                "test_negatives": int((y_test == 0).sum()),
                **metrics,
            }
            fold_metrics.append(fold_row)
            per_fold_rows.append(fold_row)
            prediction_rows.append(
                pd.DataFrame(
                    {
                        "model": model_name,
                        "sequence_id": merged.loc[test_mask, "sequence_id"].values,
                        "true_label": y_test.values,
                        "predicted_label": predicted_label.values,
                        "predicted_score": predicted_score.values,
                        "fold_id": int(fold_id),
                        "split_policy": SPLIT_POLICY,
                    }
                )
            )
        summary_rows.append(summarize_model_metrics(model_name, fold_metrics))

    summary = pd.DataFrame(summary_rows)
    per_fold = pd.DataFrame(per_fold_rows)
    predictions = pd.concat(prediction_rows, ignore_index=True)

    summary_path = output_path / "leakage_aware_model_comparison_summary.csv"
    per_fold_path = output_path / "leakage_aware_model_comparison_per_fold.csv"
    predictions_path = output_path / "leakage_aware_predictions.csv"
    json_path = output_path / "leakage_aware_metrics_summary.json"

    summary.to_csv(summary_path, index=False)
    per_fold.to_csv(per_fold_path, index=False)
    predictions.to_csv(predictions_path, index=False)

    payload = {
        "input_path": str(input_path),
        "split_manifest_path": str(split_manifest_path),
        "split_policy": SPLIT_POLICY,
        "feature_columns": FEATURE_COLUMNS,
        "model_families": list(MODEL_CONFIG_PATHS.keys()),
        "metrics": ["roc_auc", "pr_auc", "precision", "recall", "f1", "mcc"],
        "summary": summary.to_dict(orient="records"),
        "outputs_written": [str(summary_path), str(per_fold_path), str(predictions_path), str(json_path)],
        "caveats": [
            "Sensitivity rerun only; not biological validation or wet-lab validation.",
            "Uses committed leakage-aware group-stratified split manifest.",
            "Does not update manuscript claims or canonical random-stratified metrics.",
        ],
    }
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    return payload


def main() -> None:
    """Run leakage-aware baseline sensitivity analysis."""
    args = parse_args()
    payload = run_leakage_aware_baselines(
        input_path=args.input,
        split_manifest_path=args.split_manifest,
        output_dir=args.output_dir,
    )
    print(json.dumps({"status": "ok", "outputs_written": payload["outputs_written"]}, indent=2))


if __name__ == "__main__":
    main()
