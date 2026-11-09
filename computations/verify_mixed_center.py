#!/usr/bin/env python3
"""Exact finite-field checks of Fermat-type cubic centrality in 15 mixed directions.

No floating arithmetic. Checks degree 4 only, not a universal proof.
"""
from itertools import product
from collections import defaultdict
from random import Random
P=1009
letters='xyzuv'
words=[''.join(w) for w in product(letters,repeat=4)]
index={w:i for i,w in enumerate(words)}
def mon(w,c=1): return {w:c%P}
def add(*polys):
    out=defaultdict(int)
    for pol in polys:
        for w,c in pol.items(): out[w]=(out[w]+c)%P
    return {w:c for w,c in out.items() if c}
def scale(pol,c): return {w:v*c%P for w,v in pol.items() if v*c%P}
def mul(a,b):
    out=defaultdict(int)
    for w,c in a.items():
        for v,d in b.items():out[w+v]=(out[w+v]+c*d)%P
    return {w:c for w,c in out.items() if c}
def power(a,n):
    ans=mon('')
    for _ in range(n):ans=mul(ans,a)
    return ans
def lin(a,b):return add(scale(mon('u'),a),scale(mon('v'),b))
def quad(a,b,c):return add(scale(mon('uu'),a),scale(mon('uv'),b),scale(mon('vv'),c))
def mixed_coefficients(params):
    return tuple(lin(*q) for q in params[:3])+tuple(quad(*q) for q in params[3:])+({},)
def row_span(rows):
    pivots={}
    for row in rows:
        r={j:c%P for j,c in row.items() if c%P}
        while r:
            k=min(r)
            if k in pivots:
                factor=r[k]
                for j,c in pivots[k].items():
                    z=(r.get(j,0)-factor*c)%P
                    if z:r[j]=z
                    elif j in r:del r[j]
            else:
                inv=pow(r[k],-1,P)
                pivots[k]={j:c*inv%P for j,c in r.items()}
                break
    return pivots
def belongs(p,pivots):
    r={index[w]:c%P for w,c in p.items() if c%P}
    while r:
        k=min(r)
        if k not in pivots:return False
        factor=r[k]
        for j,c in pivots[k].items():
            z=(r.get(j,0)-factor*c)%P
            if z:r[j]=z
            elif j in r:del r[j]
    return True
def check(h,coeff,drop_quadratic=False):
    A,B,C,D,E,H,g=coeff
    x,y,z=mon('x'),mon('y'),mon('z')
    relations=[
        add(mon('xy'),scale(mon('yx'),-1),
            scale(add(power(z,2),mul(B,y),mul(C,x),H),-h)),
        add(mon('yz'),scale(mon('zy'),-1),
            scale(add(power(x,2),mul(A,y),mul(C,z),D),-h)),
        add(mon('zx'),scale(mon('xz'),-1),
            scale(add(power(y,2),mul(A,x),mul(B,z),E),-h))]
    for c in 'uv':
        for t in letters:
            if c!=t:relations.append(add(mon(c+t),scale(mon(t+c),-1)))
    S=add(mon('xxx'),mon('yyy'),mon('zzz'))
    T=add(*(mon(w) for w in ('xyz','xzy','yxz','yzx','zxy','zyx')))
    half=pow(2,-1,P)
    sym=lambda a,b:scale(add(mul(a,b),mul(b,a)),half)
    w6=pow(6,-1,P);w9=pow(9,-1,P);w18=pow(18,-1,P)
    omega=add(scale(S,pow(3,-1,P)),scale(T,-h*h*w9),
        mul(A,add(sym(x,y),scale(power(z,2),h**4*w18))),
        mul(B,add(sym(y,z),scale(power(x,2),h**4*w18))),
        mul(C,add(sym(z,x),scale(power(y,2),h**4*w18))),
        mul(add(D,scale(power(B,2),h*h*w6) if not drop_quadratic else {},
                scale(mul(A,C),-h**4*w18)),x),
        mul(add(E,scale(power(C,2),h*h*w6) if not drop_quadratic else {},
                scale(mul(A,B),-h**4*w18)),y),
        mul(add(H,scale(power(A,2),h*h*w6) if not drop_quadratic else {},
                scale(mul(B,C),-h**4*w18)),z),g)
    rows=[]
    for relation in relations:
        for n in range(3):
            for prefix in product(letters,repeat=n):
                for suffix in product(letters,repeat=2-n):
                    a=''.join(prefix);b=''.join(suffix)
                    row={index[a+w+b]:c for w,c in relation.items() if c}
                    if row:rows.append(row)
    basis=row_span(rows)
    flags=[]
    for q in 'xyz':
        comm=add(mul(omega,mon(q)),scale(mul(mon(q),omega),-1))
        flags.append(belongs(comm,basis))
    return len(basis), flags
def main():
    rng=Random(2111)
    total=0
    for h in (0,1,2,5,13):
        for j in range(3):
            params=[tuple(rng.randrange(P) for _ in range(2)) for _ in range(3)]
            params += [tuple(rng.randrange(P) for _ in range(3)) for _ in range(3)]
            rank,flags=check(h,mixed_coefficients(params))
            assert rank==555 and all(flags),(h,j,rank,flags)
            total+=1
    print(f'PASS: {total} exact F_{P} specializations; degree-4 relation ideal rank=555')
    only_A=mixed_coefficients([(1,0),(0,0),(0,0),(0,0,0),(0,0,0),(0,0,0)])
    assert all(check(1,only_A)[1])
    assert not all(check(1,only_A,drop_quadratic=True)[1])
    print('PASS: omitting h^2 A^2 z/6 breaks centrality (negative control)')
    print('SCOPE: exact finite tests, NOT a proof of universal centrality.')
if __name__=='__main__':main()
