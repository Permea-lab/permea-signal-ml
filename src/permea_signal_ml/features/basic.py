"""Basic sequence features."""

from __future__ import annotations

import pandas as pd


def add_basic_features(
    frame: pd.DataFrame,
    sequence_column: str = "sequence",
) -> pd.DataFrame:
    """Add simple deterministic basic features."""
    result = frame.copy()
    if sequence_column in result.columns:
        sequence = result[sequence_column].fillna("").astype(str)
        result["length"] = sequence.str.len()
    return result
