# Updated references.bib Comparator Entries Post-Audit - 2026-05-07

## 1. Purpose and Scope

This report audits the updated `references.bib` comparator entries added after the verified comparator BibTeX candidate pack.

Scope:

- Verify that the eight newly added comparator keys exist exactly once.
- Check for duplicate citation keys.
- Check for obvious BibTeX syntax/formatting issues.
- Confirm direct peptide comparator and adjacent compound BBB predictor coverage.
- Identify remaining reference and source-to-claim risks before commit.

This is an audit report only. It does not modify `references.bib`, manuscript files, data artifacts, result artifacts, figure artifacts, model outputs, split artifacts, or leakage-audit artifacts.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Working Tree State

Observed working tree at audit time:

- Modified:
  - `references.bib`
- Untracked:
  - `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
  - `docs/reports/2026-05-07-updated-references-bib-post-audit.md`

No manuscript, data, result, figure, model, split, or leakage-audit artifact modification was observed.

## 3. Added Comparator Entry Checklist

| Key | Expected role | Verification result |
| --- | --- | --- |
| `naseem2023bbbpep` | Direct BBB-PEP-prediction peptide comparator. | Present exactly once. |
| `tang2025deepb3p` | Direct DeepB3P peptide comparator. | Present exactly once. |
| `arif2025deepb3pred` | Direct DeepB3Pred peptide comparator. | Present exactly once. |
| `shaker2021lightbbb` | Adjacent compound-level LightBBB predictor. | Present exactly once. |
| `tang2022deepb3` | Adjacent compound-level Deep-B3 predictor. | Present exactly once. |
| `kumar2022deepredbbb` | Adjacent compound-level DeePred-BBB predictor. | Present exactly once. |
| `parakkal2022deepbbbp` | Adjacent compound-level DeepBBBP predictor. | Present exactly once. |
| `oliveira2026titanbbb` | Adjacent compound-level TITAN-BBB preprint. | Present exactly once. |

Verdict: Pass.

## 4. Duplicate Key Check

Duplicate key check result: no duplicate BibTeX keys detected.

Existing keys were preserved. The update did not replace or remove:

- `b3pred_2021`
- `bbppredict_2022`
- `augur_2024`
- `deepb3p3_2023`

Verdict: Pass.

## 5. BibTeX Syntax / Formatting Check

Observed checks:

- The added entries use standard `@article{key, ...}` structure.
- Brace-balance check over `references.bib` returned zero net imbalance.
- The added entries include closing braces.
- Required fields from the Task 135 candidate pack were copied into `references.bib`.
- No obvious malformed entry boundary was detected.

Verdict: Pass for commit.

Remaining caveat:

- This is a lightweight syntax/formatting check, not a full BibTeX compiler/export check.

## 6. Existing Keys Skipped and Why

The following existing keys were intentionally left unchanged:

- `b3pred_2021`
- `bbppredict_2022`
- `augur_2024`

Reason:

- Task 136 instructed not to overwrite existing `b3pred_2021`, `bbppredict_2022`, or `augur_2024` unless exact duplicates required cleanup.
- The verified candidate pack can support a future metadata-normalization pass for these existing keys, but that was not part of Task 136.

## 7. Confusing Key Review

`deepb3p3_2023` remains unresolved.

Current state:

- `deepb3p3_2023` remains unchanged.
- `tang2025deepb3p` was added as a separate verified DeepB3P entry.
- `arif2025deepb3pred` was added as a separate verified DeepB3Pred entry.

Risk:

- DeepB3P, DeepB3Pred, and `deepb3p3_2023` are name-similar and should not be conflated in manuscript citations.

Required future action:

- Perform a source-to-claim citation pass that decides exactly which sentence should cite `deepb3p3_2023`, `tang2025deepb3p`, and `arif2025deepb3pred`.
- Do not remove or rename `deepb3p3_2023` without a deliberate identity review.

## 8. Direct Peptide Comparator Coverage

Direct BBB-penetrating peptide comparator coverage is now stronger.

Existing or added direct comparator keys include:

- `b3pred_2021`
- `bbppredict_2022`
- `naseem2023bbbpep`
- `augur_2024`
- `tang2025deepb3p`
- `arif2025deepb3pred`

Related peptide/database keys already present:

- `brainpeps_2012`
- `b3pdb_2021`
- `bbppred_2021`
- `brainpeppass_2024`
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`

Boundary:

- These entries support comparator/related-work context.
- They do not support a state-of-the-art claim, direct leaderboard claim, robust generalization claim, biological validation claim, or dataset redistribution claim.

## 9. Adjacent Compound BBB Predictor Coverage

Adjacent compound-level BBB predictor coverage is now present in `references.bib` through:

- `shaker2021lightbbb`
- `tang2022deepb3`
- `kumar2022deepredbbb`
- `parakkal2022deepbbbp`
- `oliveira2026titanbbb`

Boundary:

- These entries should be used only for adjacent compound-level BBB permeability context.
- They should not be treated as direct peptide predictors.
- Permea metrics should not be compared directly against these models without matched task/data/split/evaluation compatibility.

## 10. Source-to-Claim Warnings

Required source-to-claim boundaries:

- Do not claim Permea is state-of-the-art.
- Do not claim Permea outperforms any direct peptide or adjacent compound comparator.
- Do not use comparator references as evidence of Permea biological, wet-lab, in-vivo, therapeutic, or clinical validation.
- Do not use B3Pred/B3Pdb references to close local dataset redistribution rights.
- Do not use the B3Pred article's CC BY status as proof that local row-level processed data can be redistributed.
- Keep TITAN-BBB, LightBBB, Deep-B3, DeePred-BBB, and DeepBBBP explicitly adjacent to the peptide task.
- Keep leakage-aware sensitivity wording bounded; comparator citations do not establish leakage-free status.

## 11. Remaining Reference Issues

Remaining issues before broader review or public submission:

- Existing keys `b3pred_2021`, `bbppredict_2022`, and `augur_2024` still use older abbreviated metadata and may need normalization against the verified candidate pack.
- `deepb3p3_2023` identity and manuscript citation role remain unresolved.
- Existing `and others` author fields remain in several older entries.
- Recent/future-dated entries still need source-to-claim and publication-status review where applicable.
- Dataset/source/legal citation remains unresolved.
- Manuscript v0.3 has not yet integrated the newly added keys.
- Final source-to-claim cleanup remains pending.

## 12. Whether `references.bib` Is Safe to Commit

Verdict: safe to commit.

Rationale:

- The eight newly added keys are present exactly once.
- No duplicate keys were detected.
- No obvious BibTeX syntax or brace-balance issue was detected.
- Existing keys were preserved.
- Added metadata came from the verified Task 135 candidate pack.
- No manuscript claims or metric values were changed.

This does not make the bibliography final or public-submission-ready.

## 13. Recommended Next Task

Recommended next task:

**Task 138 - Commit Verified Comparator BibTeX Candidate Pack and references.bib Updates**

Suggested commit scope:

- `references.bib`
- `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
- `docs/reports/2026-05-07-updated-references-bib-post-audit.md`

After commit, a separate manuscript task should integrate the new citation keys into v0.3 and run a source-to-claim audit.

## Required Conclusion

- `references.bib` is safe to commit as a verified comparator BibTeX update.
- Manuscript citation integration and source-to-claim cleanup remain pending.
- Dataset redistribution remains unresolved.
- Public bioRxiv remains **Hold / not submission-ready**.

