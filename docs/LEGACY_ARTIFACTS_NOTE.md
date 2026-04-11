# Legacy Artifacts Note

## Purpose

This note records which imported legacy BBB artifacts are currently present in `permea-signal-ml` and why they are retained.

## Imported legacy artifacts currently present

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `results/metrics/legacy_baseline_ml_results.csv`
- `results/metrics/legacy_benchmark_ml_results.csv`
- `results/tables/legacy_rf_feature_importance.csv`
- `figures/legacy_rf_feature_importance.png`

## Why they are kept

- historical continuity from earlier BBB analysis
- comparison against regenerated benchmark-contract reruns
- preservation of earlier evidence surfaces that still have practical reference value
- support for migration, provenance review, and publication-support packaging

## Why they are not equivalent to regenerated benchmark outputs

- they were not produced by the current repository pipeline
- they do not carry current run manifests
- they do not fully satisfy the current output naming and artifact contract
- dataset version, attribution, and licensing remain pending confirmation
- they should therefore be treated as imported legacy artifacts rather than current benchmark evidence
