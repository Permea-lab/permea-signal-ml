# Harsh Review — Reviewer B Biological/Skeptical v0.1

## Purpose

This is an internal harsh review from the biological/skeptical perspective. It is not external reviewer feedback.

Reviewer B evaluates whether the current manuscript and evidence package preserve biological claim discipline, avoid overinterpretation, and keep computational candidate prioritization distinct from biological validation.

## Materials reviewed

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`
- `REVIEWER_PACKET_V0_1.md`
- `FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`
- `DATASET.md`
- `FIRST_EVIDENCE_SUMMARY.md`
- `V0_1_EVIDENCE_PACKAGE.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`
- `HARSH_REVIEW_COUNCIL_CHARTER_V0_1.md`
- `HARSH_REVIEW_ROUND_0_BASELINE_V0_1.md`

## Reviewer B verdict

Verdict: Pass for trusted review.

The manuscript and review packet repeatedly state that the current work is computational, benchmark-specific, and not experimentally validated. No blocking P1 biological overclaim was found. The main risk is reader overinterpretation of terms such as "permeability-related signal," "BBB-oriented," and broader Permea ambition if excerpts are separated from the limitations.

## Main biological concerns

- The manuscript does not claim wet-lab validation and explicitly states no experimental validation is included.
- Computational prioritization is generally separated from biological validation, especially in the abstract, results, limitations, and reviewer note.
- BBB/permeability wording is cautious enough for trusted review, but the wording remains biologically sensitive and should be monitored.
- Feature importance is explicitly described as model behavior, not mechanism.
- Therapeutic and clinical implications are explicitly rejected in limitations and circulation docs.
- Platform ambition is present in broader support framing, but current manuscript scope is narrow enough.
- Future validation is framed as future work, not current evidence.
- Limitations are prominent and candid enough for trusted review.

## Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before trusted review? | Required before preprint? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B-01 | P1 | Claim boundary | No blocking biological overclaim found, but "permeability-related signal" could be overread by a skeptical biologist. | `PREPRINT_DRAFT_V0_1.md`; `FIRST_EVIDENCE_SUMMARY.md` | `PREPRINT_DRAFT_V0_1.md` | Continue pairing phrase with computational, benchmark-specific, candidate-prioritization qualifiers. | No | Yes |
| B-02 | P1 | Validation boundary | Computational candidate prioritization is clearly separated from validation, but this boundary must remain visible in any abstract or outreach excerpt. | Abstract, limitations, `REVIEWER_NOTE_V0_1.md` | `PREPRINT_DRAFT_V0_1.md`; outreach text | Do not excerpt results without the no-validation boundary. | No | Yes |
| B-03 | P1 | Feature importance | Feature importance is correctly non-mechanistic in the draft. Risk returns if figures are used without cautious captions. | Feature-importance section; `PREPRINT_ASSEMBLY_V0_1.md` | Figure captions; `PREPRINT_DRAFT_V0_1.md` | Preserve non-mechanistic captions and wording. | No | Yes |
| B-04 | P2 | Platform ambition | Broader Permea standard-layer framing may sound larger than current evidence if detached from limitations. | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Support docs; outreach materials | Keep current wedge and evidence-boundary language adjacent to broader ambition. | No | Yes |
| B-05 | P2 | Dataset biological meaning | Dataset provenance and label origin remain unresolved enough to limit biological interpretation. | `DATASET.md` | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Avoid treating labels as direct biological truth; keep provenance caveat explicit. | No | Yes |
| B-06 | P3 | Limitations visibility | Limitations are strong, but preprint readers may need an even clearer one-sentence summary near results. | `PREPRINT_DRAFT_V0_1.md` | `PREPRINT_DRAFT_V0_1.md` | Consider adding/retaining a concise "computational only" transition around results. | No | No |
| B-07 | P4 | Biological validation | Wet-lab validation is the right future direction but not current evidence. | Limitations and future-work language. | Future roadmap | Log as future work only. | No | No |

## Harsh questions for the authors

- Could a biologist misread this as wet-lab validated delivery?
- Does any sentence imply solved BBB delivery?
- Does feature importance read like mechanism?
- Does the manuscript distinguish computational ranking from biological function?
- Are future wet-lab claims framed as future validation, not current evidence?
- Does the broader Permea platform ambition appear only as context, not as proof?
- Would a reader understand that current labels and dataset provenance constrain biological interpretation?

## Reviewer B recommended next actions

Must fix before wider circulation:

- None blocking trusted review circulation.

Should fix before preprint:

- Preserve no-validation language in abstract, results, limitations, and figure captions.
- Keep feature-importance text explicitly non-mechanistic.
- Keep platform ambition subordinate to the BBB-oriented computational wedge.
- Clarify that labels and dataset surface do not by themselves establish biological truth.

Can defer to future work:

- Wet-lab validation.
- Mechanistic experiments.
- Broader BBB or delivery generalization.
- Therapeutic or clinical framing.
