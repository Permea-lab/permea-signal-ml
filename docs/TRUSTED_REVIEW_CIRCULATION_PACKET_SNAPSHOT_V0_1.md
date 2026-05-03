# Trusted Review Circulation Packet Snapshot v0.1

## Purpose

This snapshot defines the trusted review circulation packet after P1 claim-boundary tightening and P2 provenance/benchmark clarification.

This is for trusted review circulation. It is not public preprint submission, is not external peer review, does not add new scientific evidence, and does not change the current manuscript claims. It is a human-operated dispatch guide for selecting packet contents, disclosing caveats, and preparing feedback intake.

## Current readiness status

- Trusted review circulation: Go with caveats
- Public preprint submission: Not yet
- Public deck circulation: Hold until deck materials are available and claim-aligned

## Current evidence boundary

The current package supports a bounded claim:

- initial computational evidence
- learnable permeability-related signal on the current benchmark surface
- sequence-derived physicochemical features
- benchmark-oriented baseline modeling
- candidate prioritization before experimental validation

The current package does not claim:

- wet-lab validation
- solved delivery
- broad biological generalization
- therapeutic or clinical efficacy
- mechanistic proof from feature importance
- biological validation from computational prioritization

## Packet routing by reviewer type

### Reviewer A — computational/reproducibility

Packet type: extended packet by default.

Purpose: benchmark framing, provenance clarity, artifact traceability, reproducibility, and evidence-boundary review.

Required documents:

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/CIRCULATION_GUIDE_V0_1.md`
- `docs/REVIEWER_NOTE_V0_1.md`
- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`

Optional internal context if appropriate:

- `docs/HARSH_REVIEW_POST_P1_P2_COUNCIL_CHECK_V0_1.md`

Artifact references:

- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `figures/regenerated_rf_feature_importance.png`
- `results/metrics/`
- `results/manifests/`
- `results/predictions/`
- `results/tables/*_ranking.csv`
- `results/tables/*_summary.csv`

### Reviewer B — biological/skeptical

Packet type: minimum packet first, extended materials available on request.

Purpose: biological claim-boundary review, wet-lab interpretation risk, and limitation adequacy.

Required documents:

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/CIRCULATION_GUIDE_V0_1.md`
- `docs/REVIEWER_NOTE_V0_1.md`

Optional documents:

- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`

Optional internal context if appropriate:

- `docs/HARSH_REVIEW_ROUND_1_P1_CLAIM_BOUNDARY_CHANGELOG_V0_1.md`

### Reviewer C — technical clarity

Packet type: minimum packet.

Purpose: narrative clarity, reading order, category misunderstanding risk, and whether a first-time technical reader understands the current claim.

Required documents:

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/CIRCULATION_GUIDE_V0_1.md`
- `docs/REVIEWER_NOTE_V0_1.md`

Optional documents:

- `docs/FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`

Optional internal context if appropriate:

- `docs/HARSH_REVIEW_POST_P1_P2_COUNCIL_CHECK_V0_1.md`

Internal harsh review docs should generally not be sent by default. They are optional internal context only if the human operator wants to disclose internal audit history. The default reviewer-facing packet should remain clean and easy to read.

## Caveats to disclose

Disclose these caveats when relevant:

- dataset version remains `pending_confirmation`
- attribution/licensing remain unconfirmed
- original label-source criteria remain partially unresolved
- duplicate, near-duplicate, and sequence-similarity leakage status remains unaudited
- no wet-lab validation has been performed
- public preprint submission is not yet recommended

These caveats do not block trusted review. They do block public preprint readiness until resolved, sufficiently disclosed, or explicitly deferred.

## Reviewer-specific questions

Reviewer A — computational/reproducibility:

- Is dataset provenance clear enough for trusted review?
- Are label/source criteria caveats visible enough?
- Are split policy and seed clear?
- Is class imbalance and PR-AUC interpretation handled responsibly?
- Is artifact-to-claim traceability clear?
- Are leakage-risk caveats explicit enough?
- Is the imported-versus-regenerated distinction understandable?
- Is the package computationally trustworthy enough for preprint preparation, assuming unresolved caveats are preserved?

Reviewer B — biological/skeptical:

- Could the manuscript be misread as wet-lab validated delivery?
- Does BBB/permeability wording remain bounded and computational?
- Is feature importance clearly model-level rather than mechanistic?
- Are therapeutic or clinical implications avoided?
- Are limitations strong enough?

Reviewer C — technical clarity:

- Can the current claim be stated in one sentence?
- Is the reading order clear?
- Is the minimum packet usable without insider context?
- Is the current wedge separated from broader platform ambition?
- Are limitations visible enough?
- Does the package read like evidence rather than platform marketing?

## Outreach template mapping

Use `docs/REVIEW_OUTREACH_TEMPLATES_V0_1.md`.

- Reviewer A: Template A — Computational reviewer
- Reviewer B: Template B — Biologically literate reviewer
- Reviewer C: Template C — General technical clarity reviewer

Customize each message to identify the packet type and ask for claim-boundary feedback.

## Feedback intake path

Use:

- `docs/REVIEW_FEEDBACK_LOG_V0_1.md`
- `docs/REVISION_PRIORITY_FRAMEWORK_V0_1.md`

Intake rules:

- log each substantive feedback point separately
- assign P0-P4 priority internally
- do not implement reviewer suggestions immediately
- separate current-package revisions from future-work suggestions
- preserve the distinction between internal harsh council findings and external trusted-review feedback

## Send/no-send checklist

- [ ] Repo clean.
- [ ] Latest packet snapshot committed.
- [ ] Reviewer A extended packet assembled.
- [ ] Reviewer B minimum packet assembled.
- [ ] Reviewer C minimum packet assembled, if included.
- [ ] Unresolved caveats visible.
- [ ] Outreach templates selected.
- [ ] Feedback log ready.
- [ ] Priority framework ready.
- [ ] No P0 blockers.
- [ ] No P1 blockers.
- [ ] Public preprint not represented as ready.
- [ ] Deck not included unless separately claim-aligned.

## Recommended next step

1. Commit this snapshot.
2. Select actual reviewers manually.
3. Send packets using `REVIEW_OUTREACH_TEMPLATES_V0_1.md`.
4. Collect feedback.
5. Run a feedback-intake task before implementing revisions.
