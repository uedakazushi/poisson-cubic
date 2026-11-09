#!/usr/bin/env python3
"""Exact input checks, not a verification of dg smoothness or equivalence.

Checks the unique overlap and central cubic in the first nodal/cuspidal
block, and the elementary smoothness obstruction values for the special
commutative fivefolds. Arithmetic is over Q(r,u); no sampling is used.
"""
from __future__ import annotations
import argparse
import json
from functools import lru_cache
from pathlib import Path
from typing import Mapping
import sympy as sp

r, u = sp.symbols('r u')
Word = tuple[str, ...]
Polynomial = dict[Word, sp.Expr]

def clean(p: Mapping[Word, sp.Expr]) -> Polynomial:
    ans: Polynomial = {}
    for w, c in p.items():
        c = sp.cancel(c)
        if c != 0:
            ans[w] = c
    return ans

def add(*ps: Mapping[Word, sp.Expr]) -> Polynomial:
    out: Polynomial = {}
    for p in ps:
        for w, c in p.items():
            out[w] = out.get(w, sp.S.Zero) + c
    return clean(out)

def scale(p: Mapping[Word, sp.Expr], c: sp.Expr) -> Polynomial:
    return clean({w: c * a for w, a in p.items()})

def word(s: str) -> Word:
    return tuple(s)

def system(kind: str):
    if kind == 'cuspidal':
        rules = {
            word('yz'): {word('zy'): 1, word('zz'): r, word('x'): 2*r*u},
            word('xz'): {word('zx'): 1, word('yy'): -3*r},
            word('xy'): {word('yx'): 1, word('zx'): 2*r, word('yy'): -3*r**2},
        }
        center = {
            word('zzx'): 1, word('yyy'): 1, word('zyy'): -3*r,
            word('xx'): u, word('yx'): -6*r**2*u,
            word('zx'): -6*r**3*u, word('yy'): 12*r**4*u,
        }
    elif kind == 'nodal':
        q = (2+r)/(2-r)
        rules = {
            word('yz'): {word('zy'): q, word('x'): 4*r*u/(2-r)},
            word('xz'): {word('zx'): 1/q, word('yy'): -6*r/(2+r)},
            word('xy'): {word('yx'): q, word('zz'): 6*r/(2-r)},
        }
        center = {
            word('zzz'): 1,
            word('yyy'): ((2-r)/(2+r))**3,
            word('zyx'): (r**2+12)/(3*(2+r)**2),
            word('xx'): (r**2+12)*u/(6*(2+r)),
            word('zy'): -24*r**2*u/(2+r)**2,
            word('x'): -24*r**3*u**2/(2+r)**2,
        }
    else:
        raise ValueError(kind)

    @lru_cache(maxsize=None)
    def normal_word(w: Word) -> Polynomial:
        for i in range(len(w)-1):
            pair = w[i:i+2]
            if pair in rules:
                out: Polynomial = {}
                for mid, c in rules[pair].items():
                    term = normal_word(w[:i] + mid + w[i+2:])
                    for v, a in term.items():
                        out[v] = out.get(v, sp.S.Zero) + c*a
                return clean(out)
        return {w: sp.S.One}

    def normal(p: Mapping[Word, sp.Expr]) -> Polynomial:
        return add(*(scale(normal_word(w), c) for w, c in p.items()))

    def forced_first(w: Word, i: int) -> Polynomial:
        return normal({w[:i]+mid+w[i+2:]: c
                       for mid, c in rules[w[i:i+2]].items()})

    # Only ambiguity for leading words xy,xz,yz is xyz.
    overlap = add(forced_first(word('xyz'), 0),
                  scale(forced_first(word('xyz'), 1), -1))
    assert overlap == {}, (kind, 'overlap', overlap)

    commutators = {}
    for letter in 'xyz':
        right = normal({w+(letter,): c for w, c in center.items()})
        left = normal({(letter,)+w: c for w, c in center.items()})
        diff = add(right, scale(left, -1))
        assert diff == {}, (kind, letter, diff)
        commutators[letter] = 'identically zero'

    naive = {w: sp.sympify(c).subs(u, 0) for w, c in center.items()}
    naive[word('xx')] = naive.get(word('xx'), 0) + u
    naive_nonzero = []
    for letter in 'xyz':
        diff = add(normal({w+(letter,): c for w, c in naive.items()}),
                   scale(normal({(letter,)+w: c for w, c in naive.items()}), -1))
        if diff:
            naive_nonzero.append(letter)
    assert naive_nonzero, (kind, 'negative control unexpectedly central')
    return {
        'coefficient_ring': 'Q[r,u]' if kind == 'cuspidal' else 'Q[r,u,(4-r^2)^-1]',
        'overlap_xyz': 'identically zero',
        'center_commutators': commutators,
        'naive_mixed_lift_nonzero_commutators': naive_nonzero,
        'normal_word_cache_size': normal_word.cache_info().currsize,
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=None)
    args = parser.parse_args()
    out = {
        'date_jst': '2026-11-10', 'version': 'v14',
        'scope': 'Existing nonelliptic input identities only; no proof of residual smoothness, ER, or categorical equivalence.',
        'cuspidal': system('cuspidal'), 'nodal': system('nodal'),
        'special_fiber_smoothness': {
            'u_zero': 'Analytic elimination proof in research_notes.md; not inferred from finite sampling.',
            'u_one_small_branch_9_times_Fu': [27+4*j for j in range(4)],
            'u_one_nodal_nonzero_branch_9_times_Fu': [2943+4*j for j in range(4)],
        },
    }
    for vals in out['special_fiber_smoothness'].values():
        if isinstance(vals, list):
            assert all(v != 0 for v in vals)
    text = json.dumps(out, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text)

if __name__ == '__main__':
    main()
