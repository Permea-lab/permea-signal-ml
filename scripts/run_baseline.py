"""Run a minimal baseline benchmark workflow.

Example:
python scripts/run_baseline.py \
  --data-config configs/data/default.yaml \
  --feature-config configs/features/physicochemical.yaml \
  --model-config configs/models/random_forest.yaml \
  --eval-config configs/eval/default.yaml \
  --output-prefix smoke_test_rf
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from sklearn.model_selection import StratifiedKFold

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.data.load import load_table
from permea_signal_ml.data.validate import validate_binary_labels, validate_required_columns
from permea_signal_ml.eval.metrics import aggregate_metrics, compute_binary_metrics
from permea_signal_ml.eval.plots import save_score_distribution_figure
from permea_signal_ml.eval.ranking import rank_candidates
from permea_signal_ml.features.basic import add_basic_features
from permea_signal_ml.features.physicochemical import add_physicochemical_features
from permea_signal_ml.models.baselines import build_baseline_model
from permea_signal_ml.provenance.manifest import RunManifest


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run a minimal baseline benchmark.")
    parser.add_argument("--data-config", required=True)
    parser.add_argument("--feature-config", required=True)
    parser.add_argument("--model-config", required=True)
    parser.add_argument("--eval-config", required=True)
    parser.add_argument("--output-prefix", required=True)
    return parser.parse_args()


def load_yaml(path: str) -> dict[str, object]:
    """Load a YAML config file."""
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def build_feature_frame(
    frame: pd.DataFrame,
    sequence_column: str,
    enabled_features: list[str],
) -> pd.DataFrame:
    """Build the enabled feature frame."""
    featured = add_basic_features(frame, sequence_column=sequence_column)
    featured = add_physicochemical_features(featured, sequence_column=sequence_column)
    return featured[enabled_features].copy()


def get_binary_predictions(model: object, x_test: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Return predicted labels and positive-class scores."""
    if hasattr(model, "predict_proba"):
        scores = model.predict_proba(x_test)[:, 1]
    elif hasattr(model, "decision_function"):
        raw_scores = np.asarray(model.decision_function(x_test), dtype=float)
        scores = 1.0 / (1.0 + np.exp(-raw_scores))
    else:
        scores = np.asarray(model.predict(x_test), dtype=float)

    predicted = (scores >= 0.5).astype(int)
    return predicted, scores


def ensure_output_dirs() -> dict[str, Path]:
    """Create output directories and return them."""
    directories = {
        "metrics": ROOT / "results" / "metrics",
        "predictions": ROOT / "results" / "predictions",
        "tables": ROOT / "results" / "tables",
        "manifests": ROOT / "results" / "manifests",
        "figures": ROOT / "figures",
    }
    for path in directories.values():
        path.mkdir(parents=True, exist_ok=True)
    return directories


def main() -> None:
    """Run the v0.1 baseline workflow."""
    args = parse_args()

    data_config = load_yaml(args.data_config)
    feature_config = load_yaml(args.feature_config)
    model_config = load_yaml(args.model_config)
    eval_config = load_yaml(args.eval_config)

    dataset = load_table(str(ROOT / str(data_config["input_path"])))

    id_column = str(data_config["id_column"])
    sequence_column = str(data_config["sequence_column"])
    label_column = str(data_config["label_column"])
    required_columns = [
        id_column,
        sequence_column,
        label_column,
        str(data_config.get("source_column", "source")),
    ]

    validate_required_columns(dataset, required_columns)
    validate_binary_labels(dataset, label_column)

    enabled_features = list(feature_config["enabled_features"])
    feature_frame = build_feature_frame(dataset, sequence_column, enabled_features)
    labels = dataset[label_column].astype(int)

    cv_folds = int(eval_config["cv_folds"])
    random_seed = int(eval_config["random_seed"])
    splitter = StratifiedKFold(
        n_splits=cv_folds,
        shuffle=True,
        random_state=random_seed,
    )

    fold_metrics: list[dict[str, float]] = []
    prediction_rows: list[pd.DataFrame] = []

    for fold_index, (train_idx, test_idx) in enumerate(splitter.split(feature_frame, labels), start=1):
        x_train = feature_frame.iloc[train_idx]
        x_test = feature_frame.iloc[test_idx]
        y_train = labels.iloc[train_idx]
        y_test = labels.iloc[test_idx]

        model = build_baseline_model(model_config)
        model.fit(x_train, y_train)

        predicted_label, predicted_score = get_binary_predictions(model, x_test)
        fold_metrics.append(compute_binary_metrics(y_test, predicted_label, predicted_score))

        prediction_rows.append(
            pd.DataFrame(
                {
                    "sequence_id": dataset.iloc[test_idx][id_column].values,
                    "true_label": y_test.values,
                    "predicted_label": predicted_label,
                    "predicted_score": predicted_score,
                    "fold": fold_index,
                }
            )
        )

    predictions = pd.concat(prediction_rows, ignore_index=True)
    ranking = rank_candidates(predictions, score_column="predicted_score", id_column="sequence_id")
    mean_metrics = aggregate_metrics(fold_metrics)

    split_policy = f"{eval_config['split_policy']}_{cv_folds}"
    directories = ensure_output_dirs()

    metrics_path = directories["metrics"] / f"{args.output_prefix}_metrics.json"
    predictions_path = directories["predictions"] / f"{args.output_prefix}_predictions.csv"
    ranking_path = directories["tables"] / f"{args.output_prefix}_ranking.csv"
    summary_path = directories["tables"] / f"{args.output_prefix}_summary.csv"
    manifest_path = directories["manifests"] / f"{args.output_prefix}_manifest.json"
    figure_path = directories["figures"] / f"{args.output_prefix}_score_distribution.png"

    metrics_payload = {
        "model_name": model_config["model_name"],
        "dataset_name": data_config["dataset_name"],
        "dataset_version": data_config.get("dataset_version"),
        "split_policy": split_policy,
        "cv_folds": cv_folds,
        "random_seed": random_seed,
        "mean_metrics": mean_metrics,
    }

    with open(metrics_path, "w", encoding="utf-8") as handle:
        json.dump(metrics_payload, handle, indent=2)

    predictions.to_csv(predictions_path, index=False)
    ranking.to_csv(ranking_path, index=False)

    summary = pd.DataFrame(
        [
            {
                "run_id": args.output_prefix,
                "dataset_name": data_config["dataset_name"],
                "dataset_version": data_config.get("dataset_version"),
                "model_name": model_config["model_name"],
                "split_policy": split_policy,
                "cv_folds": cv_folds,
                "random_seed": random_seed,
                "roc_auc": mean_metrics["roc_auc"],
                "pr_auc": mean_metrics["pr_auc"],
                "precision": mean_metrics["precision"],
                "recall": mean_metrics["recall"],
                "f1": mean_metrics["f1"],
                "mcc": mean_metrics["mcc"],
            }
        ]
    )
    summary.to_csv(summary_path, index=False)

    save_score_distribution_figure(predictions, figure_path)

    manifest = RunManifest(
        run_id=args.output_prefix,
        dataset_name=str(data_config["dataset_name"]),
        dataset_version=data_config.get("dataset_version"),
        feature_config=args.feature_config,
        model_name=str(model_config["model_name"]),
        model_config=args.model_config,
        split_policy=split_policy,
        random_seed=random_seed,
        metrics_file=str(metrics_path.relative_to(ROOT)),
        predictions_file=str(predictions_path.relative_to(ROOT)),
        ranking_file=str(ranking_path.relative_to(ROOT)),
        summary_file=str(summary_path.relative_to(ROOT)),
        figure_file=str(figure_path.relative_to(ROOT)),
        generated_at=datetime.now(timezone.utc).isoformat(),
    )

    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest.to_dict(), handle, indent=2)

    print(json.dumps({"status": "ok", "output_prefix": args.output_prefix}, indent=2))


if __name__ == "__main__":
    main()
