#!/usr/bin/env python3
"""Exact object-index counts for first A-infinity products; no smoothness test."""
import argparse
import json
from functools import lru_cache
from math import comb

def counts(n):
    N=n+2; a=n-1; k=n+2
    @lru_cache(None)
    def paths(start,current,length,p,target):
        if length==k:
            return int(p==(1 if target==0 else 2) and
                       (current>=start if target==0 else start-current>=a))
        ans=0
        for nxt in range(N):
            if nxt>current:
                ans+=paths(start,nxt,length+1,p,target)
            elif current-nxt>=a and p<(1 if target==0 else 2):
                ans+=paths(start,nxt,length+1,p+1,target)
        return ans
    lo=sum(paths(i,i,0,0,0) for i in range(N))
    hi=sum(paths(i,i,0,0,n) for i in range(N))
    @lru_cache(None)
    def ident(start,cur,length,p):
        if length==k:return int(cur==start and p==1)
        ans=0
        for nxt in range(N):
            if nxt>cur:ans+=ident(start,nxt,length+1,p)
            elif cur-nxt>=a and p==0:ans+=ident(start,nxt,length+1,1)
        return ans
    diagonal=sum(ident(i,i,0,0) for i in range(N))
    assert diagonal==N
    return {"n":n,"N":N,"arity":k,"output_0":lo,"output_n":hi,
            "diagonal_index_paths":diagonal,
            "planar_binary_trees":comb(2*(n+1),n+1)//(n+2)}

def obstruction_index_path():
    p=[0,1,2,3,4,0,1,2,3,4,0,1,2,3]
    inner=p[:8];outer=p[:1]+p[7:]
    assert len(p)==14 and len(inner)==len(outer)==8
    for q in (inner,outer):
        drops=sum(x-y>=4 for x,y in zip(q,q[1:]))
        assert drops==1 and all(y>x or x-y>=4 for x,y in zip(q,q[1:]))
        assert 5*drops+2-7==0
    assert len(p)-1==13 and 7+7-1==12+1
    return {"full":p,"inner":inner,"outer":outer,"bracket_coefficient":"not computed"}

def main():
    ar=argparse.ArgumentParser()
    ar.add_argument("--output")
    args=ar.parse_args()
    data=[counts(n) for n in range(3,9)]
    assert [(x["output_0"],x["output_n"]) for x in data] == [
        (185,128),(672,204),(2478,303),(9240,428),(34749,582),(131560,768)]
    c={"scope":"degree and object-index compatibility only; NOT coefficients or smoothness",
       "n5":next(v for v in data if v["n"]==5),
       "n5_double_m7_support":obstruction_index_path(),
       "by_dimension":data}
    body=json.dumps(c,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f:f.write(body)
    else:print(body,end="")
if __name__=="__main__":main()
