# Harsh Review — Reviewer C Technical Clarity v0.1

## Purpose

This is an internal harsh review from the technical clarity and narrative perspective. It is not external reviewer feedback.

Reviewer C evaluates whether a serious technical outsider can understand the manuscript, review packet, evidence boundary, and review instructions without insider context.

## Materials reviewed

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`
- `REVIEWER_PACKET_V0_1.md`
- `FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`
- `DATASET.md`
- `FIRST_EVIDENCE_SUMMARY.md`
- `V0_1_EVIDENCE_PACKAGE.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`
- `REVIEW_FEEDBACK_LOG_V0_1.md`
- `HARSH_REVIEW_COUNCIL_CHARTER_V0_1.md`
- `HARSH_REVIEW_ROUND_0_BASELINE_V0_1.md`
- `REVIEW_OPERATIONS_INDEX_V0_1.md`

## Reviewer C verdict

Verdict: Pass for trusted review.

The manuscript and packet are understandable enough for trusted review. The main clarity risk is document-stack complexity: the project now has many support and review-operation docs, so the reviewer ask must remain narrow and packet routing must be followed.

## Main clarity concerns

- A serious technical outsider can understand the current claim if they start with the preprint draft and reviewer note.
- The minimum packet explains what is claimed and not claimed.
- Reading order is clear enough but differs between some guide/index contexts because they serve different packet sizes.
- The central claim is identifiable: initial computational evidence for benchmark-oriented candidate prioritization before experimental validation.
- Platform ambition is mostly separated from current evidence, but support docs can feel larger than the manuscript.
- Repeated terms are generally consistent: computational evidence, candidate prioritization, benchmark-oriented, imported versus regenerated.
- The limitations section is strong enough for trusted review.
- Packet routing is understandable after the outreach packet.
- Review instructions are actionable.

## Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before trusted review? | Required before preprint? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | P3 | Document stack | The review-operation layer is useful but heavy. | Operations index, packet, plan, checklist, dry run, outreach packet, council docs. | `REVIEW_OPERATIONS_INDEX_V0_1.md`; outreach packet | Keep reviewer-facing packet narrow; do not send all operations docs to clarity reviewers. | No | No |
| C-02 | P3 | Reading order | Reading order varies by use case, which is reasonable but could confuse if not explained in outreach. | `CIRCULATION_GUIDE_V0_1.md`; `REVIEW_OPERATIONS_INDEX_V0_1.md`; `REVIEWER_PACKET_V0_1.md` | Outreach message | State which packet is being sent and what the reviewer should focus on. | No | No |
| C-03 | P3 | Central claim | Central claim is clear but dense in the abstract because many boundary qualifiers are packed together. | `PREPRINT_DRAFT_V0_1.md` abstract. | `PREPRINT_DRAFT_V0_1.md` | Consider later editorial tightening without weakening claim boundaries. | No | Yes |
| C-04 | P2 | Ambition versus evidence | Broader Permea framing could feel platform-like if read without the manuscript limitations. | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Support docs; outreach materials | Keep current wedge language close to broader ambition. | No | Yes |
| C-05 | P3 | Figure/table readiness | Figure and table references are adequate for trusted review but not final publication. | `PREPRINT_ASSEMBLY_V0_1.md`; `SUPPLEMENTARY_OUTLINE_V0_1.md` | Figure captions; assembly docs | Defer polish until after feedback. | No | No |
| C-06 | P4 | Deck/pitch hardening | No deck files were found, so deck narrative alignment cannot be reviewed. | Repo file inspection. | Future deck materials | Review separately when deck exists in repo. | No | No |

## Harsh questions for the authors

- Can a first-time reader state the current claim in one sentence?
- Does the package make clear that this is not a validation paper?
- Does the paper read like evidence, or like platform marketing?
- Are the manuscript, reviewer note, and circulation guide aligned?
- Does the reader know what to review and what not to review?
- Are support docs helping review, or distracting from the manuscript ask?
- Is the difference between minimum and extended packet obvious to the sender?

## Reviewer C recommended next actions

Must fix before wider circulation:

- None blocking trusted review circulation.

Should fix before preprint:

- Tighten abstract readability while preserving qualifiers.
- Keep current evidence wedge adjacent to any broader Permea context.
- Polish figure/table captions and numbering.

Can defer to future work:

- Website/deck/pitch narrative alignment.
- Full publication formatting.
- Submission package design.
