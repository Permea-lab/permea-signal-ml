"""Dataset assembly helpers."""

from __future__ import annotations

import pandas as pd


def assemble_dataset(frame: pd.DataFrame) -> pd.DataFrame:
    """Return a shallow copy of the input frame as a placeholder."""
    return frame.copy()
