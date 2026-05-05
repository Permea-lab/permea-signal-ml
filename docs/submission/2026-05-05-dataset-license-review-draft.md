# Dataset License Review Draft - 2026-05-05

## Purpose

This draft separates observed repository facts from manual legal and licensing decisions still required before any public bioRxiv posting, public repository release, dataset redistribution, or final data availability statement.

This is not legal advice. It does not conclude that redistribution is permitted. It does not approve public dataset release.

## Observed Facts

### Dataset Surface

- Current dataset surface identifier: `legacy_bbb_dataset_with_features`.
- Config path: `configs/data/legacy_bbb_dataset_with_features.yaml`.
- Config dataset version: `pending_confirmation`.
- Config input path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`.
- Config source column: `source`.
- Config notes state the dataset was prepared from imported legacy processed `dataset_with_features.csv`.
- Config notes state dataset version, attribution, and licensing must be confirmed before benchmark use.

### Visible Data Artifacts

Repo data files observed:

- `data/README.md`
- `data/examples/example_sequences.csv`
- `data/interim/.gitkeep`
- `data/processed/.gitkeep`
- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- `data/raw/.gitkeep`

The raw source dataset path remains unresolved in the repo; `data/raw/` contains only `.gitkeep`.

### Processed Dataset Artifacts That May Raise Redistribution Questions

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

These contain processed benchmark rows and may require source attribution, license, terms-of-use, and redistribution review before public release.

### Visible Licensing or Attribution Clues

- `docs/DATASET_LEGAL_AND_AVAILABILITY_STATEMENT_OPTIONS_V0_1.md` states attribution/licensing is unconfirmed.
- `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` states original source attribution and license/redistribution rights are unresolved.
- `docs/DATASET.md` states the exact public dataset version remains `pending_confirmation`.
- The repository may have a code/docs license, but existing docs state that the repository code/docs license does not establish dataset redistribution rights.

## Source Dataset(s)

Observed source-chain description from current docs:

- Imported legacy BBB-oriented processed dataset.
- Legacy processed dataset path now represented by `data/processed/legacy_bbb_dataset_with_features.csv`.
- Rerun-ready derivative represented by `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`.
- Original raw source path, source publication/data source, and original label-source criteria remain unresolved or only partially recovered.

No final source attribution is established by this draft.

## Manual Legal Decisions Still Required

Before public posting or public dataset release, a human/legal reviewer must decide:

- original dataset source and required attribution
- source terms of use
- dataset license or reuse conditions
- whether the imported processed CSV may be redistributed
- whether the rerun-ready processed CSV may be redistributed
- whether only derived artifacts may be public
- whether data should remain private/internal
- final data availability wording
- final code availability wording
- final dataset license statement or unresolved-license caveat
- final repository URL, release tag, archive policy, and commit hash to cite

## Conservative Availability Path

Until licensing and redistribution are confirmed, the safest public-facing posture is:

- do not claim processed dataset redistribution is approved
- do not claim complete provenance
- do not claim complete licensing
- use derived-artifacts-only or no-public-data wording if selected by the human/legal reviewer
- keep source, label, provenance, and leakage caveats visible

## Review Verdict

**Hold for manual legal/licensing decision.**

The repository documents enough facts to support internal review and to draft conservative data/code availability options. It does not yet document enough legal certainty to approve public dataset redistribution.

## No-Change Confirmation

- No data files were modified.
- No result artifacts were modified.
- No figure artifacts were modified.
- `references.bib` was not modified.
- Manuscript scientific content was not modified.
- No legal certainty was invented.
- Public preprint remains **Hold / not submission-ready**.
