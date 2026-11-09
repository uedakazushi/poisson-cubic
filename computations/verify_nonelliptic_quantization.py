#!/usr/bin/env python3
"""Universal QQ[h,u]-identities for the nonelliptic mixed block.

The nodal case uses only (h-2) and (h+2) as denominators. No finite-field
specialization is used. A monic Diamond-lemma proof reduces all ambiguities
to xyz; the script checks that ambiguity and all central commutators.
The Fermat companion identity is checked in a free algebra over QQ[t,s].
This does not verify properness or smoothness of a Kuznetsov category.
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import argparse
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
h, u, t, s = sp.symbols('h u t s')
Polynomial = dict[str, sp.Expr]


def clean(p: Polynomial) -> Polynomial:
    out = {}
    for w, c in p.items():
        c = sp.cancel(c)
        if c != 0:
            out[w] = c
    return out


def add(*args: Polynomial) -> Polynomial:
    d = defaultdict(lambda: sp.Integer(0))
    for p in args:
        for w, c in p.items():
            d[w] += c
    return clean(d)


def scale(p: Polynomial, a: sp.Expr) -> Polynomial:
    return clean({w: c*a for w, c in p.items()})


def mul(p: Polynomial, q: Polynomial) -> Polynomial:
    d = defaultdict(lambda: sp.Integer(0))
    for w, c in p.items():
        for v, e in q.items():
            d[w+v] += c*e
    return clean(d)


def comm(p: Polynomial, q: Polynomial) -> Polynomial:
    return add(mul(p, q), scale(mul(q, p), -1))


def serialize(p: Polynomial) -> dict[str, str]:
    return {w: str(sp.factor(c)) for w, c in sorted(p.items())}


class Block:
    def __init__(self, kind: str):
        if kind not in ('nodal', 'cuspidal'):
            raise ValueError(kind)
        self.kind = kind
        if kind == 'cuspidal':
            self.rules = {
                'yz': {'zy': sp.S.One, 'zz': h, 'x': 2*h*u},
                'xz': {'zx': sp.S.One, 'yy': -3*h},
                'xy': {'yx': sp.S.One, 'zx': 2*h, 'yy': -3*h**2},
            }
            self.omega = {
                'xx': u, 'yx': -6*h**2*u, 'yy': 12*h**4*u,
                'yyy': sp.S.One, 'zx': -6*h**3*u,
                'zyy': -3*h, 'zzx': sp.S.One,
            }
        else:
            q = (2+h)/(2-h)
            self.rules = {
                'yz': {'zy': q, 'x': 4*h*u/(2-h)},
                'xz': {'zx': 1/q, 'yy': -6*h/(2+h)},
                'xy': {'yx': q, 'zz': 6*h/(2-h)},
            }
            self.omega = {
                'x': -24*h**3*u**2/(h+2)**2,
                'xx': u*(h**2+12)/(6*(h+2)),
                'yyy': ((2-h)/(h+2))**3,
                'zy': -24*h**2*u/(h+2)**2,
                'zyx': (h**2+12)/(3*(h+2)**2),
                'zzz': sp.S.One,
            }

    @lru_cache(None)
    def normal(self, word: str) -> Polynomial:
        for i in range(len(word)-1):
            pair = word[i:i+2]
            if pair in self.rules:
                out = defaultdict(lambda: sp.Integer(0))
                for v, c in self.rules[pair].items():
                    for w, e in self.normal(word[:i]+v+word[i+2:]).items():
                        out[w] += c*e
                return clean(out)
        return {word: sp.S.One}

    def reduce(self, p: Polynomial) -> Polynomial:
        out = defaultdict(lambda: sp.Integer(0))
        for word, c in p.items():
            for w, e in self.normal(word).items():
                out[w] += c*e
        return clean(out)

    def relations(self) -> list[Polynomial]:
        if self.kind == 'cuspidal':
            return [
                {'yz': 1, 'zy': -1, 'zz': -h, 'x': -2*h*u},
                {'zx': 1, 'xz': -1, 'yy': -3*h},
                {'xy': 1, 'yx': -1, 'xz': -h, 'zx': -h},
            ]
        return [
            {'yz': 1-h/2, 'zy': -1-h/2, 'x': -2*h*u},
            {'zx': 1-h/2, 'xz': -1-h/2, 'yy': -3*h},
            {'xy': 1-h/2, 'yx': -1-h/2, 'zz': -3*h},
        ]

    def check(self) -> dict:
        # Descending active-word degree/lex order x > y > z proves termination.
        weight = {'x': 2, 'y': 1, 'z': 0}
        key = lambda w: (len(w), tuple(weight[a] for a in w))
        for bad, poly in self.rules.items():
            assert all(key(w) < key(bad) for w in poly)
        left = self.reduce({w+'z': c for w, c in self.rules['xy'].items()})
        right = self.reduce({'x'+w: c for w, c in self.rules['yz'].items()})
        assert left == right
        assert all(not self.reduce(r) for r in self.relations())
        # Cyclic-potential syzygy in the free algebra, not merely the quotient.
        assert not add(*(comm({a: sp.S.One}, r)
                         for a, r in zip('xyz', self.relations())))
        commutators = {}
        for a in 'xyz':
            p = self.reduce(mul(self.omega, {a: sp.S.One}))
            q = self.reduce(mul({a: sp.S.One}, self.omega))
            assert p == q
            commutators[a] = serialize(p)
        # Specialization at h=0 gives f_epsilon + u*x^2.
        x, y, z = sp.symbols('x y z')
        result = sum(c.subs(h, 0)*sp.prod({'x': x, 'y': y, 'z': z}[a] for a in w)
                     for w, c in self.omega.items())
        expected = (x*y*z+y**3+z**3 if self.kind == 'nodal' else x*z**2+y**3)+u*x**2
        assert sp.expand(result-expected) == 0
        # A missing quantum correction is detected without a numerical test.
        pure = {w: c.subs(u, 0) for w, c in self.omega.items()}
        naive = add(pure, {'xx': u})
        negative = {a: serialize(self.reduce(comm(naive, {a: sp.S.One}))) for a in 'xyz'}
        assert any(negative.values())
        for poly in [left, self.omega, *[self.normal(a) for a in ('xyz', 'xyzz')]]:
            for c in poly.values():
                den = sp.fraction(sp.cancel(c))[1]
                factors = sp.factor_list(den, h)[1]
                for f, _ in factors:
                    if sp.degree(f, h) > 0:
                        assert self.kind == 'nodal' and (f.subs(h, 2)==0 or f.subs(h, -2)==0)
        return {
            'ring': 'QQ[h,u]' if self.kind=='cuspidal' else 'QQ[h,u,(4-h^2)^(-1)]',
            'normal_basis': 'u^d z^a y^b x^c',
            'overlap_xyz_normal_form': serialize(left),
            'central_cubic_normal_form': serialize(self.omega),
            'equal_left_right_normal_forms': commutators,
            'negative_control_naive_central_lift': negative,
            'potential_syzygy': 'sum_i [x_i,r_i]=0 in the free algebra',
            'arithmetic': 'symbolic characteristic zero, no specialization',
        }


def fermat_identity() -> dict:
    relations = [
        {'xy': 1, 'yx': -1, 'zz': -t, '': t*s},
        {'yz': 1, 'zy': -1, 'xx': -t, '': t*s},
        {'zx': 1, 'xz': -1, 'yy': -t, '': t*s},
    ]
    terms = [
        (-3,0,'','yy'),(t**2,0,'','zx'),(-t**2,0,'x','z'),
        (-3,0,'y','y'),(-t**2,0,'z','x'),(t**2,0,'xz',''),(-3,0,'yy',''),
        (2*t**2,1,'','xx'),(-3*t,1,'','yz'),(-t**2,1,'x','x'),
        (-t**2,1,'xx',''),(3*t,1,'yz',''),
        (3,2,'','zz'),(3,2,'z','z'),(3,2,'zz',''),
        (9*s,0,'',''),(-9*s,2,'',''),
    ]
    three_center = {w: sp.Integer(3) for w in ('xxx','yyy','zzz')}
    three_center.update({w:-t**2 for w in ('xyz','xzy','yxz','yzx','zxy','zyx')})
    three_center.update({w:-9*s for w in 'xyz'})
    rhs = add(*(scale(mul(mul({pre:1},relations[i]),{post:1}),c)
                for c,i,pre,post in terms))
    assert not add(comm(three_center, {'x':1}), scale(rhs,-1))
    def cyclic(poly: Polynomial) -> Polynomial:
        return {w.translate(str.maketrans('xyz','yzx')):c for w,c in poly.items()}
    assert not add(comm(cyclic(three_center), {'y':1}), scale(cyclic(rhs),-1))
    assert not add(comm(cyclic(cyclic(three_center)), {'z':1}),scale(cyclic(cyclic(rhs)),-1))
    return {
        'ring': 'ZZ[t,s]',
        'three_center': serialize(three_center),
        'certificate_terms': [{'coefficient':str(c),'relation':i+1,'prefix':pre,'suffix':post}
                              for c,i,pre,post in terms],
        'identity': '[3C,x] = sum coefficient * prefix * r_i * suffix; cyclic x,y,z',
        'application': 't=3*mu, s=u^2/9, alpha=a+u/3,beta=b+u/3,gamma=c+u/3',
    }


def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    result={'version':'v12','date':'2026-11-09','nodal':Block('nodal').check(),
            'cuspidal':Block('cuspidal').check(),'fermat_companion':fermat_identity(),
            'scope':'Universal identities and Diamond ambiguity checks; categorical saturation not verified.'}
    path=ROOT/'computations/nonelliptic_quantization_certificate.json'
    if args.write:
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    if not path.exists():raise SystemExit('Certificate absent. Run with --write to create it.')
    if json.loads(path.read_text()) != result:raise SystemExit('Certificate mismatch')
    print('PASS: two monic Diamond systems, two overlaps, six universal central commutators, h=0 limits.')
    print('PASS: potential syzygies, denominator scopes, two negative controls, 17-term Fermat certificate.')
    print('SCOPE: exact characteristic-zero identities, not finite sampling; no assertion of residual saturation.')

if __name__=='__main__':
    main()