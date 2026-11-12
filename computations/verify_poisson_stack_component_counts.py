#!/usr/bin/env python3
"""Exact combinatorial verification for paper A's fixed/relative Poisson stacks.

For smooth Fermat cubic X_N in P^(N-1), N=n+2>=5:
  Pois(X_N)_red components = set partitions of [N] with block sizes >=3;
  [Pois(X_N)/Aut(X_N)] components = integer partitions of N into parts >=3;
  relative Poisson stack components = floor(N/3).
The equalities themselves require the paper's normal-form and orbit proofs.
This script checks only the combinatorial formulas and displayed examples.
No third-party dependencies.
"""
from functools import lru_cache
from math import comb


@lru_cache(None)
def set_partitions(N, k):
    if N == k == 0:
        return 1
    if k <= 0 or N < 3 * k:
        return 0
    return sum(comb(N - 1, b - 1) * set_partitions(N - b, k - 1)
               for b in range(3, N + 1))


@lru_cache(None)
def integer_partitions(N, minimum=3):
    if N == 0:
        return 1
    if N < minimum:
        return 0
    return sum(integer_partitions(N - b, b) for b in range(minimum, N + 1))


expected = {
    3: (1, 1, 1),
    4: (11, 2, 2),
    5: (36, 2, 2),
    6: (92, 3, 2),
    7: (491, 4, 3),
    8: (2557, 5, 3),
    9: (11353, 6, 3),
    10: (60105, 9, 4),
}

for n, triple in expected.items():
    N = n + 2
    result = (
        sum(set_partitions(N, k) for k in range(1, N // 3 + 1)),
        integer_partitions(N), N // 3
    )
    assert result == triple, (n, result, triple)
    print(f"PASS n={n}, N={N}: space={result[0]}, "
          f"fixed stack={result[1]}, relative stack={result[2]}")
print("PASS: all 8 article-A Fermat tables and rank partitions")
