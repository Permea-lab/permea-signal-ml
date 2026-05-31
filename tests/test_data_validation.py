from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.data.validate import REQUIRED_COLUMNS, validate_required_columns


def test_sequence_dataset_with_required_columns_passes_validation() -> None:
    frame = pd.DataFrame(
        {
            "sequence_id": ["seq-1"],
            "sequence": ["ACDEFGHIK"],
            "label": [1],
            "source": ["synthetic"],
        }
    )

    validate_required_columns(frame, list(REQUIRED_COLUMNS))


def test_sequence_dataset_missing_sequence_column_is_rejected() -> None:
    frame = pd.DataFrame(
        {
            "sequence_id": ["seq-1"],
            "label": [1],
            "source": ["synthetic"],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns: \\['sequence'\\]"):
        validate_required_columns(frame, list(REQUIRED_COLUMNS))
