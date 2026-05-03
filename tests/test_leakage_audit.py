from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.audits.leakage import (
    assign_stratified_folds,
    find_exact_duplicates,
    find_high_jaccard_pairs,
    find_label_conflicts,
    find_near_duplicates,
    jaccard_similarity,
    kmer_set,
    normalize_sequence,
    run_leakage_audit,
    summarize_source_group_distribution,
)


def fixture_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "sequence_id": [f"s{i}" for i in range(1, 9)],
            "sequence": ["AAA", " aaa ", "AAB", "CCC", "GGG", "TTT", "TTA", "CCC"],
            "label": [1, 1, 1, 0, 0, 1, 1, 1],
            "source": ["x", "x", "x", "y", "y", "z", "z", "y"],
        }
    )


def test_normalize_sequence() -> None:
    assert normalize_sequence(" aaa ") == "AAA"
    assert normalize_sequence(None) == ""


def test_exact_duplicate_detection() -> None:
    result = find_exact_duplicates(fixture_frame())
    duplicate_sequences = set(result["normalized_sequence"])
    assert "AAA" in duplicate_sequences
    assert "CCC" in duplicate_sequences


def test_label_conflict_detection() -> None:
    result = find_label_conflicts(fixture_frame())
    assert list(result["normalized_sequence"]) == ["CCC"]
    assert bool(result.loc[0, "label_conflict"]) is True


def test_near_duplicate_detection() -> None:
    result = find_near_duplicates(fixture_frame(), max_distance=1)
    pairs = {(row.sequence_a, row.sequence_b) for row in result.itertuples()}
    assert ("AAA", "AAB") in pairs
    assert ("TTT", "TTA") in pairs


def test_kmer_jaccard_similarity() -> None:
    assert kmer_set("ABCD", k=2) == {"AB", "BC", "CD"}
    assert jaccard_similarity({"AB", "BC"}, {"BC", "CD"}) == 1 / 3
    result = find_high_jaccard_pairs(fixture_frame(), k=2, threshold=0.5)
    assert not result.empty


def test_fold_assignment_and_source_summary() -> None:
    frame = fixture_frame()
    folded = assign_stratified_folds(frame, n_splits=2, random_state=42)
    assert "fold_id" in folded.columns
    assert len(folded) == len(frame)
    assert set(folded["fold_id"]) == {1, 2}

    summary = summarize_source_group_distribution(folded)
    assert {"source", "fold_id", "count", "fold_count_for_source", "caveat"}.issubset(summary.columns)


def test_dry_run_does_not_write_outputs(tmp_path: Path) -> None:
    input_path = tmp_path / "fixture.csv"
    output_dir = tmp_path / "audits"
    fixture_frame().to_csv(input_path, index=False)

    summary = run_leakage_audit(input_path, output_dir, n_splits=2, dry_run=True)

    assert summary["dry_run"] is True
    assert summary["outputs_written"] == []
    assert not output_dir.exists()

