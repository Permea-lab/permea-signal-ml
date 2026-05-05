# Manuscript v0.4 Citation and Source-to-Claim Audit - 2026-05-07

## Purpose and Scope

This report audits `docs/paper/permea-first-paper-manuscript-v0-4.md` for citation integration correctness, direct/adjacent comparator boundaries, source-to-claim discipline, and internal-review readiness.

This is an internal audit only. It is not external expert review, peer review, public approval, or a public preprint readiness decision.

Public bioRxiv remains **Hold / not submission-ready**.

## Materials Reviewed

- `docs/paper/permea-first-paper-manuscript-v0-4.md`
- `docs/paper/permea-first-paper-manuscript-v0-3.md`
- `references.bib`
- `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
- `docs/reports/2026-05-07-updated-references-bib-post-audit.md`
- `docs/reports/2026-05-07-comparator-reference-and-source-metadata-plan.md`
- `docs/reports/2026-05-07-bbb-landscape-based-manuscript-change-plan.md`
- `docs/reports/2026-05-07-manuscript-v0-3-landscape-positioning-audit.md`
- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`

No manuscript, bibliography, data, result, figure, model, split, or leakage-audit artifact was modified during this audit.

## 1. Metadata Consistency

Verdict: Pass.

The confirmed metadata are preserved:

- Author: Albert Heekwan Kim
- Affiliation: Permea Research
- Corresponding author email: `a.kim@permea.us`
- Funding: No funding
- Conflict of Interest: N/A
- Acknowledgements: N/A
- Ethics Statement: N/A

Note: a broad `@...` scan sees `@permea` inside the email address. This is not a citation key and should be ignored by citation-key checks.

## 2. Citation Key Existence

Verdict: Pass.

All bracketed citation keys used in manuscript v0.4 exist in `references.bib`:

- `bbb_shuttle_review_2016`
- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `naseem2023bbbpep`
- `augur_2024`
- `tang2025deepb3p`
- `arif2025deepb3pred`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `practicpp_2024`
- `perseucpp_2025`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `kumar2022deepredbbb`
- `parakkal2022deepbbbp`
- `oliveira2026titanbbb`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`

No missing citation key was found.

## 3. Direct Peptide Comparator Citation Use

Verdict: Pass.

Direct BBB-penetrating peptide comparator citations are used in direct peptide predictor context:

- B3Pdb / B3Pred: `b3pdb_2021`, `b3pred_2021`
- BBPpredict: `bbppredict_2022`
- BBB-PEP-prediction: `naseem2023bbbpep`
- Augur: `augur_2024`
- DeepB3P: `tang2025deepb3p`
- DeepB3Pred: `arif2025deepb3pred`

The manuscript does not claim Permea outperforms these methods and does not imply matched datasets, labels, splits, or evaluation policies.

## 4. Adjacent Compound BBB Predictor Citation Use

Verdict: Pass.

Adjacent compound-level BBB predictor citations are used only in adjacent compound-level context:

- LightBBB: `shaker2021lightbbb`
- Deep-B3: `tang2022deepb3`
- DeePred-BBB: `kumar2022deepredbbb`
- DeepBBBP: `parakkal2022deepbbbp`
- TITAN-BBB: `oliveira2026titanbbb`

The manuscript explicitly states that these predictors address related but different prediction surfaces and are not direct peptide-focused comparators.

## 5. B3Pred / B3Pdb Lineage Citation Use

Verdict: Pass with remaining provenance caveat.

The manuscript uses B3Pdb/B3Pred-related keys for database/predictor lineage and conservative positioning. It does not use these citations to claim:

- local Permea dataset provenance closure
- local processed dataset redistribution permission
- matched B3Pred comparison
- Permea state-of-the-art status

Remaining caveat:

- Dataset/source lineage remains unresolved. B3Pdb/B3Pred citations may support background and lineage, but they do not establish source terms or redistribution permission for the local processed dataset.

## 6. DeepB3P vs DeepB3Pred Distinction

Verdict: Pass for internal review.

Manuscript v0.4 cites DeepB3P and DeepB3Pred separately:

- `tang2025deepb3p` for DeepB3P
- `arif2025deepb3pred` for DeepB3Pred

The manuscript explicitly states that the older `deepb3p3_2023` key is intentionally not used as a DeepB3P or DeepB3Pred citation because its identity and citation role remain unresolved relative to these verified entries.

## 7. TITAN-BBB / DeePred-BBB / LightBBB / Deep-B3 / DeepBBBP Adjacency

Verdict: Pass.

The adjacent compound-level predictors are correctly constrained to broader BBB computational context. The manuscript does not treat them as direct peptide comparators and does not compare Permea metrics against them.

## 8. No-SOTA Statement

Verdict: Pass.

No-SOTA wording is present in:

- Abstract
- Introduction
- Related Work / Permea Positioning
- Discussion
- Limitations

The manuscript does not claim a state-of-the-art method, optimized predictor, or benchmark leadership.

## 9. No Leaderboard-Comparison Implication

Verdict: Pass.

The manuscript explicitly states that it does not provide a matched comparison against B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, or DeepB3Pred. It also states that adjacent compound-level predictors address different prediction surfaces.

The reported metrics remain internal benchmark-surface estimates and leakage-aware sensitivity estimates, not cross-paper leaderboard results.

## 10. Results Interpretation Discipline

Verdict: Pass.

Random-stratified and leakage-aware metrics are preserved exactly and remain bounded:

- Logistic Regression leakage-aware ROC-AUC 0.8587, PR-AUC 0.5024, MCC 0.3747
- Random Forest leakage-aware ROC-AUC 0.8718, PR-AUC 0.5807, MCC 0.5084
- Logistic Regression deltas: ROC-AUC -0.0018, PR-AUC +0.0121, MCC +0.0130
- Random Forest deltas: ROC-AUC +0.0229, PR-AUC +0.0805, MCC +0.0753

The manuscript does not reframe the metrics as biological validation, robust generalization, leakage-free status, or direct comparator superiority.

## 11. Data / Code Availability Caution

Verdict: Pass.

The Data and Code Availability section remains conservative:

- Code availability is separated from data availability.
- Processed dataset redistribution is not declared available.
- No row-level processed dataset redistribution is declared.
- Dataset availability depends on source terms, original attribution, licensing, and manual review.
- Selected aggregate derived artifacts are conditional on founder/legal and claim-boundary review.

## 12. Dataset Redistribution Status

Verdict: Unresolved, correctly represented.

Dataset redistribution remains unresolved. The manuscript does not conclude that redistribution is permitted and does not make final legal conclusions.

## 13. Remaining Source TODOs

Remaining TODOs are appropriate for internal review:

- original dataset source/citation/license/label-source criteria
- dataset source attribution, license, redistribution status, and availability wording after manual legal/licensing review
- final dataset/source citations after legal and provenance review
- final sentence-level source-to-claim review after verified comparator citation integration
- final bibliography cleanup and formatting
- `deepb3p3_2023` identity and citation role
- supplement/export formatting

## 14. `deepb3p3_2023` Unresolved Identity Role

Verdict: Safely bounded.

The unresolved `deepb3p3_2023` role is visible and does not create an unsafe claim in v0.4 because:

- it is not used as a DeepB3P citation
- it is not used as a DeepB3Pred citation
- the manuscript explicitly marks its identity and citation role as unresolved

Future work should decide whether to retain, recast, or remove manuscript use of `deepb3p3_2023` after identity review.

## 15. Public-Readiness Status

Verdict: Pass.

The manuscript preserves:

- public preprint submission: Hold / not submission-ready
- no external expert review
- no peer review
- founder/manual approval still required
- dataset/legal/reference/supplement blockers still active

## 16. Internal-Review Readiness

Verdict: v0.4 is suitable for internal review.

v0.4 improves over v0.3 by:

- integrating verified direct peptide comparator citations
- integrating verified adjacent compound-level BBB predictor citations
- reducing resolved landscape source TODOs
- preserving dataset/source/legal TODOs
- keeping direct and adjacent comparator boundaries explicit
- preserving no-SOTA and no-leaderboard language

## Risk Summary

### High-Risk Issues

None found.

No state-of-the-art, leakage-free, robust-generalization, biological validation, wet-lab validation, in-vivo validation, therapeutic efficacy, clinical efficacy, dataset redistribution, external expert review, peer-review, or public-readiness claim was introduced.

### Medium-Risk Issues

1. Dataset source, licensing, redistribution, and label-source criteria remain unresolved.
2. Final source-to-claim review remains pending after citation integration.
3. `deepb3p3_2023` identity and citation role remain unresolved.
4. Supplement/export formatting remains incomplete.

### Low-Risk Issues

1. Existing older bibliography entries may still need metadata normalization and full human cleanup.
2. Some recent/future-dated references may need final publication-status/source-to-claim review before broader review.
3. The manuscript remains markdown/internal-review oriented and not export-ready.

## Required Conclusions

- Manuscript v0.4 is suitable for internal review.
- Manuscript v0.4 should replace v0.3 as the current working manuscript.
- References/citations are safe enough for internal review.
- Dataset redistribution remains unresolved.
- Public bioRxiv remains **Hold / not submission-ready**.

## Recommended Next Task

Task 141 - Commit Manuscript v0.4 and Citation Source-Claim Audit

Suggested commit scope:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`
- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`

