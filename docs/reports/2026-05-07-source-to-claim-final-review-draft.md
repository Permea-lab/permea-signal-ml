# Source-to-Claim Final Review Draft - 2026-05-07

## 1. Purpose and Scope

This draft reviews manuscript v0.4/v0.5 claim support before any public-readiness decision. It is not final approval and does not declare public readiness.

Primary manuscript source:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Claim Inventory by Manuscript Section

| Section | Claim type | Current support | Status |
| --- | --- | --- | --- |
| Abstract | Initial computational evidence for learnable BBB-related peptide signal | Committed metric artifacts and leakage-aware reports | Supported for internal review. |
| Introduction | Peptide-focused BBB-related computational framing | Comparator citations and landscape reports | Supported with caveats. |
| Related Work | Direct peptide vs adjacent compound predictor distinction | Verified comparator BibTeX entries and v0.4 audit | Supported for internal review. |
| Methods | Dataset surface, features, models, split policies | Repo configs, reports, and committed artifact paths | Supported; provenance unresolved. |
| Results | Random-stratified and leakage-aware metrics | Existing result artifacts and audits | Supported; no rerun performed. |
| Discussion | Learnable signal and candidate prioritization before validation | Results plus claim-boundary audits | Supported if conservative wording remains. |
| Limitations | No validation, no SOTA, unresolved source/license | Submission and dataset risk reports | Supported and required. |
| Data/Code Availability | Code/data separation and no row-level redistribution declaration | Dataset decision package and row-level audit | Supported as conservative draft only. |

## 3. Citation / Source Support per Claim

Direct peptide predictor context:

- B3Pdb / B3Pred: `b3pdb_2021`, `b3pred_2021`
- BBPpredict: `bbppredict_2022`
- BBB-PEP-prediction: `naseem2023bbbpep`
- Augur: `augur_2024`
- DeepB3P: `tang2025deepb3p`
- DeepB3Pred: `arif2025deepb3pred`

Adjacent compound-level context:

- LightBBB: `shaker2021lightbbb`
- Deep-B3: `tang2022deepb3`
- DeePred-BBB: `kumar2022deepredbbb`
- DeepBBBP: `parakkal2022deepbbbp`
- TITAN-BBB: `oliveira2026titanbbb`

Metric interpretation:

- PR-AUC under imbalance: `saito_rehmsmeier_2015_prauc`
- MCC: `chicco_jurman_2020_mcc`

Software/tooling:

- scikit-learn: `scikit_learn_2011`
- pandas: `pandas_2010`
- matplotlib: `matplotlib_2007`

## 4. Internal Artifact Support per Result Claim

| Result claim | Internal support path(s) | Public caveat |
| --- | --- | --- |
| Random-stratified Dummy, LR, RF metrics | `results/tables/model_comparison_summary.csv`; `results/metrics/legacy_bbb_*_metrics.json` | Aggregate-only candidate after review. |
| Leakage-aware sensitivity metrics | `results/sensitivity/leakage_aware_model_comparison_summary.csv`; `results/sensitivity/leakage_aware_metrics_summary.json` | Sensitivity under one manifest only. |
| Per-fold sensitivity details | `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | Likely aggregate/per-fold safe after review. |
| Leakage audit summary | `results/audits/leakage_audit_summary.json` | Do not expose sequence-pair CSVs. |
| Grouping/split summary | `results/sensitivity/grouping_summary_combined.json`; `results/sensitivity/combined_group_stratified_split_summary.json` | Aggregate summary only; row-level manifest blocked. |
| Feature importance context | `results/tables/regenerated_rf_feature_importance.csv`; selected figures | Model artifact only, not mechanism. |

## 5. Unsupported or Weakly Supported Claims

The manuscript must not make these claims:

- state-of-the-art performance
- direct superiority over comparator methods
- matched leaderboard comparison
- leakage-free status
- robust generalization
- biological, wet-lab, in-vivo, therapeutic, or clinical validation
- public dataset redistribution permission
- public preprint readiness

Any language that implies these should be edited before broader review.

## 6. Direct Peptide Comparator Claim Checks

Direct comparator citations support related-work context only. They do not support:

- Permea outperforming any prior predictor
- dataset/split comparability across papers
- direct model leaderboard conclusions
- local dataset redistribution rights

Current v0.4 boundary is acceptable for internal review.

## 7. Adjacent Compound Predictor Claim Checks

Adjacent compound BBB predictor citations support broader BBB computational context only. They must remain separated from direct peptide comparator claims.

Current v0.4 boundary is acceptable for internal review if the text continues to state that these predictors are compound-level or adjacent.

## 8. Dataset Lineage Claim Checks

Supported:

- The working dataset traces operationally to an imported processed BBB-oriented peptide dataset.
- User context identifies the initial download source as the B3Pred page.

Not yet supported for public release:

- exact upstream files/version
- source terms/license
- required attribution wording
- redistribution permission
- original label-source criteria

## 9. Data Availability Claim Checks

Supported conservative language:

- code availability is separate from data availability
- processed dataset redistribution is not declared available
- dataset availability depends on source terms and manual licensing review
- selected aggregate derived artifacts require founder/legal and claim-boundary review

Unsupported:

- public processed dataset availability
- public row-level derived artifact availability
- final legal conclusion

## 10. No-SOTA / No-Validation Claim-Boundary Checks

Required boundaries remain present:

- no state-of-the-art claim
- no matched cross-paper leaderboard claim
- no leakage-free claim
- no robust generalization claim
- no biological/wet-lab/in-vivo validation claim
- no therapeutic or clinical efficacy claim
- no external expert review or peer review implication

## 11. Required Edits for v0.5 or Later

Required before broader review:

- keep direct/adjacent comparator separation visible
- keep no-SOTA statement in abstract, related work, discussion, and limitations
- keep row-level data release restrictions visible
- keep dataset source/license TODOs visible
- update supplement pointer to the aggregate-safe supplement draft
- add public-Hold language wherever submission readiness is discussed
- avoid adding new claims unless directly supported by existing repo artifacts

## 12. Public-Readiness Status

This is a draft review, not a final approval. Manuscript preparation has advanced, but public bioRxiv remains **Hold / not submission-ready** pending manual source/legal, data availability, supplement/export, reference/source-to-claim, and founder approval decisions.
