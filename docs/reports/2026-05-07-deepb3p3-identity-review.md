# deepb3p3_2023 Identity and Citation Role Review - 2026-05-07

## 1. Purpose and Scope

This report reviews the existing `deepb3p3_2023` reference key in `references.bib` and determines how it should be handled relative to the verified DeepB3P and DeepB3Pred entries added for manuscript v0.4 citation integration.

This is a documentation-only review. It does not modify `references.bib`, manuscript files, data artifacts, result artifacts, figure artifacts, model outputs, split artifacts, or leakage-audit artifacts.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Current `references.bib` Entry for `deepb3p3_2023`

Current entry:

```bibtex
@article{deepb3p3_2023,
  author = {Ma and Wolfinger},
  title = {A prediction model for blood-brain barrier penetrating peptides based on masked peptide transformers with dynamic routing},
  journal = {Briefings in Bioinformatics},
  year = {2023},
  doi = {10.1093/bib/bbad399}
}
```

Observed metadata characteristics:

- Key: `deepb3p3_2023`
- Authors: Ma and Wolfinger
- Year: 2023
- Journal: Briefings in Bioinformatics
- DOI: `10.1093/bib/bbad399`
- Title describes a prediction model for BBB-penetrating peptides based on masked peptide transformers with dynamic routing.
- The title in the current entry does not explicitly contain "DeepB3P" or "DeepB3Pred".

## 3. Whether `deepb3p3_2023` Is Used in Manuscript v0.4

Current usage result: not used as a bracketed citation key in manuscript v0.4.

Manuscript v0.4 mentions `deepb3p3_2023` only in a cautionary note:

- the key is intentionally not used as a DeepB3P or DeepB3Pred citation
- its identity and citation role remain unresolved relative to `tang2025deepb3p` and `arif2025deepb3pred`

This is a safe use because it does not cite the entry as evidence for a claim and does not conflate it with either verified comparator.

## 4. Comparison Against `tang2025deepb3p`

Verified DeepB3P entry:

```bibtex
@article{tang2025deepb3p,
  title = {{DeepB3P}: A Transformer-Based Model for Identifying Blood--Brain Barrier Penetrating Peptides with Data Augmentation Using Feedback {GAN}},
  author = {Tang, Qiang and Chen, Wei},
  journal = {Journal of Advanced Research},
  volume = {73},
  pages = {459--468},
  year = {2025},
  doi = {10.1016/j.jare.2024.08.002}
}
```

Comparison:

| Field | `deepb3p3_2023` | `tang2025deepb3p` |
| --- | --- | --- |
| Apparent title/name | Masked peptide transformer with dynamic routing | DeepB3P |
| Authors | Ma and Wolfinger | Tang and Chen |
| Year | 2023 | 2025 |
| Journal | Briefings in Bioinformatics | Journal of Advanced Research |
| DOI | `10.1093/bib/bbad399` | `10.1016/j.jare.2024.08.002` |
| Method phrase | masked peptide transformers with dynamic routing | transformer + feedback GAN data augmentation |

Assessment:

- Based on repo evidence, `deepb3p3_2023` is not the same entry as `tang2025deepb3p`.
- The entries have different authors, years, journals, DOIs, and method descriptions.
- `deepb3p3_2023` should not be used as the DeepB3P citation unless a manual source review later proves a naming relationship.

## 5. Comparison Against `arif2025deepb3pred`

Verified DeepB3Pred entry:

```bibtex
@article{arif2025deepb3pred,
  title = {{DeepB3Pred}: Blood--Brain Barrier Peptide Predictor Using Stacked {BiGRU} Model with Novel Features},
  author = {Arif, Muhammad and Musleh, Saleh and Alam, Tanvir},
  journal = {BMC Biology},
  volume = {23},
  pages = {325},
  year = {2025},
  doi = {10.1186/s12915-025-02419-0}
}
```

Comparison:

| Field | `deepb3p3_2023` | `arif2025deepb3pred` |
| --- | --- | --- |
| Apparent title/name | Masked peptide transformer with dynamic routing | DeepB3Pred |
| Authors | Ma and Wolfinger | Arif, Musleh, Alam |
| Year | 2023 | 2025 |
| Journal | Briefings in Bioinformatics | BMC Biology |
| DOI | `10.1093/bib/bbad399` | `10.1186/s12915-025-02419-0` |
| Method phrase | masked peptide transformers with dynamic routing | stacked BiGRU with novel features |

Assessment:

- Based on repo evidence, `deepb3p3_2023` is not the same entry as `arif2025deepb3pred`.
- The entries have different authors, years, journals, DOIs, and method descriptions.
- `deepb3p3_2023` should not be used as the DeepB3Pred citation.

## 6. Identity Assessment

| Candidate identity | Assessment |
| --- | --- |
| Same as DeepB3P (`tang2025deepb3p`) | No, based on current repo evidence. |
| Same as DeepB3Pred (`arif2025deepb3pred`) | No, based on current repo evidence. |
| Different work | Likely, based on current repo evidence. |
| Unclear from repo evidence | Partly unresolved: the entry appears distinct, but final naming/role should be manually verified before public submission. |

Conservative conclusion:

- `deepb3p3_2023` appears to be a different BBB-penetrating peptide predictor work from the verified DeepB3P and DeepB3Pred entries.
- Its exact manuscript role remains unresolved because the current `references.bib` title does not expose a short model name and the repo has not documented how to cite it safely.

## 7. Risk Assessment

### High-Risk Issues

None found, because manuscript v0.4 does not use `deepb3p3_2023` as evidence for DeepB3P, DeepB3Pred, state-of-the-art performance, or direct comparator superiority.

### Medium-Risk Issues

- If future manuscript text cites `deepb3p3_2023` without explaining what work it represents, readers may confuse it with DeepB3P or DeepB3Pred.
- The current key name `deepb3p3_2023` may itself imply a model name that is not visible in the current title field.
- Public submission still needs a source-to-claim review for this entry if it remains in the manuscript bibliography or is cited in text.

### Low-Risk Issues

- The entry metadata remains incomplete relative to final bibliography standards; volume, issue, pages/article number, full author names, and exact title casing may need verification.

## 8. Recommended Handling

Recommended handling now:

- Keep `deepb3p3_2023` unchanged in `references.bib`.
- Keep it unused in manuscript v0.4 unless a future source-to-claim pass assigns it a precise role.
- Do not use it as a DeepB3P citation.
- Do not use it as a DeepB3Pred citation.
- Do not remove or rename it in this task.

Recommended handling later:

- Manually verify the source identity and full metadata.
- Decide whether it should be cited as an additional direct BBB-penetrating peptide predictor work, retained as an unused bibliography entry, renamed for clarity, or removed.
- Remove only after manual approval and after confirming it is unused by all manuscripts, reports, and citation plans.

## 9. Recommended Next Task

Recommended next task:

**Task 143 - Commit deepb3p3 Identity Review**

Suggested commit scope:

- `docs/reports/2026-05-07-deepb3p3-identity-review.md`

After that, a separate task may prepare a final citation/source-to-claim cleanup plan for manuscript v0.4 and the current bibliography.

## Required Conclusion

- `references.bib` was not modified in this task.
- `deepb3p3_2023` was not removed or renamed in this task.
- From repo evidence, `deepb3p3_2023` appears distinct from both `tang2025deepb3p` and `arif2025deepb3pred`.
- Its exact manuscript role remains unresolved pending manual source-to-claim review.
- Public bioRxiv remains **Hold / not submission-ready**.
- Dataset redistribution remains unresolved.

