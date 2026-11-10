"""Absolute four-generator Koszul/curved diagonal for the genuine mixed input.
This computes a stabilized diagonal algebra, not yet residual-category Nat.
All word relations are formed before any commutative candidate is introduced.
"""
from curved_diagonal import *
import curved_diagonal as m
import time

class AbsoluteMixed(Mixed):
    ranks=[1,4,6,4,1]
    def nf(self,w):return self.anorm(tuple(a for a in w if a!=3),w.count(3))
    @staticmethod
    def fw(a):return a[0]+(3,)*a[1]
    def qbasis(self,d):
        if d<0:return []
        if d not in self.qbases:self.qbases[d]=[(self.fw(a),self.fw(b)) for i in range(d+1) for a in self.abasis(i) for b in self.abasis(d-i)]
        return self.qbases[d]
    @lru_cache(None)
    def qmonmul(self,a,b):
        out={}
        for l,lc in self.nf(b[0]+a[0]).items():
            for r,rc in self.nf(a[1]+b[1]).items():out[(self.fw(l),self.fw(r))]=lc*rc
        return out
    def qcanon(self,l,r):
        return {(self.fw(a),self.fw(b)):c*d for a,c in self.nf(l).items() for b,d in self.nf(r).items()}
    def action(self,a,c):
        out={}
        for w,v in a.items():
            for (l,r),b in c.items():out=self.add(out,self.nf(l+self.fw(w)+r),v*b)
        return out
    def omega_full(self):
        f={(3,)*u+w:c for (w,u),c in self.omega().items()};f[(3,3,3)]=m.F(1)
        return f
    def central_difference(self):
        out={}
        for w,c in self.omega_full().items():
            out=self.add(out,self.qcanon(w,()),c);out=self.add(out,self.qcanon((),w),-c)
        return out
    def dividedfull(self,f):
        out=self.zeros(4,1)
        for w,c in f.items():
            for i,a in enumerate(w):out[a][0]=self.add(out[a][0],self.qcanon(w[:i],w[i+1:]),c)
        return out
    @staticmethod
    def wi(w):
        k=0
        for a in w:k=4*k+a
        return k
    def d_mats(self):
        from itertools import combinations
        W=[sp.ones(1,1),sp.eye(4)]
        R=sp.zeros(16,6)
        for j,rel in enumerate(self.rels):
            for (w,u),c in rel.items():R[self.wi((3,)*u+w),j]=m.toexpr(c)
        for j in range(3):R[self.wi((3,j)),j+3]=1;R[self.wi((j,3)),j+3]=-1
        rows=[self.wi(w) for w in combinations(range(4),2)]
        W.append((R*R[rows,:].inv()).applyfunc(sp.cancel))
        for p in (3,4):
            L=sp.kronecker_product(sp.eye(4),W[-1]);RR=sp.kronecker_product(W[-1],sp.eye(4))
            ns=L.row_join(-RR).nullspace();inter=L*sp.Matrix.hstack(*(v[:L.cols,:] for v in ns))
            rows=[self.wi(w) for w in combinations(range(4),p)]
            inter=(inter*inter[rows,:].inv()).applyfunc(sp.cancel);W.append(inter)
        ds=[None]
        for p in range(1,5):
            M=self.zeros(self.ranks[p-1],self.ranks[p]);sub=list(combinations(range(4),p-1))
            for i,w in enumerate(sub):
                for j in range(self.ranks[p]):
                    for x in range(4):
                        cl=m.F(W[p][self.wi((x,)+w),j]);cr=m.F(W[p][self.wi(w+(x,)),j])*((-1)**p)
                        if cl:M[i][j][((x,),())]=cl
                        if cr:M[i][j][((),(x,))]=cr
            ds.append(M)
        for p in (2,3,4):assert not any(c for row in self.mmul(ds[p-1],ds[p]) for c in row)
        self.koszul=W
        return ds
    def homotopies(self):
        d=self.d_mats();f=self.central_difference();s1=[self.dividedfull(self.omega_full())]
        assert self.mmul(d[1],s1[0])==[[f]]
        for p in (1,2,3):
            rhs=self.madd(self.diag(f,self.ranks[p]),self.mmul(s1[p-1],d[p]),m.F(-1))
            s1.append(self.solve_d(d[p+1],rhs,2))
        assert self.mmul(s1[3],d[4])==[[f]]
        s2=[]
        for p in (0,1):
            rhs=[[{k:-v for k,v in c.items()} for c in row] for row in self.mmul(s1[p+1],s1[p])]
            if p:rhs=self.madd(rhs,self.mmul(s2[p-1],d[p]),m.F(-1))
            s2.append(self.solve_d(d[p+3],rhs,3))
        assert not any(c for row in self.madd(self.mmul(s1[3],s1[2]),self.mmul(s2[1],d[2])) for c in row)
        assert not any(c for row in self.madd(self.mmul(s1[3],s2[0]),self.mmul(s2[1],s1[0])) for c in row)
        return d,s1,s2
    def blocks(self,d,s1,s2):
        return [(p-1,p,0,d[p]) for p in range(1,5)]+[(p+1,p,1,s1[p]) for p in range(4)]+[(p+3,p,2,s2[p]) for p in range(2)]
    def cbasis(self,q,r):
        return [(p,i,a) for p,size in enumerate(self.ranks) if (q-p)%2==0 for i in range(size) for a in self.abasis(r+(3*q-p)//2)]
    def lifts(self,cycles,d,s1,s2):
        N=4;blocks=self.blocks(d,s1,s2);ans=[];cb=self.cbasis(0,1)
        for col in range(cycles.cols):
            f={}
            for j in range(-1,3):
                for p in range(N+1):
                    target=p+2*j
                    if target<0:continue
                    if target==0:
                        v={}
                        for k,(pp,i,a) in enumerate(cb):
                            if pp==p and cycles[k,col]:
                                v[i]=self.add(v.get(i,{}),self.qcanon(self.fw(a),()),m.F(cycles[k,col]))
                        f[j,p]=[[v.get(i,{}) for i in range(self.ranks[p])]]
                        continue
                    if target-1>N:continue
                    rhs=self.zeros(self.ranks[target-1],self.ranks[p])
                    if p and (j,p-1) in f:rhs=self.mmul(f[j,p-1],d[p])
                    for i,ss in [(1,s1),(2,s2)]:
                        mindex=p+2*(j-i)
                        if (j-i,p) in f and 0<=mindex<len(ss):rhs=self.madd(rhs,self.mmul(ss[mindex],f[j-i,p]),m.F(-1))
                        if p<len(ss) and (j-i,p+2*i-1) in f:rhs=self.madd(rhs,self.mmul(f[j-i,p+2*i-1],ss[p]))
                    if target>N:
                        assert not any(c for row in rhs for c in row),('top lifting obstruction',j,p)
                        continue
                    f[j,p]=self.solve_d(d[target],rhs,1+j)
            # Verify the complete closed endomorphism, not just the recursive equations.
            for j in range(-1,5):
                for p in range(N+1):
                    target=p+2*j-1
                    if not 0<=target<=N:continue
                    check=self.zeros(self.ranks[target],self.ranks[p])
                    if (j,p) in f and target+1<=N:check=self.mmul(d[target+1],f[j,p])
                    if p and (j,p-1) in f:check=self.madd(check,self.mmul(f[j,p-1],d[p]),m.F(-1))
                    for i,ss in [(1,s1),(2,s2)]:
                        mindex=p+2*(j-i)
                        if (j-i,p) in f and 0<=mindex<len(ss):check=self.madd(check,self.mmul(ss[mindex],f[j-i,p]))
                        if p<len(ss) and (j-i,p+2*i-1) in f:check=self.madd(check,self.mmul(f[j-i,p+2*i-1],ss[p]),m.F(-1))
                    assert not any(c for row in check for c in row),('not closed',col,j,p)
            ans.append(f)
        return ans
    def products(self,d,s1,s2):
        blocks=self.blocks(d,s1,s2);D0=self.cdiff(0,1,blocks)
        cycles=sp.Matrix.hstack(*D0.nullspace());assert cycles.cols==4
        cycles=(cycles*cycles[:4,:].inv()).applyfunc(sp.cancel)
        lifts=self.lifts(cycles,d,s1,s2)
        cb=self.cbasis(0,2);ci={k:i for i,k in enumerate(cb)};prods=[]
        for a in range(4):
            for b in range(4):
                vec=sp.zeros(len(cb),1)
                for (j,p),Fa in lifts[a].items():
                    if p+2*j!=0:continue
                    for (jj,pp),Fb in lifts[b].items():
                        if pp+2*jj!=p:continue
                        mat=self.mmul(Fa,Fb)
                        for k,c in enumerate(mat[0]):
                            for w,v in self.action({((),0):m.F(1)},c).items():vec[ci[pp,k,w]]+=m.toexpr(v)
                prods.append(vec.applyfunc(sp.cancel))
        B=self.cdiff(-1,2,blocks);D2=self.cdiff(0,2,blocks)
        assert all(all(sp.cancel(z)==0 for z in D2*p) for p in prods)
        quotient=sp.Matrix.hstack(*B.T.nullspace()).T
        assert all(all(sp.cancel(z)==0 for z in quotient*(prods[4*i+j]-prods[4*j+i])) for i in range(4) for j in range(4))
        mons=[(i,j) for i in range(4) for j in range(i,4)]
        mu=(quotient*sp.Matrix.hstack(*(prods[4*i+j] for i,j in mons))).applyfunc(sp.cancel)
        rel=mu.nullspace();return cycles,lifts,mons,rel,mu

