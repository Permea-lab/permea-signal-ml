# Cross-dataset positive overlap: B3Pred ↔ Brainpeps

*Aggregate-only result. This measures **dataset overlap** of BBB-positive peptides
across public archives. It does not measure biological transport, and it is not a
claim about any predictor's accuracy.*

## Question

Are the "positive" peptides in standard BBB benchmarks independent across datasets,
or do different benchmarks re-use the same underlying peptides?

## Datasets

| dataset | role | positives used | source |
|---|---|---|---|
| **B3Pred Dataset_3** | benchmark under audit | 269 (`label==1`); **265 unique** | standard public B3Pred surface (269 positive / 2,690 negative); processed-file hash recorded in the run manifest |
| **Brainpeps** (Van Dorpe 2012) | independent comparator archive | **137** (standard-AA, unique; primary) | official backend `brainpeps.ugent.be`, file sha256 `8ff7aad3…cc3fd`, retrieved 2026-06-28 |
| **B3Pdb** (Kumar 2021) | parent archive of B3Pred positives | not recomputed (see notes) | `webs.iiitd.edu.in/raghava/b3pdb` |

Notes:
- Per published literature, B3Pred's positives are drawn from **B3Pdb**, so the
  B3Pred↔B3Pdb relationship is reported from the source publications rather than
  recomputed here.
- At retrieval (2026-06-28) B3Pdb's documented FASTA exports returned HTTP 404; its
  browse interface was **not** scraped.
- The Brainpeps **primary** positive set is standard-amino-acid sequences only (137
  unique), for a like-for-like comparison against B3Pred's standard-AA positives. No
  sequence was transformed.

## Method

- `identity(s, t) = matched / len(shorter)` under free-gap global alignment (= LCS / shorter).
- **exact** = verbatim match after case/whitespace normalization; **near** = identity ≥ τ.
- Primary τ = 0.9. Cells are **directional**: the fraction of the **row** dataset's
  positives that also appear in the **column** dataset.
- Outputs are aggregate counts and fractions only. No sequences or per-pair mappings.

Reproduce:

```
python scripts/cross_dataset_overlap.py \
  --dataset b3pred=<b3pred_positives.csv>:sequence \
  --dataset brainpeps=<brainpeps_positives.csv>:sequence \
  --tau 0.9 --out results/cross_dataset_overlap/overlap
```

## Result (Brainpeps 137-set, τ = 0.9)

| source (row) → found in (column) | exact | near (τ = 0.9) |
|---|---|---|
| **B3Pred** (of 265) → Brainpeps | 0.279 | **0.883** |
| **Brainpeps** (of 137) → B3Pred | **0.540** | 0.825 |

**Reading.** 54.0% of Brainpeps positives appear **verbatim** in B3Pred, rising to 82.5%
as near-duplicates (identity ≥ 0.9). Conversely, 88.3% of B3Pred positives have a
near-duplicate in Brainpeps (27.9% verbatim). The two public BBB-positive archives are
largely the **same pool of peptides**, not independent datasets.

## Sensitivity (near-duplicate fractions)

| variant | Brainpeps → B3Pred | B3Pred → Brainpeps |
|---|---|---|
| τ = 0.8 (137) | 0.898 | 0.943 |
| **τ = 0.9 (137, primary)** | **0.825** | **0.883** |
| τ = 0.95 (137) | 0.825 | 0.860 |
| Brainpeps def. 230 (strip-mods core) @ τ0.9 | 0.822 | 0.925 |
| Brainpeps def. 332 (all as-is) @ τ0.9 | 0.825 | 0.883 |

- Exact overlap is flat across τ (0.540 / 0.279) by construction.
- The near-duplicate band stays **0.82–0.94** across every threshold and definition.
- The "all as-is" (332) definition reduces to the primary because modified-residue entries
  are non-amino-acid strings and cannot enter a sequence-identity comparison. The conclusion
  is robust to threshold and to the comparator's positive-set definition.

## Provenance / versioning notes

1. **B3Pdb bulk export was unavailable at retrieval (2026-06-28):** its documented FASTA
   exports return HTTP 404 on the official server.
2. **"Brainpeps" is a moving target:** the live backend returns 357 records / 332 unique
   sequences; the 2012 publication's ~259 matches no current count. Any frozen "Brainpeps
   dataset" should be pinned by retrieval date and file hash.

## Interpretation

This establishes a **shared-source precondition**: the positive universe of the standard
BBB peptide benchmark is not independent across datasets — it is largely one re-used pool.
That motivates identity-controlled evaluation: when benchmarks share most of their positives,
cross-dataset or random-split comparisons cannot be read as independent tests.

It does **not** by itself demonstrate leakage in any specific predictor, prove anything about
biological transport, or claim a new method. It is a dataset-overlap measurement.

## Limitations

- Identity convention is **LCS / shorter**, stated explicitly. The verbatim-overlap figures
  (0.540 / 0.279) are independent of the alignment convention; only the near-duplicate band
  depends on it.
- B3Pred↔B3Pdb is cited from the literature, not recomputed, because the B3Pdb bulk export
  was unavailable at retrieval.
- The Brainpeps primary set excludes modified / non-standard-AA peptides, which cannot enter
  a sequence-identity overlap regardless.
