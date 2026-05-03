# Trusted Review Feedback Intake Template v0.1

## Purpose

This template is used to intake feedback from the trusted review circulation wave after human-operated outreach.

This is for actual trusted reviewer feedback. It is not for internal harsh council findings, is not a manuscript edit document, is not public peer review, does not add new scientific evidence, and does not change the current evidence boundary.

## Intake principles

- Log first, revise later.
- Split feedback into atomic substantive points.
- Do not merge unrelated issues.
- Preserve reviewer meaning without exaggeration.
- Classify each item with P0-P4 priority.
- Separate current-package revisions from future-work suggestions.
- Do not implement scope-expanding suggestions immediately.
- Preserve the distinction between computational evidence and biological validation.
- Preserve the distinction between trusted reviewer feedback and internal harsh council findings.

## Reviewer source fields

Allowed reviewer placeholders:

- Reviewer A — computational/reproducibility
- Reviewer B — biological/skeptical
- Reviewer C — technical clarity
- External Reviewer — unspecified trusted reviewer

Do not invent real reviewer names. If real names are added later by the human operator, they should be added manually and only with permission.

## Intake table schema

Use one row per atomic feedback item.

| Feedback ID | Intake date | Reviewer placeholder | Reviewer perspective | Packet received | Feedback source format | Area | Raw feedback summary | Normalized feedback item | Priority P0-P4 | Affected document or artifact | Recommended action | Action type | Current-package edit? | Future-work item? | Required before further trusted review? | Required before public preprint? | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FB-001 | YYYY-MM-DD | Reviewer A/B/C or External Reviewer | Computational/biological/clarity/other | Minimum/extended/custom | Email/call/inline note/doc comment | Area | Summary only | Atomic item | P0-P4 | File or artifact path | Specific action or no action | See action types | yes/no | yes/no | yes/no | yes/no | logged | Notes |

Suggested action types:

- manuscript wording
- claim-boundary tightening
- provenance clarification
- benchmark-method clarification
- artifact traceability clarification
- figure/table clarification
- limitation clarification
- reviewer-packet clarification
- future wet-lab validation
- future benchmark expansion
- future model development
- future deck/pitch hardening
- no action

Suggested statuses:

- logged
- needs triage
- planned
- in progress
- resolved
- deferred
- rejected with rationale

## P0-P4 quick classification guide

| Priority | Meaning | Typical handling |
| --- | --- | --- |
| P0 | Factual or internal contradiction | Fix before further circulation |
| P1 | Claim-boundary or overinterpretation risk | Fix before public-facing circulation or preprint submission |
| P2 | Benchmark, provenance, method, dataset, or artifact clarity issue | Fix or explicitly defer before preprint submission |
| P3 | Readability, formatting, figure/table, or structure improvement | Handle after scientific clarity is stable |
| P4 | Future-work suggestion | Log as future work unless it exposes a current-package risk |

P0 examples:

- manuscript metric differs from artifact table
- document says provenance is complete while another says `pending_confirmation`

P1 examples:

- wording implies wet-lab validation
- wording implies solved BBB delivery
- feature importance reads like mechanism

P2 examples:

- reviewer cannot trace a metric to an artifact
- label/source criteria are unclear
- leakage caveat is insufficiently visible

P3 examples:

- reading order is confusing
- figure caption is unclear
- limitation section placement is weak

P4 examples:

- reviewer suggests a new model family
- reviewer suggests a wet-lab assay
- reviewer suggests an additional benchmark dataset

## Reviewer-specific intake guidance

Reviewer A feedback:

- Prioritize reproducibility, artifact traceability, provenance, metrics, leakage caveats, and split policy.
- Treat most such items as likely P2 unless the reviewer identifies a contradiction or overclaim.
- Escalate to P0 if a reported metric or artifact reference is inconsistent.
- Escalate to P1 if benchmark language implies biological validation.

Reviewer B feedback:

- Prioritize biological overread, wet-lab ambiguity, mechanism risk, therapeutic claim risk, and limitation adequacy.
- Treat claim-boundary risks as likely P1.
- Treat requested wet-lab experiments as P4 unless the request reveals that the current manuscript overclaims.

Reviewer C feedback:

- Prioritize clarity, reading order, packet usability, current-claim comprehension, and category misunderstanding risk.
- Treat most clarity items as likely P3.
- Escalate to P1 if unclear wording causes a reader to infer wet-lab validation, solved delivery, or broad biological generalization.

## Normalization examples

These are hypothetical examples for intake practice. They are not actual reviewer feedback.

Hypothetical raw feedback:

> The provenance is unclear and the feature importance sounds a bit mechanistic.

Normalize into:

| Normalized item | Likely priority | Rationale |
| --- | --- | --- |
| Provenance clarity issue | P2 | The reviewer cannot determine what is confirmed, pending, or unresolved. |
| Feature-importance mechanism risk | P1 | The reviewer may read model-level feature importance as biological mechanism. |

Hypothetical raw feedback:

> The paper is interesting, but I would like to see a transformer model and an in vivo assay.

Normalize into:

| Normalized item | Likely priority | Rationale |
| --- | --- | --- |
| New model family suggestion | P4 | This requires future model development and should not be backfilled into current claims. |
| Wet-lab assay suggestion | P4 | This is future validation work, not current evidence. |

## Revision gating rules

- P0 must be handled before further circulation.
- P1 must be handled before public-facing circulation or preprint submission.
- P2 should be handled before preprint submission, or explicitly disclosed and deferred.
- P3 should be handled after scientific clarity is stable.
- P4 should be logged as future work unless it exposes a current-package risk.
- Do not make immediate manuscript edits before triage unless a P0 contradiction is obvious and bounded.

## Feedback-to-task conversion

Use feedback intake to create scoped follow-up tasks. Examples:

- Task 019 — Intake Trusted Review Feedback Round 1
- Task 020 — Apply P0/P1 Trusted Review Corrections
- Task 021 — Apply P2 Trusted Review Provenance and Benchmark Revisions
- Task 022 — Prepare Preprint Revision Pass

Each task should identify source feedback IDs, priority levels, affected files, allowed edits, and explicit scope exclusions.

## Human operator checklist

- [ ] Reviewer identity confirmed privately.
- [ ] Packet sent according to routing.
- [ ] Feedback received.
- [ ] Feedback copied into intake template.
- [ ] Feedback split into atomic items.
- [ ] P0-P4 priority assigned.
- [ ] Affected documents or artifacts identified.
- [ ] Current-package versus future-work separation completed.
- [ ] No immediate manuscript edits before triage.
- [ ] Next Codex task selected.

