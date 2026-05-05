# Friendly Reviewer Packet for Permea Manuscript v0.2 - 2026-05-06

## 1. Purpose of the Review Packet

This packet is for selected friendly/internal reviewers evaluating the Permea first-paper manuscript v0.2 before broader review or public-submission preparation.

The purpose is to get candid feedback on scientific framing, reproducibility, claim boundaries, citation clarity, dataset/source caveats, and minimum changes needed before wider external review.

This packet is not a public preprint package. It does not imply external expert review, peer review, public bioRxiv readiness, dataset redistribution permission, or legal approval.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Current Manuscript Path

Current manuscript draft:

- `docs/paper/permea-first-paper-manuscript-v0-2.md`

Current manuscript audit:

- `docs/reports/2026-05-06-manuscript-v0-2-audit.md`

## 3. Current Manuscript Status

Manuscript v0.2 is suitable for friendly/internal review.

Current status:

- Internal-review manuscript v0.2 exists.
- Citation placeholders have been integrated sentence by sentence using existing `references.bib` keys.
- Data/code availability wording is conservative.
- Dataset redistribution remains unresolved and is not declared available.
- No high-risk claim-boundary issue was found in the v0.2 audit.
- Public bioRxiv remains **Hold / not submission-ready**.

Remaining public-submission blockers are listed below and should not be treated as resolved.

## 4. What the Manuscript Claims

The manuscript is framed as initial computational evidence for a BBB-related peptide classification task.

Allowed claim scope:

- Initial computational evidence.
- In-silico, sequence-derived physicochemical baseline analysis.
- Learnable permeability-related benchmark signal under the current dataset surface.
- Reproducible baseline evidence package using existing baseline model families.
- Leakage-aware group-stratified sensitivity rerun did not collapse the baseline signal under the tested grouping strategy.
- Logistic Regression remained broadly similar under the leakage-aware sensitivity manifest.
- Random Forest was comparable to or higher under the leakage-aware sensitivity manifest.
- Candidate-prioritization framing before experimental validation.
- Explicit limitations around dataset provenance, leakage sensitivity, source metadata, and validation status.

## 5. What the Manuscript Does Not Claim

The manuscript must not be read as claiming:

- dataset redistribution is permitted
- dataset source/legal review is complete
- all leakage concerns are fully controlled
- robust generalization
- validated BBB delivery
- true BBB performance
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- feature importance as mechanism
- external expert review
- peer review
- public bioRxiv readiness

## 6. Known Unresolved Blockers

Current blockers before public bioRxiv or public release:

- Original dataset source identity remains unresolved.
- Dataset attribution, license, source terms, and redistribution permission remain unresolved.
- Original label-source criteria remain unresolved.
- Final data/code availability wording remains unresolved.
- Final repository release URL, release tag, archive policy, and software license remain unresolved.
- `references.bib` metadata cleanup remains incomplete.
- Final citation/source-to-claim review remains incomplete.
- Supplement/export formatting remains incomplete.
- Founder/manual approval remains required.
- Final public posting decision remains required.

Dataset availability status:

- Processed dataset redistribution is not declared available.
- Code availability can be considered separately from data availability.
- Selected aggregate derived artifacts may be considered only after founder/legal and claim-boundary review.

## 7. Specific Reviewer Questions

Please answer the following questions directly.

1. Is the computational framing scientifically cautious enough?
2. Are the Methods reproducible and clear enough for an early computational evidence paper?
3. Are ROC-AUC, PR-AUC, and MCC interpreted conservatively?
4. Is leakage-aware sensitivity wording appropriately limited?
5. Are the limitations strong enough?
6. Does the candidate-prioritization framing avoid implying experimental validation?
7. Are citations and source TODOs sufficiently visible?
8. Are the dataset/source/redistribution caveats clear?
9. Are software, metric, and background citations used only for appropriate claim types?
10. Does any sentence imply robust generalization, validated biology, wet-lab confirmation, therapeutic relevance, or clinical relevance?
11. What would be the minimum change required before broader external review?
12. What would be the minimum change required before public bioRxiv preparation, assuming legal/source blockers are separately resolved?

## 8. Suggested Review Rubric

Use the following rubric.

| Area | Rating | Notes requested |
| --- | --- | --- |
| Scientific framing | Pass / Minor / Major / Blocker | Is the scope appropriately computational and bounded? |
| Methods clarity | Pass / Minor / Major / Blocker | Can a reader understand what was evaluated and from which artifacts? |
| Metric interpretation | Pass / Minor / Major / Blocker | Are ROC-AUC, PR-AUC, and MCC used cautiously? |
| Leakage-aware sensitivity wording | Pass / Minor / Major / Blocker | Does wording avoid implying full leakage control? |
| Dataset/source caveats | Pass / Minor / Major / Blocker | Are attribution, licensing, and redistribution limits clear? |
| Citation placement | Pass / Minor / Major / Blocker | Are citations integrated at useful points without over-supporting claims? |
| Limitations | Pass / Minor / Major / Blocker | Are limitations visible and strong enough? |
| Public-readiness boundary | Pass / Minor / Major / Blocker | Is it clear this is not public-submission-ready? |

Recommended severity definitions:

- Pass: no change needed before friendly/internal circulation.
- Minor: wording or formatting change recommended before broader review.
- Major: conceptual or structural revision needed before broader review.
- Blocker: claim, evidence, citation, or legal/source issue that should stop broader circulation.

## 9. Files and Reports Reviewers May Inspect

Primary files:

- `docs/paper/permea-first-paper-manuscript-v0-2.md`
- `docs/reports/2026-05-06-manuscript-v0-2-audit.md`

Citation and source context:

- `references.bib`
- `docs/reports/2026-05-06-reference-cleanup-and-citation-plan.md`
- `docs/reports/2026-05-06-reference-cleanup-post-audit.md`

Dataset/source and availability context:

- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`

Founder/submission context:

- `docs/submission/2026-05-05-founder-approval-packet-v0-1.md`

Reviewers do not need to rerun models, rerun leakage audits, generate splits, or inspect private/legal source materials for this friendly/internal review.

## 10. Recommended Reviewer Response Format

Please respond in this format:

```text
Overall recommendation:
- Pass for internal continuation / Minor revision / Major revision / Hold

Top three required changes:
1.
2.
3.

Claim-boundary concerns:
- None / list specific lines or sentences

Methods/reproducibility concerns:
- None / list specific issues

Citation/source concerns:
- None / list specific issues

Dataset/legal/availability concerns:
- None / list specific issues

Minimum change before broader external review:
-

Minimum change before public bioRxiv preparation:
-
```

## 11. Short Outreach Message Draft

```text
Hi [Name],

I have a Permea first-paper manuscript v0.2 ready for friendly/internal review. It is an in-silico computational evidence draft, not a public-submission-ready preprint. The main question is whether the scientific framing, methods clarity, leakage-aware sensitivity interpretation, and limitations are cautious enough before broader review.

Important boundaries: the draft does not claim biological validation, wet-lab validation, robust generalization, therapeutic or clinical efficacy, or dataset redistribution permission. Public bioRxiv remains on Hold while dataset/source/legal, references, supplement/export, and founder/manual approval blockers remain open.

Could you review `docs/paper/permea-first-paper-manuscript-v0-2.md` and respond using the reviewer packet questions in `docs/review/2026-05-06-friendly-reviewer-packet-v0-2.md`?

Thanks.
```

## 12. Explicit Public-Readiness Note

Manuscript v0.2 is suitable for friendly/internal review.

Manuscript v0.2 is not public-submission-ready.

Dataset redistribution remains unresolved.

Public bioRxiv remains **Hold / not submission-ready**.

This packet does not imply external expert review or peer review occurred.

## Recommended Next Task

Recommended next task:

**Task 123 - Commit Friendly Reviewer Packet for Manuscript v0.2**

Do not modify manuscript files, `references.bib`, data artifacts, result artifacts, figure artifacts, model outputs, split artifacts, or leakage audit artifacts.
