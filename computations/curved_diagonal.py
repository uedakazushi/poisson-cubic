"""Exact finite curved-diagonal experiment for the mixed three-generator block.
The central variable u is a BASE variable; this is not absolute nc-cubic Nat.
Only finite-dimensional quotient computations are certified by this program.
"""
from __future__ import annotations
from itertools import product, combinations_with_replacement, permutations
from functools import lru_cache
from math import comb
import sympy as sp
from sympy.polys.matrices import DomainMatrix

h = sp.Symbol("h")
FIELD = sp.QQ.frac_field(h)

def F(a=0, b=1):
    """Canonical exact element of Q(h); numerical parameters are allowed."""
    if FIELD.of_type(a):
        return a / FIELD.convert(b)
    return FIELD.from_sympy(sp.sympify(a) / sp.sympify(b))

def toexpr(x):
    return FIELD.to_sympy(x)

class Mixed:
    def __init__(self, h=F(1,2), lam=F(1)):
        self.h, self.lam = F(h), F(lam)
        self.tables, self.qbases = {}, {}
        self.rels=[{((1,2),0):F(1),((2,1),0):F(-1),((0,0),0):-self.h,((1,),1):-self.h*self.lam},
                   {((2,0),0):F(1),((0,2),0):F(-1),((1,1),0):-self.h,((0,),1):-self.h*self.lam},
                   {((0,1),0):F(1),((1,0),0):F(-1),((2,2),0):-self.h}]
    @staticmethod
    def add(a,b,scale=F(1)):
        out=a.copy()
        for k,v in b.items(): out[k]=out.get(k,F(0))+scale*v
        return {k:v for k,v in out.items() if v}
    def table(self,n):
        if n in self.tables: return self.tables[n]
        words=[(w,n-l) for l in range(n+1) for w in product(range(3),repeat=l)]
        words.sort(key=lambda x:(tuple(sorted(x[0]))==x[0],len(x[0]),x[0],x[1]))
        ix={w:i for i,w in enumerate(words)}; piv={}
        for k in range(n-1):
            act=n-k-2
            for l in range(act+1):
                for pre in product(range(3),repeat=l):
                    for post in product(range(3),repeat=act-l):
                        for rel in self.rels:
                            row={ix[(pre+w+post,u+k)]:c for (w,u),c in rel.items() if c}
                            while row:
                                p=min(row); a=row[p]
                                if p in piv:
                                    row=self.add(row,piv[p],-a)
                                else:
                                    piv[p]={j:c/a for j,c in row.items()};break
        free=[i for i in range(len(words)) if i not in piv]
        if len(free)!=comb(n+3,3): raise ValueError(('unexpected Hilbert dimension',n,len(free)))
        if not all(words[i][0]==tuple(sorted(words[i][0])) for i in free):
            raise ValueError(('sorted basis fails at this parameter',self.h,self.lam,n))
        normal={i:{words[i]:F(1)} for i in free}
        for p in sorted(piv,reverse=True):
            out={}
            for j,c in piv[p].items():
                if j!=p: out=self.add(out,normal[j],-c)
            normal[p]=out
        self.tables[n]={w:normal[i] for w,i in ix.items()}
        return self.tables[n]
    def anorm(self,w,u=0): return self.table(len(w)+u)[(w,u)]
    def abasis(self,d):
        return [] if d<0 else [(w,d-l) for l in range(d+1) for w in combinations_with_replacement(range(3),l)]
    def qbasis(self,d):
        if d<0:return []
        if d not in self.qbases:
            self.qbases[d]=[(a,b,d-i-j) for i in range(d+1) for j in range(d-i+1)
                for a in combinations_with_replacement(range(3),i)
                for b in combinations_with_replacement(range(3),j)]
        return self.qbases[d]
    @lru_cache(None)
    def qmonmul(self,a,b):
        # Q=A^op tensor_{Q[u]} A; free modules are RIGHT Q-modules.
        al,ar,au=a; bl,br,bu=b; out={}
        for (l,lu),lc in self.anorm(bl+al,au+bu).items():
            for (r,ru),rc in self.anorm(ar+br).items():
                key=(l,r,lu+ru);out[key]=out.get(key,F(0))+lc*rc
        return {k:c for k,c in out.items() if c}
    def qmul(self,a,b):
        out={}
        for x,c in a.items():
            for y,d in b.items():out=self.add(out,self.qmonmul(x,y),c*d)
        return out
    def sumq(self,items):
        out={}
        for a in items:out=self.add(out,a)
        return out
    def mmul(self,A,B):
        assert len(A[0])==len(B)
        return [[self.sumq(self.qmul(A[i][k],B[k][j]) for k in range(len(B)))
                  for j in range(len(B[0]))] for i in range(len(A))]
    def madd(self,A,B,scale=F(1)):
        return [[self.add(a,b,scale) for a,b in zip(ar,br)] for ar,br in zip(A,B)]
    @staticmethod
    def zeros(m,n):return [[{} for _ in range(n)] for _ in range(m)]
    @staticmethod
    def boundary(i):return {((i,),(),0):F(1),((),(i,),0):F(-1)}
    def divided(self,f):
        out=[{} for _ in range(3)]
        for (w,u),c in f.items():
            for i,a in enumerate(w):
                for (pre,pu),pc in self.anorm(w[:i],u).items():
                    for (suf,su),sc in self.anorm(w[i+1:]).items():
                        key=(pre,suf,pu+su)
                        out[a][key]=out[a].get(key,F(0))+c*pc*sc
        return [[{k:v for k,v in row.items() if v}] for row in out]
    def omega(self):
        h=self.h; a=self.lam
        f={((i,i,i),0):F(1,3) for i in range(3)}
        for w in permutations(range(3)):f[(w,0)]=-h*h/9
        f[((0,1),1)]=a/2;f[((1,0),1)]=a/2
        f[((2,),2)]=h*h*a*a/6;f[((2,2),1)]=h**4*a/18
        return f
    def central_difference(self):
        out={}
        for (w,u),c in self.omega().items():
            for (a,k),v in self.anorm(w,u).items():
                out=self.add(out,{(a,(),k):v*c})
                out=self.add(out,{((),a,k):-v*c})
        return out
    def d_mats(self):
        d1=[[self.boundary(i) for i in range(3)]]
        cols=[self.divided(r) for r in self.rels]
        d2=[[cols[j][i][0] for j in range(3)] for i in range(3)]
        d3=[[self.boundary(i)] for i in range(3)]
        assert not any(c for row in self.mmul(d1,d2) for c in row), 'd1 d2'
        assert not any(c for row in self.mmul(d2,d3) for c in row), 'd2 d3'
        return [None,d1,d2,d3]
    @staticmethod
    def diag(f,n):return [[f if i==j else {} for j in range(n)] for i in range(n)]
    def solve_d(self,D,R,degree):
        m,n,s=len(D),len(D[0]),len(R[0]); b=self.qbasis(degree);bt=self.qbasis(degree+1)
        ix={w:i for i,w in enumerate(bt)};entries={}
        for j in range(n):
            for l,w in enumerate(b):
                for i in range(m):
                    for z,c in self.qmul(D[i][j],{w:F(1)}).items():
                        entries[i*len(bt)+ix[z],j*len(b)+l]=toexpr(c)
        M=sp.MutableSparseMatrix(m*len(bt),n*len(b),entries);B=sp.zeros(m*len(bt),s)
        for i in range(m):
            for j in range(s):
                for z,c in R[i][j].items(): B[i*len(bt)+ix[z],j]=toexpr(c)
        rr,piv=DomainMatrix.from_Matrix(M.row_join(B)).to_field().rref();rr=rr.to_Matrix()
        if any(j>=M.cols for j in piv):raise ValueError(('inconsistent homotopy',M.shape))
        X=sp.zeros(M.cols,s)
        for i,p in enumerate(piv):
            for j in range(s):X[p,j]=rr[i,M.cols+j]
        assert all(sp.cancel(z)==0 for z in M*X-B)
        result=self.zeros(n,s)
        for i in range(n):
            for j in range(s):
                for l,w in enumerate(b):
                    if X[i*len(b)+l,j]:result[i][j][w]=F(X[i*len(b)+l,j])
        return result
    def homotopies(self):
        d=self.d_mats();f=self.central_difference();s1=[self.divided(self.omega())]
        assert self.mmul(d[1],s1[0])==[[f]],'initial nullhomotopy'
        for p in (1,2):
            rhs=self.madd(self.diag(f,3),self.mmul(s1[p-1],d[p]),F(-1))
            s1.append(self.solve_d(d[p+1],rhs,2))
        assert self.mmul(s1[2],d[3])==[[f]],'last nullhomotopy'
        rhs=[[{k:-v for k,v in c.items()} for c in row] for row in self.mmul(s1[1],s1[0])]
        s2=self.solve_d(d[3],rhs,3)
        assert not any(c for row in self.madd(self.mmul(s1[2],s1[1]),self.mmul(s2,d[1])) for c in row),'higher homotopy'
        return d,s1,s2

def _action(self, a, c):
    out={}
    for (w,u),v in a.items():
        for (l,r,k),b in c.items():out=self.add(out,self.anorm(l+w+r,u+k),v*b)
    return out

def _cbasis(self,q,r):
    result=[]
    for p,size in enumerate([1,3,3,1]):
        if (q-p)%2:continue
        deg=r+(3*q-p)//2
        for i in range(size):
            for a in self.abasis(deg):result.append((p,i,a))
    return result

def _blocks(self,d,s1,s2):
    # (target homological degree, source homological degree, t exponent, matrix)
    return [(p-1,p,0,d[p]) for p in (1,2,3)]+[(p+1,p,1,s1[p]) for p in (0,1,2)]+[(3,0,2,s2)]

def _cdiff(self,q,r,blocks):
    src=self.cbasis(q,r);dst=self.cbasis(q+1,r);ix={k:i for i,k in enumerate(dst)}
    entries={}
    sign=(-1)**(q+1)
    for j,(p,i,a) in enumerate(src):
        for target,source,t,M in blocks:
            if target!=p:continue
            for k in range(len(M[0])):
                for b,v in self.action({a:F(1)},M[i][k]).items():
                    row=ix[source,k,b];entries[row,j]=entries.get((row,j),0)+sign*toexpr(v)
    return sp.MutableSparseMatrix(len(dst),len(src),entries)

Mixed.action=_action
Mixed.cbasis=_cbasis
Mixed.blocks=_blocks
Mixed.cdiff=_cdiff

def _ebasis(self,q,r):
    out=[]
    ranks=[1,3,3,1]
    for p,np in enumerate(ranks):
        for s,ns in enumerate(ranks):
            if (q-p+s)%2:continue
            deg=r+(3*q-p+s)//2
            for i in range(ns):
                for j in range(np):
                    for w in self.qbasis(deg):out.append((s,i,p,j,w))
    return out

def _ediff(self,q,r,blocks):
    src=self.ebasis(q,r);dst=self.ebasis(q+1,r);ix={k:i for i,k in enumerate(dst)}
    entries={}
    def accumulate(k,c,j):
        row=ix[k];entries[row,j]=entries.get((row,j),F(0))+c
    for col,(s,i,p,j,w) in enumerate(src):
        for out,inp,_,M in blocks:
            if inp==s:
                for k in range(len(M)):
                    for z,c in self.qmul(M[k][i],{w:F(1)}).items():accumulate((out,k,p,j,z),c,col)
            if out==p:
                for k in range(len(M[0])):
                    for z,c in self.qmul({w:F(1)},M[j][k]).items():accumulate((s,i,inp,k,z),-((-1)**q)*c,col)
    return sp.MutableSparseMatrix(len(dst),len(src),{k:toexpr(c) for k,c in entries.items() if c})

def _augment(self,q,r):
    src=self.ebasis(q,r);dst=self.cbasis(q,r);ix={k:i for i,k in enumerate(dst)};entries={}
    for col,(s,i,p,j,(l,rr,u)) in enumerate(src):
        if s:continue
        for w,c in self.anorm(l+rr,u).items():entries[ix[p,j,w],col]=toexpr(c)
    return sp.MutableSparseMatrix(len(dst),len(src),entries)

def _linear_solve(M,B):
    rr,piv=DomainMatrix.from_Matrix(M.row_join(B)).to_field().rref();rr=rr.to_Matrix()
    if any(j>=M.cols for j in piv):raise ValueError(('inconsistent linear system',M.shape))
    X=sp.zeros(M.cols,B.cols)
    for i,p in enumerate(piv):
        for j in range(B.cols):X[p,j]=rr[i,M.cols+j]
    assert all(sp.cancel(z)==0 for z in M*X-B)
    return X

def _relative_products(self,d,s1,s2):
    blocks=self.blocks(d,s1,s2)
    D0=self.cdiff(0,1,blocks);cycles=sp.Matrix.hstack(*D0.nullspace())
    # Normalize p=0 components of the four classes as u,x,y,z.
    leading=cycles[:4,:]
    if leading.det()==0:raise ValueError('degree-one leading components do not form a basis')
    cycles=cycles*leading.inv()
    E0=self.ediff(0,1,blocks);Aug=self.augment(0,1)
    lifts=_linear_solve(E0.col_join(Aug),sp.zeros(E0.rows,4).col_join(cycles))
    eb=self.ebasis(0,1);cb=self.cbasis(0,2);ci={k:i for i,k in enumerate(cb)}
    sparse=[[(eb[k],F(lifts[k,j])) for k in range(lifts.rows) if lifts[k,j]] for j in range(4)]
    prods=[]
    for a in range(4):
        for b in range(4):
            # augmented composition lift_a after lift_b; only output s=0 remains.
            out={}
            for (s,i,p,j,w),c in sparse[a]:
                if s:continue
                for (ss,ii,pp,jj,ww),cc in sparse[b]:
                    if p!=ss or j!=ii:continue
                    for (l,rr,u),v in self.qmonmul(w,ww).items():
                        for z,zv in self.anorm(l+rr,u).items():
                            key=(pp,jj,z);out[key]=out.get(key,F(0))+c*cc*v*zv
            vec=sp.zeros(len(cb),1)
            for k,v in out.items():vec[ci[k]]=toexpr(v)
            prods.append(vec)
    D2=self.cdiff(0,2,blocks);B2=self.cdiff(-1,2,blocks)
    assert all(all(sp.cancel(z)==0 for z in D2*p) for p in prods)
    # quotient C^0 by incoming boundaries, using independent rows of a left annihilator.
    quotient=sp.Matrix.hstack(*B2.T.nullspace()).T
    assert all(all(sp.cancel(z)==0 for z in quotient*(prods[4*i+j]-prods[4*j+i])) for i in range(4) for j in range(4))
    mons=[(i,j) for i in range(4) for j in range(i,4)]
    mu=quotient*sp.Matrix.hstack(*(prods[4*i+j] for i,j in mons))
    relations=mu.nullspace()
    assert len(relations)==3
    return cycles,lifts,mons,relations,mu

Mixed.ebasis=_ebasis
Mixed.ediff=_ediff
Mixed.augment=_augment
Mixed.relative_products=_relative_products
