# Manuscript v0.7 Post-Cleanup Audit - 2026-05-09

## 1. Purpose and Scope

This report re-audits `docs/paper/permea-first-paper-manuscript-v0-7.md` after the narrow version-label and supplement-pointer cleanup. It verifies whether manuscript v0.7 is safe to commit as the current internal-preparation manuscript.

Reviewed materials:

- `docs/paper/permea-first-paper-manuscript-v0-7.md`
- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/reports/2026-05-09-manuscript-v0-7-title-abstract-change-note.md`
- `docs/reports/2026-05-09-manuscript-v0-7-source-to-claim-audit.md`
- `docs/reports/2026-05-09-manuscript-v0-7-version-label-cleanup-note.md`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `docs/reports/2026-05-08-supplement-v0-2-audit.md`
- `references.bib`

This audit created this report only. It did not modify manuscript v0.7, manuscript v0.6, supplement v0.2, `references.bib`, README, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It did not rerun models, rerun leakage audits, regenerate figures/results, create splits, generate DOCX/PDF, stage files, commit, or push.

This audit does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, legal/license conclusions, wet-lab validation, biological validation, therapeutic efficacy, clinical efficacy, or AlphaFold-level maturity claims.

## 2. Version / Status Check

Verdict: Pass.

Manuscript v0.7 is clearly marked as an internal-preparation manuscript draft derived from manuscript v0.6 using the title/abstract positioning cleanup plan.

The inherited incorrect v0.6 labels identified in the prior audit have been corrected:

- Study Design now says v0.7 is a title and abstract positioning revision over v0.6, not a new experiment.
- Submission-Readiness Note now says this is an internal first-paper v0.7 preparation draft.

Historical v0.6 mentions remain only where appropriate: v0.7 is derived from v0.6 and is a revision over v0.6.

No v0.5 references remain in manuscript v0.7.

## 3. Supplement Pointer Check

Verdict: Pass.

The Supplementary Materials Pointer section now points to the current internal-review supplement:

- `docs/supplement/permea-first-paper-supplement-v0-2.md`

No stale pointer to `docs/supplement/permea-first-paper-supplement-v0-1.md` remains in manuscript v0.7.

The manuscript continues to state that the supplement draft is internal-review only, uses aggregate summaries and path-level traceability, and is not a public supplement export.

## 4. Title / Abstract Check

Verdict: Pass.

The recommended title remains applied:

`A Reproducible Baseline Evidence Package for BBB-Related Peptide Permeability Signal from Sequence-Derived Features`

The abstract remains conservative and preserves:

- in-silico computational framing
- reproducible baseline evidence package positioning
- sequence-derived physicochemical feature scope
- aggregate artifact and aggregate metric language
- bounded leakage-aware sensitivity framing
- pre-experimental prioritization only
- no state-of-the-art claim
- no matched external predictor superiority claim
- no leakage-free or robust-generalization claim
- no wet-lab, biological, therapeutic, or clinical validation claim
- unresolved dataset/source/license and row-level artifact caveats
- public bioRxiv **Hold / not submission-ready** status

Task 127 did not change the title or abstract.

## 5. Citation Key Check

Verdict: Pass.

All actual bracketed citation keys in v0.7 exist in `references.bib`. The v0.7 citation key set is identical to v0.6.

Detected actual v0.7 citation keys: 25.

Missing v0.7 citation keys: none.

The corresponding-author email address contains `@permea.us`; this is not a citation key and was ignored.

## 6. Metric Preservation Check

Verdict: Pass.

Reported metric values remain unchanged from v0.6. No new performance metrics or performance claims were added.

The checked metric values include:

- random-stratified Dummy metrics: ROC-AUC 0.5000, PR-AUC 0.0909, MCC 0.0000
- random-stratified Logistic Regression metrics: ROC-AUC 0.8605, PR-AUC 0.4903, MCC 0.3618
- random-stratified Random Forest metrics: ROC-AUC 0.8489, PR-AUC 0.5002, MCC 0.4331
- leakage-aware Logistic Regression metrics: ROC-AUC 0.8587, PR-AUC 0.5024, MCC 0.3747
- leakage-aware Random Forest metrics: ROC-AUC 0.8718, PR-AUC 0.5807, MCC 0.5084
- random-stratified vs leakage-aware deltas: -0.0018, +0.0121, +0.0130, +0.0229, +0.0805, +0.0753

Metric count differences relative to v0.6: none.

## 7. Data / Code Availability Check

Verdict: Pass.

The conservative Option A posture remains intact:

- code and data availability remain under internal review
- processed row-level datasets and row-level derived artifacts are not publicly redistributed
- traceability uses aggregate metric summaries and path-level artifact traceability only
- dataset source, attribution, license, redistribution permission, original label-source criteria, and final data availability wording remain pending manual review
- public posting remains on Hold until decisions are complete

Dataset redistribution remains unresolved.

Row-level processed datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and row-level derived artifacts remain blocked from public release.

## 8. Claim-Boundary Check

Verdict: Pass.

v0.7 preserves the required claim boundaries:

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

Direct peptide comparators remain lineage/context only. Adjacent compound BBB predictors remain related but different prediction surfaces.

## 9. Public-Readiness Check

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

## 10. Commit-Readiness

Verdict: Ready to commit as a documentation-only v0.7 manuscript package.

The v0.7 package is safe to commit as the current internal-preparation manuscript package because:

- v0.7 is clearly marked internal-preparation only
- version-label cleanup is complete
- supplement pointer now targets supplement v0.2
- title and abstract preserve the approved evidence-package positioning
- citation keys are preserved and resolve to `references.bib`
- metric values are preserved
- no high-risk claim issue was found
- public bioRxiv Hold / not submission-ready status remains explicit

The expected commit package should include:

- `docs/paper/permea-first-paper-manuscript-v0-7.md`
- `docs/reports/2026-05-09-manuscript-v0-7-title-abstract-change-note.md`
- `docs/reports/2026-05-09-manuscript-v0-7-source-to-claim-audit.md`
- `docs/reports/2026-05-09-manuscript-v0-7-version-label-cleanup-note.md`
- `docs/reports/2026-05-09-manuscript-v0-7-post-cleanup-audit.md`

## 11. High-Risk Issues

None found.

No high-risk unsupported claim, public-readiness claim, dataset-redistribution claim, wet-lab validation claim, clinical efficacy claim, or AlphaFold-level claim was found in v0.7 after cleanup.

## 12. Medium-Risk Issues

None found as v0.7 cleanup or title/abstract drafting defects.

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

- v0.7 and the four v0.7 reports are currently untracked and need a controlled commit.
- Public-facing abstract and availability wording may need another pass after dataset/source/license and data/code availability decisions are resolved.
- Final Word/PDF export and figure/table integration remain separate tasks.

No low-risk issue blocks committing v0.7 as the current internal-preparation manuscript.

## 14. Remaining Blockers

Remaining blockers:

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

Recommended next task: commit the v0.7 manuscript package, then push the branch and open a documentation-only PR for review.

## Required Conclusions

Manuscript v0.7 is suitable for internal preparation.

Manuscript v0.7 should replace v0.6 as the current internal-preparation manuscript after commit.

Manuscript v0.7 is not public bioRxiv-ready.

No high-risk claim issues were found.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.
