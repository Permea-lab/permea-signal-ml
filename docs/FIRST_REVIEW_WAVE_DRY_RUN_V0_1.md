# First Review Wave Dry Run v0.1

## Purpose

This document records an internal pre-circulation dry run of the first review-wave packet for the current BBB-oriented Permea manuscript package.

This is not actual reviewer feedback. It is a packet-readiness check intended to reduce category confusion, claim expansion, and packet ambiguity before any trusted reviewer receives the materials.

## Dry-run scope

This dry run evaluates:

- packet completeness
- reading order
- claim-boundary clarity
- reviewer prompt clarity
- feedback intake readiness
- revision triage readiness

This dry run does not evaluate:

- new model performance
- new biological evidence
- wet-lab validation
- therapeutic relevance
- final submission readiness

## Packet tested

Minimum packet:

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`

Optional extended packet:

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`
- `INTERNAL_REVIEW_MEMO_V0_1.md`
- `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`

Operational docs used for intake and triage:

- `REVIEWER_PACKET_V0_1.md`
- `REVIEW_OPERATIONS_INDEX_V0_1.md`
- `FIRST_REVIEW_WAVE_PLAN_V0_1.md`
- `FIRST_REVIEW_WAVE_CHECKLIST_V0_1.md`
- `REVIEW_FEEDBACK_LOG_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`
- `REVIEW_OUTREACH_TEMPLATES_V0_1.md`

## Simulated reviewer perspectives

### Reviewer A — computational/reproducibility perspective

Likely first impression:

- The manuscript is benchmark-aware and cautious, with clear attention to rerun artifacts and provenance boundaries.
- The minimum packet shows the scientific story, but it does not provide enough supporting detail for a full reproducibility-oriented read.

What they can evaluate well from the current packet:

- high-level benchmark framing
- metric interpretation at manuscript level
- imported-versus-regenerated distinction
- whether the manuscript overclaims computational evidence

What they cannot evaluate from the current packet:

- full dataset/provenance detail
- artifact inventory and submission gaps
- supplement structure
- whether all result artifacts are easy to trace from the manuscript alone

Likely confusion points:

- the minimum packet may leave this reviewer asking where dataset, provenance, and artifact details live
- the `CIRCULATION_GUIDE_V0_1.md` reading order points to support docs that are not in the minimum packet

Documents that help reduce confusion:

- `REVIEWER_PACKET_V0_1.md`
- `DATASET.md`
- `V0_1_EVIDENCE_PACKAGE.md`
- `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`

Pre-circulation fixes, if any:

- Send Reviewer A the extended packet by default.

### Reviewer B — biological/skeptical perspective

Likely first impression:

- The packet repeatedly states that the work is computational, benchmark-specific, and not experimental validation.
- The manuscript is likely readable as a bounded candidate-prioritization package rather than a biological proof claim.

What they can evaluate well from the current packet:

- biological overclaim risk
- whether the limitations are candid
- whether feature-importance language stays descriptive
- whether the candidate-prioritization interpretation is responsible

What they cannot evaluate from the current packet:

- detailed reproducibility or artifact completeness
- formal reference adequacy
- final submission metadata readiness

Likely confusion points:

- the phrase "delivery signal" may need careful reading, but the reviewer note and manuscript limitations reduce the risk of overreading
- the broader Permea framing may sound ambitious, but the current manuscript repeatedly narrows the claim to this BBB-oriented wedge

Documents that help reduce confusion:

- `REVIEWER_NOTE_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `PREPRINT_DRAFT_V0_1.md`

Pre-circulation fixes, if any:

- No blocking fixes identified.

### Reviewer C — technical clarity perspective

Likely first impression:

- The minimum packet is usable for a clarity pass.
- The document roles are understandable, but the total package can feel document-heavy if the ask is not kept narrow.

What they can evaluate well from the current packet:

- readability
- section flow
- whether the manuscript can be followed without insider context
- whether figures and support docs are clearly signposted

What they cannot evaluate from the current packet:

- correctness of benchmark implementation
- provenance closure
- biological validation
- final submission readiness

Likely confusion points:

- the difference between manuscript-review docs and operational-review docs may need a short explanation in outreach
- the minimum packet should be described as a first-pass clarity and claim-boundary packet, not the whole evidence package

Documents that help reduce confusion:

- `REVIEWER_PACKET_V0_1.md`
- `REVIEW_OPERATIONS_INDEX_V0_1.md`
- `REVIEW_OUTREACH_TEMPLATES_V0_1.md`

Pre-circulation fixes, if any:

- Use a narrow outreach ask and avoid sending the extended packet unless needed.

## Claim-boundary dry run

| Priority | Check | Dry-run result | Action |
| --- | --- | --- | --- |
| P0 | Factual or internal contradiction | No P0 contradiction found in the reviewed packet docs. | No pre-circulation fix required. |
| P1 | Solved delivery, wet-lab validation, broad generalization, therapeutic or clinical claims | No P1 claim-boundary breach found. The packet repeatedly states computational evidence only and no experimental validation. | No pre-circulation fix required. |
| P1 | Feature-importance overinterpretation | No P1 breach found. The draft says feature importance should not be read mechanistically. | No pre-circulation fix required. |
| P2 | Benchmark/provenance/method clarity | Reviewer A should receive the extended packet because the minimum packet alone does not carry enough provenance and artifact detail. | Route Reviewer A to the extended packet. |
| P3 | Reading-order clarity | `CIRCULATION_GUIDE_V0_1.md` points to support docs beyond the minimum packet, which could confuse a minimum-packet-only reviewer unless outreach is explicit. | Clarify packet scope in outreach; no document edit required before sending. |
| P4 | Future work | Requests for new model families, new features, validation, or additional datasets should be logged as future work, not implemented in the first revision cycle by default. | Use `REVISION_PRIORITY_FRAMEWORK_V0_1.md`. |

## Minimum-packet readiness judgment

| Reviewer type | Minimum packet status | Rationale |
| --- | --- | --- |
| Reviewer A — computational/reproducibility | Ready with minor edits | The minimum packet is enough for high-level benchmark and claim-boundary review, but the extended packet is preferable for reproducibility and provenance assessment. The practical fix is packet routing, not manuscript revision. |
| Reviewer B — biological/skeptical | Ready | The minimum packet clearly asks for biological framing and overclaim review while preserving the computational-only boundary. |
| Reviewer C — technical clarity | Ready | The minimum packet is appropriate for readability, coherence, and category-clarity review. |

Must be fixed before sending:

- No P0 or obvious P1 issues were found.
- Reviewer A should receive the extended packet rather than the minimum packet if the goal is reproducibility review.

Can wait until after first feedback:

- figure polish
- formal references
- final metadata
- full supplementary prose
- new experiments, new model families, new features, or validation planning

## Feedback intake readiness

`REVIEW_FEEDBACK_LOG_V0_1.md` and `REVISION_PRIORITY_FRAMEWORK_V0_1.md` are sufficient to capture:

- contradiction issues
- claim-boundary concerns
- provenance concerns
- benchmark clarity concerns
- readability concerns
- future-work suggestions

The log has fields for reviewer placeholder, date, area, feedback, priority, action, status, and notes. The priority framework defines P0-P4 categories and clearly separates manuscript revisions from future research tasks.

No fake reviewer feedback was added to `REVIEW_FEEDBACK_LOG_V0_1.md`.

## Recommended pre-circulation edits

| Priority | Issue | Affected document | Recommended action | Required before sending? |
| --- | --- | --- | --- | --- |
| P2 | Computational/reproducibility reviewer needs more support than the minimum packet provides. | `REVIEWER_PACKET_V0_1.md`, outreach message | Send Reviewer A the extended packet by default. | Yes |
| P3 | Minimum-packet readers could wonder why `CIRCULATION_GUIDE_V0_1.md` lists support docs not included in the minimum packet. | Outreach message | State that the minimum packet is a first-pass review bundle and that support docs are available if needed. | No |

## Go / no-go recommendation

Recommendation: Go for first review wave.

Rationale: The packet consistently preserves the computational evidence boundary, avoids wet-lab validation and solved-delivery claims, and provides enough operational structure for feedback intake and triage. The only required pre-circulation action is to route Reviewer A to the extended packet by default.

## Next step

Recommended next task:

Task 004 — Finalize First Review-Wave Outreach Packet

This should turn the dry-run routing decision into final reviewer-specific outreach text and packet selection without changing the scientific scope.
