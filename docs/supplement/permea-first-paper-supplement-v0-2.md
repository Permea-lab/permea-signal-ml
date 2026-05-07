# Permea First Paper Supplement v0.2

## 1. Supplement Status Note

This supplement v0.2 draft supports internal review of manuscript v0.6:

- `docs/paper/permea-first-paper-manuscript-v0-6.md`

It is an internal supplement draft only. It is not a public supplement export and does not approve public release of row-level datasets or row-level derived artifacts.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved. Row-level processed datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and row-level derived artifacts linkable to restricted source rows remain blocked from public release unless explicit permission and manual approval are documented.

## 2. Relationship to Manuscript v0.6

Manuscript v0.6 is the current internal-preparation manuscript. This supplement aligns to v0.6 by preserving:

- aggregate-only benchmark summaries
- exact reported random-stratified and leakage-aware sensitivity metrics
- no-SOTA positioning
- direct peptide comparator vs adjacent compound BBB predictor separation
- cautious B3Pred/B3Pdb lineage framing
- conservative Option A data/code availability posture
- public bioRxiv **Hold / not submission-ready** status
- dataset redistribution unresolved status
- row-level artifact hold posture

This supplement does not introduce new experiments, rerun models, regenerate figures, create new splits, export a PDF, or update public release decisions.

## 3. Scope and Claim Boundary

This supplement uses aggregate-safe summaries and path-level artifact traceability only. It supports a conservative in-silico computational manuscript about learnable BBB-related peptide classification signal from sequence-derived physicochemical features.

It does not claim:

- state-of-the-art performance
- leakage-free status
- robust generalization
- matched leaderboard comparison against prior BBB-penetrating peptide predictors
- biological, wet-lab, in-vivo, therapeutic, or clinical validation
- public dataset redistribution permission
- final code-release approval
- external expert review or peer review

All candidate-prioritization language remains pre-experimental.

## 4. Dataset Surface Summary Without Row-Level Redistribution

Current benchmark surface:

- 2,959 rows
- sequence-derived fields: `length`, `charge`, `gravy`, `pI`, `aromaticity`
- supervised target: `label`
- operational identifiers: `sequence_id`, `source`

Internal path-level source traceability:

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

These paths are provided for internal traceability only. This supplement does not redistribute row-level peptide sequences, labels, sequence-derived features, operational identifiers, or source-row derivatives.

## 5. Data / Provenance Caveats

Dataset provenance and availability remain unresolved for public submission. The imported processed dataset and rerun-ready processed dataset may raise redistribution questions, and dataset availability depends on source terms and manual licensing review.

This supplement does not conclude that redistribution is permitted.

Required unresolved decisions:

- exact upstream dataset files/version
- B3Pred/B3Pdb source terms and license
- required attribution wording
- original label-source criteria
- processed row-level dataset redistribution decision
- row-level derived artifact release decision
- final data availability wording
- founder/manual approval

Public reproducibility may remain aggregate-only if row-level dataset redistribution is not approved.

## 6. Feature Representation Summary

The feature representation is intentionally small and sequence-derived:

- length
- charge
- gravy
- pI
- aromaticity

The representation is a baseline surface and is not a complete mechanistic model of BBB transport, peptide delivery biology, or therapeutic effect.

Feature-importance artifacts, if later shown, should be captioned as model-level artifacts, not mechanistic proof.

## 7. Baseline Model Summary

Baseline families:

- Dummy most-frequent classifier
- Logistic Regression
- Random Forest

Configuration path references:

- `configs/models/dummy.yaml`
- `configs/models/logistic_regression.yaml`
- `configs/models/random_forest.yaml`
- `configs/features/physicochemical.yaml`
- `configs/eval/default.yaml`

These model choices support reproducible baseline evidence packaging and sensitivity analysis. They do not establish optimized predictor performance or state-of-the-art status.

## 8. Evaluation Metric Summary

Reported metrics include:

- ROC-AUC
- PR-AUC
- MCC

PR-AUC is included because the task is class-imbalanced. MCC is included as an additional binary-classification summary. Metrics are interpreted as aggregate benchmark-surface estimates under the documented split and sensitivity settings.

## 9. Random-Stratified Evaluation Summary

Aggregate random-stratified metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 |
| Random Forest | 0.8489 | 0.5002 | 0.4331 |

Traceability:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`

These are aggregate result references only. Random-stratified estimates may be optimistic under documented duplicate and sequence-similarity findings.

## 10. Leakage Audit Summary

Prior leakage audit findings:

- 4 exact duplicate sequence groups, all same-label, crossing reconstructed folds
- 0 exact label conflicts
- 73 near-duplicate pairs, all same-label, including 56 cross-fold pairs
- 33 high k-mer Jaccard pairs, all same-label, including 29 cross-fold pairs
- single coarse source value: `legacy_bbb_import`
- overall benchmark optimism risk: Moderate

Aggregate traceability:

- `results/audits/leakage_audit_summary.json`

Blocked from public-facing supplement/export:

- `results/audits/near_duplicate_pairs.csv`
- `results/audits/fold_similarity_leakage_summary.csv`

This summary does not expose sequence-pair leakage table contents.

## 11. Leakage-Aware Sensitivity Summary

Aggregate leakage-aware sensitivity metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

Relative to random-stratified baseline:

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

Traceability:

- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`

This is a bounded sensitivity setting under the committed manifest. It is not proof of leakage-free status, robust generalization, or biological validation.

Blocked from public-facing supplement/export:

- `results/sensitivity/leakage_aware_predictions.csv`
- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/group_assignments_combined.csv`

## 12. Direct Peptide Comparator Context

The direct comparator landscape for manuscript v0.6 is BBB-penetrating peptide resources and predictors, including B3Pdb / B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, BrainPeps, BBPpred, BrainPepPass, ESM-BBB-Pred, and B3BPFN.

These references support lineage and context for peptide-focused sequence modeling. They do not establish:

- matched dataset comparability
- matched split comparability
- matched label comparability
- matched metric comparability
- state-of-the-art performance
- superiority over prior BBB-penetrating peptide predictors
- dataset redistribution permission

B3Pdb and B3Pred support the closest database/predictor lineage framing. Their citation role remains separate from unresolved source/license decisions for local processed dataset artifacts.

## 13. Adjacent Compound BBB Predictor Context

Adjacent compound-level BBB permeability predictors such as LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB address related but different prediction surfaces.

These works provide broader BBB computational context only. They should not be treated as direct peptide-focused comparators for this manuscript's sequence-derived peptide benchmark, and they should not be used to imply leaderboard, state-of-the-art, or matched benchmark claims.

## 14. Aggregate Result Traceability Matrix

| Manuscript / supplement result | Aggregate support | Release posture |
| --- | --- | --- |
| Random-stratified model metrics | `results/tables/model_comparison_summary.csv` | Candidate only after founder/manual, source/license, release-policy, and claim-boundary review. |
| Model-specific aggregate metrics | `results/metrics/legacy_bbb_*_metrics.json` | Candidate only after review. |
| Leakage-aware summary | `results/sensitivity/leakage_aware_model_comparison_summary.csv` | Candidate only after review. |
| Leakage-aware per-fold metrics | `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | Candidate only after review. |
| Leakage audit summary | `results/audits/leakage_audit_summary.json` | Candidate only after review. |
| Grouping/split aggregate summaries | `results/sensitivity/grouping_summary_combined.json`; `results/sensitivity/combined_group_stratified_split_summary.json` | Candidate only after review. |
| Feature-importance aggregate table | `results/tables/regenerated_rf_feature_importance.csv` | Candidate only after review; model-level only, not mechanistic proof. |

Release of aggregate artifacts must not imply permission to redistribute the underlying processed dataset.

## 15. Figure / Table Inventory Placeholders

Candidate figures after review:

| Proposed ID | Artifact | Current posture |
| --- | --- | --- |
| Figure S1 | `figures/dataset_distribution.png` | Candidate after review with dataset/provenance caveat. |
| Figure S2 | `figures/legacy_vs_rerun_metrics.png` | Candidate after review with split/leakage caveat. |
| Figure S3 | `figures/benchmark_workflow_outputs.png` | Candidate after review as workflow/artifact traceability. |
| Figure S4 | `figures/regenerated_rf_feature_importance.png` | Candidate after review with non-mechanistic caption. |
| Hold | `figures/candidate_ranking_preview.png` | Blocked from public-facing export pending source/legal and claim-boundary review. |

Candidate tables:

| Proposed ID | Content | Current posture |
| --- | --- | --- |
| Table S1 | Dataset surface summary, no row-level entries | Internal draft; public use requires provenance caveat. |
| Table S2 | Random-stratified aggregate metrics | Candidate after review. |
| Table S3 | Leakage-aware aggregate metrics | Candidate after review. |
| Table S4 | Leakage audit aggregate summary | Candidate after review; no sequence-pair rows. |
| Table S5 | Artifact release allow/hold matrix | Recommended for internal/public-boundary clarity. |
| Hold | Row-level prediction, ranking, split, group, or leakage-pair tables | Blocked from public-facing export. |

## 16. Caption Requirements Placeholder

Every future figure/table caption should include:

- artifact path
- artifact type
- split/evaluation context
- whether values are random-stratified, leakage-aware sensitivity, leakage audit, or documentation-only
- dataset/provenance caveat where relevant
- public-release posture if the artifact is internal-only

Required caption boundaries:

- `in-silico computational benchmark`
- `bounded sensitivity estimate`
- `pre-experimental prioritization only` if any prioritization artifact is discussed internally
- `model-level artifact, not mechanistic proof` for feature importance
- `dataset source, licensing, redistribution, and label-source criteria remain unresolved`

Forbidden caption implications:

- leakage-free
- robust generalization
- validated BBB delivery
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- dataset redistribution permission
- state-of-the-art performance
- AlphaFold-level maturity, adoption, or validation

## 17. Export Manifest Placeholder

No public supplement export has been generated for v0.2.

Future export manifest should record:

- manuscript version paired with the supplement
- supplement version and date
- included figures and tables
- excluded row-level artifacts
- aggregate artifact allowlist version
- row-level artifact blocklist version
- data/code availability wording version
- source-to-claim audit version
- bibliography cleanup status
- founder/manual approval status
- public posting decision

Current export status: blocked / not public-submission-ready.

## 18. Public-Safe Artifact Allow / Hold Matrix

| Artifact class | Current posture |
| --- | --- |
| Manuscript text | Internal preparation only. |
| Supplement text | Internal review only. |
| Code | Under internal review; requires repository URL, release tag/commit, software license, release-policy approval, and founder/manual approval. |
| Environment and reproducibility instructions | Candidate after review if they do not require restricted row-level data. |
| Aggregate metrics | Candidate after founder/manual, source/license, release-policy, and claim-boundary review. |
| Aggregate leakage/sensitivity summaries | Candidate after review. |
| Aggregate figures | Candidate after review. |
| Non-row-level summaries | Candidate after review. |
| Public-safe run manifests or schemas | Candidate after review if they do not expose restricted row-level information. |
| Processed row-level datasets | Do not redistribute publicly without explicit permission and manual approval. |
| Row-level labels | Blocked from public release. |
| Row-level predictions | Blocked from public release. |
| Rankings | Blocked from public release. |
| Split manifests | Blocked from public release. |
| Group assignments | Blocked from public release. |
| Sequence-pair leakage artifacts | Do not redistribute publicly without explicit permission and manual approval. |
| Upstream dataset mirrors | Blocked unless source/license permission and manual approval are documented. |
| Row-level derived artifacts linkable to restricted source rows | Blocked from public release. |
| Candidate-ranking preview artifacts | Blocked from public-facing export pending source/legal and claim-boundary review. |

Internal exposure does not imply public-release approval.

## 19. Data / Code Availability Caveats Using Option A

Current recommended posture: **Option A - Most Conservative**.

Code and data availability are currently under internal review. Processed row-level datasets and row-level derived artifacts are not publicly redistributed with this draft. The manuscript and supplement use aggregate metric summaries and path-level artifact traceability only. Dataset source, attribution, license, redistribution permission, original label-source criteria, and final data availability wording remain pending manual review. Public posting remains on Hold until these decisions are complete.

Code availability is separate from data availability. Any public code release requires repository URL confirmation, release tag/commit selection, software license confirmation, release-policy review, and founder/manual approval.

Selected aggregate metrics, aggregate figures, non-row-level summaries, and reproducibility instructions may be considered only after founder/manual, source/legal, release-policy, and claim-boundary review.

This is not a final legal or license determination.

## 20. Limitations

- Internal-review supplement only.
- No row-level sequences, labels, predictions, rankings, split manifests, group assignments, or sequence-pair leakage tables are included.
- Dataset source/license/redistribution remains unresolved.
- Original label-source criteria remain unresolved.
- Aggregate artifact release still requires review.
- Supplement captions, numbering, and export manifest remain incomplete.
- Public code release policy remains unresolved.
- Bibliography cleanup and final source-to-claim review remain pending.
- Founder/manual approval remains pending.
- No PDF or public export was generated.
- No wet-lab, in-vivo, biological, therapeutic, or clinical validation is claimed.

## 21. Export / Readiness Blockers

Public-facing supplement/export remains blocked by:

- finalize dataset source/license/redistribution decision
- finalize original label-source criteria and attribution wording
- approve row-level artifact release blocklist or keep row-level artifacts excluded
- finalize public-safe aggregate artifact allowlist
- finalize data/code availability wording
- finalize code release policy, software license, repository URL, and release tag/commit
- finalize figure/table numbering and captions
- finalize export manifest
- complete bibliography metadata cleanup
- complete final sentence-level source-to-claim review
- complete founder/manual approval
- make final public posting decision

## 22. Explicit Public-Readiness Status

This is an internal supplement draft only.

Supplement v0.2 is not a public supplement export.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.
