# Legacy BBB Rerun Plan

## Title

First Benchmark-Contract Rerun Plan for Legacy BBB Evidence

## Purpose

This document defines the first rerun objective after onboarding the legacy BBB processed dataset candidate into `permea-signal-ml`.

The objective is to move from imported legacy artifacts toward a clean benchmark-contract rerun with explicit provenance.

## Starting dataset candidate

Starting dataset candidate:

- `dataset_with_features.csv`

This is currently the strongest onboarding candidate because it is the dataset directly consumed by the legacy baseline, benchmark, and feature-importance scripts.

## Required preconditions

- imported dataset file placed into the repository deliberately
- schema verified after import
- sequence column confirmed
- label column confirmed
- stable `sequence_id` strategy defined
- source column strategy defined
- dataset version confirmed
- attribution and licensing status confirmed
- data config finalized after schema verification
- imported artifacts labeled clearly as legacy material

## First rerun target

First rerun target:

a clean benchmark-contract rerun producing:

- metrics JSON
- predictions CSV
- ranking CSV
- summary CSV
- manifest JSON
- figure output

The intended evaluation policy for the first rerun is:

- `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`

The intended initial baseline model family set remains:

- `DummyClassifier(strategy="most_frequent")`
- `LogisticRegression` with `class_weight="balanced"`
- `RandomForestClassifier` with `class_weight="balanced"`, `n_estimators=300`, `min_samples_split=5`, `min_samples_leaf=2`, `random_state=42`

## Expected outputs

Expected outputs for the first rerun:

- `results/metrics/<run_id>_metrics.json`
- `results/predictions/<run_id>_predictions.csv`
- `results/tables/<run_id>_ranking.csv`
- `results/tables/<run_id>_summary.csv`
- `results/manifests/<run_id>_manifest.json`
- `figures/<run_id>_score_distribution.png`

## Known blockers

- missing stable `sequence_id`
- missing explicit source column
- dataset version confirmation pending
- attribution confirmation pending
- licensing confirmation pending
- imported processed dataset may require schema cleanup before rerun

## Success condition

The first rerun should be considered successful only if:

- the onboarded dataset is documented clearly
- current configs are explicit and versioned
- outputs are written in the repository contract format
- a manifest is emitted
- the rerun can be distinguished clearly from imported legacy artifacts
- no legacy artifact is presented as current benchmark evidence without rerun
