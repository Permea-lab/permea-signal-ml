# Test Warnings

## Logistic Regression Penalty Deprecation Warning

Running:

```bash
python -m pytest tests/test_leakage_aware_baselines.py -q
```

may emit a scikit-learn `FutureWarning` related to `LogisticRegression` penalty handling.

Example:

```text
FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10.
To avoid this warning, leave 'penalty' set to its default value and use
'l1_ratio' or 'C' instead.
```

### Source

The warning originates from scikit-learn Logistic Regression deprecation behavior and is emitted by the dependency during baseline test execution.

### Expected Impact

The warning does not indicate benchmark failure.

Current benchmark outputs are expected to remain unchanged.

No new model-performance claims, benchmark claims, scientific conclusions, biological interpretations, or clinical interpretations should be inferred from this warning.

### Maintenance Notes

Future updates to scikit-learn may require changes to Logistic Regression configuration when support for the deprecated parameter is removed.
