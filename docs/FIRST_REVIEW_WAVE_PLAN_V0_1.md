# First Review Wave Plan v0.1

## Purpose

This document defines the first structured review wave for the current BBB-oriented Permea manuscript package.

The goal is to collect focused feedback on claim boundaries, benchmark legibility, provenance clarity, biological framing, and manuscript readability before moving toward broader external circulation or submission formatting.

## Review-wave status

Status: ready for internal or trusted-review execution.

The package is not final for public submission. It is appropriate for a small first review wave intended to identify high-priority issues before metadata finalization, formal references, supplement drafting, or export preparation.

## Recommended reviewer mix

Start with a small review group and avoid broad circulation until first-wave feedback has been logged and triaged.

| Placeholder | Reviewer type | Target count | Packet | Primary feedback needed |
| --- | --- | ---: | --- | --- |
| Reviewer A | Computational benchmark / reproducibility | 1 | Extended | Benchmark framing, artifact structure, rerun logic, metric clarity, provenance clarity |
| Reviewer B | Biological / skeptical | 1 | Minimum | Biological plausibility framing, overclaim risk, limitation clarity, experimental-validation boundary |
| Reviewer C | Technical clarity | 0-1 | Minimum | Readability, coherence, figure/table usefulness, ability to follow without insider context |

Do not invent or document real reviewer names in this plan. Replace placeholders only in private outreach tracking if needed.

## Minimum packet

Use the minimum packet when the main review goal is fast feedback on manuscript clarity and claim boundary.

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`

## Extended packet

Use the extended packet when the reviewer is likely to inspect benchmark structure, provenance, artifact organization, or submission-readiness gaps.

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`
- `DATASET.md`
- `FIRST_EVIDENCE_SUMMARY.md`
- `V0_1_EVIDENCE_PACKAGE.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`

Use `REVIEWER_PACKET_V0_1.md` as the canonical packet definition.
Reviewer A should receive this extended packet by default. The extended packet provides provenance, artifact, benchmark, and evidence-boundary context; it does not imply stronger biological validation.

## Reviewer selection criteria

Reviewer A should be able to evaluate whether the work is benchmark-aware and reproducible enough for the current claim level. This reviewer does not need to endorse the biological thesis.

Reviewer B should be able to identify biological overinterpretation risk and should be comfortable challenging language that sounds stronger than computational evidence supports.

Reviewer C should be able to read the package as a technically literate outsider and identify where the manuscript or support documents become hard to follow.

Avoid selecting reviewers whose main expected response would be to request a different project scope, a new model family, or wet-lab validation as a condition for first-wave manuscript feedback. Those comments may be useful later, but they are not the purpose of this review wave.

## What reviewers should evaluate

- whether the claim boundary is clear and consistently enforced
- whether the manuscript reads as a bounded computational evidence package
- whether benchmark framing, metric interpretation, and artifact structure are legible
- whether the imported-versus-regenerated distinction is understandable
- whether dataset and provenance limitations are sufficiently explicit
- whether figures and tables are adequate for a first review round
- whether any wording implies validation, mechanism, therapeutic relevance, or broad generalization beyond the evidence

## What reviewers should not be asked to evaluate

Reviewers should not be asked to judge the package as:

- a wet-lab validation paper
- a therapeutic efficacy paper
- a solved-delivery claim
- a broad biological generalization paper
- a final submission-ready manuscript with finalized metadata and formal references
- an optimized modeling benchmark or model-family comparison study

## Review sequence

1. Confirm the package status remains draft preprint and computational evidence only.
2. Select reviewer type and packet.
3. Customize one short message from `REVIEW_OUTREACH_TEMPLATES_V0_1.md`.
4. Send the minimum packet to Reviewer B and Reviewer C, if used.
5. Send the extended packet to Reviewer A by default.
6. Ask all reviewers to flag any sentence that sounds stronger than the current evidence supports.
7. Record each substantive comment in `REVIEW_FEEDBACK_LOG_V0_1.md`.
8. Assign P0-P4 priority using `REVISION_PRIORITY_FRAMEWORK_V0_1.md`.
9. Convert accepted or clarified feedback into a file-level revision plan.
10. Defer submission formatting until P0-P2 issues are resolved or explicitly deferred with rationale.

## Expected outputs

The first review wave should produce:

- one or more logged comments from Reviewer A
- one or more logged comments from Reviewer B
- optional clarity comments from Reviewer C
- P0-P4 priority labels for each substantive issue
- action decisions for high-priority comments
- a file-level revision plan for the next manuscript/package pass
- a clear list of future-work requests that should not be implemented in the current revision cycle

## Claim-boundary reminders

- The current package is computational evidence only.
- The current package does not claim wet-lab validation.
- The current package does not claim solved biological delivery.
- The current package does not claim mechanistic causality.
- The current package does not claim therapeutic efficacy.
- The current package does not claim broad delivery generalization.
- The current feature surface is intentionally narrow.
- The current model set is baseline-oriented.
- Provenance, attribution, and licensing gaps should remain explicit limitations.

## Completion criteria

The first review wave is complete when:

- Reviewer A or an equivalent computational/reproducibility review has been logged
- Reviewer B or an equivalent biological/claim-boundary review has been logged
- all P0 comments have an action decision
- all P1 comments have an action decision before further external-facing circulation
- all P2 comments have a planned fix or documented deferral before submission preparation
- scope-expanding future-work suggestions are separated from current manuscript revisions
- the next revision pass has a concrete file-level scope
