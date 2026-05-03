# Post Red-Team Next Development Roadmap v0.1

## Purpose

This roadmap translates `VIRTUAL_EXPERT_RED_TEAM_REVIEW_MAX_HARSH_V0_1.md` into the next development sequence for `permea-signal-ml`.

This is internal planning. It is not external expert review, not public peer review, does not add scientific evidence, and does not make the manuscript submission-ready. It converts internal virtual red-team findings into scoped work tracks while preserving the current evidence boundary.

## Current state summary

- Next internal development: Go with caveats
- Trusted review circulation: Go with caveats
- Public preprint submission: Hold
- Public deck/partner circulation: Hold
- Fatal blockers: none identified
- P0: 0
- P1: 6
- P2: 11
- P3: 6
- P4: 4

## Strategic interpretation

Internal development can proceed because no fatal contradiction or blocking P0 issue was found. The package is strong enough to keep improving without waiting for real external reviewer feedback.

Trusted review can also proceed if desired, as long as Reviewer A receives the extended packet and all unresolved caveats remain visible.

Public preprint submission must wait. The package still has unresolved provenance, attribution/licensing, label-source, leakage-audit, metadata, reference, supplement, and export-readiness gaps.

Public deck or partner materials must wait until they exist in the repo and are checked against the current evidence boundary. Any public-facing material must avoid turning benchmark metrics into delivery success probabilities or treating computational prioritization as biological validation.

The unresolved caveats are credibility risks, not reasons to stop all development. They should drive the next task sequence.

## Track A - Preprint-readiness hardening

Focus:

- formal references
- author, affiliation, correspondence, contribution, funding, conflict, and availability placeholders
- bioRxiv readiness checklist closure
- supplement scope and prose
- final manuscript export readiness
- explicit "Not yet" status until these items are complete

Primary files:

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`

Do not treat this track as public submission. It is preparation only until blockers are closed or explicitly disclosed.

## Track B - Provenance and evidence hardening

Focus:

- dataset version remains `pending_confirmation`
- attribution and licensing remain unconfirmed
- original label-source criteria remain partially unresolved
- duplicate, near-duplicate, and sequence-similarity leakage status remains unaudited
- clearer dataset-card style documentation
- explicit separation of confirmed facts, recovered benchmark settings, and unresolved items

Primary files:

- `docs/DATASET.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`

This track should clarify or audit uncertainty. It must not fill provenance gaps with unsupported certainty.

## Track C - Artifact traceability and export

Focus:

- manifest completeness
- artifact-to-claim map
- metric-to-manuscript consistency
- figure/table naming consistency
- final export bundle
- reviewer-readable artifact inventory

Primary files and artifacts:

- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `results/metrics/`
- `results/manifests/`
- `figures/regenerated_rf_feature_importance.png`
- `scripts/export_metrics.py`
- `scripts/generate_figures.py`

This track can inspect artifacts and scripts for traceability. It should not modify metric values, rerun models, or create new benchmark results unless a later task explicitly allows a bounded audit.

## Track D - Public deck / partner material hardening

Focus:

- deck materials are not currently present in `permea-signal-ml`
- public-facing claims must align with canonical regenerated metrics
- remove or soften "90% filtering," "success probability," "validated delivery," or similar overclaims if present in future public materials
- state clearly that no wet-lab validation has been performed
- separate platform ambition from the current BBB-oriented computational wedge

Primary files:

- future deck, website, partner memo, or public project-page materials after they are added to the repo
- `docs/VIRTUAL_EXPERT_RED_TEAM_REVIEW_MAX_HARSH_V0_1.md` as the public-claim risk source
- `docs/TRUSTED_REVIEW_CIRCULATION_PACKET_SNAPSHOT_V0_1.md` for current caveats

No public deck or partner material should be cleared until the actual materials are available and claim-aligned.

## Track E - Future validation and wet-lab planning

Focus:

- wet-lab path as future validation
- assay-plan placeholders
- DBTL-style planning without treating validation as current evidence
- explicit separation between current computational prioritization and future biological validation

Primary outputs:

- future validation planning document
- future assay decision matrix
- future evidence-ladder mapping

This track may plan validation, but it must not imply that validation has occurred.

## Track F - Possible permea-core promotion candidates

Potential standard-layer candidates:

- artifact-to-claim mapping pattern
- evidence-boundary checklist
- review-intake P0-P4 priority schema
- dataset/provenance caveat language
- internal virtual red-team review pattern

Do not modify `permea-core` in this task. Promotion candidates should first be collected in `permea-signal-ml`, then reviewed separately before any cross-repo move or reference update.

## Recommended task sequence

| Task | Purpose | Target docs/files | Expected output | What not to do | Blocker status | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| Task 024 — Commit Next Development Roadmap | Close this roadmap artifact. | `POST_RED_TEAM_NEXT_DEVELOPMENT_ROADMAP_V0_1.md`; `REVIEW_OPERATIONS_INDEX_V0_1.md` | Committed roadmap. | Do not edit manuscript or artifacts. | Required for clean tracking. | P2 |
| Task 025 — Run Final Artifact Traceability Export Check | Verify claim-to-artifact consistency before deeper edits. | `PREPRINT_ASSEMBLY_V0_1.md`; `model_comparison_summary.csv`; metrics JSON; manifests; figures; export/generation scripts | Traceability audit memo and issue list. | Do not rerun models or change metric values. | Blocks preprint, not trusted review. | P2 |
| Task 026 — Harden Dataset Provenance and Label-Source Documentation | Improve dataset card and provenance status. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md`; `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Clearer confirmed/unresolved provenance and label-source language. | Do not fabricate attribution, license, or label certainty. | Blocks preprint and public use. | P2 |
| Task 027 — Draft Leakage Audit Plan Without Running New Experiments | Define a future duplicate/similarity audit plan. | `DATASET.md`; `SUPPLEMENTARY_OUTLINE_V0_1.md`; new audit-plan doc if needed | Audit plan with scope, inputs, outputs, and non-claims. | Do not claim leakage-free status or run new benchmark results. | Blocks preprint unless caveated. | P2 |
| Task 028 — Prepare Preprint Metadata and Reference Gap Checklist | Identify metadata, disclosure, reference, and supplement gaps. | `PREPRINT_DRAFT_V0_1.md`; `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`; `SUPPLEMENTARY_OUTLINE_V0_1.md` | Preprint gap checklist. | Do not invent authors, affiliations, citations, funding, or disclosures. | Blocks preprint. | P2 |
| Task 029 — Prepare Public Deck Claim-Alignment Checklist | Define gates for future public/partner materials. | Future deck materials when present; red-team report; packet snapshot | Claim-alignment checklist for public materials. | Do not create or clear a deck unless materials exist. | Blocks public deck/partner use. | P1/P2 |
| Task 030 — Identify Permea-Core Promotion Candidates | Collect patterns that may belong in the standard layer. | Review ops docs; evidence boundary docs; red-team report | Promotion-candidate memo in `permea-signal-ml`. | Do not modify `permea-core`. | Does not block review or preprint. | P3 |

## Priority table

| Track | Priority | Why it matters | Immediate next task | Blocks trusted review? | Blocks public preprint? | Blocks public deck/partner use? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — Preprint-readiness hardening | P2 | Public submission requires metadata, references, supplement, and export closure. | Task 028 | No | Yes | Partly | Keep public preprint status on hold. |
| B — Provenance and evidence hardening | P2 | Provenance, label-source, licensing, and leakage caveats are the most serious credibility risks. | Task 026, then Task 027 | No | Yes | Yes | Do not over-resolve unknowns. |
| C — Artifact traceability and export | P2 | A final traceability pass reduces metric, figure, manifest, and export mismatch risk. | Task 025 | No | Yes | Partly | Best immediate technical next step. |
| D — Public deck / partner material hardening | P1/P2 | Public materials can easily overclaim metrics and platform maturity. | Task 029 after materials exist | No | No | Yes | Deck not present in repo. |
| E — Future validation and wet-lab planning | P4 | Validation path matters, but it is future evidence, not current support. | Later validation-plan task | No | No | Partly | Planning can proceed with caveats. |
| F — Permea-core promotion candidates | P3 | Some local patterns may mature into standard-layer infrastructure. | Task 030 | No | No | No | Candidate collection only. |

## Go/no-go matrix

| Path | Verdict | Reason |
| --- | --- | --- |
| Next internal development | Go with caveats | No fatal blocker; next work is scoped. |
| Trusted review circulation | Go with caveats | Caveats are explicit and Reviewer A gets extended packet. |
| Public preprint submission | Hold | Provenance, leakage, references, metadata, supplement, and export checks remain incomplete. |
| Public deck/partner circulation | Hold | No deck materials are present and public-claim misuse risk remains high. |
| Public website/project page | Hold | Public copy must be claim-aligned before launch. |
| Wet-lab planning | Go with caveats | Planning can proceed as future validation design only. |
| Permea-core promotion | Go with caveats | Candidate identification can proceed, but no cross-repo edits in this phase. |

## Decision rule

What can proceed now:

- internal roadmap execution
- trusted review circulation, if the human operator chooses to run it in parallel
- artifact traceability audit planning
- provenance and label-source documentation hardening
- leakage audit planning
- future validation planning as future work
- Permea-core promotion candidate identification inside `permea-signal-ml`

What must wait:

- public preprint submission
- public deck or partner circulation
- public website/project-page claims
- any claim that external review has occurred
- any claim that wet-lab validation exists

What must be fixed before public release:

- provenance, attribution, licensing, label-source, and leakage caveats must be resolved or prominently disclosed
- metrics must remain benchmark metrics, not success probabilities
- feature importance must remain model-level, not mechanism
- references, metadata, disclosures, supplement, figure/caption polish, and export checks must be complete
- public materials must separate platform ambition from current BBB-oriented computational evidence

What can be deferred as future work:

- new model families
- new datasets
- new benchmark wedges
- wet-lab validation execution
- broader delivery-barrier expansion
- final standard-layer promotion into `permea-core`

## Recommended immediate next Codex task

Task 024 — Commit Next Development Roadmap

## Human next action

If speed matters, proceed with the internal development roadmap now.

If external credibility matters, select real Reviewer A/B/C candidates and run trusted review in parallel with internal roadmap execution.

Do not claim external review has happened until it has.

