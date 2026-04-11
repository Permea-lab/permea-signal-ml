"""Run manifest model."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class RunManifest:
    """Manifest for a benchmarked baseline run."""

    run_id: str
    dataset_name: str
    dataset_version: str | None
    feature_config: str
    model_name: str
    model_config: str
    split_policy: str
    random_seed: int
    metrics_file: str
    predictions_file: str
    ranking_file: str
    generated_at: str
    summary_file: str | None = None
    figure_file: str | None = None

    def to_dict(self) -> dict[str, object]:
        """Return a serializable dictionary."""
        return asdict(self)
