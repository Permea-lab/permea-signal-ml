# Dataset Legal and Availability Statement Options v0.1

## Purpose

This document provides draft dataset availability, code availability, and legal-status wording options for human review before any bioRxiv v0.1 public posting decision.

This is not legal advice. It does not confirm dataset licensing, does not authorize dataset redistribution, does not approve public dataset release, and does not make the preprint submission-ready. Human and, where appropriate, legal review is required before any public posting, public repository release, dataset redistribution, or final availability statement.

Public preprint status remains **Hold / not submission-ready** until metadata, disclosure, dataset/legal, reference, supplement/export, and human approval blockers are closed.

## Known Facts

| Item | Current repo-supported status | Evidence / path |
|---|---|---|
| Raw source path | Unresolved; no raw source dataset file is present beyond `.gitkeep`. | `data/raw/.gitkeep` |
| Imported processed dataset path | Present in repo. | `data/processed/legacy_bbb_dataset_with_features.csv` |
| Rerun-ready processed dataset path | Present in repo and referenced by config. | `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` |
| Dataset config path | Present in repo. | `configs/data/legacy_bbb_dataset_with_features.yaml` |
| Dataset surface identifier | `legacy_bbb_dataset_with_features`. | `docs/DATASET.md`; config |
| Public/preprint dataset version | `pending_confirmation`. | `configs/data/legacy_bbb_dataset_with_features.yaml`; current docs |
| Row count | 2,959 data rows in both processed CSV files, excluding header. | file line counts; dataset docs |
| File-verified fields | `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, `aromaticity`; rerun-ready file also has `sequence_id`, `source`. | processed CSV headers; config |
| Attribution/licensing | Unconfirmed. | `docs/DATASET.md`; `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` |
| Original label-source criteria | Unresolved or partially unresolved. | dataset/provenance docs |
| Leakage audit | Completed first audit; moderate benchmark optimism risk remains. | `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`; `results/audits/leakage_audit_summary.json` |

## Unknowns Requiring Human or Legal Decision

- Original dataset source and required attribution.
- Source terms of use.
- Dataset license or reuse conditions.
- Redistribution permission for the imported processed CSV.
- Redistribution permission for the rerun-ready processed CSV.
- Whether processed CSV files can be public.
- Whether rerun-ready CSV files can be public.
- Whether only derived artifacts can be public.
- Whether the dataset must remain private or internal.
- Final public repository URL.
- Final release tag, archive, or commit to cite.
- Final code license statement for repository code/docs.
- Final dataset license statement, if distinct from code/docs.
- Final contact email for data/code requests, if an on-request route is used.

## Data Availability Statement Options

### Option A - Dataset Not Publicly Redistributed Yet

Use this option if dataset licensing, source attribution, or redistribution permission remains unresolved.

Draft wording:

> Code and derived non-sensitive benchmark artifacts may be made available with the public repository or release archive, subject to final repository approval. The processed peptide dataset used for the current reruns is not publicly redistributed at this time because original source attribution, licensing, redistribution permission, and final dataset-version status remain pending confirmation. The current dataset surface, processed-path status, provenance caveats, label-source limitations, and leakage-audit findings are documented in the repository.

Required human decisions before use:

- Confirm whether the code repository will be public.
- Confirm which derived artifacts can be included.
- Confirm final repository URL, release tag, and contact route.
- Confirm that withholding processed data is the selected public position.

### Option B - Processed Dataset Available After Human/Legal Approval

Use this option only if source attribution and redistribution permission are confirmed.

Draft wording:

> The processed dataset used for the benchmark reruns is available in the public repository at `[REPO_URL]`, release `[RELEASE_TAG]`, under `[LICENSE]`, with source attribution to `[SOURCE_ATTRIBUTION]`. The dataset file used for the reported reruns is `[DATASET_PATH]`; the rerun-ready configuration is `[CONFIG_PATH]`. Dataset provenance, label-source criteria, and leakage-audit caveats are documented in the accompanying dataset and supplement materials.

Required placeholders:

- `[REPO_URL]`
- `[RELEASE_TAG]`
- `[LICENSE]`
- `[SOURCE_ATTRIBUTION]`
- `[DATASET_PATH]`
- `[CONFIG_PATH]`

Do not use this option unless dataset redistribution is approved.

### Option C - Data Available on Request

Use this option if public redistribution is not approved but private sharing may be possible under defined conditions.

Draft wording:

> The processed dataset is not redistributed publicly in this release. Access may be requested from `[CONTACT_EMAIL]` and will be considered under `[CONDITIONS]`, subject to source licensing, attribution, redistribution, and institutional or company policy review. Derived tables, audit summaries, and code availability are described separately.

Required placeholders:

- `[CONTACT_EMAIL]`
- `[CONDITIONS]`

Do not use this option unless a human-approved contact and sharing policy exist.

### Option D - Derived Artifacts Only

Use this option if original or processed dataset redistribution is not approved.

Draft wording:

> The underlying imported and rerun-ready processed peptide datasets are not redistributed with this release because source attribution, licensing, and redistribution status remain unresolved or do not permit public redistribution. Derived tables, leakage-audit summaries, figures, and code may be made available where permitted and where they do not imply redistribution rights over the underlying dataset. Dataset provenance and label-source caveats remain documented as limitations.

Required human decisions before use:

- Confirm which derived artifacts can be public.
- Confirm whether derived artifacts expose any restricted source data.
- Confirm final repository URL, release tag, and license wording for code/docs.

## Code Availability Statement Options

### Option A - Public GitHub Repository

Use this option if the repository is public and the release target is approved.

Draft wording:

> Code supporting the computational benchmark workflow is available at `[REPO_URL]`, commit `[COMMIT_HASH]`, release `[RELEASE_TAG]`, under `[LICENSE]`. The repository includes scripts, configuration files, documentation, and derived artifacts needed to inspect the current benchmark package, subject to dataset availability limitations described separately.

Required placeholders:

- `[REPO_URL]`
- `[COMMIT_HASH]`
- `[RELEASE_TAG]`
- `[LICENSE]`

### Option B - Repository Available After Release Tag

Use this option if code release is planned but the final tag or archive is not yet created.

Draft wording:

> Code supporting the computational benchmark workflow will be made available after creation of an approved public release tag or archive. The final repository URL, commit, release tag, and license statement are pending human approval and should be inserted before public posting.

### Option C - Code Available on Request

Use this option if repository visibility changes or public code release is deferred.

Draft wording:

> Code is not publicly released with this version. Access may be requested from `[CONTACT_EMAIL]` under `[CONDITIONS]`, subject to human approval and any applicable repository, dataset, or company constraints.

Required placeholders:

- `[CONTACT_EMAIL]`
- `[CONDITIONS]`

## Dataset License Statement Options

Do not choose a final license statement in this planning document.

| Option | Use when | Draft wording boundary |
|---|---|---|
| Unknown / pending confirmation | Source terms are not yet confirmed. | "Dataset license and redistribution status remain pending confirmation." |
| Repository code license only | Code/docs license is known, but dataset license is separate or unconfirmed. | "The repository code/docs license does not establish dataset redistribution rights." |
| Dataset license separate from code license | Dataset source has its own confirmed terms. | "Dataset reuse follows `[DATASET_LICENSE_OR_TERMS]`, distinct from the repository code/docs license." |
| Redistribution not approved | Human/legal review decides not to redistribute dataset files. | "Processed dataset files are not redistributed in this release." |
| Redistribution approved after confirmation | Source attribution and redistribution are confirmed. | "Dataset files are redistributed under `[LICENSE]` with `[SOURCE_ATTRIBUTION]`." |

Required placeholders if a dataset license is later confirmed:

- `[DATASET_LICENSE_OR_TERMS]`
- `[LICENSE]`
- `[SOURCE_ATTRIBUTION]`

## Human Decision Checklist

- [ ] Identify original dataset source.
- [ ] Verify source terms of use.
- [ ] Verify required source attribution.
- [ ] Verify redistribution permission.
- [ ] Decide whether the imported processed dataset can be public.
- [ ] Decide whether the rerun-ready processed dataset can be public.
- [ ] Decide whether derived artifacts only can be public.
- [ ] Decide whether the dataset must remain private/internal.
- [ ] Confirm repository code/docs license statement.
- [ ] Confirm repository URL.
- [ ] Confirm release tag or archive policy.
- [ ] Confirm commit hash to cite.
- [ ] Confirm contact email, if an on-request route is used.
- [ ] Confirm final data availability statement.
- [ ] Confirm final code availability statement.
- [ ] Confirm final dataset license statement or unresolved-license caveat.
- [ ] Confirm final public posting decision.

## Recommended Current Conservative Wording

Recommended until legal/source confirmation is complete:

> The code and selected derived benchmark artifacts are planned for release through an approved repository archive, but the processed peptide dataset is not approved for public redistribution in the current package. Original dataset source attribution, licensing, redistribution permission, raw source path, public dataset version, and label-source criteria remain pending confirmation. The current manuscript and supplement should therefore describe the dataset surface, processed paths, and provenance limitations without claiming a public dataset release or complete provenance. Any public posting should retain the documented leakage caveat: current metrics are random-stratified baseline metrics and may be optimistic under measured sequence-similarity structure.

This wording is a conservative draft for human review only. It is not a final availability statement.

## Impact on bioRxiv Readiness

- Dataset/legal availability remains a blocker until the human operator chooses and approves final wording.
- Conservative wording can support a bounded preprint candidate only if accepted by human/legal review.
- Public dataset release is not approved by this document.
- Complete provenance is not claimed by this document.
- Public preprint status remains **Hold / not submission-ready**.

## Recommended Next Maintainer Task

Recommended next task: Task 071 - Commit Dataset Legal and Availability Statement Options.

## No-Change Confirmation

- No legal certainty was invented.
- No dataset redistribution permission was claimed.
- Manuscript scientific content was not modified.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Metric values were not changed.
