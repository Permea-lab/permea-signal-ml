# Harsh Review Round 1 Integrated Issue Register v0.1

## Purpose

This register consolidates internal harsh review findings from Reviewer A, Reviewer B, and Reviewer C.

These are internal council findings, not external reviewer feedback.

## Inputs

- `HARSH_REVIEW_REVIEWER_A_COMPUTATIONAL_REPRODUCIBILITY_V0_1.md`
- `HARSH_REVIEW_REVIEWER_B_BIOLOGICAL_SKEPTICAL_V0_1.md`
- `HARSH_REVIEW_REVIEWER_C_TECHNICAL_CLARITY_V0_1.md`
- `HARSH_REVIEW_ROUND_0_BASELINE_V0_1.md`

## Council-level verdict

Verdict: Continue trusted review circulation.

No P0 or blocking P1 issue was identified. The package should remain in trusted review circulation while P2 issues are tracked for preprint readiness.

## Consolidated P0-P4 table

| Integrated issue ID | Source reviewer | Priority | Area | Finding | Affected document or artifact | Recommended action | Current status | Before trusted review? | Before preprint? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | A | P2 | Dataset provenance | Dataset version, attribution, licensing, and source metadata remain unresolved. | `DATASET.md`; metrics/manifests | Keep visible for trusted review; resolve or document before public preprint. | Open | No | Yes |
| I-02 | A | P2 | Label definition | Label semantics and source criteria are not fully defined. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Clarify if recoverable; otherwise mark unresolved. | Open | No | Yes |
| I-03 | A | P2 | Leakage risk | Duplicate, near-duplicate, and sequence-similarity leakage risks are not assessed in current docs. | `PREPRINT_DRAFT_V0_1.md`; future supplement | Treat as unresolved risk unless audited. | Open | No | Yes |
| I-04 | A | P2 | Artifact traceability | Manuscript metrics trace to artifacts, but public-facing artifact-to-claim mapping could be clearer. | `model_comparison_summary.csv`; metrics JSON; `PREPRINT_ASSEMBLY_V0_1.md` | Add compact artifact-to-claim mapping before public preprint. | Open | No | Yes |
| I-05 | A/B | P1 | Metric and claim interpretation | Metrics should remain benchmark-level and not biological validation. | `PREPRINT_DRAFT_V0_1.md`; reviewer docs | Preserve cautious PR-AUC/MCC and candidate-prioritization language. | Monitoring | No | Yes |
| I-06 | B | P1 | Biological overread risk | "Permeability-related signal" can be overread if isolated from qualifiers. | `PREPRINT_DRAFT_V0_1.md`; `FIRST_EVIDENCE_SUMMARY.md` | Keep computational and benchmark-specific qualifiers adjacent. | Monitoring | No | Yes |
| I-07 | B | P1 | Feature importance | Feature importance is currently non-mechanistic, but figure/caption reuse could weaken this. | `PREPRINT_DRAFT_V0_1.md`; figures | Preserve non-mechanistic captioning. | Monitoring | No | Yes |
| I-08 | B/C | P2 | Platform ambition | Broader Permea framing could exceed current evidence if separated from limitations. | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Keep current BBB wedge and evidence boundary adjacent to broader ambition. | Open | No | Yes |
| I-09 | C | P3 | Document stack | Review-operation document stack is heavy for clarity-only readers. | Operations docs | Use minimum packet for Reviewer C and keep ask narrow. | Managed | No | No |
| I-10 | C | P3 | Reading order | Multiple reading orders exist for different use cases. | `CIRCULATION_GUIDE_V0_1.md`; `REVIEW_OPERATIONS_INDEX_V0_1.md`; `REVIEWER_PACKET_V0_1.md` | Clarify packet scope in outreach. | Managed | No | No |
| I-11 | C | P3 | Abstract density | Abstract is accurate but dense. | `PREPRINT_DRAFT_V0_1.md` | Consider editorial tightening before public preprint. | Open | No | Yes |
| I-12 | A/C | P3 | Figure/table polish | Figures and tables are reviewable but not final-submission polished. | Figures; `PREPRINT_ASSEMBLY_V0_1.md` | Defer polish until after trusted feedback. | Open | No | No |
| I-13 | A/B/C | P4 | Future research | New model families, new features, new datasets, validation, and benchmark expansion are future work. | Future roadmap | Log separately; do not implement during current review phase. | Deferred | No | No |
| I-14 | C/Round 0 | P4 | Deck alignment | No deck files were found in repo. | Future deck materials | Review separately when materials are available. | Deferred | No | No |

## Priority distribution

- P0 items: 0
- P1 items: 3
- P2 items: 5
- P3 items: 4
- P4 items: 2

## Cross-review conflicts

No direct conflicts were found across Reviewer A, Reviewer B, and Reviewer C.

The reviewers emphasize different risks:

- Reviewer A emphasizes provenance, leakage risk, and artifact traceability.
- Reviewer B emphasizes biological overread risk and validation boundaries.
- Reviewer C emphasizes document complexity and reader comprehension.

These emphases are complementary rather than conflicting.

## Recommended revision order

1. P0 first.
2. P1 second.
3. P2 third.
4. P3 after scientific clarity stabilizes.
5. P4 logged as future work.

## Scope-creep filter

Current-package revisions:

- label/provenance clarification
- artifact-to-claim mapping
- cautious metric interpretation
- non-mechanistic feature-importance captioning
- abstract/readability tightening

Future research tasks:

- new model families
- additional features
- external datasets
- duplicate/near-duplicate or similarity-aware split redesign if not already available

Future wet-lab validation:

- experimental validation of candidate prioritization
- mechanistic transport studies

Future benchmark expansion:

- additional delivery barriers
- broader sequence or modality benchmarks

Future deck/pitch hardening:

- review public-facing deck materials after they exist in the repo
- align deck claims to manuscript evidence boundaries

## Recommended next Codex task

Recommended next task:

Task 008 — Convert Harsh Review Findings into Revision Plan

Rationale: no P0 blockers were found, and P1 items are monitoring/tightening issues rather than immediate blockers. The highest-value next step is a file-level revision plan that converts P1/P2 findings into scoped manuscript and documentation actions without expanding the scientific claim.
