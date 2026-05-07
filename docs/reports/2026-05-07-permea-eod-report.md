# Permea EOD Report - 2026-05-07

## 1. Date

2026-05-07

## 2. Repo Path

`/Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml`

## 3. Branch

`master`

## 4. Latest Confirmed Commit

Latest pushed commit:

- `8357023 docs: add public-safe paper preparation package`

Final observed state after Task 152:

- `master...origin/master`
- working tree clean before Task 153 document creation

## 5. Tasks Completed Today

Major completed work:

- Resolved the pending push for the internal review packet commit.
- Created and committed the internal review packet for manuscript v0.4.
- Completed the `deepb3p3_2023` identity review and kept the key unchanged and unused.
- Completed the dataset row-level provenance / redistribution risk audit.
- Completed the supplement/export v0.4 alignment plan.
- Created and committed the public-safe paper preparation package.
- Established manuscript v0.5 as the current internal-preparation manuscript.
- Established supplement v0.1 as internal-review only.

Key commits:

- `4755959 docs: add internal review packet for manuscript v0.4`
- `8357023 docs: add public-safe paper preparation package`

## 6. Files Created / Committed

Internal review and public-safe preparation files committed today include:

- `docs/review/2026-05-07-internal-review-packet-v0-4.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/reports/2026-05-07-source-to-claim-final-review-draft.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/paper/permea-first-paper-manuscript-v0-5.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/reports/2026-05-07-automated-public-safe-paper-prep-batch-summary.md`
- `docs/reports/2026-05-07-public-safe-paper-prep-batch-audit.md`

Prior supporting files already committed before the final batch:

- `docs/reports/2026-05-07-deepb3p3-identity-review.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/reports/2026-05-07-supplement-export-v0-4-alignment-plan.md`

## 7. Current Manuscript Status

Current internal-preparation manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-5.md`

Status:

- v0.5 is the current internal-preparation manuscript.
- v0.5 is derived from v0.4 and preserves existing metrics and citation keys.
- v0.5 strengthens public-safe caveats, row-level artifact restrictions, data availability caution, and supplement pointer.
- v0.5 is not public-submission-ready.

## 8. Current Supplement Status

Current supplement draft:

- `docs/supplement/permea-first-paper-supplement-v0-1.md`

Status:

- supplement v0.1 is internal-review only.
- supplement v0.1 uses aggregate-safe summaries and path-level references.
- supplement v0.1 excludes row-level sequences, labels, predictions, rankings, split manifests, group assignments, and sequence-pair leakage CSV contents.
- supplement/export remains not public-submission-ready.

## 9. Current Reference Status

Current reference status:

- verified comparator BibTeX references are integrated in `references.bib`
- manuscript v0.5 preserves the v0.4 citation keys
- `deepb3p3_2023` remains unchanged and unused as a manuscript citation role
- source-to-claim final review remains draft-only
- older bibliography metadata cleanup and final sentence-level source-to-claim review remain pending

## 10. Current Dataset / Release Status

Current dataset/release status:

- dataset redistribution remains unresolved
- exact upstream dataset version/files remain unresolved
- B3Pred/B3Pdb source terms/license and required attribution wording remain unresolved
- original label-source criteria remain unresolved
- row-level artifacts remain blocked from public release

Blocked from public release unless explicit permission and manual approval are documented:

- row-level processed datasets
- row-level predictions
- row-level rankings
- split manifests
- group assignments
- sequence-pair leakage audit CSVs
- candidate-ranking preview artifacts

## 11. Current Public Submission Status

Public bioRxiv remains **Hold / not submission-ready**.

The public-safe paper preparation package improves internal readiness but does not approve public submission, dataset redistribution, row-level artifact release, or public export.

## 12. Unresolved Blockers

Remaining blockers:

- dataset source/version/license/attribution
- original label-source criteria
- processed dataset redistribution decision
- row-level derived artifact release decision
- final data/code availability wording
- final source-to-claim review against manuscript v0.5
- older bibliography metadata cleanup
- supplement v0.1 numbering, captions, and export-readiness pass
- figure/table/caption readiness
- public-safe repo release policy
- founder/manual approval
- public posting decision

## 13. Recommended Next Tasks

Recommended next tasks for 2026-05-08:

1. Task 154 - SOD context restore
2. Task 155 - Final source-to-claim review against manuscript v0.5
3. Task 156 - Supplement v0.1 numbering/caption/export-readiness pass
4. Task 157 - Public-safe repo release policy draft
5. Task 158 - Data/code availability final candidate wording
6. Task 159 - Founder/manual approval packet v0.5

## 14. Claim-Boundary Reminder

Maintain the following boundaries:

- Do not claim public bioRxiv readiness.
- Do not claim dataset redistribution is permitted.
- Do not make final legal conclusions about dataset licensing.
- Do not claim Permea is state-of-the-art.
- Do not claim leakage-free status.
- Do not claim robust generalization.
- Do not claim biological, wet-lab, in-vivo, therapeutic, or clinical validation.
- Do not claim therapeutic or clinical efficacy.
- Do not imply external expert review or peer review.

## 15. Final Operating State

End-of-day operating state:

- latest pushed commit: `8357023 docs: add public-safe paper preparation package`
- current internal-preparation manuscript: `docs/paper/permea-first-paper-manuscript-v0-5.md`
- current supplement draft: `docs/supplement/permea-first-paper-supplement-v0-1.md`
- public-safe artifact manifest: `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- bioRxiv blocker checklist: `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- public bioRxiv: **Hold / not submission-ready**
- dataset redistribution: unresolved
- row-level artifacts: blocked from public release
