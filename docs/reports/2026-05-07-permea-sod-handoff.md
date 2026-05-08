# Permea SOD Handoff - 2026-05-07

## Purpose

This document is the start-of-day handoff for continuing Permea work on 2026-05-07 in a new operator planning/operator session.

When the user says "SOD 진행하자", read this document first, restore repo state, summarize current status, present today priorities, and propose the next maintainer task.

## Starting Repo State

- Repo path: `/Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml`
- Remote: `https://github.com/Permea-lab/permea-signal-ml.git`
- Branch: `master`
- Latest pushed commit at 2026-05-06 EOD: `94107ec docs: add supplement export formatting plan`
- Expected starting status: clean working tree after Task 125, unless Task 126 EOD/SOD files have not yet been committed

## Run First

```bash
cd /Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml
pwd
git status --short --branch
git log --oneline -10
git remote -v
```

## Files to Read First

- `docs/reports/2026-05-06-permea-eod-report.md`
- `docs/reports/2026-05-07-permea-sod-handoff.md`
- `docs/paper/permea-first-paper-manuscript-v0-2.md`
- `docs/review/2026-05-06-friendly-reviewer-packet-v0-2.md`
- `docs/reports/2026-05-06-supplement-export-formatting-plan.md`
- `docs/reports/2026-05-06-manuscript-v0-2-audit.md`
- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`
- `docs/reports/2026-05-06-reference-cleanup-post-audit.md`

## Current Status

- Manuscript v0.2 exists and is suitable for friendly/internal review.
- Friendly reviewer packet exists.
- Supplement/export formatting plan exists.
- Reference cleanup and citation integration planning are complete for the current stage.
- Dataset attribution and availability decision package exists.
- Public bioRxiv remains **Hold / not submission-ready**.
- Dataset redistribution remains unresolved.
- Supplement/export remains not public-submission-ready.

## Yesterday's Summary

On 2026-05-06, Permea progressed from SOD restore through reference cleanup planning, conservative bibliography title-protection cleanup, dataset availability decision packaging, manuscript v0.2 drafting, v0.2 audit, friendly reviewer packet creation, and supplement/export formatting planning.

Latest pushed commit:

- `94107ec docs: add supplement export formatting plan`

## Recommended Next Tasks

1. **Task 127 - SOD context restore**
   - Read this handoff and EOD report.
   - Verify repo state.
   - Summarize current blockers and priorities.
2. **Task 128 - Friendly reviewer outreach message refinement**
   - Refine outreach language for specific friendly/internal reviewer use.
   - Do not imply external expert review or peer review.
3. **Task 129 - Supplement v0.2 alignment plan or supplement draft revision**
   - Align supplement structure with manuscript v0.2.
   - Do not modify result/data/figure artifacts.
4. **Task 130 - Dataset/source manual decision checklist refinement**
   - Prepare checklist for founder/legal/source review.
   - Do not make legal conclusions.
5. **Task 131 - Manuscript v0.3 after feedback or export planning**
   - Only after feedback or explicit instruction.

## Current Blockers

- Dataset source identity unresolved.
- Dataset license/terms unresolved.
- Processed dataset redistribution unresolved.
- Original label-source criteria unresolved.
- Final data/code availability wording unresolved.
- `references.bib` human metadata cleanup incomplete.
- Final citation/source-to-claim review incomplete.
- Supplement v0.2 not yet drafted/finalized.
- Figure/table captions and numbering incomplete.
- Export manifest incomplete.
- Founder/manual approval required.
- Final public posting decision required.

## Public Readiness Status

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Supplement/export remains not public-submission-ready.

## Claim-Boundary Reminder

Maintain these boundaries:

- This is computational/in-silico evidence only.
- Manuscript v0.2 is friendly/internal-review ready only.
- Do not claim leakage-free status.
- Do not claim robust generalization.
- Do not claim biological validation.
- Do not claim wet-lab validation.
- Do not claim in-vivo validation.
- Do not claim therapeutic or clinical efficacy.
- Do not claim dataset redistribution is permitted.
- Do not imply external expert review or peer review.

## Suggested First Maintainer Task

Use Task 127:

**Permea SOD Context Restore - 2026-05-07**

Read this handoff, verify repo state, summarize current status and blockers, and recommend the first execution task for the day.
