from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.audits.grouping import (
    assess_source_group_feasibility,
    build_combined_similarity_groups,
    build_exact_duplicate_groups,
    build_kmer_jaccard_groups,
    build_near_duplicate_graph_groups,
    edit_distance,
    jaccard_similarity,
    kmer_set,
    normalize_sequence_for_grouping,
    summarize_grouping,
)


def fixture_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "sequence_id": [f"s{i}" for i in range(1, 8)],
            "sequence": ["AAA", " aaa ", "AAB", "CCC", "CCCD", "GGG", "TTT"],
            "label": [1, 1, 1, 0, 0, 1, 1],
            "source": ["legacy_bbb_import"] * 7,
        }
    )


def test_normalize_sequence_for_grouping() -> None:
    assert normalize_sequence_for_grouping(" aaa ") == "AAA"
    assert normalize_sequence_for_grouping(None) == ""


def test_exact_duplicate_grouping() -> None:
    groups = build_exact_duplicate_groups(fixture_frame())
    duplicate_group = groups[groups["normalized_sequence"] == "AAA"]

    assert len(groups) == 7
    assert duplicate_group["group_id"].nunique() == 1
    assert set(duplicate_group["group_size"]) == {2}
    assert summarize_grouping(groups)["non_singleton_groups"] == 1


def test_edit_distance_with_threshold() -> None:
    assert edit_distance("AAA", "AAB") == 1
    assert edit_distance("AAA", "CCC", max_distance=1) > 1


def test_near_duplicate_graph_grouping() -> None:
    groups = build_near_duplicate_graph_groups(fixture_frame(), max_distance=1)
    aaa_group_id = groups.loc[groups["normalized_sequence"] == "AAA", "group_id"].iloc[0]
    aab_group_id = groups.loc[groups["normalized_sequence"] == "AAB", "group_id"].iloc[0]

    assert aaa_group_id == aab_group_id
    assert "near_duplicate_edit_distance<=1" in set(groups["grouping_method"])


def test_kmer_jaccard_grouping() -> None:
    assert kmer_set("ABCD", k=2) == {"AB", "BC", "CD"}
    assert jaccard_similarity({"AB", "BC"}, {"BC", "CD"}) == 1 / 3

    groups = build_kmer_jaccard_groups(fixture_frame(), k=2, threshold=0.5)
    ccc_group_id = groups.loc[groups["normalized_sequence"] == "CCC", "group_id"].iloc[0]
    cccd_group_id = groups.loc[groups["normalized_sequence"] == "CCCD", "group_id"].iloc[0]
    assert ccc_group_id == cccd_group_id


def test_combined_grouping_records_methods() -> None:
    groups = build_combined_similarity_groups(
        fixture_frame(),
        edit_distance_threshold=1,
        k=2,
        jaccard_threshold=0.5,
    )
    aaa_group = groups[groups["normalized_sequence"].isin(["AAA", "AAB"])]

    assert aaa_group["group_id"].nunique() == 1
    assert any("edit_distance<=1" in methods for methods in groups["methods_contributing"])
    assert any("kmer_jaccard>=0.5" in methods for methods in groups["methods_contributing"])


def test_source_feasibility_assessment() -> None:
    summary = assess_source_group_feasibility(fixture_frame())

    assert summary["source_col_present"] is True
    assert summary["number_of_unique_sources"] == 1
    assert summary["feasible_for_group_split"] is False
    assert "too coarse" in summary["caveat"]


def test_dry_run_cli_does_not_write_outputs(tmp_path: Path) -> None:
    input_path = tmp_path / "fixture.csv"
    output_dir = tmp_path / "sensitivity"
    fixture_frame().to_csv(input_path, index=False)

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_leakage_aware_groups.py"),
            "--input",
            str(input_path),
            "--output-dir",
            str(output_dir),
            "--method",
            "combined",
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
