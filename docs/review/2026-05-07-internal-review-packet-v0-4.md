# Permea Internal Review Packet for Manuscript v0.4 - 2026-05-07

## 1. Purpose of the Review Packet

This packet supports internal review of the current Permea first-paper manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`

This is an internal review packet only. It is not a public preprint packet, not a public release approval, and not evidence of external expert review or peer review.

The purpose of this review is to check whether manuscript v0.4 is scientifically cautious, structurally clear, correctly positioned against the BBB-penetrating peptide literature, and explicit about dataset, release, and validation limitations.

## 2. Current Manuscript Path

Current working manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`

Supporting review and planning files are listed in Section 13.

## 3. Current Manuscript Status

Manuscript v0.4 is suitable for internal review.

Current status:

- v0.4 is the current working manuscript.
- Verified comparator citations have been integrated.
- Direct BBB-penetrating peptide predictors are separated from adjacent compound-level BBB permeability predictors.
- No state-of-the-art or leaderboard claim is made.
- Metrics and leakage-aware sensitivity findings are preserved from existing repo reports.
- Dataset redistribution remains unresolved.
- Row-level dataset and row-level derived artifacts remain blocked from public release.
- Supplement/export remains not public-submission-ready.
- Public bioRxiv remains **Hold / not submission-ready**.

## 4. What Changed in v0.4

Compared with earlier manuscript versions, v0.4 adds or strengthens:

- Verified citation integration for direct BBB-penetrating peptide comparators.
- Verified citation integration for adjacent compound-level BBB permeability predictors.
- Clearer B3Pdb/B3Pred-lineage positioning.
- Explicit no-SOTA and no-leaderboard framing.
- More careful source-to-claim boundaries around comparator literature.
- Conservative data/code availability wording.
- Continued visibility of dataset source, license, label-source, and redistribution TODOs.
- A caution that `deepb3p3_2023` remains unchanged and unused as a manuscript citation role until manual source-to-claim review assigns it a precise use.

No metric values, model outputs, leakage-audit results, split definitions, data files, result artifacts, or figure artifacts were changed to create v0.4.

## 5. What the Manuscript Claims

The manuscript claims a bounded computational result:

- Initial computational evidence that BBB-related peptide classification signal is learnable from sequence-derived physicochemical features.
- A reproducible peptide-focused baseline/evidence package, not a SOTA predictor.
- Random-stratified and leakage-aware sensitivity metrics for the current benchmark surface.
- A leakage-aware sensitivity analysis that did not collapse baseline signal under the tested group-stratified sensitivity setting.
- Candidate prioritization before experimental validation, not validated delivery or efficacy.

Acceptable framing:

- "initial computational evidence"
- "permeability-related signal"
- "BBB-related peptide classification task"
- "sequence-derived physicochemical features"
- "candidate prioritization before experimental validation"
- "leakage-aware sensitivity analysis"

## 6. What the Manuscript Does Not Claim

The manuscript does not claim:

- Permea is state-of-the-art.
- Permea outperforms B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, or adjacent compound-level BBB predictors.
- The benchmark is leakage-free.
- The model robustly generalizes across independent datasets.
- Biological validation, wet-lab validation, in-vivo validation, therapeutic efficacy, or clinical efficacy.
- Dataset redistribution is permitted.
- Row-level processed datasets, predictions, rankings, split manifests, group assignments, or explicit sequence-pair leakage artifacts are approved for public release.
- The manuscript is public-submission-ready.
- Any external expert review or peer review has occurred.

## 7. Direct Peptide Comparator Context

Direct BBB-penetrating peptide comparator context should be reviewed against these entries and their manuscript usage:

| Comparator/resource | Current citation key(s) | Intended role |
| --- | --- | --- |
| B3Pdb / B3Pred lineage | `b3pdb_2021`, `b3pred_2021` | Dataset/resource and B3PP predictor lineage context. |
| BBPpredict | `bbppredict_2022` | Direct BBB-penetrating peptide predictor context. |
| BBB-PEP-prediction | `naseem2023bbbpep` | Direct BBB peptide prediction comparator context. |
| Augur | `augur_2024` | Direct BBB-penetrating peptide predictor and augmentation context. |
| DeepB3P | `tang2025deepb3p` | Direct modern BBB-penetrating peptide predictor context. |
| DeepB3Pred | `arif2025deepb3pred` | Direct modern BBB-penetrating peptide predictor context. |

Reviewers should check that these citations support related-work positioning only, not direct performance superiority or public-readiness claims.

## 8. Adjacent Compound BBB Predictor Context

Adjacent compound-level BBB permeability predictors are included only as contextual contrast:

| Adjacent predictor | Current citation key | Intended role |
| --- | --- | --- |
| LightBBB | `shaker2021lightbbb` | Compound-level BBB permeability context. |
| Deep-B3 | `tang2022deepb3` | Compound-level BBB permeability context; not DeepB3P. |
| DeePred-BBB | `kumar2022deepredbbb` | Compound-level BBB permeability context. |
| DeepBBBP | `parakkal2022deepbbbp` | Compound-level BBB permeability context. |
| TITAN-BBB | `oliveira2026titanbbb` | Adjacent compound/multimodal BBB permeability context. |

These entries should not be treated as direct peptide comparators. Manuscript v0.4 should not compare Permea metrics directly against these models.

## 9. Dataset / Release Restrictions

Current release posture:

- Internal review only.
- Dataset redistribution remains unresolved.
- Row-level processed dataset redistribution is not declared available.
- Row-level derived artifacts remain blocked from public release.
- Selected aggregate metrics, audit summaries, and figures may be considered only after founder/manual, source/legal, and claim-boundary review.

Blocked from public release unless explicit permission and approval are documented:

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- row-level prediction files
- row-level ranking files
- row-level split manifests
- group assignment files
- explicit sequence-pair leakage audit CSVs
- candidate ranking preview artifacts

Public-facing wording must not imply that source terms permit redistribution of local processed row-level data.

## 10. Known Unresolved Blockers

Remaining blockers before broader review or public preprint consideration:

- Exact upstream dataset version/files require confirmation.
- B3Pred source terms/license and redistribution permission require manual review.
- Required attribution wording remains unresolved.
- Original label-source criteria remain unresolved.
- Row-level derived artifact release permission remains unresolved.
- Final data/code availability wording requires founder/manual approval.
- Supplement/export remains not public-submission-ready.
- Final source-to-claim review remains pending.
- Some older bibliography metadata still needs cleanup or verification.
- `deepb3p3_2023` remains unchanged and unused; its precise future citation role remains manual-review dependent.
- Founder/manual approval and public posting decision remain pending.

## 11. Specific Internal Reviewer Questions

Internal reviewers should answer:

1. Is the v0.4 positioning clearly peptide-focused rather than generic BBB permeability prediction?
2. Is the no-SOTA boundary clear enough?
3. Are direct peptide comparators and adjacent compound predictors correctly separated?
4. Are ROC-AUC, PR-AUC, and MCC interpreted conservatively?
5. Is leakage-aware sensitivity wording appropriately limited?
6. Are dataset/source/redistribution caveats sufficiently visible?
7. Are row-level artifact restrictions clear enough?
8. Are the limitations strong enough?
9. Does the candidate-prioritization framing avoid implying experimental validation?
10. Are citation keys and source-to-claim boundaries clear enough for internal review?
11. Does the text avoid implying biological, wet-lab, in-vivo, therapeutic, or clinical validation?
12. What minimum changes are required before any broader review?

## 12. Suggested Internal Review Rubric

Use this rubric for each review category:

- Pass: acceptable for internal review with no required changes.
- Minor revision: small wording, citation, formatting, or clarity changes.
- Major revision: substantive claim, structure, citation, limitation, or release-posture issue.
- Blocker: issue that must be fixed before any broader review.

Review categories:

| Category | Rating | Notes |
| --- | --- | --- |
| Title and abstract positioning | TODO |  |
| Direct vs adjacent comparator framing | TODO |  |
| No-SOTA and no-leaderboard discipline | TODO |  |
| Methods reproducibility clarity | TODO |  |
| Metric interpretation discipline | TODO |  |
| Leakage-aware sensitivity wording | TODO |  |
| Dataset/source/license caveats | TODO |  |
| Row-level artifact release restrictions | TODO |  |
| Limitations completeness | TODO |  |
| Data/code availability caution | TODO |  |
| Supplement/export readiness caveats | TODO |  |
| Overall internal-review readiness | TODO |  |

## 13. Files / Reports Reviewers May Inspect

Primary manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`

Citation and source-to-claim support:

- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`
- `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
- `docs/reports/2026-05-07-updated-references-bib-post-audit.md`
- `docs/reports/2026-05-07-comparator-reference-and-source-metadata-plan.md`
- `references.bib`

Landscape and positioning support:

- `docs/reports/2026-05-07-bbb-landscape-based-manuscript-change-plan.md`

Dataset and release support:

- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`

Supplement/export support:

- `docs/reports/2026-05-07-supplement-export-v0-4-alignment-plan.md`

Reference ambiguity support:

- `docs/reports/2026-05-07-deepb3p3-identity-review.md`

## 14. Recommended Reviewer Response Format

```text
Reviewer:
Review date:
Overall recommendation:

Required blockers:

Claim-boundary concerns:

Comparator/citation/source-to-claim concerns:

Dataset/source/release concerns:

Metric and leakage-aware wording concerns:

Supplement/export concerns:

Minimum changes before broader review:

Optional improvements:
```

## 15. Short Internal Review Request Message Draft

```text
I am sharing Permea manuscript v0.4 for internal review only. This is not a public preprint and should not be treated as public-submission-ready.

Please focus on whether the paper is cautiously positioned as a peptide-focused computational baseline/evidence package, whether the direct BBB-penetrating peptide comparator context is separated from adjacent compound-level BBB predictor context, whether metric and leakage-aware sensitivity wording stays bounded, and whether dataset/source/row-level release restrictions are clear enough.

The main manuscript is:
docs/paper/permea-first-paper-manuscript-v0-4.md

Please use the review packet:
docs/review/2026-05-07-internal-review-packet-v0-4.md

Public bioRxiv remains Hold / not submission-ready. Dataset redistribution remains unresolved, and row-level artifacts remain blocked from public release.
```

## 16. Public bioRxiv Status

Public bioRxiv remains **Hold / not submission-ready**.

Manuscript v0.4 is suitable for internal review, but it is not public-submission-ready. Row-level artifacts remain blocked from public release. Dataset redistribution remains unresolved. Supplement/export remains not public-submission-ready.

## Required Conclusion

- Manuscript v0.4 is suitable for internal review.
- Manuscript v0.4 is not public-submission-ready.
- Row-level artifacts remain blocked from public release.
- Dataset redistribution remains unresolved.
- Supplement/export remains not public-submission-ready.
- Public bioRxiv remains **Hold / not submission-ready**.
