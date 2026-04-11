"""Minimal plotting helpers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_placeholder_plot(path: str | Path, title: str = "Placeholder Plot") -> None:
    """Save a minimal placeholder figure."""
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.plot([0, 1], [0, 1])
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def save_score_distribution_figure(
    frame: pd.DataFrame,
    path: str | Path,
    score_column: str = "predicted_score",
    label_column: str = "true_label",
) -> None:
    """Save a simple score-distribution histogram by true label."""
    fig, ax = plt.subplots(figsize=(6, 4))
    for label_value in sorted(frame[label_column].unique()):
        subset = frame.loc[frame[label_column] == label_value, score_column]
        ax.hist(subset, bins=10, alpha=0.6, label=f"label={label_value}")
    ax.set_xlabel("Predicted score")
    ax.set_ylabel("Count")
    ax.set_title("Predicted score distribution")
    ax.legend()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
