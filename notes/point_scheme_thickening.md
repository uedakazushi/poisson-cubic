# 混合nc cubicのpoint schemeのスキーム構造

**2026-11-11・v40。最初に00_research_plan.mdを読む。** 証明全文は`papers/reconstruction/point_scheme_thickening.tex`、単独原稿入口は`papers/point_scheme_thickening.tex`。

**定理。** lambda=1, h非零, h^6!=-27 の中心商B_hのpoint module初期点スキームは、Sklyanin曲線E_hと12個の二重点Spec C[ε]/ε²の非交和。u≠0で中心uの多重線形化が全点列を定数にするので、point functorは可換化で計算できる。u=1では(x²+y,y²+x,z²,1+v³+xy/3+h²z(1/6-2xy/3))。x,yは4 reduced solutions, vは各3単純根、z²だけ残り長さ2。Poisson零点は同じ式のh²z項を除いたもの。v'=v+h²z(1/6-2xy/3)/(3v²)で孤立厚化は明示的同型。ただし埋め込み接方向は異なる。

u=v=0のpoint列はSklyanin E_hで、shiftは非自明な平行移動。中心変数u,vの横方向の冪零は隣接点p0!=p1の2x2 minorが単元であることと中心性から消える。従ってE_hも余分な厚化なし。u=0,v!=0の点列は中心元Ωにより存在しない。h=0ではpoint schemeはX0全体なので、h=0を含むflatなpoint-scheme族を結論しない。

**平坦極限定理。** U=Spec C[h,(h^6+27)^(-1)] 上、E_h=V(u,v,x³+y³+z³+h²xyz)と、Sigma_h=V(x²+uy,y²+ux,z²,Omega_h^ab)の非交和Zを作る。Sigmaはu=0に点を持たず全体でu=1チャート。vの冪零shearでSigma≅Sigma_0×Uなので長さ24有限平坦。Eも滑らかな平面三次曲線族でflat。Zはgeneric point-schemeのschematic closureで、Z_0=D_0(pi_X0)（embedded schemeとして一致）。Hilbert多項式3t+24。B_0自身のpoint schemeはcubic X0全体であり混同しない。

**確実性。** u=1の厳密な方程式・二重点・接方向と全point schemeの証明を記載。Sklyanin point schemeとtranslationの既知定理を使用。計算証明書はh=1,2,3のGroebner商長24と多項式恒等式のみを検査し、一般のpoint functorを形式証明しない。先行研究の完全な新規性は未確認。

**今後。** 他のlambda（特にlambda=0）およびSklyanin退化値、一般のnc cubicへ適用できる条件を分析。Point schemeが復元可換cubicに全体として埋め込まれるとは言わない。
