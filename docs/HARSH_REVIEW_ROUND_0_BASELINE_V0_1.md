# Harsh Review Round 0 Baseline v0.1

## Purpose

This memo records an internal Round 0 harsh review of the current BBB-oriented Permea manuscript and review-operation package.

This is not external reviewer feedback. It is an internal baseline stress test using the Reviewer A/B/C council structure defined in `HARSH_REVIEW_COUNCIL_CHARTER_V0_1.md`.

## Materials reviewed

Round 0 reviewed repository-local materials only:

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`
- `REVIEWER_PACKET_V0_1.md`
- `FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`
- `FIRST_REVIEW_WAVE_DRY_RUN_V0_1.md`
- `REVIEW_FEEDBACK_LOG_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`
- `REVIEW_OPERATIONS_INDEX_V0_1.md`
- `DATASET.md`
- `FIRST_EVIDENCE_SUMMARY.md`
- `V0_1_EVIDENCE_PACKAGE.md`

No local deck, presentation, slide, pitch, PPT, or PPTX materials were found by repository file inspection. Public-facing deck alignment should be reviewed separately when those materials are available in the repo.

## Council-level baseline verdict

The current package is suitable for trusted review circulation. It is not ready for public preprint submission. Public deck circulation cannot be assessed from current repository materials because no deck was available for review.

Round 0 found no P0 contradictions and no immediate P1 claim-boundary breach that blocks trusted review circulation. The main baseline risks are P2 issues around provenance clarity, artifact traceability, and ensuring that platform ambition stays visibly subordinate to the current bounded evidence surface.

## Reviewer A baseline concerns

Reviewer A — computational/reproducibility:

- The manuscript is benchmark-aware and includes split policy, feature surface, metric set, and regenerated-versus-imported distinctions.
- The current evidence package depends on partially recovered provenance, attribution, licensing, and dataset version details that remain unresolved.
- The extended packet is necessary for Reviewer A because the minimum packet alone does not provide enough dataset, provenance, and evidence-package context.
- Metric language is cautious, but a harsh reader may still ask for stronger traceability between manuscript-level numbers and machine-readable result artifacts.
- No new model families should be added as a reflexive response to reproducibility critique; first response should be clarity and traceability.

## Reviewer B baseline concerns

Reviewer B — biological/skeptical:

- The package repeatedly states that the current work is computational and not wet-lab validation.
- Feature-importance language is explicitly non-mechanistic in the preprint draft.
- The phrase "permeability-related signal" is appropriately cautious, but it remains a sensitive phrase that should be monitored for overreading.
- Broader Permea ambition could be misread as broader biological proof if separated from the current manuscript's limitations.
- Candidate prioritization must remain clearly distinct from biological validation.

## Reviewer C baseline concerns

Reviewer C — technical clarity:

- The manuscript is readable as a bounded computational study, but the total document stack is large.
- Review packet routing is now clear, especially after the dry run and outreach packet.
- A first-pass reader may not immediately understand the difference between manuscript-facing docs, evidence docs, and review-operation docs.
- Figure and table readiness remains adequate for trusted review but not final public submission.
- Public-facing deck review cannot proceed without deck materials.

## P0/P1/P2/P3/P4 issue table

| Priority | Issue | Evidence from reviewed materials | Recommended action |
| --- | --- | --- | --- |
| P0 | No factual or internal contradiction identified in Round 0. | Metrics, feature set, split policy, and claim boundary appeared consistent across reviewed docs. | No P0 action. |
| P1 | No immediate blocking claim-boundary breach identified. | Docs repeatedly reject wet-lab validation, solved delivery, mechanistic proof, therapeutic relevance, and broad generalization claims. | Continue monitoring during outreach and revision. |
| P2 | Dataset provenance remains partially unresolved. | `DATASET.md` lists attribution, licensing, version naming, and source metadata as unresolved or still confirming. | Keep provenance limitations visible in review packets and future revisions. |
| P2 | Reviewer A needs extended packet by default. | Dry run and outreach packet identify minimum packet as insufficient for reproducibility review. | Maintain Reviewer A extended routing. |
| P2 | Manuscript-level metrics should remain traceable to result artifacts. | Preprint reports ROC-AUC, PR-AUC, and MCC values; support docs point to summary tables and regenerated artifacts. | Ask Reviewer A to stress-test traceability before public submission. |
| P2 | Platform ambition may exceed current evidence if quoted out of context. | Broader Permea standard-layer language appears in support docs, while the manuscript narrows claims to a BBB-oriented wedge. | Keep support docs attached to current evidence boundaries. |
| P3 | Document stack may feel heavy for clarity-only readers. | Review operations include packet, index, plan, checklist, dry run, outreach packet, feedback log, and priority framework. | Send Reviewer C the minimum packet and keep the ask narrow. |
| P3 | Figures and table references are reviewable but not final-submission polished. | Submission checklist and assembly docs mark figure polish and submission formatting as pending. | Defer publication polish until after trusted review feedback. |
| P4 | New model families, new features, external datasets, and wet-lab validation are future work. | Priority framework already classifies these as future-work suggestions unless they expose a current trust-blocking problem. | Log separately; do not implement in current review-operation phase. |
| P4 | Public deck alignment review is pending. | No deck/presentation files were found in the repo. | Review deck separately when materials are available. |

## Go/no-go status

| Circulation type | Status | Rationale |
| --- | --- | --- |
| Trusted review circulation | Go | No P0/P1 blockers found; Reviewer A/B/C routing and intake process are defined. |
| Public preprint submission | No-go | Metadata, formal references, supplement prose, figure polish, provenance closure, attribution, and licensing remain unresolved. |
| Public deck circulation | Hold | No deck materials were available in the repo for alignment review. |

## Immediate recommended actions

1. Proceed with trusted review circulation using `FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`.
2. Keep Reviewer A on the extended packet by default.
3. Keep Reviewer B and Reviewer C on minimum packet unless they request support docs.
4. Log incoming comments in `REVIEW_FEEDBACK_LOG_V0_1.md`.
5. Label any internal council-derived entries clearly as internal if they are moved into the feedback log.
6. Do not revise the preprint until feedback is triaged with P0-P4 priorities.

## Recommended next review round

Recommended next round:

Round 1 — Reviewer A/B/C Detailed Harsh Review Memos

The next internal council step should produce separate role-specific memos:

- Reviewer A — computational/reproducibility detailed review
- Reviewer B — biological/skeptical detailed review
- Reviewer C — technical clarity detailed review

Those memos should feed a future `FIRST_REVIEW_WAVE_REVISION_PLAN_V0_1.md` only after findings are triaged.
