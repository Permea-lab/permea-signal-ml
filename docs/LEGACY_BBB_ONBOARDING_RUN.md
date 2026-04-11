# Legacy BBB Onboarding Run

## Imported files

Imported from `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis`:

- `dataset_with_features.csv` -> `data/processed/legacy_bbb_dataset_with_features.csv`
- `rf_feature_importance.png` -> `figures/legacy_rf_feature_importance.png`
- `rf_feature_importance.csv` -> `results/tables/legacy_rf_feature_importance.csv`
- `baseline_ml_results.csv` -> `results/metrics/legacy_baseline_ml_results.csv`
- `benchmark_ml_results.csv` -> `results/metrics/legacy_benchmark_ml_results.csv`

These remain imported legacy artifacts, not regenerated benchmark-contract outputs.

## Schema adaptations made

Imported dataset inspection found:

- no `sequence_id` column
- no `source` column

Derived rerun-ready dataset created:

- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

Fields added:

- `sequence_id`
- `source`

Added values:

- `sequence_id`: deterministic `legacy_bbb_000001` style identifiers
- `source`: constant `legacy_bbb_import`

## Rerun attempts

- `RandomForest` rerun:
  - command: `python3 scripts/run_baseline.py --data-config configs/data/legacy_bbb_dataset_with_features.yaml --feature-config configs/features/physicochemical.yaml --model-config configs/models/random_forest.yaml --eval-config configs/eval/legacy_bbb_benchmark.yaml --output-prefix legacy_bbb_rf_v01`
  - status: succeeded
- `LogisticRegression` rerun:
  - command: `python3 scripts/run_baseline.py --data-config configs/data/legacy_bbb_dataset_with_features.yaml --feature-config configs/features/physicochemical.yaml --model-config configs/models/logistic_regression.yaml --eval-config configs/eval/legacy_bbb_benchmark.yaml --output-prefix legacy_bbb_lr_v01`
  - status: succeeded
  - note: sklearn emitted a deprecation warning for explicit `penalty` usage, but the run completed successfully

## Success or failure status

- overall onboarding import step: completed
- schema adaptation step: completed
- rerun step: completed successfully for RandomForest and LogisticRegression

## Regenerated outputs created

RandomForest rerun outputs:

- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`
- `results/tables/legacy_bbb_rf_v01_summary.csv`
- `results/manifests/legacy_bbb_rf_v01_manifest.json`
- `figures/legacy_bbb_rf_v01_score_distribution.png`

LogisticRegression rerun outputs:

- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/predictions/legacy_bbb_lr_v01_predictions.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `results/tables/legacy_bbb_lr_v01_summary.csv`
- `results/manifests/legacy_bbb_lr_v01_manifest.json`
- `figures/legacy_bbb_lr_v01_score_distribution.png`

## Next actions

- inspect regenerated outputs against imported legacy metrics and figures
- confirm dataset version, attribution, and licensing before wider use
- decide whether to onboard additional legacy figures as imported artifacts
- keep imported legacy artifacts clearly separated from regenerated outputs

## Follow-on documents

- `LEGACY_VS_RERUN_COMPARISON.md`
- `FIRST_EVIDENCE_SUMMARY.md`
