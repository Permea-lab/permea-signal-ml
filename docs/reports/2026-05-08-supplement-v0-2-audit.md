# Supplement v0.2 Audit - 2026-05-08

## 1. Purpose and Scope

This report audits `docs/supplement/permea-first-paper-supplement-v0-2.md` for alignment with manuscript v0.6, public-safe artifact restrictions, row-level artifact exclusion, source-to-claim discipline, and internal-review readiness.

Reviewed materials:

- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/reports/2026-05-08-supplement-v0-1-to-v0-6-alignment-audit.md`
- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `references.bib`

This audit does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, wet-lab validation, clinical claims, or final legal/license conclusions.

## 2. Current Working Tree State

Before this audit report, the worktree contained two untracked documentation files from Tasks 076 and 077:

- `docs/reports/2026-05-08-supplement-v0-1-to-v0-6-alignment-audit.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`

This report is the third untracked documentation file in the supplement-alignment package.

No supplement, manuscript, reference, data, result, figure, model, split, prediction, ranking, or leakage-audit artifact was modified by this audit.

## 3. Version / Status Alignment

Verdict: Pass.

Supplement v0.2 explicitly states that it supports internal review of manuscript v0.6 and references:

- `docs/paper/permea-first-paper-manuscript-v0-6.md`

It correctly states that manuscript v0.6 is the current internal-preparation manuscript.

Supplement v0.2 is marked as:

- internal supplement draft only
- not a public supplement export
- not approving public release of row-level datasets or row-level derived artifacts
- public bioRxiv **Hold / not submission-ready**

Supplement v0.1 remains present and unchanged.

## 4. Public-Safe Artifact Compliance

Verdict: Pass for internal review; public-facing release remains blocked.

Supplement v0.2 uses aggregate summaries and path-level artifact traceability only. It does not include row-level peptide sequences, row-level labels, row-level predictions, ranking tables, split manifests, group assignments, or sequence-pair leakage CSV contents.

The public-safe allow/hold matrix is present and covers:

- code under internal review
- environment and reproducibility instructions as candidates after review
- aggregate metrics as candidates after review
- aggregate leakage/sensitivity summaries as candidates after review
- aggregate figures as candidates after review
- processed row-level datasets blocked without explicit permission and manual approval
- row-level labels blocked
- row-level predictions blocked
- rankings blocked
- split manifests blocked
- group assignments blocked
- sequence-pair leakage artifacts blocked without explicit permission and manual approval
- upstream dataset mirrors blocked unless source/license permission and manual approval are documented
- row-level derived artifacts linkable to restricted source rows blocked
- candidate-ranking preview artifacts blocked from public-facing export

This aligns with the public-safe artifact manifest.

## 5. Row-Level Artifact Exclusion

Verdict: Pass.

Supplement v0.2 does not include restricted row-level contents. It names restricted artifact paths only as internal traceability or as blocked-from-public-export examples.

This is acceptable for internal review. Any later public-facing export should re-check whether restricted path names should remain visible or be replaced with more generic artifact-class descriptions under the final release policy.

## 6. Dataset / Provenance Caveats

Verdict: Pass.

Supplement v0.2 preserves the required caveats:

- dataset provenance and availability remain unresolved
- source terms and manual licensing review remain required
- redistribution permission is not concluded
- exact upstream dataset files/version remain unresolved
- B3Pred/B3Pdb source terms and license remain unresolved
- attribution wording remains unresolved
- original label-source criteria remain unresolved
- processed row-level dataset redistribution decision remains unresolved
- row-level derived artifact release decision remains unresolved
- founder/manual approval remains pending

B3Pred/B3Pdb lineage is kept separate from local processed dataset redistribution permission.

## 7. Data / Code Availability

Verdict: Pass.

Supplement v0.2 applies the conservative Option A posture. It states that code and data availability are under internal review, processed row-level datasets and row-level derived artifacts are not publicly redistributed, and public posting remains on Hold until dataset/source/license and manual decisions are complete.

The supplement does not declare any row-level artifact publicly available.

Aggregate artifacts remain conditional on founder/manual, source/legal, release-policy, and claim-boundary review.

## 8. Result / Metric Traceability

Verdict: Pass.

Supplement v0.2 preserves aggregate metric values from manuscript v0.6 and supplement v0.1. No new metric values were invented.

The supplement correctly presents:

- random-stratified aggregate metrics
- leakage audit aggregate summary counts
- leakage-aware aggregate sensitivity metrics
- random-stratified vs leakage-aware deltas
- aggregate/path-level traceability only

The supplement does not present row-level predictions, ranking tables, split manifests, group assignments, or sequence-pair leakage rows.

## 9. Comparator Context

Verdict: Pass.

Supplement v0.2 adds direct peptide comparator context and adjacent compound BBB predictor context aligned with manuscript v0.6.

Direct peptide comparator context is limited to lineage/background and does not claim matched dataset, split, label, metric, state-of-the-art, superiority, or redistribution permission.

Adjacent compound-level BBB predictors are explicitly described as related but different prediction surfaces and not direct peptide-focused comparators.

## 10. Claim Hygiene

Verdict: Pass.

Supplement v0.2 preserves the required claim boundaries. It does not claim:

- wet-lab validation
- in-vivo validation
- biological validation
- therapeutic efficacy
- clinical efficacy
- universal delivery prediction
- state-of-the-art performance
- matched leaderboard comparison
- AlphaFold-level maturity, adoption, performance, or validation
- dataset redistribution permission
- public bioRxiv readiness

Candidate-prioritization language remains pre-experimental.

## 11. Figure / Table / Caption / Export Readiness

Verdict: Pass for internal-review draft; not export-ready.

Supplement v0.2 includes figure/table inventory placeholders, caption requirements, and an export manifest placeholder.

The blockers remain visible:

- final figure/table numbering
- final captions
- export manifest
- final aggregate artifact allowlist
- row-level artifact blocklist or exclusion decision
- source-to-claim review after formatting
- founder/manual approval

No public supplement export has been generated.

## 12. Internal-Review Readiness

Verdict: Pass.

Supplement v0.2 is safe for internal review and should replace supplement v0.1 as the current internal-review supplement after commit.

Reason: v0.2 fixes the v0.5/v0.6 version mismatch, adopts the Option A data/code availability posture, adds direct peptide vs adjacent compound comparator boundaries, expands the allow/hold matrix, and preserves public-safe row-level restrictions.

Supplement v0.2 is not public submission-ready.

## 13. Risk Findings

### High-Risk Issues

None found.

### Medium-Risk Issues

None found as v0.2 drafting defects.

The following remain medium-risk blockers for broader/public release, but they are correctly preserved in v0.2:

- dataset source/license/redistribution remains unresolved
- row-level release decision remains unresolved
- final data/code approval remains pending
- captions/numbering/export manifest remain incomplete
- bibliography cleanup remains pending
- final source-to-claim review remains pending
- founder/manual approval remains pending
- final public posting decision remains pending

### Low-Risk Issues

- Supplement v0.2 remains untracked and should be committed only with the Task 076 and Task 078 audit reports after review.
- Restricted artifact paths are named for internal traceability and blocklist clarity; public-facing export should re-check whether final release policy allows those path names to remain visible.
- Figure/table/caption/export placeholders are deliberately incomplete and need a later formatting/export task.

## 14. Required Conclusion

Supplement v0.2 is safe for internal review.

Supplement v0.2 should replace supplement v0.1 as the current internal-review supplement after commit.

Supplement v0.2 is not public submission-ready.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.

No high-risk issues were found.

## 15. Recommended Next Task

Recommended next task: commit the supplement alignment package containing:

- `docs/reports/2026-05-08-supplement-v0-1-to-v0-6-alignment-audit.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `docs/reports/2026-05-08-supplement-v0-2-audit.md`
