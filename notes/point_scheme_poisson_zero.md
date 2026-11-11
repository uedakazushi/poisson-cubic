# 混合nc cubicのpoint schemeとPoisson零点

**2026-11-11 / v38。最初に00_research_plan.mdを読む。** 論文Cの新しい証明は `papers/reconstruction/point_scheme_poisson_zero.tex`。

## セット論の結論

混合族lambda=1, h!=0, h^6!=-27でB_h=A_h/(Omega_h)。u=v=0の部分は3D Sklyanin [y,z]=hx², [z,x]=hy², [x,y]=hz²で、点列の初期点はE_h: x³+y³+z³+h²xyz=0。中心Ω|_(u=v=0)はSklyaninの中心三次元、すべての点モジュールを消す。uまたはv非零なら中心一次元との交換関係で点列は定数、そこでz=0, x²+uy=y²+ux=0, F1=0。u=1にしてx=y=0とx³=-1,y=-x²の場合に分かれ、v³=-1または-4/3、合計12点Σ。従ってpoint module初期点集合=E_h⊔Σ。

Poisson零点の台=E_0⊔Σ、E_0: sum cubes=0。u=1でcritical equationsは横断的にx,y,v方向が単純で、z²だけが残るからPoisson零点schemeのΣ部分は12点の長さ2ずつ、合計24。point schemeの12点の厚化は未確認。同じ曲線E_hは計算済み復元候補G_h+v³のu=v=0制限でも現れるが、point scheme全体がG上にあるとは主張しない。

**反例:** h=1で(1,1,-1,0,0)はE_hの点モジュールだがF1=1/3なので元の可換cubic X0の点ではない。一般hでもxyz≠0ならF1=-h²xyz/3≠0。

## 意味と次の検証

非可換point schemeとPoisson零点が一致するのではなく、零点の孤立部分は変形しても点として残り、楕円曲線部分はHesse pencilで動く。h=0のpoint schemeはX0全体で、E_hの極限との混同に注意。

次は12点のpoint schemeのscheme構造を多重線形化した三次制約込みで厳密に検査し、Sklyanin成分との非交和のscheme同定を追求する。既知3D Sklyanin点モジュール結果の仮定 h^6!=-27 を維持する。任意のnc cubicへの一般化は未証明。
