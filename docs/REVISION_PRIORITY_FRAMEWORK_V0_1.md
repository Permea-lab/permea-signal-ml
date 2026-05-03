# Revision Priority Framework v0.1

## Purpose

This framework defines how first-wave review feedback should be triaged and converted into disciplined manuscript or repository revisions.

The goal is to revise by evidence risk and clarity impact, not by reaction to the loudest comment. The framework should prevent scope creep and preserve the current boundary between computational benchmark evidence and future biological validation.

## Priority levels

| Priority | Meaning | Required handling |
| --- | --- | --- |
| P0 | Factual error or internal contradiction | Must fix before any further circulation |
| P1 | Claim-boundary or overinterpretation risk | Must fix before external-facing circulation |
| P2 | Benchmark, provenance, method, dataset, or artifact clarity issue | Should fix before preprint submission |
| P3 | Readability, formatting, figure/table, or structure improvement | Fix after scientific clarity is stable |
| P4 | Future-work suggestion | Log but do not implement immediately unless it strengthens the current trust surface |

## Examples

P0 examples:

- manuscript reports a metric differently from `results/tables/model_comparison_summary.csv`
- methods and results describe different feature sets
- the draft contradicts `DATASET.md` on row count, fields, split policy, or provenance status
- a figure caption describes an artifact as regenerated when it is imported

P1 examples:

- wording implies wet-lab validation
- wording implies mechanistic causality from feature importance
- wording implies therapeutic efficacy or clinical relevance
- wording implies broad BBB or delivery generalization beyond the current wedge
- reviewer reads the manuscript as a solved-delivery claim

P2 examples:

- the benchmark contract is hard to understand
- imported-versus-regenerated artifacts are confusing
- split policy or random seed is not sufficiently clear
- provenance gaps are mentioned but not connected to claim limits
- output artifacts are listed but their role is unclear

P3 examples:

- section order makes the manuscript harder to follow
- figure placement could be improved
- table naming is inconsistent
- support documents are useful but reading order is unclear
- prose is accurate but too dense for first-pass review

P4 examples:

- add a new model family
- add structural or assay-derived features
- run wet-lab validation
- create a new benchmark wedge
- expand to additional delivery barriers
- build a larger external comparison study

## How to convert comments into actions

For each substantive comment:

1. Copy the reviewer observation into `REVIEW_FEEDBACK_LOG_V0_1.md`.
2. Assign one priority level from P0-P4.
3. Separate the reviewer observation from the action decision.
4. Identify the file or artifact that would need to change.
5. Decide whether the action is Accept, Reject, Defer, Clarify, or Incorporated.
6. For accepted P0-P2 items, write a specific file-level action.
7. For P4 items, record the idea as future work unless it directly improves current evidence trust without expanding claims.

## How to avoid scope creep

- Do not add experiments to satisfy a manuscript-clarity concern.
- Do not add model families unless the current review wave reveals a trust-blocking baseline gap.
- Do not turn future validation requests into current evidence claims.
- Do not broaden the biological scope beyond the BBB-oriented wedge.
- Do not convert a reviewer preference into a requirement unless it affects credibility, clarity, or claim discipline.
- Do not hide provenance gaps with softer wording; document them as limitations.

## Manuscript revisions versus future research tasks

Treat a comment as a manuscript or repo revision when it can be handled by:

- tightening claim language
- correcting a factual inconsistency
- improving the explanation of existing artifacts
- clarifying dataset, split, provenance, or metric language
- improving figure/table references or reading order
- aligning support docs with the current manuscript

Treat a comment as future research when it requires:

- new experiments
- new biological validation
- new model families
- new features
- new datasets
- new benchmark wedges
- external literature synthesis beyond the current source anchors

Future research tasks can be logged, but they should not block first-wave manuscript revision unless the reviewer identifies a trust issue that invalidates current interpretation.

## Preserving the current evidence boundary

Revision should preserve these boundaries:

- current evidence is computational and benchmark-specific
- current interpretation is candidate prioritization before experimental validation
- regenerated current-contract artifacts are the main present-tense evidence surface
- imported historical artifacts are continuity material, not primary current evidence
- feature importance is descriptive model behavior, not mechanism
- dataset provenance, attribution, and licensing gaps remain visible limitations
- submission preparation waits until first-wave P0-P2 issues are resolved or explicitly deferred

## File-level revision targets

| Feedback type | Likely file targets |
| --- | --- |
| Claim-boundary concern | `PREPRINT_DRAFT_V0_1.md`, `REVIEWER_NOTE_V0_1.md`, `FIRST_EVIDENCE_SUMMARY.md` |
| Benchmark framing concern | `PREPRINT_DRAFT_V0_1.md`, `V0_1_EVIDENCE_PACKAGE.md`, `PAPER_PACKAGE_V0_1.md` |
| Dataset/provenance concern | `DATASET.md`, `PROVENANCE.md`, `PREPRINT_DRAFT_V0_1.md` |
| Imported-versus-regenerated confusion | `IMPORTED_VS_REGENERATED.md`, `PREPRINT_DRAFT_V0_1.md`, `CIRCULATION_GUIDE_V0_1.md` |
| Figure/table concern | `FIGURE_INVENTORY.md`, `PREPRINT_ASSEMBLY_V0_1.md`, figure captions in `PREPRINT_DRAFT_V0_1.md` |
| Submission-readiness concern | `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`, `SUPPLEMENTARY_OUTLINE_V0_1.md` |
| Scope-expanding future work | Future roadmap or later issue tracking, not current manuscript claims |

## Revision-pass template

Use this structure when planning a revision pass:

| Item | Priority | Source feedback | File target | Planned action | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | P0-P4 | Reviewer / note | File path | Specific change | Open |

## Completion criteria

A revision pass is complete when:

- all P0 items are fixed or explicitly rejected with rationale
- all P1 items are fixed before further external-facing circulation
- all P2 items have either a fix or a documented deferral
- P4 items are separated from current manuscript revision work
- manuscript-facing files remain consistent with support docs
- no revised wording introduces a stronger biological claim than the current evidence supports
