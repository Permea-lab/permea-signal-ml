# Literature Survey Source Landscape v0.1

## Purpose

This memo summarizes the literature landscape from the deep-research survey titled "Survey of Studies Relevant to Permea Signal ML v0.1" for reference planning.

This is not manuscript text, not a final bibliography, and not a source of final repo citations. Citation markers from prior research sessions are not valid repo citations and must not be copied into manuscript-facing text. Every candidate reference listed here must be independently verified before insertion into the manuscript, supplement, or any future bibliography. Public preprint status remains **Not yet**.

## Survey handling note

The survey is used only to extract reference themes, candidate paper names, likely manuscript support roles, and verification priorities. No DOI, PMID, title metadata, author list, journal, year, URL, or citation string is accepted from the survey unless it is later verified from an authoritative source.

## High-level landscape summary

The survey describes a literature progression that is useful for organizing future references:

1. Experimental and review background on blood-brain barrier peptide delivery and cell-penetrating peptides.
2. Early BBB peptide predictors and curated BBB peptide resources.
3. A dataset and predictor lineage around Brainpeps, B3Pdb, BBPpred, B3Pred, and BBPpredict.
4. Later deep-learning, structure-aware, and protein-language-model-oriented BBB peptide predictors.
5. Adjacent CPP and peptide-transport benchmark methods that may help contextualize evaluation choices.
6. Newer benchmark-hygiene work focused on k-mer, homology, leakage, and similarity-aware splitting.

## Permea positioning derived from the survey

Permea Signal ML v0.1 should not claim to be the state of the art BBB peptide predictor. It should not claim biological validation, validated delivery, or robust generalization. The defensible contribution is benchmark discipline, transparency, leakage/provenance disclosure, and a reproducible baseline evidence package.

The safest positioning is as a versioned computational evidence release: a documented, reproducible, random-stratified baseline benchmark surface with explicit caveats around provenance, label-source criteria, leakage risk, and public preprint readiness.

## Candidate reference clusters

### A. Biological BBB / peptide-delivery background

- candidate reference names from survey: BBB peptide-delivery reviews; CPP delivery reviews; barrier-permeability background sources
- why this cluster matters: supports the biological-delivery bottleneck context without turning Permea results into biological proof
- manuscript section it may support: Introduction; Discussion; Limitations
- verification status: unverified candidate cluster
- risk/caveat: background sources must not be used to imply Permea has experimentally validated BBB transport

### B. BBB peptide databases and dataset lineage

- candidate reference names from survey: Brainpeps; B3Pdb
- why this cluster matters: may establish upstream dataset/resource lineage and attribution context
- manuscript section it may support: Dataset; Methods; Data availability; Supplement
- verification status: unverified candidates
- risk/caveat: source relationship to the current processed dataset must be confirmed before citation; dataset license and redistribution status remain unresolved

### C. Early BBB peptide ML predictors

- candidate reference names from survey: BBPpred; B3Pred; BBPpredict
- why this cluster matters: may define inherited benchmark assumptions, predictor lineage, and field context
- manuscript section it may support: Related Work; Methods / Dataset lineage; Discussion
- verification status: unverified candidates
- risk/caveat: should not be used to overstate Permea as a superior predictor; verify whether these sources are predictors, datasets, or both

### D. Deep-learning / PLM / structure-aware predictors

- candidate reference names from survey: SCMB3PP; DeepB3P3; Augur; BrainPepPass; ESM-BBB-Pred; B3BPFN
- why this cluster matters: provides context for modern modeling directions and helps position Permea as baseline-oriented rather than architecture-first
- manuscript section it may support: Related Work; Discussion / Future Work
- verification status: unverified candidates
- risk/caveat: architecture-heavy comparisons should be descriptive only; Permea v0.1 should not claim performance superiority or broad generalization against these methods

### E. Adjacent CPP and peptide transport benchmarks

- candidate reference names from survey: PepBenchmark; PractiCPP; PerseuCPP
- why this cluster matters: may support broader peptide benchmark context, CPP evaluation practices, and related transport-prediction framing
- manuscript section it may support: Related Work; Discussion; Benchmark limitations
- verification status: unverified candidates
- risk/caveat: adjacent CPP benchmarks may not be BBB-specific and should not be cited as direct BBB dataset evidence unless verified

### F. Leakage / similarity-aware / benchmark hygiene

- candidate reference names from survey: k-mer leakage or similarity-aware benchmark hygiene studies; homology-aware split studies; train-test contamination studies
- why this cluster matters: supports conservative language around same-label duplicates, near-duplicates, cross-fold similarity, and possible optimism in random-stratified metrics
- manuscript section it may support: Methods; Limitations; Supplement leakage appendix
- verification status: unverified candidate cluster
- risk/caveat: cite only sources that directly support leakage, homology, similarity-aware splitting, or benchmark optimism claims

### G. Dataset documentation and reproducibility

- candidate reference names from survey: Datasheets for Datasets; model-card or dataset-card style documentation references; benchmark reproducibility references
- why this cluster matters: supports the artifact-traceability and dataset/provenance checklist framing
- manuscript section it may support: Introduction; Methods; Supplement; Data/code availability
- verification status: unverified candidates
- risk/caveat: documentation frameworks support reporting discipline, not model validity or biological conclusions

### H. Metrics and evaluation

- candidate reference names from survey: PR-AUC / imbalance reference; MCC reference
- why this cluster matters: supports class-imbalance interpretation and binary-classification metric reporting
- manuscript section it may support: Methods; Results; Limitations
- verification status: unverified candidate cluster
- risk/caveat: metric references should support evaluation interpretation only and must not be used to imply robust generalization

### I. Software citations

- candidate reference names from survey: scikit-learn; pandas; matplotlib; possible feature-calculation source such as ProtParam
- why this cluster matters: supports Methods and Code availability statements for implementation dependencies and sequence-derived feature definitions
- manuscript section it may support: Methods; Code availability; Supplement reproducibility
- verification status: unverified candidates
- risk/caveat: cite only software actually used in the repo or manuscript; verify preferred citation format from package/project guidance

## Safe Related Work structure

1. Biological background: BBB delivery bottleneck and peptide/CPP context.
2. Predictor lineage: early BBB peptide resources and predictors, followed by newer deep-learning, structure-aware, and PLM-oriented methods.
3. Benchmark inheritance problem: dataset lineage, label-source uncertainty, and provenance challenges.
4. Leakage/similarity-aware benchmark gap: duplicate, near-duplicate, homology, and k-mer/similarity-aware evaluation concerns.
5. Permea positioning: baseline evidence package, artifact traceability, and conservative leakage/provenance disclosure.

## Language boundaries

Safe language:

- benchmark-oriented baseline
- random-stratified baseline metrics
- potentially optimistic under leakage risk
- candidate prioritization before experimental validation
- model-level feature importance, not mechanism
- versioned computational evidence release
- provenance-limited benchmark surface

Forbidden language:

- state of the art predictor
- validated BBB delivery
- leakage-free benchmark
- robust generalization proven
- biological mechanism proven
- experimentally validated transport
- therapeutic or clinical efficacy

## Next action

Verify references one by one before any manuscript insertion. Create `references.bib` only after candidate metadata and claim relevance are verified. Insert citation placeholders only after verified references are mapped to specific manuscript claims.
