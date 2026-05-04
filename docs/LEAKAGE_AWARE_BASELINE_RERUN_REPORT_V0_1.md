# Leakage-Aware Baseline Rerun Report v0.1

## Purpose

This report summarizes reruns of the existing baseline model families under the committed leakage-aware group-stratified split manifest.

This is computational sensitivity analysis. It is not biological validation, not wet-lab validation, does not prove robust generalization, does not make the dataset leakage-free, and does not make the public preprint submission-ready. Public preprint status remains **Hold / not submission-ready**.

## Inputs

| Field | Value |
|---|---|
| Dataset path | `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` |
| Split manifest path | `results/sensitivity/combined_group_stratified_split_manifest.csv` |
| Split policy | `leakage_aware_group_stratified` |
| Feature columns | `length`, `charge`, `gravy`, `pI`, `aromaticity` |
| Label column | `label` |
| Model families | Dummy most-frequent, Logistic Regression, Random Forest |
| Metrics | ROC-AUC, PR-AUC, precision, recall, F1, MCC |
| Output directory | `results/sensitivity/` |

Model settings were read from the existing baseline configs:

- `configs/models/dummy.yaml`
- `configs/models/logistic_regression.yaml`
- `configs/models/random_forest.yaml`

## Generated Outputs

| Output | Status |
|---|---|
| `results/sensitivity/leakage_aware_model_comparison_summary.csv` | Generated |
| `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | Generated |
| `results/sensitivity/leakage_aware_predictions.csv` | Generated |
| `results/sensitivity/leakage_aware_metrics_summary.json` | Generated |

No canonical random-stratified result artifacts were overwritten. No manuscript files, figure artifacts, data files, or `references.bib` were modified.

## Leakage-Aware Metric Summary

Metrics below are sensitivity estimates under the `leakage_aware_group_stratified` split manifest. They are not validated performance claims.

| Model | ROC-AUC | PR-AUC | MCC | Test rows | Positives | Negatives |
|---|---:|---:|---:|---:|---:|---:|
| Dummy most-frequent | 0.5000000000 | 0.0909086752 | 0.0000000000 | 2,959 | 269 | 2,690 |
| Logistic Regression | 0.8587118998 | 0.5024344330 | 0.3747151202 | 2,959 | 269 | 2,690 |
| Random Forest | 0.8717668903 | 0.5807054539 | 0.5084459767 | 2,959 | 269 | 2,690 |

## Comparison to Random-Stratified Baseline

| Model | Random ROC-AUC | Leakage-aware ROC-AUC | Delta | Random PR-AUC | Leakage-aware PR-AUC | Delta | Random MCC | Leakage-aware MCC | Delta | Interpretation caveat |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Dummy most-frequent | 0.5000000000 | 0.5000000000 | 0.0000000000 | 0.0909086752 | 0.0909086752 | 0.0000000000 | 0.0000000000 | 0.0000000000 | 0.0000000000 | Sanity baseline is unchanged. |
| Logistic Regression | 0.8605197837 | 0.8587118998 | -0.0018078839 | 0.4903136018 | 0.5024344330 | 0.0121208312 | 0.3617558873 | 0.3747151202 | 0.0129592329 | Broadly similar under this split manifest. |
| Random Forest | 0.8488935260 | 0.8717668903 | 0.0228733643 | 0.5001631580 | 0.5807054539 | 0.0805422959 | 0.4331184653 | 0.5084459767 | 0.0753275114 | Higher under this manifest, but not validation. |

## Interpretation

Result category: performance broadly stable under this grouping strategy, with Random Forest higher under the generated split manifest.

This improves confidence that the current benchmark signal is not solely an artifact of the original random-stratified fold reconstruction under this specific grouping strategy. It does not establish robust generalization, leakage-free status, biological validation, wet-lab validation, or delivery performance. The current manuscript should not be updated until the sensitivity results are reviewed and claim-boundary language is prepared.

Follow-up investigation: `docs/LEAKAGE_AWARE_BASELINE_RERUN_FINDINGS_INVESTIGATION_V0_1.md` reviews random-vs-leakage-aware deltas, fold-level stability, allowed manuscript wording, forbidden wording, and remaining limitations before any manuscript update.

## Remaining Limitations

- The upstream combined group assignment retained the `max_pairs=10000` caveat, so grouping may be incomplete.
- The `source` field remains too coarse for source-aware split control.
- Dataset provenance, source-chain, attribution, licensing, redistribution, and label-source blockers remain unresolved.
- No external validation was performed.
- No wet-lab validation was performed.
- No biological validation was performed.
- The feature set remains limited to sequence-derived physicochemical descriptors.
- These results are sensitivity estimates, not final public-preprint claims.

## Recommended Next Task

Task 089 - Commit Leakage-Aware Baseline Rerun Outputs
