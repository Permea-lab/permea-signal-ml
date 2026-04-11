# Artifact Naming

## Recommended `run_id`

Use a short, stable run identifier:

- `<dataset_shortname>_<model_shortname>_<version_or_date>`

Examples:

- `bbbv01_rf_20260411`
- `biocore_lr_v0`

## File patterns

- metrics JSON: `<run_id>_metrics.json`
- predictions CSV: `<run_id>_predictions.csv`
- ranking CSV: `<run_id>_ranking.csv`
- summary CSV: `<run_id>_summary.csv`
- manifest JSON: `<run_id>_manifest.json`
- figure PNG: `<run_id>_score_distribution.png`

## Purpose

These names are intended to keep benchmark outputs easy to trace, compare, and move into manuscript-support or evidence-package workflows.
