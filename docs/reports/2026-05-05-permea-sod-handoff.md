# Permea SOD Handoff - 2026-05-05

## Purpose

This document is the start-of-day handoff for continuing Permea work in a new ChatGPT/Codex conversation.

When the user says "SOD 진행하자", this document should be read first, together with `docs/reports/2026-05-04-permea-eod-report.md`.

Prompt files for starting new sessions:

- ChatGPT prompt: `docs/reports/2026-05-05-permea-chatgpt-sod-prompt.md`
- Codex prompt: `docs/reports/2026-05-05-permea-codex-sod-prompt.md`

## How to Use This SOD Document

1. Read this document.
2. Confirm repository state.
3. Summarize yesterday's completed work.
4. Present today's top priorities.
5. Ask the user to choose a path if a decision is required.
6. Produce the Codex prompt for the next task.

## Current Repo State to Verify

Run:

```bash
cd /Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml
git status -sb
git log --oneline -10
git remote -v
git ls-remote --heads origin master
```

Expected:

- Branch: `master`.
- Working tree: clean.
- Latest remote commit: `3f0d982` or newer.
- Remote: `https://github.com/Permea-lab/permea-signal-ml.git`.

## Yesterday's Summary

On 2026-05-04, the post-sensitivity manuscript package reached internal-continuation status:

- Leakage-aware grouping utilities, group assignments, split manifests, and baseline rerun outputs were completed.
- Leakage-aware findings were investigated and interpreted conservatively.
- Manuscript candidate, preprint draft, and supplement draft were updated with sensitivity findings.
- Final post-sensitivity claim/citation audit passed.
- Post-sensitivity founder/manual decision brief was prepared.
- Remote package was pushed through `3f0d982 docs: add post-sensitivity founder decision brief`.

## Current Scientific Status

- Evidence package is strong enough for a caveated computational preprint path after operational cleanup.
- P0/P1 blockers: none for internal continuation.
- Public preprint status: **Hold / not submission-ready**.
- Remaining blockers are operational, legal, reference, export, and founder/manual approval items.
- Sensitivity findings support the computational benchmark-signal claim under the specific grouping strategy.
- Findings do not establish leakage-free status, robust generalization, biological validation, or wet-lab validation.

## Today's Likely Priorities

### Priority 1 - Metadata/Disclosure Completion

- Author list.
- Affiliation.
- Corresponding email.
- ORCID.
- Funding, competing interests, acknowledgements, and ethics statements.

### Priority 2 - `references.bib` Cleanup

- Full author lists.
- Venue, page, volume, issue, DOI, and URL cleanup.
- Citation-source-claim review.

### Priority 3 - Dataset Legal/Availability Decision

- Decide whether public data, private data, or derived-artifacts-only release is appropriate.
- Finalize code availability statement.
- Finalize dataset license or unresolved-license statement.

### Priority 4 - Supplement/Export Formatting

- Caption review.
- File path review.
- Export manifest review.
- Figure/table inclusion and formatting review.

### Priority 5 - Final bioRxiv Readiness Audit

- Recheck metadata, legal, references, supplement/export, claim boundaries, and posting approval.

## Decision Options for Today

### Option A - Fastest Path to bioRxiv Candidate

Fill metadata, legal, reference, and supplement/export blockers; keep leakage-aware sensitivity result as supporting computational evidence; run final readiness audit.

### Option B - Polish Manuscript First

Review manuscript text manually or virtually for readability, related work, and presentation before metadata/legal closure.

### Option C - Prepare Website Evidence Archive in Parallel

Prepare website evidence archive only after strict claim-boundary review. Do not imply bioRxiv posting, peer review, biological validation, or public approval.

Recommended: start with metadata/disclosure and references cleanup because scientific evidence is now sufficiently defensible for internal candidate status.

## ChatGPT SOD Behavior Rule

When user says "SOD 진행하자":

- Load the latest SOD handoff doc.
- Summarize current state.
- Show today's priorities.
- Propose the next Codex task.
- Do not assume public preprint is ready.
- Maintain claim discipline.

## Suggested ChatGPT Prompt for New Conversation

Canonical prompt file: `docs/reports/2026-05-05-permea-chatgpt-sod-prompt.md`.

```text
We are continuing Permea from the 2026-05-05 SOD handoff. Read docs/reports/2026-05-05-permea-sod-handoff.md and docs/reports/2026-05-04-permea-eod-report.md. Current repo is /Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml. Latest pushed package includes leakage-aware sensitivity results and manuscript updates. Public bioRxiv remains Hold. Start by summarizing current status and proposing today's next task.
```

## Suggested Codex Prompt for New Conversation

Canonical prompt file: `docs/reports/2026-05-05-permea-codex-sod-prompt.md`.

## Suggested Codex First Task for SOD

Task 100 - Commit Permea 2026-05-04 EOD and 2026-05-05 SOD Reports

## No-Change Confirmation

- Manuscript scientific content was not modified by this handoff.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- Metric values were not changed.
- No public-preprint-ready, leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
