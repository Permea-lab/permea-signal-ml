# Harsh Review Post-P1/P2 Council Check v0.1

## Purpose

This memo re-runs the internal harsh review council after P1 claim-boundary tightening and P2 provenance/benchmark clarity revisions.

This is internal review. It is not external reviewer feedback, does not replace real expert review, and does not add new scientific evidence, benchmark results, model outputs, or biological claims. The purpose is to assess whether the current package is safer for trusted review circulation and whether any P0/P1/P2 issues remain before wider circulation or preprint preparation.

## Inputs

- `HARSH_REVIEW_ROUND_1_P1_CLAIM_BOUNDARY_CHANGELOG_V0_1.md`
- `HARSH_REVIEW_ROUND_1_P2_PROVENANCE_BENCHMARK_CHANGELOG_V0_1.md`
- `HARSH_REVIEW_ROUND_1_INTEGRATED_ISSUE_REGISTER_V0_1.md`
- `HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md`
- `PREPRINT_DRAFT_V0_1.md`
- `DATASET.md`
- `FIRST_EVIDENCE_SUMMARY.md`
- `V0_1_EVIDENCE_PACKAGE.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`
- `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `INTERNAL_REVIEW_MEMO_V0_1.md`
- `REVIEWER_PACKET_V0_1.md`
- `FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`

Result artifacts were inspected only for traceability context. No result artifacts were modified.

## Post-revision summary

P1 status: improved. The package now more consistently frames metrics as benchmark-level computational evidence, candidate prioritization as pre-experimental, and feature importance as model-level behavior rather than mechanistic proof.

P2 status: improved as documentation clarity. Dataset version, attribution/licensing, label-source criteria, and duplicate/similarity leakage status remain unresolved, but they are now visible in `DATASET.md`, the manuscript draft, the assembly document, the submission checklist, and the P2 changelog.

Remaining unresolved issues:

- dataset version remains `pending_confirmation`
- attribution/licensing remain unconfirmed
- original label-source criteria remain partially unresolved
- duplicate, near-duplicate, and sequence-similarity leakage status remains unaudited
- formal metadata, references, full supplement, and final submission formatting remain incomplete

Result artifact modification status: no result artifacts were modified during P1 or P2 revision tasks.

Claim-boundary status: no current wet-lab validation, solved delivery, therapeutic efficacy, broad biological generalization, biological validation, or mechanistic proof claim was identified in the revised package.

## Reviewer A post-revision check

Verdict: Improved and trusted-review ready.

Remaining strengths:

- `DATASET.md` now separates current dataset surface, label status, recovered benchmark settings, unresolved provenance, and leakage/duplicate status.
- `PREPRINT_DRAFT_V0_1.md` now states that dataset version, attribution/licensing, source-level metadata, and label-source criteria remain partially unresolved.
- Split policy and seed are visible as recovered benchmark settings, not as leakage-control guarantees.
- `PREPRINT_ASSEMBLY_V0_1.md` now includes a compact artifact-to-claim table.
- `model_comparison_summary.csv`, metrics JSON files, manifests, and regenerated feature-importance artifacts are easier to trace from manuscript claims.

Remaining concerns:

- Reviewer A still requires the extended packet by default because the minimum packet is not enough for provenance, artifact, and benchmark scrutiny.
- Dataset version remains `pending_confirmation`.
- Attribution/licensing remain unconfirmed.
- Original label-source criteria remain partially unresolved.
- Duplicate, near-duplicate, and sequence-similarity leakage audits remain future work.

Remaining P0/P1/P2 issues:

- P0: none.
- P1: no blockers.
- P2: unresolved provenance and leakage-audit items remain, but they are clearly caveated.

Trusted-review readiness: Go with extended packet.

Preprint readiness: Not yet.

## Reviewer B post-revision check

Verdict: Improved and trusted-review ready.

Remaining strengths:

- The manuscript explicitly states computational evidence only and no experimental validation.
- Candidate prioritization is repeatedly framed as before experimental validation.
- Feature importance is framed as model-level behavior and explicitly not mechanistic proof.
- The current wedge is described as bounded and computational, not solved delivery or broad biological validation.
- Dataset labels are not treated as independently verified biological truth.

Remaining concerns:

- A biologist could still overread isolated phrases such as "permeability-related signal" if copied without surrounding qualifiers, so future excerpts and deck text should preserve computational and benchmark-specific context.
- Biological validation remains future work.
- Dataset and label provenance gaps limit biological interpretation.

Remaining P0/P1/P2 issues:

- P0: none.
- P1: no blockers.
- P2: dataset and label provenance still constrain biological interpretation.

Trusted-review readiness: Go.

Preprint readiness: Not yet.

## Reviewer C post-revision check

Verdict: Improved with caveats.

Remaining strengths:

- A serious technical outsider should be able to state the current claim in one sentence: the package provides initial computational evidence that sequence-derived physicochemical features support benchmark-oriented candidate prioritization on a bounded BBB-oriented peptide dataset before experimental validation.
- The package is clearer about what is claimed and not claimed.
- The extended packet purpose is clear for computational/reproducibility review.
- Limitations are more visible after P1/P2 revisions.
- The post-P1/P2 changelogs make revision intent traceable.

Remaining concerns:

- The review-operation document stack is still heavy.
- Preprint-readiness status requires careful reading across several docs.
- Public deck circulation cannot be evaluated because no deck materials are present in the repo.
- P3 readability work remains useful after the P0/P1/P2 safety checks are closed.

Remaining P0/P1/P2 issues:

- P0: none.
- P1: no blockers.
- P2: unresolved items remain visible and should be carried into preprint planning.

Trusted-review readiness: Go with caveats.

Preprint readiness: Not yet.

## Consolidated issue table

No remaining P0 items were identified.

No remaining P1 blockers were identified.

| Issue ID | Priority | Area | Current status | Affected document or artifact | Recommended action | Required before trusted review? | Required before preprint? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PP2-01 | P2 | Dataset version | Explicitly documented as `pending_confirmation`; not resolved. | `DATASET.md`; manifests; `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Confirm final dataset version label or keep explicit unresolved-status language. | No | Yes |
| PP2-02 | P2 | Attribution/licensing | Explicitly documented as unconfirmed. | `DATASET.md`; `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`; `INTERNAL_REVIEW_MEMO_V0_1.md` | Confirm attribution/licensing or state unresolved status in final preprint materials. | No | Yes |
| PP2-03 | P2 | Label-source criteria | Partially clarified; original criteria remain unresolved. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Confirm label-source criteria if recoverable; otherwise preserve limitation language. | No | Yes |
| PP2-04 | P2 | Duplicate/similarity leakage | Clearly documented as unaudited and not leakage-free. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md`; `SUPPLEMENTARY_OUTLINE_V0_1.md` | Run a future audit or preserve explicit limitation before preprint submission. | No | Yes |
| PP2-05 | P2 | Artifact-to-claim traceability | Improved and reviewable; final export check still useful. | `PREPRINT_ASSEMBLY_V0_1.md`; `model_comparison_summary.csv`; metrics JSON; manifests | Perform final traceability check before preprint export. | No | Yes |

## Readiness verdicts

Trusted review circulation: Go with caveats.

Rationale: no P0 or P1 blocker remains, and P2 caveats are explicit enough for trusted review, especially if Reviewer A receives the extended packet.

Public preprint submission: Not yet.

Rationale: dataset version, attribution/licensing, label-source criteria, duplicate/similarity leakage status, full supplement, references, metadata, and final formatting remain incomplete or unresolved.

Public deck circulation: Hold until deck materials are available and claim-aligned.

Rationale: no deck materials were found in the repo. Any future deck should be checked against the same computational-evidence and claim-boundary constraints before circulation.

## Recommended next step

Task 015 — Commit Post-P1/P2 Harsh Review Check

Rationale: this task creates and stages the post-revision council memo. The next step should close the memo before starting a new revision or outreach phase.
