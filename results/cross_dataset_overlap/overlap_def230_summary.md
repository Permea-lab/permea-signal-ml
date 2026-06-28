# Cross-dataset overlap audit (BBB positives)

- Identity: `matched / shorter_length` (free-gap = LCS / shorter)
- Near-duplicate threshold: tau = 0.9
- Cells = fraction of the **row** dataset's positives found in the **column** dataset.
- **Aggregate-only**: no sequences, per-pair mappings, or manifests are emitted.

## Dataset sizes

| dataset | rows | valid | invalid | unique |
| --- | --- | --- | --- | --- |
| b3pred | 269 | 269 | 0 | 265 |
| brainpeps | 230 | 230 | 0 | 230 |

## Exact overlap (verbatim)

| A \ B | b3pred | brainpeps |
| --- | --- | --- |
| **b3pred** | 1.000 | 0.358 |
| **brainpeps** | 0.413 | 1.000 |

## Near-duplicate overlap (identity >= 0.9)

| A \ B | b3pred | brainpeps |
| --- | --- | --- |
| **b3pred** | 1.000 | 0.925 |
| **brainpeps** | 0.822 | 1.000 |
