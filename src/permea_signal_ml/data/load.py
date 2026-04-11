"""Dataset loading helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_table(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset into a DataFrame."""
    return pd.read_csv(Path(path))
