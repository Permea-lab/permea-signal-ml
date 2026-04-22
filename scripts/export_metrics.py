"""Export compact benchmark tables for the current evidence package."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.data.load import load_table
from permea_signal_ml.features.basic import add_basic_features
from permea_signal_ml.features.physicochemical import add_physicochemical_features
from permea_signal_ml.models.baselines import build_baseline_model


RUN_SPECS = [
    ("legacy_bbb_dummy_v01", "dummy", "regenerated dummy baseline rerun"),
    ("legacy_bbb_lr_v01", "logistic_regression", "regenerated logistic baseline rerun"),
    ("legacy_bbb_rf_v01", "random_forest", "regenerated random-forest baseline rerun"),
]


def load_yaml(path: Path) -> dict[str, object]:
    """Load a YAML config file."""
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def export_model_comparison_summary() -> Path:
    """Write a compact regenerated-model comparison table."""
    rows: list[dict[str, object]] = []

    for run_id, model_name, notes in RUN_SPECS:
        metrics_path = ROOT / "results" / "metrics" / f"{run_id}_metrics.json"
        with metrics_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        mean_metrics = payload["mean_metrics"]
        rows.append(
            {
                "model": model_name,
                "roc_auc": float(mean_metrics["roc_auc"]),
                "pr_auc": float(mean_metrics["pr_auc"]),
                "precision": float(mean_metrics["precision"]),
                "recall": float(mean_metrics["recall"]),
                "f1": float(mean_metrics["f1"]),
                "mcc": float(mean_metrics["mcc"]),
                "artifact_type": "regenerated",
                "run_id": run_id,
                "notes": notes,
            }
        )

    frame = pd.DataFrame(
        rows,
        columns=[
            "model",
            "roc_auc",
            "pr_auc",
            "precision",
            "recall",
            "f1",
            "mcc",
            "artifact_type",
            "run_id",
            "notes",
        ],
    )
    output_path = ROOT / "results" / "tables" / "model_comparison_summary.csv"
    frame.to_csv(output_path, index=False, float_format="%.10f")
    return output_path


def build_feature_frame(
    frame: pd.DataFrame,
    sequence_column: str,
    enabled_features: list[str],
) -> pd.DataFrame:
    """Build the enabled feature frame for model fitting."""
    featured = add_basic_features(frame, sequence_column=sequence_column)
    featured = add_physicochemical_features(featured, sequence_column=sequence_column)
    return featured[enabled_features].copy()


def export_regenerated_rf_feature_importance() -> Path:
    """Fit the regenerated RF baseline on the full dataset and export importances."""
    data_config = load_yaml(ROOT / "configs" / "data" / "legacy_bbb_dataset_with_features.yaml")
    feature_config = load_yaml(ROOT / "configs" / "features" / "physicochemical.yaml")
    model_config = load_yaml(ROOT / "configs" / "models" / "random_forest.yaml")

    dataset = load_table(str(ROOT / str(data_config["input_path"])))
    enabled_features = list(feature_config["enabled_features"])
    feature_frame = build_feature_frame(
        dataset,
        sequence_column=str(data_config["sequence_column"]),
        enabled_features=enabled_features,
    )
    labels = dataset[str(data_config["label_column"])].astype(int)

    model = build_baseline_model(model_config)
    model.fit(feature_frame, labels)

    importance_frame = pd.DataFrame(
        {
            "feature": enabled_features,
            "importance": model.feature_importances_,
            "run_id": "legacy_bbb_rf_v01",
            "model": "random_forest",
            "artifact_type": "regenerated",
        }
    ).sort_values("importance", ascending=False, ignore_index=True)

    output_path = ROOT / "results" / "tables" / "regenerated_rf_feature_importance.csv"
    importance_frame.to_csv(output_path, index=False, float_format="%.10f")
    return output_path


def main() -> None:
    """Write the current comparison and feature-importance tables."""
    summary_path = export_model_comparison_summary()
    importance_path = export_regenerated_rf_feature_importance()
    print(
        json.dumps(
            {
                "status": "ok",
                "model_comparison_summary": str(summary_path.relative_to(ROOT)),
                "rf_feature_importance": str(importance_path.relative_to(ROOT)),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
