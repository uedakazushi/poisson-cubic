#!/usr/bin/env python3
"""Exact combinatorial checks for Fermat and relative Poisson cubic component counts.
This does not verify the Poisson normal-form theorem or scheme reducedness.
"""
from functools import lru_cache
from math import comb

@lru_cache(None)
def partitions(n, k):
    if k == 0:
        return int(n == 0)
    return sum(comb(n - 1, j - 1) * partitions(n - j, k - 1)
               for j in range(3, n + 1))

def relative_dim(N, k):
    m = N - 3 * k
    ell = comb(m + 2, 3) + k * (10 + 6 * m + 3 * comb(m + 1, 2))
    return k * (3 * N - 8) + ell - N * N

expected = {5:[1],6:[1,10],7:[1,35],8:[1,91],9:[1,210,280],
            10:[1,456,2100],11:[1,957,10395],
            12:[1,1969,42735,15400]}
relative = {5:[17],6:[30,4],7:[48,16],8:[72,34],
            9:[103,59,6],10:[142,92,24],11:[190,134,51],
            12:[248,186,88,8]}
for N in range(5, 20):
    fixed = [partitions(N, k) for k in range(1, N // 3 + 1)]
    dims = [relative_dim(N, k) for k in range(1, N // 3 + 1)]
    if N in expected:
        assert fixed == expected[N], (N, fixed)
    if N in relative:
        assert dims == relative[N], (N, dims)
    assert fixed[0] == 1
    for k in range(1, N // 3):
        assert dims[k - 1] - dims[k] == 3 * (3 * k - 1) * (N - 3 * k) + 8
    print(f"n={N-2}: fixed Fermat={fixed}, total={sum(fixed)}, "
          f"relative components={N//3}, relative dimensions={dims}")
print("PASS: all exact arithmetic checks (N=5..19)")
