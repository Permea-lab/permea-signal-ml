"""Dataset validation helpers."""

from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = ("sequence_id", "sequence", "label", "source")


def validate_columns(frame: pd.DataFrame) -> list[str]:
    """Return missing required columns."""
    return [column for column in REQUIRED_COLUMNS if column not in frame.columns]


def validate_required_columns(frame: pd.DataFrame, required_columns: list[str]) -> None:
    """Raise if the required columns are missing."""
    missing = [column for column in required_columns if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_binary_labels(frame: pd.DataFrame, label_column: str) -> None:
    """Raise if labels are not binary-compatible."""
    labels = pd.Series(frame[label_column]).dropna().unique().tolist()
    if len(labels) != 2:
        raise ValueError(f"Expected exactly 2 label values, found {labels}")
