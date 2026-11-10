#!/usr/bin/env python3
"""Certify the mixed curved diagonal over Q[h]_(h), lambda=1.

All matrices are constructed from noncommutative relations. The cubic is used
only in a final comparison. This is not a verification of categorical Nat.
A small certificate is saved by default. --full-output also saves all finite
matrices, which are exactly regenerable and need not be tracked by Git.
"""
from __future__ import annotations
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
import sympy as sp
import curved_diagonal as cd
from regular_diagonal import RegularAbsolute,residue,local_solve
from verify_curved_diagonal import c_checks,matrix_witness,scalar_matrix,rank,zero,zero_product,text


def raw_products(a,lifts):
    """Actual ordered compositions, augmented to C_2^0 (not coefficient products)."""
    cb=a.cbasis(0,2);ci={k:i for i,k in enumerate(cb)};prods=[]
    for aa in range(4):
        for b in range(4):
            vec=sp.zeros(len(cb),1)
            for (j,p),Fa in lifts[aa].items():
                if p+2*j!=0:continue
                for (jj,pp),Fb in lifts[b].items():
                    if pp+2*jj!=p:continue
                    mat=a.mmul(Fa,Fb)
                    for k,c in enumerate(mat[0]):
                        for w,v in a.action({((),0):cd.F(1)},c).items():
                            vec[ci[pp,k,w]]+=cd.toexpr(v)
            prods.append(vec.applyfunc(sp.cancel))
    return sp.Matrix.hstack(*prods)


def regular_product(a,d,s1,s2,lifts):
    """Choose six actual cross-product classes by a unit minor at h=0."""
    P=raw_products(a,lifts)
    mons=[(i,j) for i in range(4) for j in range(i,4)]
    symcols=[4*i+j for i,j in mons]
    cross=[k for k,(i,j) in enumerate(mons) if i!=j]
    blocks=a.blocks(d,s1,s2);B=a.cdiff(-1,2,blocks);d0=a.cdiff(0,2,blocks)
    assert zero_product(d0,P)
    T=B.row_join(P[:,[symcols[k] for k in cross]])
    X,proof=local_solve(T,P)
    assert proof['rank']==10 and proof['columns']==list(range(10))
    H=X[4:,:];mu=H[:,symcols]
    assert all(zero(H[:,4*i+j]-H[:,4*j+i]) for i in range(4) for j in range(4))
    assert mu[:,cross]==sp.eye(6)
    for x in mu:residue(x)
    det0=T.extract(proof['rows'],list(range(10))).applyfunc(residue).det()
    assert det0!=0
    return mu,mons,{'rows':proof['rows'],'columns':proof['columns'],'residue_determinant':str(det0)}


def check_qmat_regular(M):
    for row in M:
        for entry in row:
            for v in entry.values():residue(cd.toexpr(v))



def denominator_audit(full):
    """Exact coefficient-denominator audit; no categorical interpretation."""
    def values(obj):
        if isinstance(obj, str):
            yield obj
        elif isinstance(obj, dict):
            for val in obj.values():
                yield from values(val)
        elif isinstance(obj, list):
            for val in obj:
                yield from values(val)
    expressions=set(values(full))
    denominator=sp.Poly(1, cd.h, domain=sp.QQ)
    for value in expressions:
        expr=sp.sympify(value, locals={"h":cd.h})
        den=sp.Poly(sp.fraction(sp.cancel(expr))[1], cd.h, domain=sp.QQ)
        denominator=sp.lcm(denominator,den).monic()
    expected=(cd.h**3-1)*(cd.h**6+162)
    assert sp.expand(denominator.as_expr()-expected)==0
    return {"distinct_coefficients":len(expressions),
            "monic_lcm":str(denominator.as_expr()),
            "factorization":str(sp.factor(denominator.as_expr())),
            "scope":"Coefficients of stored finite matrices only; not a categorical smoothness discriminant."}


def run():
    a=RegularAbsolute(cd.h,1);d,s1,s2=a.homotopies()
    for M in d[1:]+s1+s2:check_qmat_regular(M)
    print('PASS: curvature identities and all homotopies regular at h=0',flush=True)
    cycles,lifts,mons,relations,rational_mu=a.products(d,s1,s2)
    for c in cycles:residue(c)
    for f in lifts:
        for M in f.values():check_qmat_regular(M)
    print('PASS: four regular closed endomorphisms and all ordered products',flush=True)
    mu,mons,minor=regular_product(a,d,s1,s2,lifts)
    checks=c_checks(a,d,s1,s2);special={}
    for r in (1,2):
        blocks=a.blocks(d,s1,s2);dm=a.cdiff(-1,r,blocks);d0=a.cdiff(0,r,blocks)
        ranks=[rank(dm.applyfunc(residue)),rank(d0.applyfunc(residue))]
        assert ranks==checks[str(r)]['ranks']
        special[str(r)]={'ranks':ranks,'H0_rank':d0.cols-sum(ranks)}
    assert [special[str(r)]['H0_rank'] for r in (1,2)]==[4,6]
    print('PASS: unit-minor product and H0 base change',flush=True)
    u,x,y,z=sp.symbols('u x y z');xs=[u,x,y,z];h=cd.h;L=1+h**6/54
    # Only here is the polynomial candidate introduced.
    G=(x**3+y**3+z**3)/3+h**2*x*y*z/3+L*u*x*y-h**4*u*z**2/18-h**2*u**2*z/12+(1+sp.Rational(29,648)*h**6+h**12/4374)*u**3
    quadrics=[(3+h**6/54)*u*u-h*h*u*z/6+x*y,
              x*x+h*h*y*z/3+L*u*y,
              y*y+h*h*x*z/3+L*u*x,
              z*z-h**4*u*z/18-(13*h*h/12+h**8/162)*u*u]
    coeff=lambda f: [sp.Poly(f,xs).coeff_monomial(xs[i]*xs[j]) for i,j in mons]
    Q=sp.Matrix.hstack(*(sp.Matrix(coeff(q)) for q in quadrics))
    grads=sp.Matrix.hstack(*(sp.Matrix(coeff(sp.diff(G,v))) for v in xs))
    assert zero(mu*Q) and zero(mu*grads) and zero(rational_mu*grads)
    assert rank(mu)==6 and rank(Q)==4 and rank(grads)==4
    assert rank(Q.applyfunc(residue))==4
    A=sp.Matrix([[L,0,0,-h**4/18],[0,1,0,0],[0,0,1,0],[h*h/3,0,0,1]])
    assert zero(grads-Q*A.T) and sp.cancel(A.det()-1-h**6/27)==0
    F0=(x**3+y**3+z**3)/3+u**3+u*x*y
    assert sp.expand(G.subs(h,0)-F0)==0
    assert zero(cycles.applyfunc(residue)-sp.eye(cycles.rows,4))
    full={'d':[matrix_witness(M) for M in d[1:]],'s1':[matrix_witness(M) for M in s1],
          's2':[matrix_witness(M) for M in s2],'cycles':scalar_matrix(cycles),
          'lifts':[{f'{j}:{p}':matrix_witness(M) for (j,p),M in sorted(f.items())} for f in lifts],
          'mu':scalar_matrix(mu),'unit_minor_choices':a.local_receipts}
    digest=hashlib.sha256(json.dumps(full,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    grouped=Counter((tuple(r['shape']),r['rank'],r['rhs'],r['coefficient_degree']) for r in a.local_receipts)
    result={'version':'nc-cubic-v27','date':'2026-11-11','base':'Q[h]_(h)','lambda':1,
      'scope':'Finite curved diagonal and its low-degree composition algebra; categorical Nat comparison NOT established.',
      'checks':{'curvature':True,'closed_lifts':True,'all_coefficients_regular_at_zero':True,
                'ordered_products_closed':True,'commutators_are_boundaries':True,
                'unit_minor_quotient':True,'same_kernel_as_v26':True,
                'specialization_is_classical_jacobian':True,'H0_commutes_with_all_Artin_base_changes':True},
      'small_complexes_generic':checks,'small_complexes_special':special,
      'degree_two_class_basis':['u*x','u*y','u*z','x*y','x*z','y*z'],
      'quadratic_monomial_order':[str(xs[i]*xs[j]) for i,j in mons],
      'product_matrix':scalar_matrix(mu),'kernel_generators':[text(q) for q in quadrics],
      'integrated_cubic':text(G),'gradient_change_determinant':text(A.det()),
      'boundary_and_class_unit_minor':minor,'number_of_local_systems':len(a.local_receipts),
      'local_system_shapes':[{'shape':list(sh),'rank':r,'rhs':s,'coefficient_degree':de,'count':count}
          for (sh,r,s,de),count in sorted(grouped.items())],
      'coefficient_denominator_audit':denominator_audit(full),
      'full_witness_sha256':digest,
      'full_witness_reproduction':'Use --full-output build/regular_diagonal_full.json; hash is canonical sorted compact UTF-8 JSON.',
      'not_established':['Identification with compact Hochschild cup products or categorical rotation products.',
                         'All-order comparison with the chosen formal commutative model.',
                         'Generic rotation-preserving categorical equivalence or relative smoothness.']}
    print('PASS: unchanged polynomial cubic and regular gradient basis',flush=True)
    return result,full


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('build/regular_diagonal_certificate.json'))
    p.add_argument('--full-output',type=Path)
    a=p.parse_args();summary,full=run();a.output.parent.mkdir(exist_ok=True,parents=True)
    a.output.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if a.full_output:
        a.full_output.parent.mkdir(exist_ok=True,parents=True)
        a.full_output.write_text(json.dumps(full,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(a.output,flush=True)
