"""Leakage-aware split manifest utilities.

These helpers assign fold IDs from existing group assignments. They do not
train models, compute performance metrics, or establish robust generalization.
"""

from __future__ import annotations

import json
import hashlib
from pathlib import Path
from typing import Any

import pandas as pd


REQUIRED_GROUP_COLUMNS = {"row_index", "group_id"}
SPLIT_POLICY = "leakage_aware_group_stratified"


def load_group_assignments(path: str | Path) -> pd.DataFrame:
    """Load group assignments and validate required columns."""
    group_path = Path(path)
    if not group_path.exists():
        raise FileNotFoundError(f"Group assignment file not found: {group_path}")

    frame = pd.read_csv(group_path)
    missing = sorted(REQUIRED_GROUP_COLUMNS - set(frame.columns))
    if missing:
        raise ValueError(f"Missing required group assignment columns: {missing}")
    return frame


def attach_labels_to_groups(
    dataset_df: pd.DataFrame,
    group_df: pd.DataFrame,
    label_col: str = "label",
) -> pd.DataFrame:
    """Attach dataset labels to row-level group assignments by row index."""
    if label_col not in dataset_df.columns:
        raise ValueError(f"Missing label column: {label_col}")
    if "row_index" not in group_df.columns:
        raise ValueError("Missing group assignment column: row_index")
    if group_df["row_index"].duplicated().any():
        raise ValueError("Group assignments contain duplicate row_index values")
    if len(dataset_df) != len(group_df):
        raise ValueError("Dataset and group assignment row counts differ")

    max_index = len(dataset_df) - 1
    invalid = group_df[(group_df["row_index"] < 0) | (group_df["row_index"] > max_index)]
    if not invalid.empty:
        raise ValueError("Group assignments contain row_index values outside dataset bounds")

    labels = dataset_df.reset_index(drop=True).reset_index().rename(columns={"index": "row_index"})
    labels = labels[["row_index", label_col]]
    merged = group_df.copy().merge(labels, on="row_index", how="left", validate="one_to_one")
    if merged[label_col].isna().any():
        raise ValueError("Missing labels after attaching dataset labels to groups")
    return merged


def summarize_groups_for_splitting(
    group_df_with_labels: pd.DataFrame,
    label_col: str = "label",
) -> pd.DataFrame:
    """Summarize row-level assignments into group-level split inputs."""
    required = {"group_id", label_col}
    missing = sorted(required - set(group_df_with_labels.columns))
    if missing:
        raise ValueError(f"Missing required columns for group summary: {missing}")

    rows: list[dict[str, Any]] = []
    for group_id, group in group_df_with_labels.groupby("group_id", sort=True, dropna=False):
        labels = group[label_col].astype(int)
        positive_count = int((labels == 1).sum())
        negative_count = int((labels == 0).sum())
        labels_present = sorted(str(label) for label in labels.unique())
        majority_label = 1 if positive_count >= negative_count else 0
        rows.append(
            {
                "group_id": group_id,
                "group_size": int(len(group)),
                "positive_count": positive_count,
                "negative_count": negative_count,
                "majority_label": int(majority_label),
                "labels_present": "|".join(labels_present),
            }
        )
    return pd.DataFrame(
        rows,
        columns=[
            "group_id",
            "group_size",
            "positive_count",
            "negative_count",
            "majority_label",
            "labels_present",
        ],
    )


def assign_group_stratified_folds(
    group_summary_df: pd.DataFrame,
    n_splits: int = 5,
    random_state: int = 42,
) -> pd.DataFrame:
    """Assign each group to one fold with a deterministic stratification heuristic."""
    if n_splits < 2:
        raise ValueError("n_splits must be at least 2")
    required = {"group_id", "group_size", "positive_count", "negative_count"}
    missing = sorted(required - set(group_summary_df.columns))
    if missing:
        raise ValueError(f"Missing required group summary columns: {missing}")
    if len(group_summary_df) < n_splits:
        raise ValueError("Number of groups must be at least n_splits")

    frame = group_summary_df.copy()
    # Stable pseudo-random tie-breaker lets random_state affect equivalent groups
    # without making assignments non-reproducible.
    frame["_tie_breaker"] = frame["group_id"].map(
        lambda group_id: int(
            hashlib.sha256(f"{random_state}:{group_id}".encode("utf-8")).hexdigest()[:12],
            16,
        )
    )
    frame["_imbalance"] = (frame["positive_count"] - frame["negative_count"]).abs()
    frame["_bucket"] = frame.apply(
        lambda row: (
            "mixed"
            if int(row["positive_count"]) > 0 and int(row["negative_count"]) > 0
            else "positive"
            if int(row["positive_count"]) > 0
            else "negative"
        ),
        axis=1,
    )

    fold_state = {
        fold_id: {"rows": 0, "positive": 0, "negative": 0, "groups": 0}
        for fold_id in range(1, n_splits + 1)
    }
    assignments: list[dict[str, Any]] = []

    bucket_order = ["mixed", "positive", "negative"]
    ordered_parts = [
        frame[frame["_bucket"] == bucket].sort_values(
            ["group_size", "_imbalance", "_tie_breaker", "group_id"],
            ascending=[False, False, True, True],
        )
        for bucket in bucket_order
    ]
    ordered = pd.concat(ordered_parts, ignore_index=True)

    for _, row in ordered.iterrows():
        best_fold = 1
        best_score: tuple[int, int, int, int] | None = None
        for fold_id, state in fold_state.items():
            if row["_bucket"] == "positive":
                score = (state["positive"], state["rows"], state["groups"], fold_id)
            elif row["_bucket"] == "negative":
                score = (state["negative"], state["rows"], state["groups"], fold_id)
            else:
                score = (state["rows"], state["positive"] + state["negative"], state["groups"], fold_id)
            if best_score is None or score < best_score:
                best_score = score
                best_fold = fold_id

        fold_state[best_fold]["positive"] += int(row["positive_count"])
        fold_state[best_fold]["negative"] += int(row["negative_count"])
        fold_state[best_fold]["rows"] += int(row["group_size"])
        fold_state[best_fold]["groups"] += 1
        assignments.append({"group_id": row["group_id"], "fold_id": best_fold})

    return pd.DataFrame(assignments, columns=["group_id", "fold_id"]).sort_values("group_id").reset_index(drop=True)


def build_split_manifest(
    dataset_df: pd.DataFrame,
    group_df: pd.DataFrame,
    group_to_fold: pd.DataFrame,
    label_col: str = "label",
    sequence_id_col: str = "sequence_id",
) -> pd.DataFrame:
    """Build a row-level split manifest from groups and fold assignments."""
    if label_col not in dataset_df.columns:
        raise ValueError(f"Missing label column: {label_col}")

    frame = group_df.copy()
    if sequence_id_col in frame.columns:
        frame = frame.drop(columns=[sequence_id_col])
    frame = frame.merge(group_to_fold, on="group_id", how="left", validate="many_to_one")
    if frame["fold_id"].isna().any():
        raise ValueError("Missing fold assignment for at least one group")

    dataset = dataset_df.reset_index(drop=True).reset_index().rename(columns={"index": "row_index"})
    columns = ["row_index", label_col]
    if sequence_id_col in dataset.columns:
        columns.append(sequence_id_col)
    dataset = dataset[columns]
    frame = frame.merge(dataset, on="row_index", how="left", validate="one_to_one")
    if frame[label_col].isna().any():
        raise ValueError("Missing label for at least one split manifest row")

    if sequence_id_col not in frame.columns:
        frame[sequence_id_col] = ""
    if "group_size" not in frame.columns:
        sizes = frame.groupby("group_id").size().rename("group_size")
        frame = frame.merge(sizes, on="group_id", how="left", validate="many_to_one")
    if "grouping_method" not in frame.columns:
        frame["grouping_method"] = ""

    manifest = pd.DataFrame(
        {
            "row_index": frame["row_index"].astype(int),
            "sequence_id": frame[sequence_id_col],
            "label": frame[label_col].astype(int),
            "group_id": frame["group_id"],
            "fold_id": frame["fold_id"].astype(int),
            "split_policy": SPLIT_POLICY,
            "group_size": frame["group_size"].astype(int),
            "grouping_method": frame["grouping_method"],
        }
    )
    return manifest.sort_values("row_index").reset_index(drop=True)


def summarize_split_manifest(split_manifest_df: pd.DataFrame, label_col: str = "label") -> dict[str, Any]:
    """Summarize row and group balance in a split manifest."""
    required = {"group_id", "fold_id", label_col, "group_size"}
    missing = sorted(required - set(split_manifest_df.columns))
    if missing:
        raise ValueError(f"Missing required split manifest columns: {missing}")

    group_folds = split_manifest_df.groupby("group_id")["fold_id"].nunique()
    crossing_groups = sorted(str(group_id) for group_id, count in group_folds.items() if count > 1)
    fold_counts = split_manifest_df.groupby("fold_id").size().sort_index()
    fold_label_table = (
        split_manifest_df.groupby(["fold_id", label_col]).size().unstack(fill_value=0).sort_index()
    )
    group_counts = split_manifest_df.groupby("fold_id")["group_id"].nunique().sort_index()
    largest_group = split_manifest_df.groupby("fold_id")["group_size"].max().sort_index()
    positive_rates = split_manifest_df.groupby("fold_id")[label_col].mean().sort_index()

    caveats = []
    if crossing_groups:
        caveats.append("At least one group crosses folds; manifest should not be used for group-aware reruns.")
    if int(split_manifest_df["group_size"].max()) > 1:
        caveats.append("At least one non-singleton group is kept within one fold.")

    return {
        "number_of_rows": int(len(split_manifest_df)),
        "number_of_groups": int(split_manifest_df["group_id"].nunique()),
        "n_splits": int(split_manifest_df["fold_id"].nunique()),
        "fold_counts": {str(int(key)): int(value) for key, value in fold_counts.items()},
        "fold_label_counts": {
            str(int(fold_id)): {str(label): int(count) for label, count in row.items()}
            for fold_id, row in fold_label_table.to_dict(orient="index").items()
        },
        "positive_rate_by_fold": {
            str(int(key)): float(value) for key, value in positive_rates.items()
        },
        "group_counts_by_fold": {str(int(key)): int(value) for key, value in group_counts.items()},
        "largest_group_size_by_fold": {str(int(key)): int(value) for key, value in largest_group.items()},
        "groups_crossing_folds": int(len(crossing_groups)),
        "crossing_group_ids": crossing_groups,
        "caveats": caveats,
    }


def export_split_manifest(
    split_manifest_df: pd.DataFrame,
    summary: dict[str, Any],
    output_dir: str | Path,
    prefix: str = "combined_group_stratified",
) -> tuple[Path, Path]:
    """Write split manifest CSV and summary JSON when explicitly called."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    manifest_path = output_path / f"{prefix}_split_manifest.csv"
    summary_path = output_path / f"{prefix}_split_summary.json"
    split_manifest_df.to_csv(manifest_path, index=False)
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
    return manifest_path, summary_path
