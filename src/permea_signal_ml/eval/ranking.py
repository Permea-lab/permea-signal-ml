"""Candidate ranking helpers."""

from __future__ import annotations

import pandas as pd


def rank_candidates(
    frame: pd.DataFrame,
    score_column: str = "predicted_score",
    id_column: str = "sequence_id",
) -> pd.DataFrame:
    """Return candidates sorted by descending score with explicit rank."""
    ranking = frame[[id_column, score_column]].copy()
    ranking = ranking.sort_values(score_column, ascending=False).reset_index(drop=True)
    ranking["rank"] = ranking.index + 1
    return ranking[[id_column, score_column, "rank"]]
