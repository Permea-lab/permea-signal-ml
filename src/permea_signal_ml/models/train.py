"""Training helpers."""

from __future__ import annotations


def train_model(model: object, x_train, y_train) -> object:
    """Fit a model and return it."""
    model.fit(x_train, y_train)
    return model
