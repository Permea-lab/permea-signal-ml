# Final Post-Sensitivity Claim and Citation Audit v0.1

## Purpose

This audit reviews the post-sensitivity manuscript package for claim-boundary and citation consistency after leakage-aware sensitivity findings were incorporated.

This is an internal audit only. It is not external expert review, not peer review, not public approval, and not new scientific evidence. It does not rerun models, rerun leakage audit, run new split generation, modify result artifacts, change metric values, add references, or approve public posting. Public preprint status remains **Hold / not submission-ready**.

## Materials Reviewed

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `references.bib`
- `docs/CITATION_CONSISTENCY_CHECK_V0_1.md`
- `docs/LEAKAGE_AWARE_MANUSCRIPT_UPDATE_CHANGELOG_V0_1.md`
- `docs/LEAKAGE_AWARE_BASELINE_RERUN_FINDINGS_INVESTIGATION_V0_1.md`
- `docs/LEAKAGE_AWARE_BASELINE_RERUN_REPORT_V0_1.md`
- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`
- `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/FOUNDER_APPROVAL_SUMMARY_PREPRINT_CANDIDATE_V0_1.md`
- `docs/REVIEW_OPERATIONS_INDEX_V0_1.md`

## Citation Audit Result

Citation-key extraction was run across:

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`

Unique citation keys checked: 18.

Keys found:

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
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `matplotlib_2007`
- `pandas_2010`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`

Results:

- Missing citation keys: none.
- Citation keys absent from `references.bib`: none.
- Unused `references.bib` keys relative to checked manuscript/supplement files: none.
- Deferred placeholder keys used: none.
- New Task 092 citation keys without `references.bib` entries: none found.

Citation-use caveat: key presence is internally consistent, but `references.bib` remains a draft bibliography with human cleanup still required. This audit does not finalize author lists, metadata, citation formatting, or source-to-claim approval.

Verdict: **Pass for key-level citation consistency; human bibliography cleanup remains required.**

## Claim-Boundary Audit Result

Phrases checked:

- leakage-free
- leakage fully controlled
- robust generalization
- robustly generalizes
- validated performance
- validated BBB delivery
- biological validation
- wet-lab validation
- true BBB performance
- therapeutic efficacy
- clinical efficacy
- mechanism
- mechanistic proof
- preprint ready
- submission ready
- external expert review
- peer review

Unsafe claims found: none.

All matches reviewed were in one of the following safe contexts:

- explicit negation
- forbidden-claim list
- conservative limitation wording
- status wording that public preprint remains Hold / not submission-ready
- internal-review wording that does not imply external expert review or peer review

Verdict: **Pass for post-sensitivity claim-boundary consistency.**

## Sensitivity Metric Audit Result

Verified leakage-aware sensitivity metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

Verified deltas against the random-stratified baseline:

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.0000 | 0.0000 | 0.0000 |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

Interpretation verified:

- Leakage-aware group-stratified rerun did not collapse the baseline signal under this specific grouping strategy.
- Logistic Regression remained broadly similar.
- Random Forest was comparable to or higher under this manifest.
- Results increase confidence relative to the initial leakage concern.
- Results are not leakage-free evidence, robust-generalization evidence, biological validation, wet-lab validation, therapeutic efficacy, clinical efficacy, or true BBB performance.

No metric changes were made.

Verdict: **Pass for sensitivity metric and interpretation consistency.**

## P0/P1 Issue Status

- P0 issues: 0
- P1 issues: 0
- P2 issues: remaining human/manual approval, dataset legal/licensing, bibliography cleanup, supplement/export formatting, and final source-to-claim review blockers.
- P3/P4 issues: final polish, formatting, and optional additional sensitivity/provenance refinements.

## Final Internal Verdict

**Pass for internal continuation.**

The post-sensitivity manuscript package is internally consistent enough for the next internal closure task. This verdict does not approve public posting and does not make the package submission-ready.

## Remaining Blockers

- final author metadata
- disclosures
- dataset legal/licensing and redistribution decisions
- data/code availability decisions
- `references.bib` human cleanup and approval
- final citation/source-claim review
- supplement/export formatting
- founder/manual approval
- public posting decision

## Recommended Next Task

Task 095 - Commit Final Post-Sensitivity Claim and Citation Audit
