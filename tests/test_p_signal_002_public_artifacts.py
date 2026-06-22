from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = [
    ROOT / "docs" / "reports" / "p-signal-002-esm2-embedding-comparison.md",
    ROOT / "results" / "p_signal_002" / "esm2_embedding_model_comparison.csv",
    ROOT / "results" / "p_signal_002" / "esm2_embedding_per_fold_metrics.csv",
    ROOT / "results" / "p_signal_002" / "esm2_embedding_leakage_summary.json",
    ROOT / "results" / "p_signal_002" / "esm2_embedding_run_manifest.json",
]


def _json_keys(value: Any) -> set[str]:
    if isinstance(value, dict):
        keys = set(value)
        for item in value.values():
            keys.update(_json_keys(item))
        return keys
    if isinstance(value, list):
        keys: set[str] = set()
        for item in value:
            keys.update(_json_keys(item))
        return keys
    return set()


def test_p_signal_002_public_artifacts_exist() -> None:
    for artifact in ARTIFACTS:
        assert artifact.exists(), artifact


def test_p_signal_002_model_comparison_is_aggregate_only() -> None:
    path = ROOT / "results" / "p_signal_002" / "esm2_embedding_model_comparison.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 3
    assert {row["model"] for row in rows} == {"dummy", "logistic_regression", "random_forest"}
    assert {row["split_policy"] for row in rows} == {"leakage_aware_group_stratified"}
    assert {int(row["folds"]) for row in rows} == {5}
    assert {int(row["test_rows_total"]) for row in rows} == {2959}
    assert {int(row["test_positive_total"]) for row in rows} == {269}
    assert {int(row["test_negative_total"]) for row in rows} == {2690}
    assert "balanced_accuracy" in rows[0]

    forbidden_cols = {
        "sequence",
        "sequence_id",
        "label",
        "prediction",
        "embedding",
        "group_id",
        "group_assignment",
        "split",
        "split_manifest",
        "path",
    }
    assert not (forbidden_cols & set(rows[0]))


def test_p_signal_002_per_fold_metrics_are_aggregate_only() -> None:
    path = ROOT / "results" / "p_signal_002" / "esm2_embedding_per_fold_metrics.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 15
    assert {row["model"] for row in rows} == {"dummy", "logistic_regression", "random_forest"}
    assert {int(row["fold_id"]) for row in rows} == {1, 2, 3, 4, 5}
    assert {row["split_policy"] for row in rows} == {"leakage_aware_group_stratified"}
    assert sum(int(row["test_rows"]) for row in rows if row["model"] == "dummy") == 2959

    forbidden_cols = {
        "sequence",
        "sequence_id",
        "label",
        "prediction",
        "embedding",
        "group_id",
        "group_assignment",
        "split_manifest",
        "path",
    }
    assert not (forbidden_cols & set(rows[0]))


def test_p_signal_002_json_artifacts_parse_and_are_public_safe() -> None:
    leakage = json.loads(
        (ROOT / "results" / "p_signal_002" / "esm2_embedding_leakage_summary.json").read_text(
            encoding="utf-8"
        )
    )
    manifest = json.loads(
        (ROOT / "results" / "p_signal_002" / "esm2_embedding_run_manifest.json").read_text(
            encoding="utf-8"
        )
    )

    assert leakage["row_count"] == 2959
    assert leakage["label_counts"] == {"negative": 2690, "positive": 269}
    assert leakage["groups_crossing_folds"] == 0
    assert leakage["near_duplicate_pair_count"] == 73
    assert "max_pairs=10000" in " ".join(leakage["caveats"])
    assert manifest["model_id"] == "facebook/esm2_t12_35M_UR50D"
    assert manifest["representation_dim"] == 480
    assert manifest["dataset_release_boundary"] == "dataset_not_redistributed_publicly"

    forbidden_keys = {
        "sequence",
        "sequence_id",
        "embedding",
        "prediction",
        "group_assignment",
        "split_manifest",
        "dataset_private_reference",
    }
    assert not (forbidden_keys & _json_keys(leakage))
    assert not (forbidden_keys & _json_keys(manifest))


def test_p_signal_002_public_artifacts_do_not_expose_private_surfaces() -> None:
    forbidden = [
        "/" + "data/permea",
        "/" + "Users/",
        "local" + "_only",
        "permea-private" + "-doctrine",
        "AI " + "Champion",
        "H" + "100",
        "K-" + "EXAONE",
        "KO" + "RA",
        "model " + "cache",
        "hugging" + "face",
        "private " + "path",
        "private " + "run",
        "private " + "log",
    ]
    for artifact in ARTIFACTS:
        text = artifact.read_text(encoding="utf-8")
        for phrase in forbidden:
            assert phrase not in text, f"{phrase!r} leaked in {artifact}"


def test_p_signal_002_report_contains_required_boundaries_and_caveats() -> None:
    report = (
        ROOT / "docs" / "reports" / "p-signal-002-esm2-embedding-comparison.md"
    ).read_text(encoding="utf-8")

    required = [
        "aggregate computational representation comparison",
        "facebook/esm2_t12_35M_UR50D",
        "dataset is not redistributed",
        "Row-level data, raw sequences, embeddings, predictions, split manifests, and group assignments are not public",
        "max_pairs=10000",
        "Source-aware biological interpretation is limited",
        "P-SIGNAL-001 aggregate physicochemical baseline",
        "0.8718",
        "0.5807",
        "0.5084",
    ]
    for phrase in required:
        assert phrase in report


def test_p_signal_002_report_matches_p_signal_001_baseline_artifact() -> None:
    report = (
        ROOT / "docs" / "reports" / "p-signal-002-esm2-embedding-comparison.md"
    ).read_text(encoding="utf-8")
    baseline_path = ROOT / "results" / "p_signal_001" / "physchem_baseline_model_comparison.csv"
    with baseline_path.open(newline="", encoding="utf-8") as handle:
        baseline_rows = {row["model"]: row for row in csv.DictReader(handle)}

    random_forest = baseline_rows["random_forest"]
    expected_values = {
        "roc_auc": "0.8718",
        "pr_auc": "0.5807",
        "mcc": "0.5084",
    }
    for metric, rounded in expected_values.items():
        assert f"{float(random_forest[metric]):.4f}" == rounded
        assert rounded in report

    stale_values = ["0.7533", "0.2767"]
    for value in stale_values:
        assert value not in report


def test_p_signal_002_report_has_no_unsupported_affirmative_claims() -> None:
    report = (
        ROOT / "docs" / "reports" / "p-signal-002-esm2-embedding-comparison.md"
    ).read_text(encoding="utf-8")
    lower = report.lower()

    unsupported_affirmative_claims = [
        "is wet-lab validated",
        "is in-vivo validated",
        "has clinical relevance",
        "has therapeutic efficacy",
        "solves delivery",
        "provides universal delivery prediction",
        "achieves state-of-the-art",
        "the dataset is publicly available",
        "proves transport",
        "provides biological transport proof",
    ]
    for phrase in unsupported_affirmative_claims:
        assert phrase not in lower
