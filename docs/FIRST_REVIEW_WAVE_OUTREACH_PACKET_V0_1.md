# First Review Wave Outreach Packet v0.1

## Purpose

This document assembles the first review-wave outreach plan and packet routing after the internal dry run.

It is intended for practical circulation planning only. It does not add new evidence, new benchmark results, or new biological claims.

## Status

Status: ready for first review wave

Basis: `FIRST_REVIEW_WAVE_DRY_RUN_V0_1.md` found no P0 or P1 issues.

Remaining P2: Reviewer A needs more provenance, artifact, benchmark, and evidence-boundary context than the minimum packet provides. This is handled by routing Reviewer A to the extended packet by default.

## Reviewer assignment table

| Reviewer placeholder | Review perspective | Packet type | Core documents | Optional documents | Primary questions | Desired feedback format | Intake destination |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reviewer A | Computational/reproducibility | Extended by default | `PREPRINT_DRAFT_V0_1.md`; `CIRCULATION_GUIDE_V0_1.md`; `REVIEWER_NOTE_V0_1.md`; `DATASET.md`; `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md`; `PREPRINT_ASSEMBLY_V0_1.md`; `SUPPLEMENTARY_OUTLINE_V0_1.md` | `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` if submission-readiness context is useful | Is the benchmark framing legible? Are provenance and artifact boundaries clear? Is the imported-versus-regenerated distinction understandable? | Specific comments by document/section, with severity if possible | `REVIEW_FEEDBACK_LOG_V0_1.md` |
| Reviewer B | Biological/skeptical | Minimum first; extended materials available on request | `PREPRINT_DRAFT_V0_1.md`; `CIRCULATION_GUIDE_V0_1.md`; `REVIEWER_NOTE_V0_1.md` | `DATASET.md`; `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Does any wording overstate biological meaning? Are limitations candid? Does candidate prioritization remain distinct from validation? | Claim-boundary comments and flagged sentences | `REVIEW_FEEDBACK_LOG_V0_1.md` |
| Reviewer C | Technical clarity | Minimum | `PREPRINT_DRAFT_V0_1.md`; `CIRCULATION_GUIDE_V0_1.md`; `REVIEWER_NOTE_V0_1.md` | Support docs only if requested | Is the manuscript readable without insider context? Is the packet easy to follow? Are figures and document roles clear? | Readability and structure comments | `REVIEW_FEEDBACK_LOG_V0_1.md` |

## Packet routing

Reviewer A receives the extended packet by default. This is for review usefulness: the extended packet provides provenance, artifact, benchmark, and evidence-boundary context. It does not imply stronger biological validation.

Reviewer B receives the minimum packet first. Extended materials are available on request if dataset, evidence-package, or provenance context would improve the review.

Reviewer C receives the minimum packet. The goal is technical clarity and readability, not full benchmark or provenance review.

## Outreach message selection

Use `REVIEW_OUTREACH_TEMPLATES_V0_1.md` as follows:

- Reviewer A: Template A — Computational reviewer
- Reviewer B: Template B — Biologically literate reviewer
- Reviewer C: Template C — General technical clarity reviewer

Customize each message to state the selected packet type and to ask explicitly for claim-boundary feedback.

## Feedback intake process

Use `REVIEW_FEEDBACK_LOG_V0_1.md` and `REVISION_PRIORITY_FRAMEWORK_V0_1.md`.

Process:

1. Receive feedback.
2. Log each substantive point separately.
3. Assign P0-P4 priority.
4. Separate manuscript edits from future-work suggestions.
5. Do not implement scope-expanding suggestions immediately.
6. Convert accepted P0-P2 items into a file-level revision plan.

## Claim-boundary reminders

- no wet-lab validation claims
- no solved delivery claims
- no broad biological generalization
- no therapeutic or clinical efficacy claims
- computational candidate prioritization is not biological validation
- feature importance should not be treated as mechanistic proof

## Send/no-send checklist

- [ ] Latest committed review-operation docs confirmed.
- [ ] Dry-run memo committed.
- [ ] Packet routing updated.
- [ ] Reviewer A extended packet assembled.
- [ ] Reviewer B minimum packet assembled.
- [ ] Reviewer C minimum packet assembled, if Reviewer C is included.
- [ ] Feedback log ready.
- [ ] Priority framework ready.
- [ ] Outreach templates selected.
- [ ] No unresolved P0/P1 issues.

## Next step after outreach

After outreach, collect feedback, log it in `REVIEW_FEEDBACK_LOG_V0_1.md`, perform priority-based revision planning, and only then revise `PREPRINT_DRAFT_V0_1.md`.
