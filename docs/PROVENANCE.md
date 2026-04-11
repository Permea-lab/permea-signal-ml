# Provenance

## Title

Permea Signal ML v0.1 Provenance Contract

## Purpose

This document defines the provenance expectations for Permea Signal ML v0.1. The repository treats provenance as part of the benchmark contract rather than as optional metadata.

Metrics, predictions, ranking outputs, and figures should be traceable to dataset version, feature configuration, model configuration, split policy, and code state.

## What is tracked

The repository is expected to track:

- dataset identity and version
- feature configuration
- model identity and model configuration
- split policy
- random seed
- output artifact paths
- generation timestamp

This information should be sufficient to understand what was run and to reconstruct the context of a result.

## Run manifest fields

Each benchmarked run should emit a manifest containing fields such as:

- `run_id`
- `dataset_name`
- `dataset_version`
- `feature_config`
- `model_name`
- `model_config`
- `split_policy`
- `random_seed`
- `metrics_file`
- `predictions_file`
- `ranking_file`
- `generated_at`

Additional fields may be added when they improve traceability without obscuring the minimal benchmark contract.

## Dataset version tracking

Datasets should be versioned explicitly whenever practical.

At minimum, a run should be able to answer:

- which dataset name was used
- which dataset version was used
- whether the run used raw, interim, or processed material
- which label framing and split policy applied to that version

## Feature configuration tracking

Feature extraction settings should be recorded by config path or config identifier.

This includes:

- enabled feature list
- any transformation or normalization assumptions
- feature extraction version or config reference

The purpose is to ensure that feature differences are treated as explicit benchmark variables rather than undocumented code drift.

## Model configuration tracking

Model settings should be recorded through named config files or serialized config references.

This includes:

- model family
- key model parameters
- class weighting or imbalance handling
- seed where relevant

## Output artifact tracking

The repository expects run outputs to be organized and tracked as explicit artifacts.

Expected artifact classes:

- metrics files
- prediction files
- ranking files
- manifest files
- figure files

Typical locations:

- `results/metrics/`
- `results/predictions/`
- `results/tables/`
- `results/manifests/`
- `figures/`

## Reproducibility expectations

Canonical benchmark outputs should satisfy the following:

- traceable dataset version
- explicit feature config
- explicit model config
- explicit split policy
- fixed random seed
- machine-readable outputs
- manifest emitted alongside outputs

Outputs that do not satisfy these conditions may still be useful for exploration, but they should not be treated as stable benchmark evidence.

## Example manifest

```json
{
  "run_id": "signal-ml-v0.1-rf-001",
  "dataset_name": "bbb_signal_v0",
  "dataset_version": "0.1.0",
  "feature_config": "configs/features/physicochemical.yaml",
  "model_name": "random_forest",
  "model_config": "configs/models/random_forest.yaml",
  "split_policy": "stratified_kfold_5",
  "random_seed": 42,
  "metrics_file": "results/metrics/signal-ml-v0.1-rf-001_metrics.json",
  "predictions_file": "results/predictions/signal-ml-v0.1-rf-001_predictions.csv",
  "ranking_file": "results/tables/signal-ml-v0.1-rf-001_ranking.csv",
  "generated_at": "2026-04-11T10:00:00Z"
}
```

## Previously generated results

Legacy results imported from earlier work may still be useful, but they should be marked clearly as imported artifacts unless they are rerun under the current benchmark contract.
