"""Leakage-aware sequence grouping utilities.

These helpers build group assignments for future sensitivity analysis. They do
not assign folds, train models, compute performance metrics, or establish that
the benchmark is leakage-free.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd

from permea_signal_ml.audits.leakage import (
    edit_distance as _edit_distance,
    jaccard_similarity as _jaccard_similarity,
    kmer_set as _kmer_set,
    normalize_sequence,
)


GROUP_ASSIGNMENT_COLUMNS = [
    "row_index",
    "sequence_id",
    "normalized_sequence",
    "group_id",
    "group_type",
    "group_size",
    "grouping_method",
    "methods_contributing",
]


class _UnionFind:
    """Small deterministic union-find for connected-component grouping."""

    def __init__(self, nodes: list[int]) -> None:
        self.parent = {node: node for node in nodes}

    def find(self, node: int) -> int:
        parent = self.parent[node]
        if parent != node:
            self.parent[node] = self.find(parent)
        return self.parent[node]

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        lower, higher = sorted((root_left, root_right))
        self.parent[higher] = lower


def normalize_sequence_for_grouping(seq: object) -> str:
    """Return the normalized sequence string used for grouping."""
    return normalize_sequence(seq)


def edit_distance(a: str, b: str, max_distance: int | None = None) -> int:
    """Compute Levenshtein edit distance with optional early stopping."""
    return _edit_distance(a, b, max_distance=max_distance)


def kmer_set(seq: str, k: int) -> set[str]:
    """Return the k-mer set for a normalized sequence."""
    return _kmer_set(seq, k=k)


def jaccard_similarity(a: set[str], b: set[str]) -> float:
    """Compute Jaccard similarity between two k-mer sets."""
    return _jaccard_similarity(a, b)


def _prepare_frame(df: pd.DataFrame, sequence_col: str) -> pd.DataFrame:
    if sequence_col not in df.columns:
        raise ValueError(f"Missing sequence column: {sequence_col}")

    frame = df.copy().reset_index(drop=False).rename(columns={"index": "row_index"})
    frame["normalized_sequence"] = frame[sequence_col].map(normalize_sequence_for_grouping)
    if "sequence_id" not in frame.columns:
        frame["sequence_id"] = ""
    return frame


def _component_assignments(
    frame: pd.DataFrame,
    edges: list[tuple[int, int, str]],
    group_type: str,
    grouping_method: str,
    caveats: list[str] | None = None,
) -> pd.DataFrame:
    nodes = list(range(len(frame)))
    union_find = _UnionFind(nodes)
    edge_methods: dict[int, set[str]] = defaultdict(set)

    for left, right, method in edges:
        union_find.union(left, right)
        root = union_find.find(left)
        edge_methods[root].add(method)

    components: dict[int, list[int]] = defaultdict(list)
    for node in nodes:
        components[union_find.find(node)].append(node)

    ordered_components = sorted(components.values(), key=lambda members: (min(members), len(members)))
    component_for_node: dict[int, tuple[str, int, str]] = {}
    for component_number, members in enumerate(ordered_components, start=1):
        roots = {union_find.find(member) for member in members}
        methods = sorted({method for root in roots for method in edge_methods.get(root, set())})
        if not methods:
            methods = [grouping_method]
        method_text = "|".join(methods)
        group_id = f"{group_type}_{component_number:05d}"
        for member in members:
            component_for_node[member] = (group_id, len(members), method_text)

    rows: list[dict[str, Any]] = []
    for node, row in frame.iterrows():
        group_id, group_size, methods = component_for_node[int(node)]
        rows.append(
            {
                "row_index": int(row["row_index"]),
                "sequence_id": row.get("sequence_id", ""),
                "normalized_sequence": row["normalized_sequence"],
                "group_id": group_id,
                "group_type": group_type,
                "group_size": int(group_size),
                "grouping_method": grouping_method,
                "methods_contributing": methods,
            }
        )

    result = pd.DataFrame(rows, columns=GROUP_ASSIGNMENT_COLUMNS)
    result.attrs["grouping_method"] = grouping_method
    result.attrs["caveats"] = caveats or []
    return result


def build_exact_duplicate_groups(df: pd.DataFrame, sequence_col: str = "sequence") -> pd.DataFrame:
    """Return row-level group assignments for identical normalized sequences."""
    frame = _prepare_frame(df, sequence_col)
    buckets: dict[str, list[int]] = defaultdict(list)
    for node, sequence in enumerate(frame["normalized_sequence"]):
        buckets[sequence].append(node)

    edges: list[tuple[int, int, str]] = []
    for members in buckets.values():
        first = members[0]
        for member in members[1:]:
            edges.append((first, member, "exact_duplicate"))

    return _component_assignments(
        frame,
        edges=edges,
        group_type="exact_duplicate",
        grouping_method="exact_duplicate",
    )


def _pair_indices(row_count: int, max_pairs: int | None) -> tuple[list[tuple[int, int]], bool]:
    pairs: list[tuple[int, int]] = []
    truncated = False
    for left in range(row_count):
        for right in range(left + 1, row_count):
            if max_pairs is not None and len(pairs) >= max_pairs:
                return pairs, True
            pairs.append((left, right))
    return pairs, truncated


def build_near_duplicate_graph_groups(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    max_distance: int = 1,
    max_pairs: int | None = None,
) -> pd.DataFrame:
    """Group rows by edit-distance connected components."""
    if max_distance < 0:
        raise ValueError("max_distance must be non-negative")

    frame = _prepare_frame(df, sequence_col)
    pairs, truncated = _pair_indices(len(frame), max_pairs=max_pairs)
    sequences = list(frame["normalized_sequence"])
    edges: list[tuple[int, int, str]] = []

    for left, right in pairs:
        distance = edit_distance(sequences[left], sequences[right], max_distance=max_distance)
        if distance <= max_distance:
            edges.append((left, right, f"edit_distance<={max_distance}"))

    caveats = []
    if truncated:
        caveats.append(f"Pairwise comparison stopped after max_pairs={max_pairs}; grouping may be incomplete.")

    return _component_assignments(
        frame,
        edges=edges,
        group_type="near_duplicate",
        grouping_method=f"near_duplicate_edit_distance<={max_distance}",
        caveats=caveats,
    )


def build_kmer_jaccard_groups(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    k: int = 3,
    threshold: float = 0.8,
    max_pairs: int | None = None,
) -> pd.DataFrame:
    """Group rows by k-mer Jaccard connected components."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    frame = _prepare_frame(df, sequence_col)
    pairs, truncated = _pair_indices(len(frame), max_pairs=max_pairs)
    kmers = [kmer_set(sequence, k=k) for sequence in frame["normalized_sequence"]]
    edges: list[tuple[int, int, str]] = []

    for left, right in pairs:
        similarity = jaccard_similarity(kmers[left], kmers[right])
        if similarity >= threshold:
            edges.append((left, right, f"kmer_jaccard>={threshold:g}"))

    caveats = []
    if truncated:
        caveats.append(f"Pairwise comparison stopped after max_pairs={max_pairs}; grouping may be incomplete.")

    return _component_assignments(
        frame,
        edges=edges,
        group_type="kmer_jaccard",
        grouping_method=f"kmer{k}_jaccard>={threshold:g}",
        caveats=caveats,
    )


def build_combined_similarity_groups(
    df: pd.DataFrame,
    sequence_col: str = "sequence",
    edit_distance_threshold: int = 1,
    k: int = 3,
    jaccard_threshold: float = 0.8,
    max_pairs: int | None = None,
) -> pd.DataFrame:
    """Group rows using exact, edit-distance, and k-mer Jaccard edges."""
    if edit_distance_threshold < 0:
        raise ValueError("edit_distance_threshold must be non-negative")
    if not 0 <= jaccard_threshold <= 1:
        raise ValueError("jaccard_threshold must be between 0 and 1")

    frame = _prepare_frame(df, sequence_col)
    pairs, truncated = _pair_indices(len(frame), max_pairs=max_pairs)
    sequences = list(frame["normalized_sequence"])
    kmers = [kmer_set(sequence, k=k) for sequence in sequences]
    edges: list[tuple[int, int, str]] = []

    for left, right in pairs:
        if sequences[left] == sequences[right]:
            edges.append((left, right, "exact_duplicate"))
            continue
        distance = edit_distance(
            sequences[left],
            sequences[right],
            max_distance=edit_distance_threshold,
        )
        if distance <= edit_distance_threshold:
            edges.append((left, right, f"edit_distance<={edit_distance_threshold}"))
        similarity = jaccard_similarity(kmers[left], kmers[right])
        if similarity >= jaccard_threshold:
            edges.append((left, right, f"kmer_jaccard>={jaccard_threshold:g}"))

    caveats = []
    if truncated:
        caveats.append(f"Pairwise comparison stopped after max_pairs={max_pairs}; grouping may be incomplete.")

    return _component_assignments(
        frame,
        edges=edges,
        group_type="combined_similarity",
        grouping_method=(
            "combined_exact"
            f"+edit_distance<={edit_distance_threshold}"
            f"+kmer{k}_jaccard>={jaccard_threshold:g}"
        ),
        caveats=caveats,
    )


def summarize_grouping(group_df: pd.DataFrame) -> dict[str, Any]:
    """Summarize a group assignment table."""
    if group_df.empty:
        return {
            "number_of_rows": 0,
            "number_of_groups": 0,
            "singleton_groups": 0,
            "non_singleton_groups": 0,
            "largest_group_size": 0,
            "grouping_method": group_df.attrs.get("grouping_method", ""),
            "caveats": group_df.attrs.get("caveats", []),
        }

    group_sizes = group_df.groupby("group_id", dropna=False).size()
    return {
        "number_of_rows": int(len(group_df)),
        "number_of_groups": int(len(group_sizes)),
        "singleton_groups": int((group_sizes == 1).sum()),
        "non_singleton_groups": int((group_sizes > 1).sum()),
        "largest_group_size": int(group_sizes.max()),
        "grouping_method": group_df.attrs.get("grouping_method", group_df["grouping_method"].iloc[0]),
        "caveats": group_df.attrs.get("caveats", []),
    }


def assess_source_group_feasibility(df: pd.DataFrame, source_col: str = "source") -> dict[str, Any]:
    """Assess whether the source column can support source-aware splitting."""
    if source_col not in df.columns:
        return {
            "source_col_present": False,
            "number_of_unique_sources": 0,
            "source_counts": {},
            "feasible_for_group_split": False,
            "caveat": f"Source column missing: {source_col}",
        }

    counts = df[source_col].fillna("").astype(str).value_counts(dropna=False).sort_index()
    unique_count = int(len(counts))
    feasible = unique_count > 1
    caveat = (
        "Multiple source values are present; inspect class balance before using source-aware split."
        if feasible
        else "Source field is too coarse for source-aware group splitting."
    )
    return {
        "source_col_present": True,
        "number_of_unique_sources": unique_count,
        "source_counts": {str(key): int(value) for key, value in counts.items()},
        "feasible_for_group_split": bool(feasible),
        "caveat": caveat,
    }


def export_group_assignments(group_df: pd.DataFrame, output_path: str | Path) -> None:
    """Write group assignments to CSV when explicitly called."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    group_df.to_csv(path, index=False)


def write_grouping_summary(summary: dict[str, Any], output_path: str | Path) -> None:
    """Write a grouping summary JSON when explicitly called."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
