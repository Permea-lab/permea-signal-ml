from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import importlib.util

SCRIPT_PATH = ROOT / "scripts" / "run_leakage_aware_baselines.py"
spec = importlib.util.spec_from_file_location("run_leakage_aware_baselines", SCRIPT_PATH)
runner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(runner)


def fixture_dataset() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "sequence_id": [f"s{i}" for i in range(12)],
            "label": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            "length": [5, 6, 5, 6, 7, 8, 7, 8, 9, 10, 9, 10],
            "charge": [0, 1, 0, 1, -1, 2, -1, 2, 0, 1, 0, 1],
            "gravy": [0.1, -0.2, 0.2, -0.3, 0.3, -0.4, 0.4, -0.5, 0.5, -0.6, 0.6, -0.7],
            "pI": [6.0, 8.0, 6.1, 8.1, 5.9, 8.2, 6.2, 8.3, 6.3, 8.4, 6.4, 8.5],
            "aromaticity": [0.0, 0.2, 0.0, 0.2, 0.1, 0.3, 0.1, 0.3, 0.2, 0.4, 0.2, 0.4],
        }
    )


def fixture_manifest() -> pd.DataFrame:
    rows = []
    for index in range(12):
        rows.append(
            {
                "row_index": index,
                "sequence_id": f"s{index}",
                "label": index % 2,
                "group_id": f"g{index}",
                "fold_id": (index % 3) + 1,
                "split_policy": "leakage_aware_group_stratified",
                "group_size": 1,
                "grouping_method": "fixture",
            }
        )
    return pd.DataFrame(rows)


def test_validate_inputs_and_group_integrity() -> None:
    merged = runner.validate_inputs(fixture_dataset(), fixture_manifest())

    assert len(merged) == 12
    assert set(merged["fold_id"]) == {1, 2, 3}


def test_validate_inputs_rejects_group_crossing() -> None:
    manifest = fixture_manifest()
    manifest.loc[0, "group_id"] = "shared"
    manifest.loc[1, "group_id"] = "shared"
    manifest.loc[0, "fold_id"] = 1
    manifest.loc[1, "fold_id"] = 2

    try:
        runner.validate_inputs(fixture_dataset(), manifest)
    except ValueError as exc:
        assert "crosses folds" in str(exc)
    else:
        raise AssertionError("Expected group crossing validation error")


def test_model_families_limited() -> None:
    assert set(runner.MODEL_CONFIG_PATHS) == {"dummy", "logistic_regression", "random_forest"}


def test_metric_aggregation_shape() -> None:
    fold_metrics = [
        {"roc_auc": 0.5, "pr_auc": 0.1, "precision": 0.0, "recall": 0.0, "f1": 0.0, "mcc": 0.0, "test_rows": 4, "test_positives": 2, "test_negatives": 2},
        {"roc_auc": 0.7, "pr_auc": 0.2, "precision": 0.5, "recall": 0.5, "f1": 0.5, "mcc": 0.2, "test_rows": 4, "test_positives": 2, "test_negatives": 2},
    ]
    summary = runner.summarize_model_metrics("dummy", fold_metrics)

    assert summary["model"] == "dummy"
    assert summary["roc_auc"] == 0.6
    assert "roc_auc_std" in summary
    assert summary["test_rows_total"] == 8


def test_runner_writes_only_requested_output_dir(tmp_path: Path) -> None:
    dataset_path = tmp_path / "dataset.csv"
    manifest_path = tmp_path / "manifest.csv"
    output_dir = tmp_path / "sensitivity"
    fixture_dataset().to_csv(dataset_path, index=False)
    fixture_manifest().to_csv(manifest_path, index=False)

    payload = runner.run_leakage_aware_baselines(dataset_path, manifest_path, output_dir)

    assert set(Path(path).parent for path in payload["outputs_written"]) == {output_dir}
    assert (output_dir / "leakage_aware_model_comparison_summary.csv").exists()
    assert (output_dir / "leakage_aware_model_comparison_per_fold.csv").exists()
    assert (output_dir / "leakage_aware_predictions.csv").exists()
    assert (output_dir / "leakage_aware_metrics_summary.json").exists()
