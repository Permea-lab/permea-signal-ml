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
| REFQ-001 | BBB peptide databases and dataset lineage | Brainpeps | Candidate upstream BBB peptide resource or dataset-lineage source | Dataset / Methods / Related Work | `REF_NEEDED_DATASET_SOURCE` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, resource status, relationship to current dataset | Official paper, database page, repository, or indexed literature record | Must verify whether it is directly related to current processed dataset. |
| REFQ-002 | BBB peptide databases and dataset lineage | B3Pdb | Candidate BBB peptide database/source resource | Dataset / Methods / Related Work | `REF_NEEDED_DATASET_SOURCE` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, resource status, license/redistribution terms if available | Official paper, database page, repository, or indexed literature record | High priority because dataset attribution remains unresolved. |
| REFQ-003 | Early BBB peptide ML predictors | BBPpred | Candidate early BBB peptide predictor | Related Work | `REF_NEEDED_DATASET_SOURCE` / `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, predictor scope, dataset used | Publisher record, PubMed, Crossref, official repository/page | Verify whether it supports predictor lineage, dataset lineage, or both. |
| REFQ-004 | Early BBB peptide ML predictors | B3Pred | Candidate inherited BBB peptide benchmark/predictor source | Dataset / Methods / Related Work | `REF_NEEDED_DATASET_SOURCE` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, dataset source relationship, license/redistribution terms if available | Publisher record, PubMed, Crossref, official repository/page | Highest priority if it is the direct upstream source. |
| REFQ-005 | Early BBB peptide ML predictors | BBPpredict | Candidate BBB peptide predictor/source lineage item | Related Work | `REF_NEEDED_DATASET_SOURCE` / `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, predictor scope, dataset source | Publisher record, PubMed, Crossref, official repository/page | Avoid treating as direct source unless verified. |
| REFQ-006 | Deep-learning / PLM / structure-aware predictors | SCMB3PP | Candidate modern BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, method type, evaluation setup | Publisher record, PubMed, Crossref, official repository/page | Use for context only unless direct claim relevance is verified. |
| REFQ-007 | Deep-learning / PLM / structure-aware predictors | DeepB3P3 | Candidate deep-learning BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, method type, dataset used | Publisher record, PubMed, Crossref, official repository/page | Do not imply Permea outperforms it. |
| REFQ-008 | Deep-learning / PLM / structure-aware predictors | Augur | Candidate BBB or peptide predictor in survey landscape | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact domain and relation to BBB peptides | Publisher record, PubMed, Crossref, official repository/page | Name may be ambiguous; verify exact source identity. |
| REFQ-009 | Deep-learning / PLM / structure-aware predictors | BrainPepPass | Candidate modern BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, predictor scope, evaluation setup | Publisher record, PubMed, Crossref, official repository/page | Context only until verified. |
| REFQ-010 | Deep-learning / PLM / structure-aware predictors | ESM-BBB-Pred | Candidate PLM-oriented BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, PLM use, dataset and evaluation details | Publisher record, PubMed, Crossref, official repository/page | Avoid architecture comparison unless verified. |
| REFQ-011 | Deep-learning / PLM / structure-aware predictors | B3BPFN | Candidate newer BBB peptide predictor | Related Work / Future Work | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, model type, evaluation setup | Publisher record, PubMed, Crossref, official repository/page | Optional context unless central to Related Work. |
| REFQ-012 | Adjacent CPP and peptide transport benchmarks | PepBenchmark | Candidate adjacent peptide/CPP benchmark source | Related Work / Benchmark context | `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, benchmark scope | Publisher record, PubMed, Crossref, official repository/page | Verify whether BBB-specific or adjacent only. |
| REFQ-013 | Adjacent CPP and peptide transport benchmarks | PractiCPP | Candidate CPP benchmark or predictor source | Related Work / Benchmark context | `REF_NEEDED_CPP_BACKGROUND` / `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, CPP scope | Publisher record, PubMed, Crossref, official repository/page | Adjacent CPP source may not support BBB-specific claims. |
| REFQ-014 | Adjacent CPP and peptide transport benchmarks | PerseuCPP | Candidate CPP benchmark or predictor source | Related Work / Benchmark context | `REF_NEEDED_CPP_BACKGROUND` / `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, CPP scope | Publisher record, PubMed, Crossref, official repository/page | Verify spelling and exact source identity. |
| REFQ-015 | Metrics and evaluation | PR-AUC / imbalance reference | Candidate metric interpretation source | Methods / Results | `REF_NEEDED_PRAUC_IMBALANCE` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact support for PR-AUC under imbalance | Publisher record, statistics/ML source, official docs if appropriate | Required for v0.1 if PR-AUC remains emphasized. |
| REFQ-016 | Metrics and evaluation | MCC reference | Candidate metric definition or interpretation source | Methods / Results | `REF_NEEDED_MCC` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, support for MCC definition/use | Publisher record, statistics/ML source, official docs if appropriate | Required if MCC remains reported prominently. |
| REFQ-017 | Dataset documentation and reproducibility | Datasheets for Datasets | Candidate dataset documentation framework source | Methods / Supplement / Data availability | `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL | Publisher record, arXiv, official project page | Supports documentation practice only, not model validity. |
| REFQ-018 | Software citations | scikit-learn | Candidate software citation | Methods / Code availability | `REF_NEEDED_SOFTWARE_CITATIONS` | Candidate only | Preferred citation, authors/project, year, venue/DOI/URL, version relevance | Official scikit-learn citation guidance; package docs | Cite only if methods or software list requires it. |
| REFQ-019 | Software citations | pandas | Candidate software citation | Methods / Code availability | `REF_NEEDED_SOFTWARE_CITATIONS` | Candidate only | Preferred citation, authors/project, year, venue/DOI/URL, version relevance | Official pandas citation guidance; package docs | Verify package was used in current repo workflow. |
| REFQ-020 | Software citations | matplotlib | Candidate software citation | Methods / Code availability | `REF_NEEDED_SOFTWARE_CITATIONS` | Candidate only | Preferred citation, authors/project, year, venue/DOI/URL, version relevance | Official matplotlib citation guidance; package docs | Verify whether final manuscript needs software citation. |
| REFQ-021 | Sequence-derived physicochemical features | ProtParam / physicochemical feature reference candidate | Candidate source for sequence-derived feature definitions | Methods | `REF_NEEDED_SEQUENCE_FEATURES` | Candidate only | Full title or official documentation identity, authors/project, year, DOI/PMID/URL, feature definitions supported | Official documentation, primary methods paper, or package/project citation guidance | Must verify whether actual feature computation matches this source. |
| REFQ-022 | Biological BBB / peptide-delivery background | BBB peptide-delivery background reference candidate | Candidate background support for BBB barrier and peptide-delivery context | Introduction / Discussion | `REF_NEEDED_BBB_BACKGROUND` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact background claim supported | Publisher record, PubMed, Crossref, official review/paper page | Must support background only; not evidence for Permea validation. |
| REFQ-023 | Leakage / similarity-aware / benchmark hygiene | Leakage or sequence-similarity benchmark hygiene reference candidate | Candidate support for train-test contamination, k-mer/homology leakage, or similarity-aware splitting | Methods / Limitations / Supplement | `REF_NEEDED_LEAKAGE_SIMILARITY` | Candidate only | Full title, authors, year, venue, DOI/PMID/URL, exact leakage or similarity-aware evaluation claim supported | Publisher record, PubMed, Crossref, arXiv, official repository/page if applicable | Required for conservative leakage language; must not be used to claim current benchmark is leakage-free. |

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
