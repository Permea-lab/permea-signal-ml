from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.audits.splits import (
    assign_group_stratified_folds,
    attach_labels_to_groups,
    build_split_manifest,
    load_group_assignments,
    summarize_groups_for_splitting,
    summarize_split_manifest,
)


def fixture_dataset() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "sequence_id": [f"s{i}" for i in range(10)],
            "sequence": [f"SEQ{i}" for i in range(10)],
            "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        }
    )


def fixture_groups() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "row_index": list(range(10)),
            "sequence_id": [f"s{i}" for i in range(10)],
            "normalized_sequence": [f"SEQ{i}" for i in range(10)],
            "group_id": ["g1", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"],
            "group_type": ["combined_similarity"] * 10,
            "group_size": [2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
            "grouping_method": ["combined"] * 10,
        }
    )


def test_load_group_assignments_validation(tmp_path: Path) -> None:
    path = tmp_path / "groups.csv"
    fixture_groups().to_csv(path, index=False)

    loaded = load_group_assignments(path)
    assert len(loaded) == 10

    bad_path = tmp_path / "bad.csv"
    pd.DataFrame({"row_index": [0]}).to_csv(bad_path, index=False)
    with pytest.raises(ValueError, match="group_id"):
        load_group_assignments(bad_path)


def test_attach_labels_to_groups() -> None:
    attached = attach_labels_to_groups(fixture_dataset(), fixture_groups())

    assert "label" in attached.columns
    assert list(attached["label"]) == list(fixture_dataset()["label"])


def test_group_summary() -> None:
    attached = attach_labels_to_groups(fixture_dataset(), fixture_groups())
    summary = summarize_groups_for_splitting(attached)
    group_one = summary[summary["group_id"] == "g1"].iloc[0]

    assert int(group_one["group_size"]) == 2
    assert int(group_one["positive_count"]) == 1
    assert int(group_one["negative_count"]) == 1
    assert group_one["labels_present"] == "0|1"


def test_deterministic_fold_assignment_and_group_integrity() -> None:
    attached = attach_labels_to_groups(fixture_dataset(), fixture_groups())
    group_summary = summarize_groups_for_splitting(attached)

    first = assign_group_stratified_folds(group_summary, n_splits=3, random_state=42)
    second = assign_group_stratified_folds(group_summary, n_splits=3, random_state=42)

    assert first.equals(second)
    assert set(first["fold_id"]) == {1, 2, 3}
    assert first["group_id"].is_unique


def test_split_manifest_and_summary() -> None:
    dataset = fixture_dataset()
    groups = fixture_groups()
    attached = attach_labels_to_groups(dataset, groups)
    group_summary = summarize_groups_for_splitting(attached)
    group_to_fold = assign_group_stratified_folds(group_summary, n_splits=3, random_state=42)
    manifest = build_split_manifest(dataset, groups, group_to_fold)
    summary = summarize_split_manifest(manifest)

    assert len(manifest) == len(dataset)
    assert set(manifest["split_policy"]) == {"leakage_aware_group_stratified"}
    assert summary["groups_crossing_folds"] == 0
    assert summary["number_of_rows"] == 10


def test_cli_dry_run_does_not_write_outputs(tmp_path: Path) -> None:
    dataset_path = tmp_path / "dataset.csv"
    groups_path = tmp_path / "groups.csv"
    output_dir = tmp_path / "sensitivity"
    fixture_dataset().to_csv(dataset_path, index=False)
    fixture_groups().to_csv(groups_path, index=False)

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_leakage_aware_split_manifest.py"),
            "--input",
            str(dataset_path),
            "--groups",
            str(groups_path),
            "--output-dir",
            str(output_dir),
            "--n-splits",
            "3",
            "--dry-run",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    summary = json.loads(result.stdout)
    assert summary["dry_run"] is True
    assert summary["outputs_written"] == []
    assert not output_dir.exists()
