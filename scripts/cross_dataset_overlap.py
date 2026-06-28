#!/usr/bin/env python3
"""Cross-dataset overlap audit for BBB-positive peptides.

Quantifies how much published BBB benchmarks re-use the same POSITIVE peptides
across datasets (shared-source provenance). For each ordered pair (A, B) it
reports the fraction of A's positives that also appear in B, both verbatim
(exact) and as near-duplicates (sequence identity >= tau).

Identity convention (matches the project's private align clusterer):
    identity(a, b) = matched / shorter_length
    matched        = length of the longest common subsequence (free-gap)
So identity = LCS(a, b) / min(len(a), len(b)), and is always in [0, 1].

AGGREGATE-ONLY BY DESIGN. This tool never writes, prints, or returns row-level
sequences, per-pair sequence mappings, or split manifests. Outputs contain only
counts, fractions, and dataset-level sizes.
"""

import argparse
import csv
import os
import sys
from collections import Counter

VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")
# Extended/ambiguity codes tolerated as valid residues (still counted as valid).
EXTENDED_AA = set("BJOUXZ")
ALLOWED_AA = VALID_AA | EXTENDED_AA


# --------------------------------------------------------------------------- #
# Core sequence comparison
# --------------------------------------------------------------------------- #
def lcs_len(a, b):
    """Length of the longest common subsequence of two strings (free-gap)."""
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return 0
    # Keep the inner loop over the shorter string for memory.
    if m > n:
        a, b = b, a
        n, m = m, n
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        ai = a[i - 1]
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                left, up = cur[j - 1], prev[j]
                cur[j] = left if left >= up else up
        prev = cur
    return prev[m]


def identity(a, b):
    """Sequence identity = LCS(a, b) / shorter_length, in [0, 1]."""
    shorter = min(len(a), len(b))
    if shorter == 0:
        return 0.0
    return lcs_len(a, b) / shorter


# --------------------------------------------------------------------------- #
# Dataset loading (positives only; the caller is responsible for filtering)
# --------------------------------------------------------------------------- #
def normalize(seq):
    """Trivial normalization: strip whitespace, uppercase."""
    return "".join(seq.split()).upper()


def is_valid(seq):
    return len(seq) > 0 and all(c in ALLOWED_AA for c in seq)


def load_fasta(path):
    seqs = []
    cur = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if cur:
                    seqs.append("".join(cur))
                    cur = []
            else:
                cur.append(line)
    if cur:
        seqs.append("".join(cur))
    return seqs


def load_csv(path, column):
    seqs = []
    with open(path, newline="") as fh:
        reader = csv.DictReader(fh)
        if column not in (reader.fieldnames or []):
            raise SystemExit(
                f"[error] column '{column}' not found in {path}; "
                f"available: {reader.fieldnames}"
            )
        for row in reader:
            seqs.append(row[column])
    return seqs


def load_dataset(spec):
    """Parse a --dataset spec of the form name=path[:column].

    .fasta/.fa paths are read as FASTA. Otherwise a column must be given as
    name=path.csv:column. Returns (name, stats_dict, normalized_unique_seqs).
    """
    if "=" not in spec:
        raise SystemExit(f"[error] bad --dataset spec (need name=path): {spec!r}")
    name, rhs = spec.split("=", 1)
    name = name.strip()

    lower = rhs.lower()
    if lower.endswith(".fasta") or lower.endswith(".fa"):
        path, column = rhs, None
        raw = load_fasta(path)
    elif ":" in rhs:
        path, column = rhs.rsplit(":", 1)
        raw = load_csv(path, column)
    else:
        # CSV/TSV without a named column is ambiguous; require explicit column.
        raise SystemExit(
            f"[error] dataset {name!r}: specify a column as path:column "
            f"(or use a .fasta file). Got: {rhs!r}"
        )

    rows = len(raw)
    normed = [normalize(s) for s in raw]
    valid = [s for s in normed if is_valid(s)]
    unique = sorted(set(valid))
    stats = {
        "name": name,
        "path": path,
        "column": column,
        "rows": rows,
        "valid": len(valid),
        "invalid": rows - len(valid),
        "unique": len(unique),
    }
    return name, stats, unique


# --------------------------------------------------------------------------- #
# Overlap computation
# --------------------------------------------------------------------------- #
def pair_overlap(a_seqs, b_seqs, tau):
    """Return (exact_count, near_count) of A-sequences found in B.

    exact: A-sequence is verbatim present in B.
    near : A-sequence has identity >= tau against some B-sequence
           (exact matches are a subset of near matches).
    """
    b_set = set(b_seqs)
    exact = 0
    near = 0
    for a in a_seqs:
        if a in b_set:
            exact += 1
            near += 1
            continue
        for b in b_seqs:
            if identity(a, b) >= tau:
                near += 1
                break
    return exact, near


def build_matrices(datasets, tau):
    """datasets: ordered list of (name, unique_seqs). Returns names, exact, near.

    Cells are fractions of the ROW dataset's positives found in the COLUMN
    dataset. Diagonal is 1.0 by definition (a set fully contains itself).
    """
    names = [n for n, _ in datasets]
    seqs = {n: s for n, s in datasets}
    exact = {}
    near = {}
    for a in names:
        exact[a] = {}
        near[a] = {}
        denom = len(seqs[a]) or 1
        for b in names:
            if a == b:
                exact[a][b] = 1.0
                near[a][b] = 1.0
                continue
            ex, nr = pair_overlap(seqs[a], seqs[b], tau)
            exact[a][b] = ex / denom
            near[a][b] = nr / denom
    return names, exact, near


# --------------------------------------------------------------------------- #
# Output (aggregate-only)
# --------------------------------------------------------------------------- #
def fmt_matrix_md(names, mat):
    head = "| A \\ B | " + " | ".join(names) + " |"
    sep = "| --- | " + " | ".join("---" for _ in names) + " |"
    lines = [head, sep]
    for a in names:
        cells = " | ".join(f"{mat[a][b]:.3f}" for b in names)
        lines.append(f"| **{a}** | {cells} |")
    return "\n".join(lines)


def write_matrix_csv(path, names, mat):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["A_source\\B_target"] + names)
        for a in names:
            w.writerow([a] + [f"{mat[a][b]:.6f}" for b in names])


def write_sizes_csv(path, stats_list):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["dataset", "rows", "valid", "invalid", "unique"])
        for s in stats_list:
            w.writerow([s["name"], s["rows"], s["valid"], s["invalid"], s["unique"]])


def write_summary(path, stats_list, names, exact, near, tau):
    lines = []
    lines.append("# Cross-dataset overlap audit (BBB positives)")
    lines.append("")
    lines.append(f"- Identity: `matched / shorter_length` (free-gap = LCS / shorter)")
    lines.append(f"- Near-duplicate threshold: tau = {tau}")
    lines.append("- Cells = fraction of the **row** dataset's positives found in "
                 "the **column** dataset.")
    lines.append("- **Aggregate-only**: no sequences, per-pair mappings, or "
                 "manifests are emitted.")
    lines.append("")
    lines.append("## Dataset sizes")
    lines.append("")
    lines.append("| dataset | rows | valid | invalid | unique |")
    lines.append("| --- | --- | --- | --- | --- |")
    for s in stats_list:
        lines.append(f"| {s['name']} | {s['rows']} | {s['valid']} | "
                     f"{s['invalid']} | {s['unique']} |")
    lines.append("")
    lines.append("## Exact overlap (verbatim)")
    lines.append("")
    lines.append(fmt_matrix_md(names, exact))
    lines.append("")
    lines.append(f"## Near-duplicate overlap (identity >= {tau})")
    lines.append("")
    lines.append(fmt_matrix_md(names, near))
    lines.append("")
    with open(path, "w") as fh:
        fh.write("\n".join(lines))


def run(args):
    datasets = []
    stats_list = []
    for spec in args.dataset:
        name, stats, unique = load_dataset(spec)
        datasets.append((name, unique))
        stats_list.append(stats)
    if len(datasets) < 2:
        raise SystemExit("[error] need >= 2 datasets to compute overlap")

    names, exact, near = build_matrices(datasets, args.tau)

    out_dir = os.path.dirname(args.out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    write_sizes_csv(args.out + "_sizes.csv", stats_list)
    write_matrix_csv(args.out + "_exact_matrix.csv", names, exact)
    write_matrix_csv(args.out + "_near_matrix.csv", names, near)
    write_summary(args.out + "_summary.md", stats_list, names, exact, near, args.tau)

    print(f"[ok] wrote {args.out}_summary.md")
    print(f"[ok] wrote {args.out}_sizes.csv")
    print(f"[ok] wrote {args.out}_exact_matrix.csv")
    print(f"[ok] wrote {args.out}_near_matrix.csv")
    for s in stats_list:
        print(f"     {s['name']}: rows={s['rows']} valid={s['valid']} "
              f"unique={s['unique']}")


# --------------------------------------------------------------------------- #
# Self-test
# --------------------------------------------------------------------------- #
def selftest():
    checks = []

    def check(label, cond):
        checks.append((label, bool(cond)))

    # LCS basics
    check("lcs identical", lcs_len("ACDEFG", "ACDEFG") == 6)
    check("lcs empty", lcs_len("", "ACD") == 0)
    check("lcs subsequence", lcs_len("ACDE", "AXCXDXE") == 4)
    check("lcs classic ABCBDAB/BDCAB == 4", lcs_len("ABCBDAB", "BDCAB") == 4)
    check("lcs disjoint", lcs_len("AAAA", "CCCC") == 0)

    # identity = LCS / shorter
    check("identity identical == 1.0", identity("ACDEFG", "ACDEFG") == 1.0)
    check("identity contained == 1.0", identity("ACDE", "AXCXDXE") == 1.0)
    check("identity half", abs(identity("ACDEFG", "ACDXXX") - 0.5) < 1e-9)
    check("identity classic 4/5", abs(identity("ABCBDAB", "BDCAB") - 0.8) < 1e-9)
    check("identity symmetric",
          abs(identity("ACDEFG", "ACDXXX") - identity("ACDXXX", "ACDEFG")) < 1e-9)

    # validity / normalization
    check("normalize strips/upper", normalize(" ac de ") == "ACDE")
    check("valid standard", is_valid("ACDEFGHIKLMNPQRSTVWY"))
    check("invalid digit", not is_valid("ACD1"))
    check("invalid empty", not is_valid(""))

    # pair_overlap: A has 4 seqs; B contains 2 exact, +1 near at tau=0.8
    A = ["ACDEFG", "KLMNPQ", "ABCBDAB", "WWWWWW"]
    B = ["ACDEFG", "KLMNPQ", "BDCAB"]  # BDCAB ~ ABCBDAB at identity 0.8
    ex, nr = pair_overlap(A, B, tau=0.8)
    check("pair exact == 2", ex == 2)
    check("pair near == 3", nr == 3)
    ex2, nr2 = pair_overlap(A, B, tau=0.95)
    check("pair near tightens to 2 at tau=0.95", nr2 == 2 and ex2 == 2)

    # exact is always a subset of near
    check("exact <= near", ex <= nr)

    # matrices diagonal == 1.0
    names, exm, nem = build_matrices([("A", sorted(set(A))), ("B", sorted(set(B)))], 0.8)
    check("diag exact 1.0", exm["A"]["A"] == 1.0 and exm["B"]["B"] == 1.0)
    check("diag near 1.0", nem["A"]["A"] == 1.0 and nem["B"]["B"] == 1.0)

    passed = sum(1 for _, ok in checks if ok)
    total = len(checks)
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    print(f"\n{passed}/{total} checks passed")
    return passed == total


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true",
                   help="run internal tests and exit")
    p.add_argument("--dataset", action="append", default=[],
                   metavar="name=path[:column]",
                   help="a positives-only dataset; .fasta or path.csv:column")
    p.add_argument("--tau", type=float, default=0.9,
                   help="near-duplicate identity threshold (default 0.9)")
    p.add_argument("--out", default=None,
                   help="output path prefix (writes *_summary.md, *_*_matrix.csv, "
                        "*_sizes.csv)")
    args = p.parse_args(argv)

    if args.selftest:
        ok = selftest()
        sys.exit(0 if ok else 1)

    if not args.out:
        raise SystemExit("[error] --out is required for a real run")
    run(args)


if __name__ == "__main__":
    main()
