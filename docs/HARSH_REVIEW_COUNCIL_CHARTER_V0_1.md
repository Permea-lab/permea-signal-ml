# Harsh Review Council Charter v0.1

## Purpose

This charter defines an internal harsh review council for the current BBB-oriented Permea manuscript and review-operation package.

The council exists to stress-test claim boundaries, reproducibility posture, biological interpretation, and reader clarity before or alongside human-led trusted review. It does not replace external expert review.

## Council status

Status: internal review layer.

The council uses placeholder reviewer roles only:

- Reviewer A — computational/reproducibility
- Reviewer B — biological/skeptical
- Reviewer C — technical clarity

No real reviewer names, institutions, emails, affiliations, credentials, or external feedback should be added to this document.

## Definition of harsh review

Harsh review means rigorous, skeptical, and evidence-boundary focused. It does not mean insulting, dismissive, performative, or adversarial for its own sake.

A harsh review should ask what a skeptical reader could reasonably misunderstand, reject, or challenge. It should identify weak claims, unclear provenance, confusing routing, unsupported interpretation, and places where ambition may exceed the current evidence surface.

## Reviewer A — computational/reproducibility

Reviewer A evaluates whether the current package is computationally legible and reproducibility-oriented enough for its stated claim level.

Reviewer A should evaluate:

- benchmark framing
- metric interpretation
- regenerated versus imported artifact boundaries
- dataset and provenance clarity
- split policy and rerun traceability
- whether outputs are sufficiently discoverable from the review packet
- whether computational claims stay tied to current-contract artifacts

Reviewer A should not evaluate:

- biological validation
- therapeutic relevance
- wet-lab feasibility
- whether the project should add new model families in the current review cycle

## Reviewer B — biological/skeptical

Reviewer B evaluates whether the manuscript is biologically cautious and resistant to overinterpretation.

Reviewer B should evaluate:

- biological plausibility framing
- overclaim risk
- whether candidate prioritization is distinct from validation
- whether feature importance is kept descriptive rather than mechanistic
- whether limitations are candid enough
- whether broader Permea ambition leaks into current evidence claims

Reviewer B should not evaluate:

- implementation details of rerun scripts
- full artifact reproducibility
- whether new validation experiments should be added before internal review
- final public submission formatting

## Reviewer C — technical clarity

Reviewer C evaluates whether the manuscript and review packet can be understood by a technically literate reader without insider context.

Reviewer C should evaluate:

- reading order
- document role clarity
- manuscript flow
- figure and table signposting
- whether packet routing is clear
- whether operational review docs are easy to use

Reviewer C should not evaluate:

- biological truth
- model frontier quality
- external citation completeness
- final submission readiness

## P0-P4 priority mapping

Use the same priority system as `REVISION_PRIORITY_FRAMEWORK_V0_1.md`.

| Priority | Meaning | Council handling |
| --- | --- | --- |
| P0 | Factual or internal contradiction | Must be fixed before further circulation |
| P1 | Claim-boundary or overinterpretation risk | Must be fixed before external-facing circulation |
| P2 | Benchmark, provenance, method, dataset, or artifact clarity issue | Should be fixed before preprint submission or broad circulation |
| P3 | Readability, formatting, figure/table, or structure improvement | Fix after P0-P2 items are stable |
| P4 | Future-work suggestion | Log separately; do not implement immediately unless it strengthens current trust without expanding claims |

## Claim-boundary rules

Council findings must preserve these rules:

- no wet-lab validation claims
- no solved delivery claims
- no broad biological generalization
- no therapeutic or clinical efficacy claims
- no mechanistic proof from feature importance
- no implication that computational candidate prioritization equals biological validation
- no new evidence claims without new evidence

## Evidence-boundary rules

The council should treat the current evidence as:

- computational
- benchmark-specific
- BBB-oriented
- baseline-model oriented
- based on sequence-derived physicochemical features
- dependent on partially recovered and partially unresolved dataset provenance
- useful for candidate prioritization before experimental validation

The council should not treat the current package as:

- experimentally validated
- mechanistically explanatory
- clinically interpretable
- a universal BBB prediction system
- a broad delivery platform result

## Reviewer placeholder rules

- Use Reviewer A, Reviewer B, and Reviewer C only.
- Do not invent real identities.
- Do not invent affiliations or credentials.
- Do not invent external feedback.
- Clearly label internal council findings as internal.

## Review round structure

Round 0 — baseline internal harsh review:

- identify obvious P0-P2 risks from current repository materials
- assess whether trusted review circulation can proceed
- identify which deeper council review should happen next

Round 1 — role-specific detailed review:

- Reviewer A: computational/reproducibility memo
- Reviewer B: biological/skeptical memo
- Reviewer C: technical clarity memo

Round 2 — integrated revision planning:

- merge accepted findings into a file-level revision plan
- separate manuscript revisions from future research tasks
- preserve the current evidence boundary

## Output format for each review round

Each council round should include:

- materials reviewed
- role or council perspective
- issue table using P0-P4
- go/no-go status by circulation type
- recommended actions
- explicit note that findings are internal, not external reviewer feedback

## Feeding findings into review operations

Council findings can feed into `REVIEW_FEEDBACK_LOG_V0_1.md` only when clearly labeled as:

`Internal Harsh Council — Round N`

Council findings may also feed a future `FIRST_REVIEW_WAVE_REVISION_PLAN_V0_1.md`. That revision plan should separate:

- accepted manuscript edits
- documentation cleanup
- deferred future-work suggestions
- rejected or clarified comments

The council must not use internal findings to expand scientific claims or simulate external endorsement.
