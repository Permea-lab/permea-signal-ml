"""Generate simple repository and paper-support figures.

This script produces a small set of publication-adjacent figures from
existing repository artifacts without introducing additional modeling logic.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"


def ensure_figures_dir() -> None:
    """Ensure the figures directory exists."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def save_dataset_distribution() -> Path:
    """Create the dataset distribution figure from known onboarding counts."""
    labels = ["Positive", "Negative"]
    values = [269, 2690]

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(labels, values)
    ax.set_title("Initial BBB Dataset Distribution")
    ax.set_ylabel("Count")
    ax.set_ylim(0, max(values) * 1.15)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + max(values) * 0.02,
            str(value),
            ha="center",
            va="bottom",
        )

    fig.tight_layout()
    output_path = FIGURES_DIR / "dataset_distribution.png"
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    return output_path


def load_legacy_metric_frame() -> pd.DataFrame:
    """Load legacy benchmark metrics into a normalized long-form frame."""
    path = RESULTS_DIR / "metrics" / "legacy_benchmark_ml_results.csv"
    frame = pd.read_csv(path)
    frame = frame.rename(
        columns={
            "roc_auc_mean": "roc_auc",
            "pr_auc_mean": "pr_auc",
            "f1_mean": "f1",
            "mcc_mean": "mcc",
        }
    )
    frame["source"] = "Legacy imported"
    frame["model_label"] = frame["model"].replace(
        {
            "Dummy_MostFrequent": "Dummy",
            "LogisticRegression": "Logistic Regression",
            "RandomForest": "Random Forest",
        }
    )
    return frame[["model_label", "source", "roc_auc", "pr_auc", "f1", "mcc"]]


def load_rerun_metric_frame() -> pd.DataFrame:
    """Load regenerated rerun metrics into a normalized long-form frame."""
    mapping = {
        "legacy_bbb_dummy_v01_metrics.json": "Dummy",
        "legacy_bbb_lr_v01_metrics.json": "Logistic Regression",
        "legacy_bbb_rf_v01_metrics.json": "Random Forest",
    }
    rows: list[dict[str, object]] = []
    for filename, model_label in mapping.items():
        path = RESULTS_DIR / "metrics" / filename
        payload = json.loads(path.read_text())
        row = {
            "model_label": model_label,
            "source": "Regenerated rerun",
            **payload["mean_metrics"],
        }
        rows.append(row)
    return pd.DataFrame(rows)[["model_label", "source", "roc_auc", "pr_auc", "f1", "mcc"]]


def save_legacy_vs_rerun_metrics() -> Path:
    """Create a grouped comparison chart for legacy vs rerun metrics."""
    legacy = load_legacy_metric_frame()
    rerun = load_rerun_metric_frame()
    combined = pd.concat([legacy, rerun], ignore_index=True)

    metrics = ["roc_auc", "pr_auc", "f1", "mcc"]
    model_order = ["Dummy", "Logistic Regression", "Random Forest"]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharey=False)
    axes = axes.flatten()

    for ax, metric in zip(axes, metrics):
        metric_frame = combined[["model_label", "source", metric]].copy()
        legacy_vals = [
            float(
                metric_frame[
                    (metric_frame["model_label"] == model)
                    & (metric_frame["source"] == "Legacy imported")
                ][metric].iloc[0]
            )
            for model in model_order
        ]
        rerun_vals = [
            float(
                metric_frame[
                    (metric_frame["model_label"] == model)
                    & (metric_frame["source"] == "Regenerated rerun")
                ][metric].iloc[0]
            )
            for model in model_order
        ]
        x_positions = list(range(len(model_order)))
        width = 0.35
        ax.bar([x - width / 2 for x in x_positions], legacy_vals, width=width, label="Legacy imported")
        ax.bar([x + width / 2 for x in x_positions], rerun_vals, width=width, label="Regenerated rerun")
        ax.set_title(metric.replace("_", "-").upper())
        ax.set_xticks(x_positions)
        ax.set_xticklabels(model_order, rotation=15, ha="right")
        ax.set_ylim(0, 1.0)
        ax.set_ylabel("Score")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="center left",
        bbox_to_anchor=(0.88, 0.5),
        frameon=False,
    )
    fig.suptitle("Legacy vs Regenerated Benchmark Evidence", y=0.98)
    fig.tight_layout(rect=(0, 0, 0.86, 0.95))
    output_path = FIGURES_DIR / "legacy_vs_rerun_metrics.png"
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    return output_path


def save_rf_feature_importance() -> Path:
    """Create a feature-importance chart from imported RF values."""
    path = RESULTS_DIR / "tables" / "legacy_rf_feature_importance.csv"
    frame = pd.read_csv(path)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(frame["feature"], frame["importance"])
    ax.set_title("Random Forest Feature Importance")
    ax.set_ylabel("Importance")
    ax.set_xlabel("Feature")
    fig.tight_layout()
    output_path = FIGURES_DIR / "legacy_rf_feature_importance_chart.png"
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    return output_path


def save_candidate_ranking_preview() -> Path:
    """Create a preview chart from the regenerated RF ranking table."""
    path = RESULTS_DIR / "tables" / "legacy_bbb_rf_v01_ranking.csv"
    frame = pd.read_csv(path).head(10)

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(frame["sequence_id"], frame["predicted_score"])
    ax.set_title("Candidate Ranking Preview")
    ax.set_ylabel("Predicted score")
    ax.set_xlabel("Sequence ID")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    output_path = FIGURES_DIR / "candidate_ranking_preview.png"
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    return output_path


def add_box(ax: plt.Axes, xy: tuple[float, float], text: str) -> None:
    """Draw a simple text box in axis coordinates."""
    ax.text(
        xy[0],
        xy[1],
        text,
        ha="center",
        va="center",
        transform=ax.transAxes,
        bbox={"boxstyle": "round,pad=0.4", "facecolor": "white", "edgecolor": "black"},
        fontsize=10,
    )


def add_arrow(ax: plt.Axes, start: tuple[float, float], end: tuple[float, float]) -> None:
    """Draw a simple arrow in axis coordinates."""
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        xycoords=ax.transAxes,
        textcoords=ax.transAxes,
        arrowprops={"arrowstyle": "->", "linewidth": 1.2},
    )


def save_benchmark_workflow_outputs() -> Path:
    """Create a simple static workflow diagram using matplotlib text and arrows."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Benchmark Workflow Outputs")
    ax.axis("off")

    add_box(ax, (0.15, 0.78), "Imported legacy\nartifacts")
    add_box(ax, (0.40, 0.78), "Onboarded dataset")
    add_box(ax, (0.65, 0.78), "Rerun-ready\ndataset")
    add_box(ax, (0.85, 0.78), "Benchmark reruns")

    add_box(ax, (0.22, 0.32), "metrics JSON")
    add_box(ax, (0.38, 0.32), "predictions CSV")
    add_box(ax, (0.54, 0.32), "ranking CSV")
    add_box(ax, (0.70, 0.32), "summary CSV")
    add_box(ax, (0.84, 0.32), "manifest JSON\nand figures")

    add_arrow(ax, (0.21, 0.78), (0.34, 0.78))
    add_arrow(ax, (0.46, 0.78), (0.59, 0.78))
    add_arrow(ax, (0.71, 0.78), (0.80, 0.78))

    for x in [0.22, 0.38, 0.54, 0.70, 0.84]:
        add_arrow(ax, (0.85, 0.70), (x, 0.40))

    fig.tight_layout()
    output_path = FIGURES_DIR / "benchmark_workflow_outputs.png"
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    return output_path


def main() -> None:
    """Generate all requested figures."""
    ensure_figures_dir()
    outputs = [
        save_dataset_distribution(),
        save_legacy_vs_rerun_metrics(),
        save_rf_feature_importance(),
        save_candidate_ranking_preview(),
        save_benchmark_workflow_outputs(),
    ]
    for output in outputs:
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
