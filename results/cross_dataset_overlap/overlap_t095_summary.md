# Cross-dataset overlap audit (BBB positives)

- Identity: `matched / shorter_length` (free-gap = LCS / shorter)
- Near-duplicate threshold: tau = 0.95
- Cells = fraction of the **row** dataset's positives found in the **column** dataset.
- **Aggregate-only**: no sequences, per-pair mappings, or manifests are emitted.

## Dataset sizes

| dataset | rows | valid | invalid | unique |
| --- | --- | --- | --- | --- |
| b3pred | 269 | 269 | 0 | 265 |
| brainpeps | 137 | 137 | 0 | 137 |

## Exact overlap (verbatim)

| A \ B | b3pred | brainpeps |
| --- | --- | --- |
| **b3pred** | 1.000 | 0.279 |
| **brainpeps** | 0.540 | 1.000 |

## Near-duplicate overlap (identity >= 0.95)

| A \ B | b3pred | brainpeps |
| --- | --- | --- |
| **b3pred** | 1.000 | 0.860 |
| **brainpeps** | 0.825 | 1.000 |
