"""Inference helpers."""

from __future__ import annotations

import numpy as np


def predict_scores(model: object, x):
    """Return positive-class scores when available."""
    if hasattr(model, "predict_proba"):
        return model.predict_proba(x)[:, 1]
    if hasattr(model, "decision_function"):
        return np.asarray(model.decision_function(x))
    return np.asarray(model.predict(x))
