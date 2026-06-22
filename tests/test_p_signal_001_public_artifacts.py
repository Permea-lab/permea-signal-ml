from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = [
    ROOT / "docs" / "reports" / "p-signal-001-leakage-controlled-physchem-baseline.md",
    ROOT / "results" / "p_signal_001" / "physchem_baseline_model_comparison.csv",
    ROOT / "results" / "p_signal_001" / "physchem_baseline_per_fold_metrics.csv",
    ROOT / "results" / "p_signal_001" / "physchem_baseline_leakage_summary.json",
    ROOT / "results" / "p_signal_001" / "physchem_baseline_run_manifest.json",
]


def test_p_signal_001_public_artifacts_exist() -> None:
    for artifact in ARTIFACTS:
        assert artifact.exists(), artifact


def test_p_signal_001_model_comparison_shape() -> None:
    path = ROOT / "results" / "p_signal_001" / "physchem_baseline_model_comparison.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert {row["model"] for row in rows} == {"dummy", "logistic_regression", "random_forest"}
    assert {row["split_policy"] for row in rows} == {"leakage_aware_group_stratified"}
    assert {int(row["folds"]) for row in rows} == {5}
    assert {int(row["test_rows_total"]) for row in rows} == {2959}
    assert {int(row["test_positive_total"]) for row in rows} == {269}
    assert {int(row["test_negative_total"]) for row in rows} == {2690}
    assert "balanced_accuracy" in rows[0]


def test_p_signal_001_manifest_is_public_safe() -> None:
    manifest_path = ROOT / "results" / "p_signal_001" / "physchem_baseline_run_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert manifest["dataset_private_reference"] == "private_local_b3pred_dataset3_rerun_ready_csv"
    assert manifest["dataset_sha256"] == "2e8d3fc30becfdd00ad7cd25eedd5e6c00df7698747ea358b4cc97f4268f8abf"
    assert manifest["release_classification"]["row_level_dataset"] == "private_only_rights_review_required"
    assert manifest["split_policy"] == "leakage_aware_group_stratified"


def test_p_signal_001_public_artifacts_do_not_expose_private_surfaces() -> None:
    forbidden = [
        "/" + "Users/",
        "local" + "_only",
        "permea-private" + "-doctrine",
        "AI " + "Champion",
        "H" + "100",
        "K-" + "EXAONE",
        "KO" + "RA",
        "state-of" + "-the-art",
        "solved " + "delivery",
        "universal " + "delivery",
        "clin" + "ical",
        "thera" + "peutic",
        "Alpha" + "Fold",
    ]
    for artifact in ARTIFACTS:
        text = artifact.read_text(encoding="utf-8")
        for phrase in forbidden:
            assert phrase not in text, f"{phrase!r} leaked in {artifact}"
