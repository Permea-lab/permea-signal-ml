# Manuscript v0.5 Source-to-Claim Audit - 2026-05-08

## 1. Purpose and Scope

This report audits `docs/paper/permea-first-paper-manuscript-v0-5.md` for source-to-claim boundaries, citation support, dataset/release caveats, no-SOTA positioning, supplement alignment, and remaining public-readiness blockers.

This is an internal audit report only. It is not public-readiness approval, legal review, external expert review, peer review, or a public bioRxiv submission decision.

Public bioRxiv remains **Hold / not submission-ready**.

Reviewed materials:

- `docs/paper/permea-first-paper-manuscript-v0-5.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/reports/2026-05-07-source-to-claim-final-review-draft.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/reports/2026-05-07-public-safe-paper-prep-batch-audit.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`
- `references.bib`
- `README.md`

No manuscript, supplement, reference, data, result, figure, model, split, prediction, ranking, or leakage-audit artifact was modified for this audit.

## 2. Current Manuscript Status

Manuscript v0.5 is the current internal-preparation manuscript draft. It is a public-safe polish draft derived from v0.4 and explicitly states that it does not declare public preprint readiness.

Current status:

- suitable for internal preparation
- not public bioRxiv-ready
- public bioRxiv remains Hold / not submission-ready
- dataset redistribution remains unresolved
- row-level artifacts remain blocked from public release
- supplement/export remains incomplete

## 3. Citation Key Existence Check

Verdict: Pass.

All actual bracketed citation keys used in manuscript v0.5 were found in `references.bib`:

- `arif2025deepb3pred`
- `augur_2024`
- `b3bpfn_2026`
- `b3pdb_2021`
- `b3pred_2021`
- `bbb_shuttle_review_2016`
- `bbppred_2021`
- `bbppredict_2022`
- `brainpeppass_2024`
- `brainpeps_2012`
- `chicco_jurman_2020_mcc`
- `esm_bbb_pred_2025`
- `kumar2022deepredbbb`
- `matplotlib_2007`
- `naseem2023bbbpep`
- `oliveira2026titanbbb`
- `pandas_2010`
- `parakkal2022deepbbbp`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `tang2025deepb3p`

Note: a raw `@...` scan also detects `@permea` inside the corresponding-author email address. This is not a citation key.

## 4. Direct Peptide Comparator Citation Check

Verdict: Pass.

Manuscript v0.5 keeps direct BBB-penetrating peptide comparator context separate from Permea result claims. Direct peptide context includes:

- B3Pdb / B3Pred: `b3pdb_2021`, `b3pred_2021`
- BBPpredict: `bbppredict_2022`
- BBB-PEP-prediction: `naseem2023bbbpep`
- Augur: `augur_2024`
- DeepB3P: `tang2025deepb3p`
- DeepB3Pred: `arif2025deepb3pred`
- Additional peptide context: `brainpeps_2012`, `bbppred_2021`, `brainpeppass_2024`, `esm_bbb_pred_2025`, `b3bpfn_2026`

The manuscript does not claim that Permea outperforms these methods, uses matched datasets/splits, or establishes a leaderboard comparison.

## 5. Adjacent Compound BBB Predictor Citation Check

Verdict: Pass.

Adjacent compound-level BBB predictors are clearly marked as related but different prediction surfaces:

- LightBBB: `shaker2021lightbbb`
- Deep-B3: `tang2022deepb3`
- DeePred-BBB: `kumar2022deepredbbb`
- DeepBBBP: `parakkal2022deepbbbp`
- TITAN-BBB: `oliveira2026titanbbb`

The manuscript explicitly states that TITAN-BBB and DeePred-BBB are compound/SMILES BBB permeability work, not direct peptide predictors for the current first paper.

## 6. B3Pred / B3Pdb Lineage Claim Check

Verdict: Pass with unresolved provenance caveat.

The B3Pdb/B3Pred lineage is used as background and positioning for peptide-focused BBB predictor context. The manuscript does not use B3Pdb/B3Pred citations to claim:

- local dataset provenance closure
- local processed dataset redistribution permission
- matched B3Pred comparison
- Permea state-of-the-art status

Remaining unresolved items:

- exact upstream dataset files/version
- source terms/license
- required attribution wording
- original label-source criteria
- row-level processed dataset release permission

The `deepb3p3_2023` key remains present in `references.bib` but is intentionally not used as a DeepB3P or DeepB3Pred citation in v0.5.

## 7. Permea Result Claim Support Check

Verdict: Pass for internal preparation.

The random-stratified and leakage-aware result claims are supported by existing committed aggregate artifacts and prior audit reports.

Supported internal result claims:

- Dummy most-frequent behaves as a class-prior sanity baseline.
- Logistic Regression and Random Forest show learnable benchmark signal under the random-stratified baseline surface.
- Under the tested leakage-aware group-stratified sensitivity manifest, the baseline signal did not collapse.
- Feature-importance discussion is bounded as model-level behavior, not mechanism.

Key aggregate support paths:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/audits/leakage_audit_summary.json`

The result claims remain internal benchmark-surface claims, not external validation, matched comparator claims, or biological validation claims.

## 8. Dataset / Release Caveat Check

Verdict: Pass.

Manuscript v0.5 clearly states:

- dataset provenance and availability remain unresolved
- processed dataset redistribution is not declared available
- dataset availability depends on source terms, original attribution, licensing, and manual review
- row-level processed datasets, predictions, rankings, split manifests, group assignments, and sequence-pair leakage artifacts are excluded from the public-facing package unless explicit permission and manual approval are documented
- selected aggregate derived artifacts require founder/legal and claim-boundary review

This is consistent with the public-safe artifact manifest and row-level provenance/redistribution risk audit.

## 9. Data / Code Availability Claim Check

Verdict: Pass for conservative draft status.

The Data and Code Availability section separates code availability from data availability. It does not claim a release tag, archive, or public processed dataset availability.

Remaining required decisions:

- public repository URL/release tag for code availability
- software license/release policy confirmation
- dataset source/license/attribution decision
- public data availability wording
- whether the final posture is no processed dataset redistribution, derived artifacts only, data available on request, or another approved option

## 10. No-SOTA Claim-Boundary Check

Verdict: Pass.

No-SOTA language is visible in the abstract, introduction, related work, Permea positioning, methods, discussion, and limitations.

The manuscript does not claim:

- state-of-the-art performance
- optimized predictor status
- matched leaderboard superiority
- direct benchmark comparison against direct peptide predictors
- direct benchmark comparison against compound-level predictors

## 11. No Wet-Lab / Clinical Validation Check

Verdict: Pass.

Manuscript v0.5 states that this is an in-silico computational study only. It does not claim:

- wet-lab validation
- biological validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- external validation
- peer review

Candidate prioritization is framed as before experimental validation.

## 12. Supplement Alignment Check

Verdict: Pass for internal review; public export remains blocked.

Supplement v0.1 aligns with manuscript v0.5 by:

- using aggregate-safe summaries
- avoiding row-level peptide sequences, labels, predictions, rankings, split manifests, group assignments, and sequence-pair leakage CSV contents
- preserving no-SOTA, no-validation, and no-public-readiness boundaries
- listing aggregate result traceability
- preserving a release allow/hold matrix

Remaining supplement/export blockers:

- final supplement section order
- figure/table numbering
- captions
- export manifest
- final public-safe artifact allowlist
- final check that public-facing supplement excludes blocked row-level artifacts

## 13. Unsupported or Weakly Supported Claims

No high-risk unsupported claims were found in manuscript v0.5.

Claims that remain weak, conditional, or not yet public-ready:

- dataset lineage and availability claims remain conditional because exact source files/version, license, terms, attribution, and label-source criteria are unresolved
- code availability remains conditional until repository release/tag/license wording is finalized
- aggregate artifact public release remains conditional on founder/legal and claim-boundary review
- leakage-aware sensitivity supports bounded sensitivity only, not full leakage control or robust generalization
- direct comparator citations support context only, not direct performance comparison

## 14. Required Edits Before Broader Review

Required before broader review or public-readiness consideration:

1. Resolve or explicitly preserve dataset source/license/redistribution blockers.
2. Finalize data/code availability wording.
3. Complete full bibliography metadata cleanup.
4. Complete sentence-level source-to-claim review against v0.5 as the primary manuscript.
5. Finalize supplement numbering, captions, and export manifest.
6. Confirm public-safe artifact allowlist and row-level artifact blocklist.
7. Obtain founder/manual approval before any public posting decision.

## 15. Remaining bioRxiv Blockers

Public bioRxiv remains **Hold / not submission-ready**.

Remaining blockers:

- dataset source, license, attribution, and redistribution posture
- row-level artifact release decision
- data/code availability wording
- final source-to-claim approval
- bibliography metadata cleanup and formatting
- supplement/export package completion
- figure/table/caption public-safe review
- founder/manual approval

## 16. Whether Manuscript v0.5 Remains Internal-Preparation Only

Verdict: Yes.

Manuscript v0.5 is suitable for internal preparation and continued claim-boundary/source review. It is not public bioRxiv-ready.

Dataset redistribution remains unresolved. Row-level processed datasets and row-level derived artifacts remain blocked from public release unless explicit permission and approval are documented.

## 17. Recommended Next Task

Recommended next task: Task 052 - Draft required v0.5 source-to-claim edits and data/code availability candidate wording without modifying manuscript v0.5.

## Required Conclusion

- Manuscript v0.5 is suitable for internal preparation.
- Manuscript v0.5 is not public bioRxiv-ready.
- Dataset redistribution remains unresolved.
- Row-level artifacts remain blocked from public release.
- No high-risk claim issues were found.
