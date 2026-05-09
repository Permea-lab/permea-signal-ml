# Manuscript v0.7 Source-to-Claim Audit - 2026-05-09

## 1. Purpose and Scope

This report audits `docs/paper/permea-first-paper-manuscript-v0-7.md` for source-to-claim boundaries, citation-key preservation, metric preservation, title/abstract risk, public-readiness language, and readiness to become the current internal-preparation manuscript.

Reviewed materials:

- `docs/paper/permea-first-paper-manuscript-v0-7.md`
- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/reports/2026-05-09-manuscript-v0-7-title-abstract-change-note.md`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `docs/reports/2026-05-08-supplement-v0-2-audit.md`
- `docs/reports/2026-05-09-bibliography-and-export-readiness-audit.md`
- `docs/reports/2026-05-09-citation-rendering-export-readiness-check.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `references.bib`

This audit created this report only. It did not modify manuscript v0.7, manuscript v0.6, supplement v0.2, `references.bib`, README, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It did not rerun models, rerun leakage audits, regenerate figures/results, create splits, generate DOCX/PDF, stage files, commit, or push.

This audit does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, legal/license conclusions, wet-lab validation, biological validation, therapeutic efficacy, clinical efficacy, or AlphaFold-level maturity claims.

## 2. v0.7 Status

Verdict: Pass for internal-preparation draft, with low-risk version-label cleanup recommended before commit.

Manuscript v0.7 is clearly introduced as an internal-preparation manuscript draft derived from v0.6 using the title/abstract positioning cleanup plan. It does not declare public preprint readiness. It preserves public bioRxiv **Hold / not submission-ready** status and lists the same major blockers: dataset/source licensing decisions, final data/code availability approval, final source-to-claim review, supplement/export completion, bibliography cleanup, and founder/manual approval.

Manuscript v0.6 remains unchanged in this worktree.

Low-risk version-label carryover remains in v0.7:

- the Study Design section still says, "Version v0.6 is a wording and source-to-claim clarity revision over v0.5"
- the Submission-Readiness Note still says, "This manuscript draft is an internal first-paper v0.6 preparation draft"

These are editorial/version-label issues, not claim-boundary issues, but they should be corrected before commit if v0.7 is intended to replace v0.6.

## 3. Title Audit

Verdict: Pass.

The v0.7 title is:

`A Reproducible Baseline Evidence Package for BBB-Related Peptide Permeability Signal from Sequence-Derived Features`

The title supports the expert-panel positioning: a reproducible baseline evidence package, not a state-of-the-art predictor. It does not imply wet-lab validation, clinical utility, robust general-purpose predictor maturity, AlphaFold-level maturity, dataset redistribution permission, or matched leaderboard status.

The title is safer than the v0.6 title because "Baseline Evidence Package" better foregrounds traceability and bounded evidence rather than predictor performance.

## 4. Abstract Audit

Verdict: Pass.

The v0.7 abstract foregrounds:

- in-silico computational study framing
- reproducible baseline evidence package positioning
- sequence-derived physicochemical features
- BBB-related peptide classification task
- aggregate artifacts and aggregate metrics
- bounded leakage-aware group-stratified sensitivity setting
- cautious pre-experimental prioritization only
- unresolved dataset source, attribution, license, redistribution permission, label-source criteria, and public data/code availability
- row-level processed datasets and row-level derived artifacts not declared publicly available
- public bioRxiv **Hold / not submission-ready**

The abstract does not imply:

- state-of-the-art performance
- matched external predictor superiority
- leakage-free status
- robust generalization
- wet-lab validation
- biological validation
- therapeutic efficacy
- clinical efficacy
- dataset redistribution permission
- AlphaFold-level maturity, adoption, performance, or validation

The wording "bounded leakage-aware sensitivity setting" is safer than v0.6's more prominent "did not collapse" framing.

## 5. Citation Key Check

Verdict: Pass.

All actual bracketed citation keys in v0.7 are identical to v0.6 and exist in `references.bib`:

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

Missing v0.7 citation keys: none.

The corresponding-author email address contains `@permea.us`; this is not a citation key and was ignored in the citation-key check.

## 6. Metric Preservation Check

Verdict: Pass.

All reported metric values checked from v0.6 are preserved in v0.7. No new performance metric values were added, removed, or changed.

Preserved metric values include:

- random-stratified Dummy metrics: ROC-AUC 0.5000, PR-AUC 0.0909, MCC 0.0000
- random-stratified Logistic Regression metrics: ROC-AUC 0.8605, PR-AUC 0.4903, MCC 0.3618
- random-stratified Random Forest metrics: ROC-AUC 0.8489, PR-AUC 0.5002, MCC 0.4331
- leakage-aware Logistic Regression metrics: ROC-AUC 0.8587, PR-AUC 0.5024, MCC 0.3747
- leakage-aware Random Forest metrics: ROC-AUC 0.8718, PR-AUC 0.5807, MCC 0.5084
- random-stratified vs leakage-aware deltas: -0.0018, +0.0121, +0.0130, +0.0229, +0.0805, +0.0753

No new state-of-the-art, matched comparator, robust-generalization, or validated-performance claim was added.

## 7. Comparator Framing Check

Verdict: Pass.

Direct peptide comparators remain separated from adjacent compound BBB predictors. B3Pdb/B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, BrainPeps, BBPpred, BrainPepPass, ESM-BBB-Pred, and B3BPFN remain context/lineage citations rather than matched benchmarks.

Adjacent compound-level BBB predictors remain described as related but different prediction surfaces, not direct peptide-focused comparators.

v0.7 does not imply matched datasets, matched labels, matched splits, matched metrics, SOTA status, or superiority over prior BBB-penetrating peptide predictors.

## 8. Dataset / Data Availability Check

Verdict: Pass.

The conservative Option A posture remains intact:

- code and data availability remain under internal review
- processed row-level datasets and row-level derived artifacts are not publicly redistributed
- manuscript traceability uses aggregate metric summaries and path-level artifact traceability only
- dataset source, attribution, license, redistribution permission, original label-source criteria, and final data availability wording remain pending manual review
- public posting remains on Hold until decisions are complete

The manuscript does not declare publicly available row-level processed datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, or row-level derived artifacts linkable to restricted source rows.

## 9. Claim-Boundary Check

Verdict: Pass.

v0.7 preserves the required boundaries:

- no wet-lab validation claim
- no biological validation claim
- no in-vivo validation claim
- no therapeutic efficacy claim
- no clinical efficacy claim
- no universal delivery prediction claim
- no state-of-the-art claim
- no matched leaderboard claim
- no leakage-free claim
- no robust generalization claim
- no dataset redistribution permission claim
- no AlphaFold-level performance, adoption, standardization, or validation claim

Feature importance remains framed as a model-level artifact, not mechanistic proof.

## 10. Public-Readiness Check

Verdict: Not public bioRxiv-ready.

Public bioRxiv remains **Hold / not submission-ready**.

Remaining public-readiness blockers include:

- dataset source, license, attribution, and redistribution decision
- original label-source criteria
- row-level artifact release blocklist or exclusion approval
- data/code availability approval
- bibliography metadata cleanup and final citation formatting/export check
- final sentence-level source-to-claim review
- figure/table numbering, captions, and export manifest
- aggregate artifact allowlist and release-policy approval
- founder/manual approval and final public posting decision

## 11. High-Risk Issues

None found.

No high-risk unsupported claim, public-readiness claim, dataset-redistribution claim, wet-lab validation claim, clinical efficacy claim, or AlphaFold-level claim was found in v0.7.

## 12. Medium-Risk Issues

None found as v0.7 title/abstract drafting defects.

The following remain medium-risk blockers for broader/public release, but they are correctly preserved as blockers:

- dataset source/license/redistribution remains unresolved
- row-level processed dataset and row-level derived artifact release decisions remain unresolved
- final data/code availability approval remains pending
- final source-to-claim approval remains pending
- supplement/export remains incomplete
- bibliography final verification remains pending
- founder/manual approval remains pending

## 13. Low-Risk Issues

Low-risk issues:

- v0.7 contains inherited v0.6 wording in the Study Design section and Submission-Readiness Note.
- v0.7 still points to older supplementary material draft paths in the Supplementary Materials Pointer section, inherited from v0.6.
- v0.7 and the v0.7 change note are currently untracked and should be committed only after the minor version-label cleanup is addressed or accepted.
- Public-facing abstract wording may need another pass after dataset/source/license and data/code availability decisions are resolved.

These issues do not create high-risk claim problems, but the version-label carryover should be corrected before v0.7 is committed as the current internal-preparation manuscript.

## 14. Remaining Blockers

Remaining blockers:

- fix low-risk v0.7 version-label carryover before commit
- dataset source/license/redistribution decision
- original label-source criteria and attribution wording
- row-level artifact release decision
- data/code availability wording approval
- code release policy, repository URL, software license, and release tag/archive approval
- final bibliography/source verification
- final sentence-level source-to-claim review
- figure/table/caption/export manifest finalization
- founder/manual approval
- final public posting decision

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.

## 15. Recommended Next Task

Recommended next task: apply a narrow v0.7 version-label cleanup to update the inherited v0.6 references in the Study Design and Submission-Readiness Note, then re-run this audit or append a short audit addendum before committing.

After that, v0.7 can replace v0.6 as the current internal-preparation manuscript in a documentation-only commit.

## Required Conclusions

Manuscript v0.7 is suitable for internal preparation, with low-risk version-label cleanup recommended before commit.

Manuscript v0.7 should replace v0.6 as the current internal-preparation manuscript after the minor version-label cleanup is completed and committed.

Manuscript v0.7 is not public bioRxiv-ready.

No high-risk claim issues were found.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.
