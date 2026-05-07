# Permea SOD Handoff - 2026-05-08

## 1. Starting Repo State

Start in:

```bash
cd /Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml
```

Expected state from 2026-05-07 EOD:

- branch: `master`
- remote: `https://github.com/Permea-lab/permea-signal-ml.git`
- latest pushed commit: `8357023 docs: add public-safe paper preparation package`
- working tree should be clean after the next EOD/SOD docs are committed

## 2. Latest Pushed Commit

- `8357023 docs: add public-safe paper preparation package`

## 3. Files to Read First

Read these first:

- `docs/reports/2026-05-07-permea-eod-report.md`
- `docs/paper/permea-first-paper-manuscript-v0-5.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/reports/2026-05-07-source-to-claim-final-review-draft.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/reports/2026-05-07-public-safe-paper-prep-batch-audit.md`

Supporting files:

- `docs/review/2026-05-07-internal-review-packet-v0-4.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/reports/2026-05-07-supplement-export-v0-4-alignment-plan.md`
- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`
- `references.bib`

## 4. Current Manuscript Path

Current internal-preparation manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-5.md`

Status:

- internal-preparation manuscript
- not public-submission-ready
- preserves v0.4 metrics and citation keys
- includes public-safe caveats and row-level artifact restrictions

## 5. Current Supplement Path

Current supplement draft:

- `docs/supplement/permea-first-paper-supplement-v0-1.md`

Status:

- internal-review only
- aggregate-safe summaries and path-level references only
- not public-submission-ready

## 6. Current Public-Safe Artifact Manifest Path

- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`

Use this file to enforce row-level artifact blocklists and aggregate artifact candidate allowlists.

## 7. Current bioRxiv Blocker Checklist Path

- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`

Use this file to keep public submission status as Hold / not submission-ready until blockers are manually closed.

## 8. Recommended Next Tasks

Recommended next tasks:

1. Task 154 - SOD context restore
2. Task 155 - Final source-to-claim review against manuscript v0.5
3. Task 156 - Supplement v0.1 numbering/caption/export-readiness pass
4. Task 157 - Public-safe repo release policy draft
5. Task 158 - Data/code availability final candidate wording
6. Task 159 - Founder/manual approval packet v0.5

## 9. Public bioRxiv Status

Public bioRxiv remains **Hold / not submission-ready**.

Do not assume public preprint readiness.

## 10. Dataset Redistribution Status

Dataset redistribution remains unresolved.

Unresolved items:

- exact upstream source files/version
- source terms/license
- required attribution wording
- original label-source criteria
- processed dataset redistribution permission
- row-level derived artifact release permission

## 11. Row-Level Artifact Status

Row-level artifacts remain blocked from public release.

Blocked classes include:

- row-level processed datasets
- row-level predictions
- row-level rankings
- split manifests
- group assignments
- sequence-pair leakage CSVs
- candidate-ranking preview artifacts

## 12. Claim-Boundary Reminder

Maintain the current boundaries:

- internal preparation only
- no public bioRxiv readiness claim
- no dataset redistribution permission claim
- no final legal/licensing conclusion
- no state-of-the-art claim
- no leakage-free claim
- no robust generalization claim
- no biological, wet-lab, in-vivo, therapeutic, or clinical validation claim
- no external expert review or peer review implication
