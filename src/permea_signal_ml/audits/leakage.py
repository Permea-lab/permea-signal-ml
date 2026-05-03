"""Sequence leakage audit utilities.

These helpers implement dataset-structural audit checks only. They do not
train models, rerun benchmarks, change metric values, or establish that a
dataset is leakage-free.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.model_selection import StratifiedKFold


PLANNED_OUTPUTS = (
    "sequence_duplicate_audit.csv",
    "label_conflict_audit.csv",
    "near_duplicate_pairs.csv",
    "sequence_similarity_summary.csv",
    "fold_similarity_leakage_summary.csv",
    "source_group_leakage_summary.csv",
    "leakage_audit_summary.json",
)


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset and validate the minimum leakage-audit columns."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

    frame = pd.read_csv(dataset_path)
    missing = [column for column in ("sequence", "label") if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return frame


def normalize_sequence(seq: object) -> str:
    """Return a conservative normalized sequence string."""
    if pd.isna(seq):
        return ""
    return str(seq).strip().upper()


def _with_normalized_sequence(df: pd.DataFrame, sequence_col: str) -> pd.DataFrame:
    """Return a copy with a normalized sequence helper column."""
    if sequence_col not in df.columns:
        raise ValueError(f"Missing sequence column: {sequence_col}")

    frame = df.copy()
    frame["_normalized_sequence"] = frame[sequence_col].map(normalize_sequence)
    return frame


def _label_set(labels: pd.Series) -> str:
    """Return a stable, display-safe label set."""
    return "|".join(sorted(str(label) for label in labels.dropna().unique()))


def find_exact_duplicates(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    label_col: str = "label",
) -> pd.DataFrame:
    """Identify normalized sequences that appear more than once."""
    if label_col not in df.columns:
        raise ValueError(f"Missing label column: {label_col}")

    frame = _with_normalized_sequence(df, sequence_col)
    grouped = frame.groupby("_normalized_sequence", dropna=False)
    rows: list[dict[str, Any]] = []

    for normalized_sequence, group in grouped:
        if len(group) <= 1:
            continue
        labels = group[label_col].dropna().unique()
        rows.append(
            {
                "normalized_sequence": normalized_sequence,
                "count": int(len(group)),
                "label_set": _label_set(group[label_col]),
                "label_count": int(len(labels)),
                "label_conflict": bool(len(labels) > 1),
            }
        )

    return pd.DataFrame(
        rows,
        columns=[
            "normalized_sequence",
            "count",
            "label_set",
            "label_count",
            "label_conflict",
        ],
    )


def find_label_conflicts(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    label_col: str = "label",
) -> pd.DataFrame:
    """Identify identical normalized sequences with multiple labels."""
    duplicates = find_exact_duplicates(df, sequence_col=sequence_col, label_col=label_col)
    if duplicates.empty:
        return duplicates
    return duplicates[duplicates["label_conflict"]].reset_index(drop=True)


def edit_distance(a: str, b: str, max_distance: int | None = None) -> int:
    """Compute Levenshtein edit distance with optional early stopping."""
    if a == b:
        return 0
    if max_distance is not None and abs(len(a) - len(b)) > max_distance:
        return max_distance + 1

    previous = list(range(len(b) + 1))
    for i, char_a in enumerate(a, start=1):
        current = [i]
        row_min = current[0]
        for j, char_b in enumerate(b, start=1):
            insertion = current[j - 1] + 1
            deletion = previous[j] + 1
            substitution = previous[j - 1] + (char_a != char_b)
            value = min(insertion, deletion, substitution)
            current.append(value)
            row_min = min(row_min, value)
        if max_distance is not None and row_min > max_distance:
            return max_distance + 1
        previous = current
    return previous[-1]


def find_near_duplicates(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    max_distance: int = 1,
    max_pairs: int | None = None,
) -> pd.DataFrame:
    """Find sequence pairs within a small edit distance."""
    if max_distance < 0:
        raise ValueError("max_distance must be non-negative")

    frame = _with_normalized_sequence(df, sequence_col).reset_index(drop=False)
    rows: list[dict[str, Any]] = []

    for left in range(len(frame)):
        seq_a = frame.at[left, "_normalized_sequence"]
        for right in range(left + 1, len(frame)):
            seq_b = frame.at[right, "_normalized_sequence"]
            distance = edit_distance(seq_a, seq_b, max_distance=max_distance)
            if distance <= max_distance:
                rows.append(
                    {
                        "index_a": int(frame.at[left, "index"]),
                        "index_b": int(frame.at[right, "index"]),
                        "sequence_a": seq_a,
                        "sequence_b": seq_b,
                        "edit_distance": int(distance),
                    }
                )
                if max_pairs is not None and len(rows) >= max_pairs:
                    return pd.DataFrame(rows)
    return pd.DataFrame(rows, columns=["index_a", "index_b", "sequence_a", "sequence_b", "edit_distance"])


def kmer_set(seq: object, k: int) -> set[str]:
    """Return the k-mer set for a normalized sequence."""
    if k <= 0:
        raise ValueError("k must be positive")
    normalized = normalize_sequence(seq)
    if len(normalized) < k:
        return {normalized} if normalized else set()
    return {normalized[index : index + k] for index in range(len(normalized) - k + 1)}


def jaccard_similarity(a: set[str], b: set[str]) -> float:
    """Compute Jaccard similarity between two sets."""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def find_high_jaccard_pairs(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    k: int = 3,
    threshold: float = 0.8,
    max_pairs: int | None = None,
) -> pd.DataFrame:
    """Find sequence pairs whose k-mer Jaccard similarity meets a threshold."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    frame = _with_normalized_sequence(df, sequence_col).reset_index(drop=False)
    kmers = [kmer_set(sequence, k=k) for sequence in frame["_normalized_sequence"]]
    rows: list[dict[str, Any]] = []

    for left in range(len(frame)):
        for right in range(left + 1, len(frame)):
            similarity = jaccard_similarity(kmers[left], kmers[right])
            if similarity >= threshold:
                rows.append(
                    {
                        "index_a": int(frame.at[left, "index"]),
                        "index_b": int(frame.at[right, "index"]),
                        "sequence_a": frame.at[left, "_normalized_sequence"],
                        "sequence_b": frame.at[right, "_normalized_sequence"],
                        "jaccard_similarity": float(similarity),
                    }
                )
                if max_pairs is not None and len(rows) >= max_pairs:
                    return pd.DataFrame(rows)
    return pd.DataFrame(
        rows,
        columns=["index_a", "index_b", "sequence_a", "sequence_b", "jaccard_similarity"],
    )


def assign_stratified_folds(
    df: pd.DataFrame,
    label_col: str = "label",
    n_splits: int = 5,
    shuffle: bool = True,
    random_state: int = 42,
) -> pd.DataFrame:
    """Return a copy of the frame with reconstructed stratified fold IDs."""
    if label_col not in df.columns:
        raise ValueError(f"Missing label column: {label_col}")

    frame = df.copy()
    labels = frame[label_col]
    splitter = StratifiedKFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
    frame["fold_id"] = -1
    for fold_id, (_, test_index) in enumerate(splitter.split(frame, labels), start=1):
        frame.loc[frame.index[test_index], "fold_id"] = fold_id
    return frame


def summarize_cross_fold_similarity(
    df_with_folds: pd.DataFrame,
    sequence_col: str = "sequence",
    fold_col: str = "fold_id",
    k: int = 3,
    threshold: float = 0.8,
    max_pairs: int | None = None,
) -> pd.DataFrame:
    """Find high-similarity sequence pairs that appear in different folds."""
    if fold_col not in df_with_folds.columns:
        raise ValueError(f"Missing fold column: {fold_col}")

    pairs = find_high_jaccard_pairs(
        df_with_folds,
        sequence_col=sequence_col,
        k=k,
        threshold=threshold,
        max_pairs=max_pairs,
    )
    if pairs.empty:
        pairs["fold_a"] = []
        pairs["fold_b"] = []
        pairs["fold_pair"] = []
        return pairs

    pairs["fold_a"] = pairs["index_a"].map(df_with_folds[fold_col])
    pairs["fold_b"] = pairs["index_b"].map(df_with_folds[fold_col])
    pairs = pairs[pairs["fold_a"] != pairs["fold_b"]].copy()
    pairs["fold_pair"] = pairs.apply(
        lambda row: f"{min(row['fold_a'], row['fold_b'])}-{max(row['fold_a'], row['fold_b'])}",
        axis=1,
    )
    return pairs.reset_index(drop=True)


def summarize_source_group_distribution(
    df: pd.DataFrame,
    source_col: str = "source",
    fold_col: str = "fold_id",
) -> pd.DataFrame:
    """Summarize how source/group labels are distributed across folds."""
    if source_col not in df.columns:
        return pd.DataFrame(
            [
                {
                    "source": "",
                    "fold_id": "",
                    "count": 0,
                    "fold_count_for_source": 0,
                    "caveat": f"Source column missing: {source_col}",
                }
            ]
        )
    if fold_col not in df.columns:
        raise ValueError(f"Missing fold column: {fold_col}")

    counts = (
        df.groupby([source_col, fold_col], dropna=False)
        .size()
        .reset_index(name="count")
        .rename(columns={source_col: "source", fold_col: "fold_id"})
    )
    fold_counts = counts.groupby("source")["fold_id"].nunique().rename("fold_count_for_source")
    summary = counts.merge(fold_counts, on="source", how="left")
    summary["caveat"] = summary["fold_count_for_source"].map(
        lambda count: "source spans multiple folds" if count > 1 else ""
    )
    return summary


def run_leakage_audit(
    input_path: str | Path,
    output_dir: str | Path,
    sequence_col: str = "sequence",
    label_col: str = "label",
    source_col: str = "source",
    n_splits: int = 5,
    random_state: int = 42,
    kmer_size: int = 3,
    jaccard_threshold: float = 0.8,
    max_pairs: int | None = 10000,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run the leakage audit or return a dry-run execution plan."""
    frame = load_dataset(input_path)
    planned = [str(Path(output_dir) / filename) for filename in PLANNED_OUTPUTS]

    if dry_run:
        return {
            "dry_run": True,
            "input_path": str(input_path),
            "row_count": int(len(frame)),
            "columns": list(frame.columns),
            "planned_outputs": planned,
            "outputs_written": [],
        }

    frame_with_folds = assign_stratified_folds(
        frame,
        label_col=label_col,
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state,
    )
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    duplicates = find_exact_duplicates(frame, sequence_col=sequence_col, label_col=label_col)
    conflicts = find_label_conflicts(frame, sequence_col=sequence_col, label_col=label_col)
    near_duplicates = find_near_duplicates(frame, sequence_col=sequence_col, max_distance=1, max_pairs=max_pairs)
    high_similarity = find_high_jaccard_pairs(
        frame,
        sequence_col=sequence_col,
        k=kmer_size,
        threshold=jaccard_threshold,
        max_pairs=max_pairs,
    )
    cross_fold = summarize_cross_fold_similarity(
        frame_with_folds,
        sequence_col=sequence_col,
        fold_col="fold_id",
        k=kmer_size,
        threshold=jaccard_threshold,
        max_pairs=max_pairs,
    )
    source_summary = summarize_source_group_distribution(
        frame_with_folds,
        source_col=source_col,
        fold_col="fold_id",
    )

    outputs = {
        "sequence_duplicate_audit.csv": duplicates,
        "label_conflict_audit.csv": conflicts,
        "near_duplicate_pairs.csv": near_duplicates,
        "sequence_similarity_summary.csv": high_similarity,
        "fold_similarity_leakage_summary.csv": cross_fold,
        "source_group_leakage_summary.csv": source_summary,
    }
    for filename, table in outputs.items():
        table.to_csv(output_path / filename, index=False)

    summary = {
        "dry_run": False,
        "input_path": str(input_path),
        "row_count": int(len(frame)),
        "duplicate_sequence_groups": int(len(duplicates)),
        "label_conflict_groups": int(len(conflicts)),
        "near_duplicate_pairs": int(len(near_duplicates)),
        "high_jaccard_pairs": int(len(high_similarity)),
        "cross_fold_high_similarity_pairs": int(len(cross_fold)),
        "source_group_rows": int(len(source_summary)),
        "outputs_written": [str(output_path / filename) for filename in PLANNED_OUTPUTS],
    }
    with open(output_path / "leakage_audit_summary.json", "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
    return summary

