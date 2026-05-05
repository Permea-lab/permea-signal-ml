# Dataset Attribution and Data Availability Decision Package - 2026-05-06

## Purpose

This package organizes the dataset attribution, licensing, redistribution, and data/code availability decisions still required for Permea manuscript v0.2 and any future public release.

This document is not legal advice. It does not conclude that dataset redistribution is permitted. It does not approve public dataset release, public bioRxiv posting, or public repository release.

Public bioRxiv remains **Hold / not submission-ready**.

## Materials Reviewed

- `docs/submission/2026-05-05-dataset-license-review-draft.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`
- `docs/reports/2026-05-06-reference-cleanup-and-citation-plan.md`
- `docs/reports/2026-05-06-reference-cleanup-post-audit.md`
- `docs/paper/permea-first-paper-manuscript-v0-1.md`
- `README.md`
- `references.bib`
- `data/README.md`
- `configs/data/legacy_bbb_dataset_with_features.yaml`
- visible `data/` and `results/` artifact paths

## 1. Current Dataset/Source Status

Observed current dataset surface:

- Dataset identifier: `legacy_bbb_dataset_with_features`
- Dataset version: `pending_confirmation`
- Dataset config: `configs/data/legacy_bbb_dataset_with_features.yaml`
- Current rerun-ready input path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- Imported processed path: `data/processed/legacy_bbb_dataset_with_features.csv`
- Source column: `source`
- Current operational source value described in config: `legacy_bbb_import`

Current source-chain status:

- The dataset is described as prepared from an imported legacy processed `dataset_with_features.csv`.
- The original raw source path is not present in `data/raw/`.
- `data/raw/` contains only `.gitkeep`.
- Original source publication/data source is unresolved.
- Original label-source criteria are unresolved.
- Dataset attribution, licensing, source terms, and redistribution permission remain unresolved.

The current source field is operational metadata. It should not be treated as original upstream attribution.

## 2. Observed Repo Data Artifacts

### Data Files

Visible data artifacts:

- `data/README.md`
- `data/examples/example_sequences.csv`
- `data/interim/.gitkeep`
- `data/processed/.gitkeep`
- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- `data/raw/.gitkeep`

Interpretation:

- `data/examples/example_sequences.csv` is documented as a synthetic smoke-test example, not benchmark evidence.
- `data/processed/legacy_bbb_dataset_with_features.csv` is an imported processed dataset artifact.
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` is a rerun-ready processed derivative.
- `data/raw/` does not contain the raw upstream dataset.

### Result and Derived Artifacts

Visible derived artifacts include:

- Random-stratified summary tables and metrics under `results/tables/` and `results/metrics/`.
- Leakage audit outputs under `results/audits/`.
- Leakage-aware group assignment, split manifest, and rerun outputs under `results/sensitivity/`.
- Figures under `figures/` referenced by README and manuscript-support materials.

Interpretation:

- These are derived artifacts from the repository workflow.
- Public release of derived artifacts may be easier to justify than processed dataset redistribution, but still requires founder/manual review because derived artifacts may expose row-level information, predictions, labels, or sequence identifiers.

## 3. Source-Required / Manual-Decision Items

The following items require manual founder/legal/source review:

- Original dataset source identity.
- Original source publication or official dataset page.
- Required attribution wording.
- Dataset license or terms of use.
- Whether imported processed data may be redistributed.
- Whether rerun-ready processed data may be redistributed.
- Whether row-level derived artifacts may be released publicly.
- Whether aggregate-only derived artifacts may be released publicly.
- Whether data should remain private/internal.
- Final data availability statement.
- Final code availability statement.
- Final repository release URL, commit hash, tag, archive policy, and software license.
- Whether any dataset/source citation should be added to `references.bib`.

Do not infer these from the repository name, code/docs license, current GitHub remote, or processed file presence.

## 4. Existing Citation Keys Related to Dataset/Source

Existing keys that are relevant to BBB peptide resource or predictor context:

- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `augur_2024`
- `brainpeppass_2024`
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`

Use boundary:

- These keys may support background, database, archive, or predictor lineage after citation cleanup.
- They do not currently establish the exact source identity, attribution requirements, licensing terms, redistribution rights, or label-source criteria for the processed Permea dataset.

Current source-required key gap:

- Original dataset source/publication: source required.
- Dataset license/terms: source required.
- Original label-source criteria: source required.

No new references should be added until exact source metadata are verified.

## 5. Dataset Attribution Wording Candidates

### Candidate A - Conservative Unresolved Attribution

Use if original source attribution remains unresolved:

```text
The benchmark uses an imported legacy BBB-oriented processed peptide dataset that has been converted into a rerun-ready repository surface. The original upstream source attribution, dataset version, license, redistribution status, and original label-source criteria remain pending confirmation. The current `source` field is operational metadata (`legacy_bbb_import`) and should not be interpreted as original source attribution.
```

### Candidate B - Processed Dataset Path Disclosure

Use when disclosing current repository paths without approving redistribution:

```text
The internal rerun-ready dataset surface is stored in the repository as `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`, derived from `data/processed/legacy_bbb_dataset_with_features.csv`. These files document the benchmark surface used for current reruns, but public redistribution remains unresolved pending source attribution, licensing, and legal review.
```

### Candidate C - Future Confirmed Attribution Placeholder

Use only after manual verification:

```text
TODO after source verification: The dataset was derived from [verified source name/citation], subject to [verified license/terms]. Attribution and redistribution permissions are described according to the verified source terms.
```

Do not use Candidate C publicly until the bracketed values are verified.

## 6. Data Availability Wording Candidates

### Candidate A - No Public Dataset Redistribution Yet

Safest current default:

```text
The processed peptide dataset used in this benchmark is not approved for public redistribution in the current draft because source attribution, license terms, redistribution permission, raw source path, public dataset version, and original label-source criteria remain pending manual confirmation. Aggregate benchmark summaries, audit summaries, and code may be released where approved, but such release does not imply redistribution rights for the underlying processed dataset.
```

### Candidate B - Derived Artifacts Only

Use if founder/legal review approves derived artifacts but not processed data:

```text
Processed dataset redistribution is not currently approved. Public release, if approved, will be limited to code and selected derived artifacts such as aggregate metric summaries, audit summaries, and documentation. Row-level files containing sequences, labels, predictions, group assignments, or split manifests will remain withheld unless source terms and manual legal review explicitly permit release.
```

### Candidate C - Data Available on Request

Use only if a contact route and sharing policy are approved:

```text
Processed data are not publicly redistributed with this release. Access may be considered on request subject to source terms, licensing restrictions, and manual approval by Permea. Request approval does not imply that redistribution is permitted.
```

### Candidate D - Public Processed Dataset

Not currently supported:

```text
Do not use until source attribution, license, redistribution permission, public dataset version, label-source criteria, and release policy are explicitly verified and approved.
```

## 7. Code Availability Wording Candidates

### Candidate A - Code Release Pending

Current conservative wording:

```text
Code supporting the computational benchmark workflow is planned for release through an approved Permea repository or archive, pending final repository URL, commit hash, release tag, archive policy, and software license confirmation. Code availability is separate from data availability and does not imply permission to redistribute the processed dataset.
```

### Candidate B - Code Available, Data Restricted

Use only after repository release approval:

```text
Code supporting the computational benchmark workflow is available at [approved repository URL and release tag/commit]. Dataset availability is described separately because processed dataset redistribution depends on source attribution, license terms, and manual legal review.
```

Do not fill the bracketed fields until release details are approved.

## 8. Recommended Safest Public-Release Posture

Recommended current posture: **No public processed dataset redistribution yet; code and selected aggregate derived artifacts only after review.**

Rationale:

- Original dataset source attribution is unresolved.
- Dataset license and redistribution permission are unresolved.
- Raw source path is absent from the repo.
- Original label-source criteria are unresolved.
- Row-level derived artifacts may expose sequences, labels, predictions, group IDs, or split assignments.
- Public bioRxiv and public repository release require founder/manual approval.

Recommended release separation:

1. Code availability can proceed only after repository release URL, commit/tag, archive policy, and software license are approved.
2. Processed data files should remain withheld unless explicit source terms permit redistribution.
3. Row-level derived artifacts should be reviewed separately because they may partially reproduce dataset contents.
4. Aggregate metrics, audit summaries, and documentation may be candidates for public release after claim-boundary and legal review.

## 9. Manual Founder/Legal Decision Checklist

Before public preprint, public repository release, or dataset release:

- [ ] Identify original dataset source.
- [ ] Verify source citation metadata.
- [ ] Verify dataset license or terms of use.
- [ ] Decide whether processed dataset redistribution is permitted.
- [ ] Decide whether rerun-ready processed data can be public.
- [ ] Decide whether row-level predictions, rankings, split manifests, group assignments, or audit CSVs can be public.
- [ ] Decide whether aggregate-only derived artifacts can be public.
- [ ] Decide final data availability route: no data, derived artifacts only, on request, or public processed dataset.
- [ ] Approve exact dataset attribution wording.
- [ ] Approve exact data availability wording.
- [ ] Approve exact code availability wording.
- [ ] Approve final repository URL, commit/tag, release policy, and software license.
- [ ] Decide whether new dataset/source references must be added to `references.bib`.
- [ ] Re-run final citation/source-claim review after wording is selected.
- [ ] Confirm public bioRxiv readiness only after all blockers close.

## 10. Recommended Next Task

Recommended next task:

**Task 118 - Commit Dataset Attribution and Availability Decision Package**

After commit, the next substantive work should be:

**Task 119 - Resolve Dataset Source Attribution and Availability Wording With Founder/Legal Input**

That task should collect the manual decisions above before manuscript v0.2 citation and availability integration.

## No-Change Confirmation

- Manuscript files were not modified.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Model, split, and leakage audit artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- No legal conclusion was made.
- No dataset redistribution permission was claimed.
- Public bioRxiv remains **Hold / not submission-ready**.
