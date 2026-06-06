from __future__ import annotations

import sys
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.models.baselines import build_baseline_model


def test_logistic_regression_penalty_warning_is_known() -> None:
    model = build_baseline_model(
        {
            "model_name": "logistic_regression",
            "penalty": "l2",
            "C": 1.0,
            "max_iter": 1000,
            "class_weight": "balanced",
            "random_state": 42,
        }
    )

    X = [
        [0.1, 0.0, 0.2, 6.0, 0.0],
        [0.2, 1.0, -0.1, 8.0, 0.2],
        [0.3, -1.0, 0.3, 5.8, 0.1],
        [0.4, 2.0, -0.2, 8.2, 0.3],
    ]
    y = [0, 1, 0, 1]

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        model.fit(X, y)

    messages = [str(item.message) for item in caught]
    assert any("'penalty' was deprecated" in message for message in messages)
