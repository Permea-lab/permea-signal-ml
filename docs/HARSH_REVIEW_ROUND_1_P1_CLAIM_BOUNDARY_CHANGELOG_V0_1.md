# Harsh Review Round 1 P1 Claim-Boundary Changelog v0.1

## Purpose

This changelog records focused P1 claim-boundary tightening edits made after the Round 1 internal harsh review.

This is an internal revision artifact. It is not external reviewer feedback, does not add new scientific evidence, and does not expand claims. The edits documented here are intended to reduce overinterpretation risk while preserving the current legitimate claim: initial computational evidence for learnable permeability-related signal and candidate prioritization before experimental validation under a bounded benchmark surface.

## Inputs

- `HARSH_REVIEW_ROUND_1_INTEGRATED_ISSUE_REGISTER_V0_1.md`
- `HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`

## P1 worklist

| P1 issue ID | Source reviewer | Area | Risk summary | Affected document or artifact | Planned edit type | Status |
| --- | --- | --- | --- | --- | --- | --- |
| I-05 | A/B | Metric and claim interpretation | Metrics could be overread as biological validation rather than benchmark-level evidence. | `PREPRINT_DRAFT_V0_1.md`; reviewer docs | Keep ROC-AUC, PR-AUC, MCC, and baseline results tied to the current computational benchmark surface and candidate prioritization before experimental validation. | Applied |
| I-06 | B | Biological overread risk | "Permeability-related signal" could be overread if separated from computational and benchmark-specific qualifiers. | `PREPRINT_DRAFT_V0_1.md`; `FIRST_EVIDENCE_SUMMARY.md` | Add or preserve computational, benchmark-specific, and bounded-dataset qualifiers around permeability-related signal language. | Applied |
| I-07 | B | Feature importance | Feature importance could be misread as mechanistic proof if reused without careful captions or local context. | `PREPRINT_DRAFT_V0_1.md`; `PREPRINT_ASSEMBLY_V0_1.md`; feature-importance figure references | Reinforce model-level feature-importance language and explicitly avoid mechanistic interpretation. | Applied |

## Edits applied

| Change ID | Linked P1 issue ID | Document edited | Section or local heading | Previous risk pattern | New claim-boundary direction | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1-C01 | I-05, I-06 | `PREPRINT_DRAFT_V0_1.md` | Abstract | Results and permeability-related signal language could be read too broadly if detached from the evidence boundary. | Described the package as an initial BBB-oriented computational evidence package, tied signal to the benchmark surface, and stated that the contribution is not biological confirmation or validated delivery performance. | Applied |
| P1-C02 | I-06 | `PREPRINT_DRAFT_V0_1.md` | Introduction | Permeability-related signal language could sound like a biological assertion outside the bounded dataset surface. | Reframed the question as computational permeability-related signal detectable on a bounded dataset surface. | Applied |
| P1-C03 | I-05 | `PREPRINT_DRAFT_V0_1.md` | Baseline comparison and candidate-prioritization interpretation | Metrics and ranking outputs could be read as stand-alone predictive or biological validation claims. | Reframed results as non-trivial benchmark signal on the present computational surface and candidate prioritization prior to experimental validation, not evidence of biological activity. | Applied |
| P1-C04 | I-07 | `PREPRINT_DRAFT_V0_1.md` | Regenerated model-level feature-importance summary | Feature-importance section title and figure reuse could weaken the non-mechanistic boundary. | Renamed the section to model-level feature importance while preserving explicit language that the ordering is not a mechanistic explanation. | Applied |
| P1-C05 | I-05, I-06 | `FIRST_EVIDENCE_SUMMARY.md` | Current question, main findings, and Permea context | Evidence summary could be overread as broader delivery evidence if quoted without caveats. | Added computational and benchmark-surface qualifiers and stated that the current evidence should not be treated as validated delivery performance. | Applied |
| P1-C06 | I-05, I-06 | `V0_1_EVIDENCE_PACKAGE.md` | Purpose and current evidence summary | "Public evidence surface" and benchmark signal language could be read as stronger than current computational evidence. | Reframed the package as a public computational evidence surface and stated that it does not establish biological validation or delivery performance. | Applied |
| P1-C07 | I-07 | `PREPRINT_ASSEMBLY_V0_1.md` | Figure/table plan and section-to-asset mapping | Feature-importance figure reference could be reused without non-mechanistic context. | Updated the figure and mapping language to describe model-level Random Forest feature importance, not mechanistic evidence. | Applied |
| P1-C08 | I-05, I-06, I-07 | `HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md` | P1 plan | Revision-plan statuses still showed P1 tightening as planned. | Marked I-05, I-06, and I-07 as applied in the P1 tightening pass. | Applied |

## Claim-boundary rules reinforced

- no wet-lab validation claims
- no solved delivery claims
- no broad biological generalization
- no therapeutic or clinical efficacy claims
- feature importance is not mechanistic proof
- computational prioritization is not biological validation
- platform ambition remains separate from current evidence

## Remaining work

Remaining P1 monitoring items:

- Continue preserving benchmark-level metric interpretation in any future abstract, figure caption, outreach excerpt, or deck text.
- Continue keeping "permeability-related signal" adjacent to computational and benchmark-specific qualifiers.
- Continue treating feature importance as model-level behavior only.

P2 provenance, benchmark, and method clarity items:

- dataset provenance/version/attribution/licensing remain partially unresolved
- label/source criteria need stronger preprint-facing clarification
- duplicate, near-duplicate, and sequence-similarity leakage risks remain unresolved questions, not confirmed defects
- artifact-to-claim traceability should be improved before public preprint submission
- platform ambition should remain visibly bounded by the current evidence surface

P3 readability and structure items:

- abstract density and figure/table polish remain appropriate for a later readability pass after P1/P2 clarity is stable
- packet and reading-order complexity should remain managed through routing rather than broadening reviewer-facing materials

P4 future-work items:

- new model families, new features, new datasets, benchmark expansion, and wet-lab validation remain future work
- public deck/pitch alignment remains deferred until deck materials exist in the repo

## Recommended next Codex task

Task 011 — Commit P1 Claim-Boundary Tightening
