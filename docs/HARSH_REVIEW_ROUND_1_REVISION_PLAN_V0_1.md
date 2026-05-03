# Harsh Review Round 1 Revision Plan v0.1

## Purpose

This memo converts internal harsh council Round 1 findings into a priority-based revision plan.

This is internal review planning. It is not external reviewer feedback, does not represent third-party peer review, does not expand the scientific evidence boundary, and does not implement manuscript revisions yet. Its purpose is to turn the Round 1 issue register into scoped next actions while preserving the distinction between current computational benchmark evidence and future biological validation.

## Inputs

- `HARSH_REVIEW_COUNCIL_CHARTER_V0_1.md`
- `HARSH_REVIEW_ROUND_0_BASELINE_V0_1.md`
- `HARSH_REVIEW_REVIEWER_A_COMPUTATIONAL_REPRODUCIBILITY_V0_1.md`
- `HARSH_REVIEW_REVIEWER_B_BIOLOGICAL_SKEPTICAL_V0_1.md`
- `HARSH_REVIEW_REVIEWER_C_TECHNICAL_CLARITY_V0_1.md`
- `HARSH_REVIEW_ROUND_1_INTEGRATED_ISSUE_REGISTER_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`

## Current readiness summary

Trusted review circulation: Continue.

The Round 1 council found no P0 issue and no blocking P1 issue. Trusted review can continue because the current package repeatedly identifies the evidence as computational, benchmark-oriented, and intended for candidate prioritization before experimental validation.

Public preprint submission: Not yet.

Preprint submission should wait until provenance, label/source criteria, leakage-risk language, artifact-to-claim traceability, and claim-boundary tightening are handled or explicitly deferred. These are not trusted-review blockers, but they are public scrutiny risks.

Public deck circulation: Hold until deck materials are available and claim-aligned.

No deck, presentation, pitch, PPT, or slide materials were found inside `permea-signal-ml` during Round 1 inspection. Public-facing deck alignment should be reviewed separately after such materials exist in the repo.

## Priority distribution

Source of truth: `HARSH_REVIEW_ROUND_1_INTEGRATED_ISSUE_REGISTER_V0_1.md`.

- P0 count: 0
- P1 count: 3
- P2 count: 5
- P3 count: 4
- P4 count: 2

## P0 plan

No P0 issues were identified in Round 1.

If a factual contradiction is found during a later revision pass, stop trusted circulation until the contradiction is corrected or explicitly rejected with rationale.

## P1 plan - claim-boundary tightening

| Issue ID | Area | Affected document or artifact | Revision intent | Recommended wording direction | Required before trusted review? | Required before preprint? | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-05 | Metric and claim interpretation | `PREPRINT_DRAFT_V0_1.md`; reviewer docs | Keep ROC-AUC, PR-AUC, and MCC framed as benchmark-level evidence, not biological validation. | Pair metrics with "current benchmark surface," "baseline comparison," and "candidate prioritization before experimental validation." | No | Yes | Planned |
| I-06 | Biological overread risk | `PREPRINT_DRAFT_V0_1.md`; `FIRST_EVIDENCE_SUMMARY.md` | Keep "permeability-related signal" adjacent to computational and benchmark-specific qualifiers. | Avoid isolated wording that could read as solved BBB prediction or validated delivery. | No | Yes | Planned |
| I-07 | Feature importance | `PREPRINT_DRAFT_V0_1.md`; figures | Preserve feature importance as model-level behavior only. | Use "model-level feature importance" or "descriptive model signal"; avoid mechanism, causality, transport mechanism, or biological proof language. | No | Yes | Planned |

P1 revisions should specifically avoid wet-lab validation ambiguity, solved delivery language, broad biological generalization, therapeutic or clinical efficacy implications, and treating computational prioritization as biological validation.

## P2 plan - provenance, benchmark, and method clarity

| Issue ID | Area | Affected document or artifact | Revision intent | Required artifact or clarification | Required before trusted review? | Required before preprint? | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Dataset provenance | `DATASET.md`; metrics/manifests | Make unresolved dataset version, attribution, licensing, and source metadata visible and traceable. | Confirm if possible; otherwise document unresolved status clearly. Do not soften provenance gaps into implied closure. | No | Yes | Planned |
| I-02 | Label definition | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Clarify label semantics and source criteria as far as current records support. | Add a preprint-facing label/source note if recoverable; otherwise state that original labeling criteria remain partially unresolved. | No | Yes | Planned |
| I-03 | Leakage risk | `PREPRINT_DRAFT_V0_1.md`; future supplement | Represent duplicate, near-duplicate, and sequence-similarity leakage as unresolved risk unless audited. | Do not claim leakage exists or is absent without an audit. Plan a limitation note or future audit item. | No | Yes | Planned |
| I-04 | Artifact traceability | `results/tables/model_comparison_summary.csv`; metrics JSON; `PREPRINT_ASSEMBLY_V0_1.md` | Add a compact artifact-to-claim mapping for manuscript metrics and regenerated figures/tables. | Map reported metrics to `model_comparison_summary.csv`, relevant metrics JSON/manifests if present, and regenerated feature-importance artifacts. | No | Yes | Planned |
| I-08 | Platform ambition | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Keep broader Permea framing visibly bounded by the current BBB-oriented computational wedge. | Keep evidence-boundary language adjacent to any platform or standard-layer context. | No | Yes | Planned |

This task does not create new benchmark results, run new model comparisons, add new model families, or add biological evidence. If an artifact cannot be clarified from existing repo contents, the revision should document the gap rather than fill it with unsupported claims.

## P3 plan - readability and structure

| Issue ID | Area | Affected document | Readability or structure improvement | Dependency on P1/P2 resolution | Status |
| --- | --- | --- | --- | --- | --- |
| I-09 | Document stack | Review-operation docs | Keep reviewer-facing packets narrow; avoid sending operations docs to clarity-only reviewers. | None; routing is already mostly handled. | Managed |
| I-10 | Reading order | `CIRCULATION_GUIDE_V0_1.md`; `REVIEW_OPERATIONS_INDEX_V0_1.md`; `REVIEWER_PACKET_V0_1.md` | Make packet scope explicit in outreach and reviewer instructions. | None; depends mainly on outreach discipline. | Managed |
| I-11 | Abstract density | `PREPRINT_DRAFT_V0_1.md` | Tighten abstract readability while preserving claim-boundary qualifiers. | Should happen after P1 wording decisions are stable. | Planned |
| I-12 | Figure/table polish | Figures; `PREPRINT_ASSEMBLY_V0_1.md` | Polish captions, table naming, and figure placement for publication readiness. | Should happen after P1/P2 evidence and artifact mapping are stable. | Planned |

P3 work should follow claim-boundary and evidence-clarity work. Readability improvements must not remove necessary caveats.

## P4 plan - future work

| Issue ID | Future-work category | Why it is deferred | Belongs to |
| --- | --- | --- | --- |
| I-13 | Future research and model development | New model families, new features, new datasets, validation, and benchmark expansion would expand the current evidence surface and are outside this review-operation phase. | Future research; future wet-lab validation; future benchmark expansion; future model development |
| I-14 | Future deck/pitch hardening | No public-facing deck materials were found in the repo. Deck alignment cannot be reviewed or revised without actual materials. | Future public deck hardening |

P4 items should not become immediate manuscript claims. They can be logged as future directions only when clearly separated from current evidence.

## Revision sequence

1. Confirm no P0 contradictions.
2. Apply P1 claim-boundary tightening.
3. Apply P2 provenance, benchmark, and method clarity revisions.
4. Apply P3 readability and packet-structure improvements.
5. Log P4 as future work without expanding claims.
6. Re-run internal harsh council check after revisions.
7. Continue trusted external review or prepare a preprint revision pass.

## Document-specific action map

| Document or artifact | Relevant issue IDs | Revision type | Priority | Action summary | Owner placeholder | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `docs/PREPRINT_DRAFT_V0_1.md` | I-02, I-03, I-05, I-06, I-07, I-11 | Claim-boundary, methods clarity, readability | P1/P2/P3 | Tighten metric interpretation, label/provenance language, leakage-risk limitation, feature-importance wording, and abstract density without adding new claims. | Manuscript owner | Planned |
| `docs/DATASET.md` | I-01, I-02 | Provenance and label clarity | P2 | Clarify dataset version, attribution, licensing, source metadata, and label/source criteria as confirmed, unresolved, or future work. | Evidence owner | Planned |
| `docs/FIRST_EVIDENCE_SUMMARY.md` | I-06, I-08 | Claim boundary and ambition/evidence alignment | P1/P2 | Keep "permeability-related signal" and broader Permea context visibly bounded by computational benchmark evidence. | Evidence owner | Planned |
| `docs/V0_1_EVIDENCE_PACKAGE.md` | I-08 | Evidence-boundary alignment | P2 | Keep platform/standard framing subordinate to the current BBB-oriented computational evidence package. | Evidence owner | Planned |
| `docs/SUPPLEMENTARY_OUTLINE_V0_1.md` | I-01, I-02, I-03, I-04 | Supplement planning | P2 | Ensure supplement outline reserves space for provenance, label definition, leakage-risk status, and artifact-to-claim mapping. | Manuscript owner | Planned |
| `docs/PREPRINT_ASSEMBLY_V0_1.md` | I-04, I-12 | Artifact and figure/table traceability | P2/P3 | Map manuscript claims to regenerated tables/figures and mark final polish as post-feedback work. | Manuscript owner | Planned |
| `docs/CIRCULATION_GUIDE_V0_1.md` | I-10 | Reader routing | P3 | Preserve clear reading order and review scope for trusted reviewers. | Review-ops owner | Managed |
| `docs/REVIEWER_NOTE_V0_1.md` | I-05, I-10 | Reviewer instruction and claim boundary | P1/P3 | Preserve no-validation and candidate-prioritization boundaries in any reviewer-facing summary. | Review-ops owner | Managed |
| `results/tables/model_comparison_summary.csv` | I-04, I-05 | Artifact source | P1/P2 | Treat as a source artifact for metric traceability; do not modify values in this planning task. | Evidence owner | Reference only |
| `results/tables/regenerated_rf_feature_importance.csv` | I-07, I-12 | Artifact source | P1/P3 | Treat as a source artifact for non-mechanistic feature-importance reporting; do not modify values in this planning task. | Evidence owner | Reference only |
| `figures/regenerated_rf_feature_importance.png` | I-07, I-12 | Figure source | P1/P3 | Use only with captions that state feature importance is descriptive model behavior, not mechanism. | Manuscript owner | Planned |

## Scope-creep filter

Current-package revisions:

- tighten claim language
- clarify provenance and label/source boundaries
- clarify benchmark and metric traceability
- improve reader legibility and packet routing
- preserve non-mechanistic feature-importance framing

External review intake:

- use `REVIEW_FEEDBACK_LOG_V0_1.md` for actual reviewer comments
- keep internal harsh council findings separate from external reviewer feedback
- apply P0-P4 triage before implementing feedback

Future research tasks:

- new datasets
- additional features
- expanded comparisons
- sequence-similarity-aware benchmark redesign if not already supported by current artifacts

Future wet-lab validation:

- experimental validation of prioritized candidates
- biological mechanism or transport studies

Future benchmark expansion:

- additional barrier classes
- broader sequence or modality benchmarks

Future model development:

- new model families
- deeper model selection or hyperparameter campaigns

Future public deck hardening:

- create or review deck materials only after they exist in the repo
- align deck claims to manuscript evidence boundaries before public circulation

Current revisions should improve claim discipline, provenance clarity, benchmark clarity, and reader legibility. Future work should not be backfilled into current claims.

## Go/no-go after Round 1

Status: Continue trusted review circulation.

Rationale: Round 1 found no P0 issues and no blocking P1 issues. P1 items require monitoring and tightening before public-facing preprint use, while P2 items should be resolved or explicitly documented before preprint submission.

## Recommended next Codex task

Task 009 — Commit Round 1 Revision Plan

Rationale: this task creates and stages the revision plan but does not commit it. The next step should close the planning artifact cleanly before any manuscript or evidence-doc revision pass begins.
