# Reference Verification Queue for bioRxiv v0.1

## Purpose

This queue lists candidate references that require verification before inclusion in the bioRxiv v0.1 preprint package.

No reference is accepted until verified. No citation is inserted by this document. Survey citations are treated as leads only, and prior-chat citation markers are not valid repo citations.

## Verification status legend

- Candidate only
- Metadata verified
- Claim relevance verified
- Ready for bibliography
- Rejected / not relevant
- Needs replacement

## Candidate reference table

| Queue ID | Reference cluster | Candidate reference name | Claimed role in survey | Target manuscript section | Placeholder key | Verification status | Required metadata to verify | Verification source to check | Notes / risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REFQ-001 | BBB peptide databases and dataset lineage | Brainpeps | Candidate upstream BBB peptide resource or dataset-lineage source | Dataset / Methods / Related Work | `REF_BRAINPEPS_DATABASE`; `REF_NEEDED_DATASET_SOURCE` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, lead authors, year, venue, DOI verified from Task 044 context; current dataset relationship still requires manuscript-specific caution | External verification reported in Task 044 context; verification source noted as UGent bibliographic record | Use for BBB peptide database lineage and heterogeneous BBB transport evidence; do not use to resolve dataset licensing. |
| REFQ-002 | BBB peptide databases and dataset lineage | B3Pdb | Candidate BBB peptide database/source resource | Dataset / Methods / Related Work | `REF_B3PDB_DATABASE`; `REF_NEEDED_DATASET_SOURCE` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, lead authors, year, venue, DOI verified from Task 044 context; license/redistribution terms still need dataset-policy review | External verification reported in Task 044 context; verification source noted as CNGBdb / BioinformaticsHome style record | High priority for dataset/database lineage; does not settle processed dataset redistribution status. |
| REFQ-003 | Early BBB peptide ML predictors | BBPpred | Candidate early BBB peptide predictor | Related Work | `REF_BBPPRED`; `REF_NEEDED_DATASET_SOURCE` / `REF_NEEDED_BBB_BACKGROUND` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, lead authors, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Use as early sequence-based BBB peptide classifier / logistic-regression comparator. |
| REFQ-004 | Early BBB peptide ML predictors | B3Pred | Candidate inherited BBB peptide benchmark/predictor source | Dataset / Methods / Related Work | `REF_B3PRED`; `REF_NEEDED_DATASET_SOURCE` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, lead authors, year, venue, DOI verified from Task 044 context; exact current dataset relationship still needs careful language | External verification reported in Task 044 context | Direct comparator and likely dataset-lineage reference; do not overuse to claim Permea dataset novelty. |
| REFQ-005 | Early BBB peptide ML predictors | BBPpredict | Candidate BBB peptide predictor/source lineage item | Related Work | `REF_BBPPREDICT`; `REF_NEEDED_DATASET_SOURCE` / `REF_NEEDED_BBB_BACKGROUND` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, lead authors, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Evaluation comparator; do not imply Permea used its nested-CV or independent-test design. |
| REFQ-006 | Deep-learning / PLM / structure-aware predictors | SCMB3PP | Candidate modern BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, method type, evaluation setup | Publisher record, PubMed, Crossref, official repository/page | Use for context only unless direct claim relevance is verified. |
| REFQ-007 | Deep-learning / PLM / structure-aware predictors | DeepB3P3 | Candidate deep-learning BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, method type, dataset used | Publisher record, PubMed, Crossref, official repository/page | Do not imply Permea outperforms it. |
| REFQ-008 | Deep-learning / PLM / structure-aware predictors | Augur | Candidate BBB or peptide predictor in survey landscape | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact domain and relation to BBB peptides | Publisher record, PubMed, Crossref, official repository/page | Name may be ambiguous; verify exact source identity. |
| REFQ-009 | Deep-learning / PLM / structure-aware predictors | BrainPepPass | Candidate modern BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, predictor scope, evaluation setup | Publisher record, PubMed, Crossref, official repository/page | Context only until verified. |
| REFQ-010 | Deep-learning / PLM / structure-aware predictors | ESM-BBB-Pred | Candidate PLM-oriented BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, PLM use, dataset and evaluation details | Publisher record, PubMed, Crossref, official repository/page | Avoid architecture comparison unless verified. |
| REFQ-011 | Deep-learning / PLM / structure-aware predictors | B3BPFN | Candidate newer BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, model type, evaluation setup | Publisher record, PubMed, Crossref, official repository/page | Optional context unless central to Related Work. |
| REFQ-012 | Adjacent CPP and peptide transport benchmarks | PepBenchmark | Candidate adjacent peptide/CPP benchmark source | Related Work / Benchmark context | `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, benchmark scope | Publisher record, PubMed, Crossref, official repository/page | Verify whether BBB-specific or adjacent only. |
| REFQ-013 | Adjacent CPP and peptide transport benchmarks | PractiCPP | Candidate CPP benchmark or predictor source | Related Work / Benchmark context | `REF_PRACTICPP_IMBALANCE`; `REF_NEEDED_CPP_BACKGROUND` / `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, lead authors, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Adjacent CPP benchmark realism, imbalance, deduplication, conflicting-label removal, and negative/unlabeled caution; not direct BBB validation. |
| REFQ-014 | Adjacent CPP and peptide transport benchmarks | PerseuCPP | Candidate CPP benchmark or predictor source | Related Work / Benchmark context | `REF_NEEDED_CPP_BACKGROUND` / `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, CPP scope | Publisher record, PubMed, Crossref, official repository/page | Verify spelling and exact source identity. |
| REFQ-015 | Metrics and evaluation | PR-AUC / imbalance reference | Candidate metric interpretation source | Methods / Results | `REF_PRAUC_IMBALANCE`; `REF_NEEDED_PRAUC_IMBALANCE` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, authors, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Required for PR-AUC interpretation under imbalanced labels. |
| REFQ-016 | Metrics and evaluation | MCC reference | Candidate metric definition or interpretation source | Methods / Results | `REF_MCC_BINARY_CLASSIFICATION`; `REF_NEEDED_MCC` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Full title, authors, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Required if MCC remains reported prominently. |
| REFQ-017 | Dataset documentation and reproducibility | Datasheets for Datasets | Candidate dataset documentation framework source | Methods / Supplement / Data availability | `REF_DATASETS_FOR_DATASETS`; `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Partially verified / needs final metadata completion; claim relevance verified | Title, lead authors, year, and venue provided in Task 044 context; DOI and exact final bibliographic details not provided | External verification reported in Task 044 context; one more metadata-completion pass needed | Supports documentation practice only, not model validity or dataset licensing closure. |
| REFQ-018 | Software citations | scikit-learn | Candidate software citation | Methods / Code availability | `REF_SCIKIT_LEARN`; `REF_NEEDED_SOFTWARE_CITATIONS` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Title, authors, year, venue, and volume/pages provided in Task 044 context | External verification reported in Task 044 context | Software citation for Logistic Regression, Random Forest, StratifiedKFold, and metrics. |
| REFQ-019 | Software citations | pandas | Candidate software citation | Methods / Code availability | `REF_PANDAS`; `REF_NEEDED_SOFTWARE_CITATIONS` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Title, author, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Software citation for dataframe/CSV processing. |
| REFQ-020 | Software citations | matplotlib | Candidate software citation | Methods / Code availability | `REF_MATPLOTLIB`; `REF_NEEDED_SOFTWARE_CITATIONS` | Metadata verified; claim relevance verified; Ready for bibliography preparation | Title, author, year, venue, DOI verified from Task 044 context | External verification reported in Task 044 context | Software citation for figure generation. |
| REFQ-021 | Sequence-derived physicochemical features | ProtParam / physicochemical feature reference candidate | Candidate source for sequence-derived feature definitions | Methods | `REF_PROTPARAM_FEATURES`; `REF_NEEDED_SEQUENCE_FEATURES` | Partially verified / needs canonical citation verification; claim relevance verified | Tool/reference name and supported role provided in Task 044 context; canonical paper citation, year, venue, DOI/PMID/URL not provided | External verification reported in Task 044 context; canonical citation still needs verification | Use as feature/tool support only after canonical citation is resolved. |
| REFQ-022 | Biological BBB / peptide-delivery background | BBB peptide-delivery background reference candidate | Candidate background support for BBB barrier and peptide-delivery context | Introduction / Discussion | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact background claim supported | Publisher record, PubMed, Crossref, official review/paper page | Must support background only; not evidence for Permea validation. |
| REFQ-023 | Leakage / similarity-aware / benchmark hygiene | Leakage or sequence-similarity benchmark hygiene reference candidate | Candidate support for train-test contamination, k-mer/homology leakage, or similarity-aware splitting | Methods / Limitations / Supplement | `REF_NEEDED_LEAKAGE_SIMILARITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact leakage or similarity-aware evaluation claim supported | Publisher record, PubMed, Crossref, arXiv, official repository/page if applicable | Required for conservative leakage language; must not be used to claim current benchmark is leakage-free. |

## Task 044 status update

The following references were externally verified in the Task 044 context and are ready for bibliography preparation unless noted as partial:

- `REF_BRAINPEPS_DATABASE`
- `REF_B3PDB_DATABASE`
- `REF_B3PRED`
- `REF_BBPPRED`
- `REF_BBPPREDICT`
- `REF_PRAUC_IMBALANCE`
- `REF_MCC_BINARY_CLASSIFICATION`
- `REF_SCIKIT_LEARN`
- `REF_PANDAS`
- `REF_MATPLOTLIB`
- `REF_PRACTICPP_IMBALANCE`

The following references are partially verified and need final metadata completion or canonical citation verification:

- `REF_DATASETS_FOR_DATASETS`
- `REF_PROTPARAM_FEATURES`

The following references remain unverified and must stay in the queue:

- `REF_PEPBENCHMARK_KMER_HOMOLOGY`
- `REF_PERSEUCPP`
- `REF_AUGUR`
- `REF_BRAINPEPPASS`
- `REF_ESM_BBB_PRED`
- `REF_B3BPFN`
- `REF_DEEPB3P3`
- `REF_BBB_SHUTTLE_REVIEW`
- `REF_CPP_CLINICAL_REVIEW`

## Priority ranking

### Priority 1 - Required for v0.1 preprint

- dataset/source lineage: Brainpeps, B3Pdb, BBPpred, B3Pred, BBPpredict as applicable after verification
- BBB/peptide biological background
- PR-AUC/imbalance reference
- MCC reference
- leakage/similarity-aware benchmark evaluation source
- software citations for methods/code availability if required

### Priority 2 - Strongly recommended

- modern BBB predictors: SCMB3PP, DeepB3P3, Augur, BrainPepPass, ESM-BBB-Pred, B3BPFN
- CPP benchmark papers: PepBenchmark, PractiCPP, PerseuCPP
- dataset documentation and reproducibility references

### Priority 3 - Optional context

- newer architecture-heavy predictors not needed for core v0.1 claims
- design-oriented deep models
- broad survey references that are useful for background but not necessary for claim support

## Verification workflow

1. Run web or literature search in a later task, not in this planning task.
2. Verify title, authors, year, venue, DOI if present, PMID if present, and stable URL.
3. Confirm the exact manuscript claim supported by the candidate.
4. Record verification status and evidence source in this queue.
5. Create `references.bib` only after references are verified and accepted.
6. Insert citation placeholders or final citations in a later manuscript-editing task.

## Rejection criteria

A candidate should be rejected or replaced if:

- metadata cannot be verified;
- the source does not support the target manuscript claim;
- the source is too weak, too broad, or too unrelated;
- the source would encourage overclaiming;
- the source cannot be reconciled with dataset attribution, licensing, or redistribution needs where those are relevant.

## Recommended next Codex task

Task 043 — Commit Literature Survey Landscape and Reference Queue
