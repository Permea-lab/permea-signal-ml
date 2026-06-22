# P-SIGNAL-001 Leakage-Controlled Physicochemical Baseline

Date: 2026-06-21

Task: P-SIGNAL-001

## Purpose

This report records a public-safe aggregate physicochemical baseline run for the B3Pred Dataset_3 / B3Pred-derived benchmark surface.

The run used a private/local-only dataset input referenced as `private_local_b3pred_dataset3_rerun_ready_csv`. Row-level data, raw source files, row-level group assignments, row-level split manifests, row-level predictions, and sequence-pair leakage files are not redistributed here.

This is computational candidate-prioritization benchmark evidence before experimental validation.

## Public-Safe Artifacts

- `results/p_signal_001/physchem_baseline_model_comparison.csv`
- `results/p_signal_001/physchem_baseline_per_fold_metrics.csv`
- `results/p_signal_001/physchem_baseline_leakage_summary.json`
- `results/p_signal_001/physchem_baseline_run_manifest.json`

The committed artifacts are aggregate summaries only. They do not contain raw sequences or row-level prediction records.

## Dataset Boundary

| Field | Value |
| --- | --- |
| Dataset reference | `private_local_b3pred_dataset3_rerun_ready_csv` |
| Dataset SHA256 | `2e8d3fc30becfdd00ad7cd25eedd5e6c00df7698747ea358b4cc97f4268f8abf` |
| Rows | 2,959 |
| Positives | 269 |
| Negatives | 2,690 |
| Feature columns | `length`, `charge`, `gravy`, `pI`, `aromaticity` |

Dataset availability claims cannot be made until rights and redistribution posture are reviewed.

## Split And Leakage Summary

| Field | Value |
| --- | --- |
| Split policy | `leakage_aware_group_stratified` |
| Grouping method | `combined_exact+edit_distance<=1+kmer3_jaccard>=0.8` |
| Random seed | 42 |
| Folds | 5 |
| Groups | 2,958 |
| Groups crossing folds | 0 |
| Duplicate sequence groups | 4 |
| Label-conflict groups | 0 |
| Near-duplicate pairs | 73 |
| High k-mer similarity pairs | 33 |
| Reconstructed-stratified cross-fold high-similarity pairs | 29 |

The source field is coarse and not sufficient for source-aware split control. The grouping step retained the `max_pairs=10000` caveat, so sequence-similarity grouping may be incomplete.

## Aggregate Metrics

| Model | ROC-AUC | PR-AUC | Balanced accuracy | Precision | Recall | F1 | MCC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dummy | 0.5000 | 0.0909 | 0.5000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.7835 | 0.2757 | 0.7693 | 0.4057 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.6910 | 0.7388 | 0.3977 | 0.5135 | 0.5084 |

These are aggregate fold-mean metrics under the leakage-aware group-stratified split. They are not a leaderboard comparison and are not evidence of biological transport.

## Reproduction Summary

The run used existing repository scripts with private placeholders in the public manifest:

1. Build combined sequence-similarity groups.
2. Build the leakage-aware group-stratified split manifest.
3. Run the leakage audit.
4. Run dummy, logistic-regression, and random-forest physicochemical baselines.
5. Publish only aggregate metrics, aggregate leakage counts, and a public-safe run manifest.

The exact public-safe command templates are listed in `results/p_signal_001/physchem_baseline_run_manifest.json`.

## Study Result Bundle v0 Impact

| Bundle artifact | P-SIGNAL-001 impact |
| --- | --- |
| `dataset_card.md` | Still needs rights and source review; row-level data remains withheld. |
| `split_protocol.md` | Has an executed leakage-aware split policy summary. |
| `leakage_audit.md` | Has aggregate leakage counts for a bundle draft. |
| `model_comparison.csv` | Has aggregate physicochemical baseline rows. |
| `candidate_ranking.csv` | Not produced in this task. |
| `evidence_report_input.json` | Can now ingest aggregate metrics and leakage summaries. |
| `evidence_report.md` | Can be drafted from aggregate artifacts with claim boundaries. |
| `claim_boundary.md` | Must preserve private row-level data and source-rights limitations. |
| `run_manifest.json` | Public-safe run manifest created. |
| `figures/` | Not produced in this task. |

## Limitations

- Row-level data remains private and rights-review required.
- The source field is too coarse for source-aware split control.
- Sequence-similarity grouping may be incomplete under the `max_pairs=10000` cap.
- Metrics are aggregate computational benchmark results for candidate prioritization before experimental validation.
