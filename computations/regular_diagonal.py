"""Local regular choices over Q[h]_(h) for finite curved diagonals.

Only h=0 unit minors are inverted.  A completed-base/category comparison is
not inferred by this code.  Run verify_regular_diagonal.py for certificates.
"""
from __future__ import annotations
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import curved_diagonal as cd
from absolute_diagonal import AbsoluteMixed


def residue(expr):
    """Evaluate a rational function at zero, rejecting an actual h-pole."""
    n,d=sp.fraction(sp.cancel(expr))
    dn=d.subs(cd.h,0)
    if dn==0:
        raise ValueError(f'Nonregular coefficient: {expr}')
    return sp.cancel(n.subs(cd.h,0)/dn)


def local_solve(M, B):
    """Solve M X=B by a maximal minor invertible at h=0.

    The full equation is checked exactly. If the selected columns do not
    span this right-hand side, the routine stops; it never infers a generic
    rank from the residue alone.
    """
    zero=M.applyfunc(residue)
    columns=list(DomainMatrix.from_Matrix(zero).to_field().rref()[1])
    if not columns:
        if any(B):raise ValueError('Zero residue rank is not sufficient')
        return sp.zeros(M.cols,B.cols), {'rank':0,'rows':[],'columns':[]}
    rows=list(DomainMatrix.from_Matrix(zero[:,columns].T).to_field().rref()[1])
    minor=M.extract(rows,columns)
    target=B.extract(rows,list(range(B.cols)))
    aug=DomainMatrix.from_Matrix(minor.row_join(target)).convert_to(cd.FIELD)
    rr,piv=aug.rref(); rr=rr.to_Matrix()
    if tuple(piv)!=tuple(range(len(columns))):raise ValueError('Unit-minor solve failed')
    X=sp.zeros(M.cols,B.cols)
    for i,c in enumerate(columns):
        for j in range(B.cols):X[c,j]=rr[i,len(columns)+j]
    dm=lambda a:DomainMatrix.from_Matrix(a).convert_to(cd.FIELD)
    if not (dm(M)*dm(X)-dm(B)).is_zero_matrix:raise ValueError('Full local equation inconsistent')
    # The selected residue minor is nonsingular by construction. Hence every
    # computed coefficient is regular, even before simplification.
    for x in X:residue(x)
    return X,{'rank':len(columns),'rows':rows,'columns':columns}


class RegularAbsolute(AbsoluteMixed):
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw)
        self.local_receipts=[]
        self.verbose=False
    def solve_d(self,D,R,degree):
        start=time.monotonic()
        m,n,s=len(D),len(D[0]),len(R[0]); b=self.qbasis(degree);bt=self.qbasis(degree+1)
        ix={w:i for i,w in enumerate(bt)};entries={}
        for j in range(n):
            for l,w in enumerate(b):
                for i in range(m):
                    for z,c in self.qmul(D[i][j],{w:cd.F(1)}).items():
                        entries[i*len(bt)+ix[z],j*len(b)+l]=cd.toexpr(c)
        M=sp.MutableSparseMatrix(m*len(bt),n*len(b),entries);B=sp.zeros(m*len(bt),s)
        for i in range(m):
            for j in range(s):
                for z,c in R[i][j].items():B[i*len(bt)+ix[z],j]=cd.toexpr(c)
        if self.verbose: print('LOCAL SOLVE',M.shape,'rhs',s,'degree',degree,flush=True)
        X,receipt=local_solve(M,B)
        receipt.update(shape=list(M.shape),rhs=s,coefficient_degree=degree)
        self.local_receipts.append(receipt)
        result=self.zeros(n,s)
        for i in range(n):
            for j in range(s):
                for l,w in enumerate(b):
                    if X[i*len(b)+l,j]:result[i][j][w]=cd.F(X[i*len(b)+l,j])
        if self.verbose: print('LOCAL DONE rank',receipt['rank'],'elapsed',round(time.monotonic()-start,2),flush=True)
        return result

