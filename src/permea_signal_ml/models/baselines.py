"""Baseline model registry."""

from __future__ import annotations
from logging import config

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def build_baseline_model(config: dict[str, object]) -> object:
    """Build a supported baseline model from config."""
    model_name = str(config["model_name"])

    if model_name == "dummy":
        return DummyClassifier(
            strategy=str(config.get("strategy", "most_frequent"))
        )

    if model_name == "logistic_regression":
        kwargs = {
        "C": float(config.get("C", 1.0)),
        "max_iter": int(config.get("max_iter", 1000)),
        "class_weight": config.get("class_weight"),
        "random_state": int(config.get("random_state", 42)),}

        penalty = config.get("penalty")
        # Avoid passing the default L2 penalty explicitly to prevent
        # scikit-learn penalty deprecation warnings.
        if penalty not in (None, "l2"):
            kwargs["penalty"] = str(penalty)

        return LogisticRegression(**kwargs)

    if model_name == "random_forest":
        return RandomForestClassifier(
            n_estimators=int(config.get("n_estimators", 200)),
            max_depth=config.get("max_depth"),
            min_samples_split=int(config.get("min_samples_split", 2)),
            class_weight=config.get("class_weight"),
            random_state=int(config.get("random_state", 42)),
        )

    raise ValueError(f"Unsupported model_name: {model_name}")
