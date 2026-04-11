"""Physicochemical feature extraction.

Some descriptors here are simplified approximations for v0.1 baseline use.
They are intended for transparent benchmarking, not for biochemical closure.
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd

_HYDROPATHY = {
    "A": 1.8,
    "C": 2.5,
    "D": -3.5,
    "E": -3.5,
    "F": 2.8,
    "G": -0.4,
    "H": -3.2,
    "I": 4.5,
    "K": -3.9,
    "L": 3.8,
    "M": 1.9,
    "N": -3.5,
    "P": -1.6,
    "Q": -3.5,
    "R": -4.5,
    "S": -0.8,
    "T": -0.7,
    "V": 4.2,
    "W": -0.9,
    "Y": -1.3,
}

_AROMATIC = set("FWY")
_POSITIVE = set("KRH")
_NEGATIVE = set("DE")


def _mean(values: Iterable[float]) -> float:
    """Return a safe mean for a sequence of values."""
    values = list(values)
    return float(sum(values) / len(values)) if values else 0.0


def _charge(sequence: str) -> float:
    """Compute a simple net-charge approximation."""
    return float(sum(residue in _POSITIVE for residue in sequence) - sum(residue in _NEGATIVE for residue in sequence))


def _aromaticity(sequence: str) -> float:
    """Compute fraction of aromatic residues."""
    return float(sum(residue in _AROMATIC for residue in sequence) / len(sequence)) if sequence else 0.0


def _gravy(sequence: str) -> float:
    """Compute a simple hydropathy average."""
    return _mean(_HYDROPATHY.get(residue, 0.0) for residue in sequence)


def _isoelectric_point_placeholder(sequence: str) -> float:
    """Return a coarse pI proxy from net charge and sequence length.

    This is a placeholder approximation for v0.1 and should not be treated
    as a robust biochemical pI calculation.
    """
    if not sequence:
        return 7.0
    return float(7.0 + (_charge(sequence) / max(len(sequence), 1)) * 3.0)


def add_physicochemical_features(
    frame: pd.DataFrame,
    sequence_column: str = "sequence",
) -> pd.DataFrame:
    """Add lightweight deterministic physicochemical features."""
    result = frame.copy()
    if sequence_column in result.columns:
        sequences = result[sequence_column].fillna("").astype(str).str.upper()
        result["charge"] = sequences.map(_charge)
        result["aromaticity"] = sequences.map(_aromaticity)
        result["gravy"] = sequences.map(_gravy)
        result["pI"] = sequences.map(_isoelectric_point_placeholder)
    return result
