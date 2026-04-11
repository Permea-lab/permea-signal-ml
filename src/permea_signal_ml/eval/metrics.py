"""Metric computation helpers."""

from __future__ import annotations

import math
from typing import Iterable

from sklearn.metrics import (
    average_precision_score,
    f1_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
    roc_auc_score,
)


def _safe_metric(metric_fn, *args) -> float:
    """Compute a metric and return NaN on undefined cases."""
    try:
        return float(metric_fn(*args))
    except ValueError:
        return math.nan


def compute_binary_metrics(y_true, y_pred, y_score) -> dict[str, float]:
    """Compute the v0.1 binary-classification metric set."""
    return {
        "roc_auc": _safe_metric(roc_auc_score, y_true, y_score),
        "pr_auc": _safe_metric(average_precision_score, y_true, y_score),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "mcc": float(matthews_corrcoef(y_true, y_pred)),
    }


def aggregate_metrics(fold_metrics: Iterable[dict[str, float]]) -> dict[str, float]:
    """Return mean metrics across folds."""
    fold_metrics = list(fold_metrics)
    metric_names = ["roc_auc", "pr_auc", "precision", "recall", "f1", "mcc"]
    return {
        metric_name: float(
            sum(metric[metric_name] for metric in fold_metrics) / len(fold_metrics)
        )
        for metric_name in metric_names
    }
