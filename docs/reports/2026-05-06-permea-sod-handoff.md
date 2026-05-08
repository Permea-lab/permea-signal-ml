# Permea SOD Handoff - 2026-05-06

## Purpose

This document is the start-of-day handoff for continuing Permea work on 2026-05-06 in a new operator planning or operator session.

Read this file first when the user says "SOD 진행하자".

## Starting Repo State

Expected starting state:

- Local path: `/Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml`
- Branch: `master`
- Remote: `https://github.com/Permea-lab/permea-signal-ml.git`
- Latest pushed commit before the 2026-05-05 EOD package: `303caac docs: add submission readiness documentation package`
- Public bioRxiv status: **Hold / not submission-ready**

Verify with:

```bash
cd /Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml
pwd
git status --short --branch
git log --oneline -10
git remote -v
```

## Files to Read First

- `docs/reports/2026-05-05-permea-eod-report.md`
- `docs/reports/2026-05-06-permea-sod-handoff.md`
- `docs/reports/2026-05-05-submission-readiness-audit.md`
- `docs/submission/2026-05-05-founder-approval-packet-v0-1.md`
- `docs/submission/2026-05-05-metadata-and-disclosures-draft.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`
- `docs/submission/2026-05-05-dataset-license-review-draft.md`

## Previous Day Summary

On 2026-05-05:

- SOD context was restored from the 2026-05-04 EOD and 2026-05-05 SOD documents.
- Submission-readiness documentation Steps 1-5 were created.
- Submission-readiness documentation Steps 6-8 were created.
- The seven-document submission readiness package was committed and pushed in Task 106.
- Public bioRxiv status remained Hold / not submission-ready.

Task 106 committed:

- `docs/reports/2026-05-05-submission-readiness-audit.md`
- `docs/reports/2026-05-05-reference-audit.md`
- `docs/reports/2026-05-05-export-readiness-check.md`
- `docs/submission/2026-05-05-dataset-license-review-draft.md`
- `docs/submission/2026-05-05-metadata-and-disclosures-draft.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`
- `docs/submission/2026-05-05-founder-approval-packet-v0-1.md`

Latest pushed commit:

- `303caac docs: add submission readiness documentation package`

## Current Status

- Manuscript candidate prepared.
- Supplement draft prepared.
- Draft `references.bib` prepared.
- Leakage-aware sensitivity completed.
- Final post-sensitivity claim/citation audit passed.
- Submission-readiness documentation drafts prepared.
- P0/P1 blockers: none for internal continuation.
- Public bioRxiv: **Hold / not submission-ready**.

## Recommended Next Tasks

1. Task 108 - Restore 2026-05-06 Permea SOD context.
2. Task 109 - Review metadata/disclosure draft with founder input.
3. Task 110 - Resolve dataset legal and data availability wording.
4. Task 111 - Clean `references.bib` after verified metadata.
5. Task 112 - Final supplement/export formatting pass.
6. Task 113 - Final bioRxiv readiness review after blockers are closed.

## Remaining Blockers

- Author metadata and author order.
- Affiliations, corresponding author, email, and ORCID decisions.
- Funding, competing interests, acknowledgements, and ethics wording.
- Dataset source attribution, license, redistribution, and legal decision.
- Data/code availability wording.
- `references.bib` human cleanup and source-claim review.
- Supplement/export formatting.
- Founder/manual approval.
- Final public posting decision.

## Claim-Boundary Reminder

Do not claim:

- public preprint readiness
- leakage-free status
- robust generalization
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- final dataset licensing or redistribution permission
- external expert review or peer review

The current evidence supports only a bounded computational benchmark-signal claim under documented limitations.
