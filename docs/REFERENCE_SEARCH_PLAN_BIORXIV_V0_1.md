# Reference Search Plan for bioRxiv v0.1

## Purpose

This plan defines the reference search and verification workflow for the bioRxiv v0.1 preprint package.

This document does not add references, does not fabricate citations, does not finalize the bibliography, and does not make the public preprint ready. Public preprint status remains **Not yet** until references, metadata, disclosure, dataset/legal, supplement/export, and claim-boundary gaps are closed or explicitly caveated.

The deep-research survey has been converted into planning artifacts only:

- `docs/LITERATURE_SURVEY_SOURCE_LANDSCAPE_V0_1.md`
- `docs/REFERENCE_VERIFICATION_QUEUE_BIORXIV_V0_1.md`

These artifacts list candidate literature themes and verification priorities. They do not verify references or add final citation metadata.

## Reference principles

- Every citation must be verified before insertion.
- No memory-only citations may be used.
- No DOI, PMID, URL, title, author list, venue, or publication year may be guessed.
- Prefer primary sources for methods, datasets, metrics, and software; use review papers only where they are the appropriate support for broad background.
- Cite methods and metrics for the exact claims they support, not for stronger claims.
- Cite the original dataset source only after confirming the upstream source, attribution requirements, and licensing or redistribution relevance.
- Software citations should follow package or project citation recommendations where available.
- Placeholder keys may be used during planning, but placeholder keys are not references.

## Reference categories

| Reference category | Manuscript section | Why needed | Minimum number of references | Preferred source type | Search query candidates | Verification criteria | Placeholder key | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BBB / biological barrier background | Introduction | Supports the BBB-oriented delivery-barrier context without expanding beyond the current computational evidence. | 1-2 | Review for broad context; primary source for specific mechanistic statements if any are retained | `blood brain barrier peptide permeability review`; `blood brain barrier drug delivery peptide review`; `blood brain barrier permeability computational peptide review` | Verify title, authors, year, venue, DOI or stable URL; confirm the source supports background framing only. | `REF_NEEDED_BBB_BACKGROUND` | Search needed |
| Peptide permeability / cell-penetrating peptide background | Introduction / Discussion | Grounds peptide and cell-penetrating peptide context while avoiding claims of validated delivery. | 1-2 | Review paper for field context; primary paper only for specific narrower claims | `cell penetrating peptide blood brain barrier review`; `peptide permeability blood brain barrier review`; `cell penetrating peptides delivery review` | Verify bibliographic metadata; confirm any cited sentence does not imply Permea wet-lab validation. | `REF_NEEDED_CPP_BACKGROUND` | Search needed |
| Sequence-derived physicochemical features | Methods | Supports feature definitions and precedent for sequence-derived descriptors such as length, charge, gravy, pI, and aromaticity. | 1-2 | Primary method/source for feature definitions; software documentation if a package calculation is cited | `peptide physicochemical properties permeability machine learning`; `protein sequence physicochemical features gravy pI aromaticity`; `amino acid sequence descriptors peptide machine learning` | Verify the source defines or justifies the specific feature family used; do not cite for biological mechanism. | `REF_NEEDED_SEQUENCE_FEATURES` | Search needed |
| Baseline ML classification methods | Methods | Supports Dummy, Logistic Regression, and Random Forest as baseline classifiers and clarifies that these are benchmark models. | 1-2 | Software documentation or canonical method references | `scikit learn logistic regression random forest classifier citation`; `random forest classifier original paper`; `logistic regression classification machine learning reference` | Verify software version relevance or original method source; confirm citation supports method description only. | `REF_NEEDED_BASELINE_ML` | Search needed |
| PR-AUC under class imbalance | Methods / Results | Supports the use of PR-AUC and interpretation under imbalanced binary classification. | 1-2 | Methods paper, evaluation guide, or statistics/ML reference | `precision recall area under curve imbalanced classification`; `PR AUC imbalanced binary classification evaluation`; `precision recall curves class imbalance machine learning` | Verify the source explicitly discusses precision-recall interpretation under imbalance. | `REF_NEEDED_PRAUC_IMBALANCE` | Search needed |
| Matthews correlation coefficient | Methods / Results | Supports MCC as a binary-classification summary metric under imbalance. | 1 | Methods or evaluation-metric reference | `Matthews correlation coefficient binary classification`; `MCC imbalanced classification metric`; `Matthews correlation coefficient machine learning evaluation` | Verify the source supports MCC definition or use, not stronger performance claims. | `REF_NEEDED_MCC` | Search needed |
| Leakage / sequence similarity / train-test contamination | Methods / Limitations | Supports leakage-risk language, cross-fold sequence-similarity caveats, and future similarity-aware evaluation. | 1-3 | Bioinformatics benchmark paper, ML leakage methods paper, or sequence-similarity evaluation reference | `train test leakage sequence similarity bioinformatics benchmark`; `sequence similarity train test split machine learning benchmark`; `data leakage bioinformatics machine learning sequence similarity` | Verify source relevance to train/test contamination, sequence similarity, or benchmark optimism. | `REF_NEEDED_LEAKAGE_SIMILARITY` | Search needed |
| Benchmark reproducibility / dataset cards / model cards | Introduction / Discussion / Supplement | Supports artifact-traceability, dataset documentation, and reproducible benchmark framing. | 1-3 | Dataset-card/model-card paper, reproducibility guidance, or benchmark documentation source | `dataset cards for machine learning datasets`; `model cards machine learning documentation`; `reproducible bioinformatics benchmark reporting` | Verify source supports documentation/reproducibility practice; do not cite as evidence of biological validity. | `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Search needed |
| Original dataset source / B3Pred or inherited source | Dataset / Methods | Required for attribution, label-source context, and dataset/legal closure. | 1 or as required by source chain | Original dataset paper, official dataset page, repository, or archived source | `B3Pred blood brain barrier peptide dataset`; `BBB peptide permeability dataset B3Pred`; `blood brain barrier peptide benchmark dataset` | Verify exact source identity, title/authors/year/URL or DOI, license/redistribution terms if available, and relationship to the current processed dataset. | `REF_NEEDED_DATASET_SOURCE` | Search needed |
| Software citations | Methods / Code availability | Supports software/tool use statements for pandas, numpy, scikit-learn, matplotlib, seaborn, PyYAML, and other cited dependencies if needed. | As needed | Official package citation instructions, package docs, or canonical software papers | `scikit learn citation`; `pandas citation`; `numpy citation`; `matplotlib citation`; `seaborn citation`; `PyYAML citation` | Verify each package's preferred citation and version relevance; include only software actually used in the paper/package. | `REF_NEEDED_SOFTWARE_CITATIONS` | Search needed |

## Suggested search queries

These are search candidates only. They are not citations and should not be copied into the manuscript as references.

| Reference category | Query candidates |
| --- | --- |
| BBB / biological barrier background | `blood brain barrier peptide permeability review`; `blood brain barrier drug delivery peptide review`; `blood brain barrier permeability computational peptide review` |
| Peptide permeability / cell-penetrating peptide background | `cell penetrating peptide blood brain barrier review`; `peptide permeability blood brain barrier review`; `cell penetrating peptides delivery review` |
| Sequence-derived physicochemical features | `peptide physicochemical properties permeability machine learning`; `protein sequence physicochemical features gravy pI aromaticity`; `amino acid sequence descriptors peptide machine learning` |
| Baseline ML classification methods | `scikit learn logistic regression random forest classifier citation`; `random forest classifier original paper`; `logistic regression classification machine learning reference` |
| PR-AUC under class imbalance | `precision recall area under curve imbalanced classification`; `PR AUC imbalanced binary classification evaluation`; `precision recall curves class imbalance machine learning` |
| Matthews correlation coefficient | `Matthews correlation coefficient binary classification`; `MCC imbalanced classification metric`; `Matthews correlation coefficient machine learning evaluation` |
| Leakage / sequence similarity / train-test contamination | `train test leakage sequence similarity bioinformatics benchmark`; `sequence similarity train test split machine learning benchmark`; `data leakage bioinformatics machine learning sequence similarity` |
| Benchmark reproducibility / dataset cards / model cards | `dataset cards for machine learning datasets`; `model cards machine learning documentation`; `reproducible bioinformatics benchmark reporting` |
| Original dataset source / B3Pred or inherited source | `B3Pred blood brain barrier peptide dataset`; `BBB peptide permeability dataset B3Pred`; `blood brain barrier peptide benchmark dataset` |
| Software citations | `scikit learn citation`; `pandas citation`; `numpy citation`; `matplotlib citation`; `seaborn citation`; `PyYAML citation` |

## Verification workflow

1. Search within the reference category using the query candidates above.
2. Select candidate sources that match the specific manuscript sentence or section need.
3. Verify title, authors, year, venue, DOI if present, PMID if present, and stable URL if no DOI is available.
4. Confirm the source supports the exact manuscript statement and does not require stronger or different wording.
5. Add the candidate to a working reference table with the placeholder key it closes.
6. Insert either a placeholder key or a final citation only after verification is complete.
7. Run a final citation consistency check to confirm every in-text citation has a reference entry and every reference entry is used or intentionally retained.

## Reference acceptance criteria

A reference may be added only if:

- title, authors, year, venue, and DOI or stable URL are verified;
- the source is relevant to the exact manuscript statement;
- the source supports the claim being cited without being stretched into stronger claims;
- the source does not convert the current computational benchmark into biological validation, robust generalization, or therapeutic/clinical evidence;
- dataset/source citations are checked for attribution, license, redistribution, and source-chain relevance where applicable;
- software citations follow package or project recommendations where available.

## Reference insertion plan

Later reference-insertion work should:

- create `references.bib` only after verified references are selected;
- keep placeholder keys in planning docs until each source is verified;
- map each placeholder key to one or more final citations;
- add citation placeholders to `docs/PREPRINT_DRAFT_V0_1.md` only where the exact sentence or paragraph needs support;
- avoid inserting references that are not used by the manuscript or supplement;
- run a final consistency check across `docs/PREPRINT_DRAFT_V0_1.md`, `references.bib`, the supplement, and availability statements.

## Current blocker status

Formal references are a blocker before bioRxiv v0.1. The absence of formal references does not block internal development or trusted review, but it does block public posting until verified citations are selected and inserted.

Reference insertion should happen after verified search, dataset/source attribution checks, and final manuscript sentence-level citation mapping.

## Recommended next Codex task

Task 043 — Commit Literature Survey Landscape and Reference Queue
