# 全Poisson構造の代数的中心三次元と一般次元量子化：現行研究ノート

**2026-11-14 / v14（論文A-v59・論文B-v59、bundle nc-cubic-v92）。再開時はまず `00_research_plan.md` を読む。**
正本はGitHub `uedakazushi/nc-cubic` の `main`。
現行公表原稿は `papers/paper_a.tex`（論文A）。
主要証明の所在：
`papers/support/papers/sections/universal_casimir_determinant.tex`
（任意のsmoothな全体三次式の代数的Casimir）、
`papers/support/papers/sections/equivariant_central_lifts.tex`
（各層の明示的な同変構成・降下とCMR公式との対応）、
`papers/support/papers/sections/intrinsic_rank_two_center.tex`
（階数二の全supportでの共変中心元、gcd(N,3)=1での全被約層への降下、補空間選択の障害）、
`papers/support/papers/sections/quantization_foundations.tex`
（PBW性・偶性・二次jet）と
`papers/support/papers/sections/algebraic_quantization.tex`
（全ブロックの主定理・正則性・平坦性）
（全Poisson構造の量子化）、
`papers/support/papers/sections/general_dimension_universal_quantization.tex`
（全次元・全k変数pencil）、
`papers/support/papers/sections/hesse_mixed_universal_center.tex`
（普遍Hesse多項式）。
詳細証明は原稿に置き、本ノートでは主要な結論・依存・障害・再現手順を整理する。

## 1. 主要結果：全ての滑らかなcubicの全Poisson構造を代数的に量子化

**定理（論文A thm:pg-quantization、thm:pg-ad-all-poisson）**：
任意のn≥3と滑らかな三次超曲面
\(X=V(F)\subset\mathbb P^{n+1}\)の任意の正則Poisson構造を考える。
正規形 \(N=n+2=3k+m\)、\(F=\sum_s f_s(x_s,u)\) を用いる。
三変数制限 \(g_s=f_s(x_s,0)\) の滑らかさは**仮定しない**。
中心三次 \(c(u)\) をブロック間に配分して、
各全体三次式 \(f_s(x_s,u)\) が滑らかな射影cubicを定めるように選べる
（lem:pg-central-splitting-smooth）。
各blockに適用したCramer行列式の比から
\( \Omega_{s,\eta_s}\in Z(A_{f_s,\eta_s})_3\)、
\(\Omega_{s,0}=f_s\) が**代数的**に得られる。
その和
\[
 \Omega_{\boldsymbol\eta}=\sum_{s=1}^k\Omega_{s,\eta_s}
\]
は厳密な中心三次元で、異なるblock間の
\(\eta_s\eta_t\)補正を必要としない。
原点近傍で各ambientはKoszul AS-regular、global dimension N、
Hilbert \((1-z)^{-N}\)。中心元は左右正則で、
商はAS-Gorenstein、injective dimension N−1、
Hilbert \((1-z^3)/(1-z)^N\)。
\(\eta_s=\lambda_s\hbar\)によって固定Fの
k次元Poisson線形族の全方向を一つの代数的族で量子化できる。
零Poisson構造は可換多項式環と中心Fで扱う。
**この固定正規形の存在証明には、外部の形式的中心元存在定理、Kontsevich formality、
Dolgushevのunimodularity判定を用いない。**
全supportでの同変選択には、既存の定階数核をh冪厚化へ持ち上げる別の議論を用いる（§2(IX)）。

**明示性の限界**：
\(g_s\)が滑らかならHesse標準形による\(\eta_s^4\)までの
短い多項式公式がある。非零の特異な\(g_s\)でも、
原点で分母が消えない\(\eta_s^2\)の**有限有理式**がある。
\(g_s=0\)ではPBW対称化した\(\operatorname{sym}(f_s)\)が全パラメータで中心となる。
全特異制限に共通する低次数の短い\(\eta_s\)-多項式を
示したわけではない。
階数二の全被約Poisson層については、gcd(N,3)=1のとき全supportにわたる代数族を構成した。
複数ブロックも含む全Poissonモジュライへの一般の同変降下は残る。
単一ブロックでは、変数分解を保つreductive群に関する同変性を
全滑らかな全体三次式で得た。三変数制限が滑らかな開と、節点・尖点の各軌道では、
中心変数によるactive座標の平行移動を含む群についても、型ごとに同変に選べる。
滑らかな制限ではgcd(m,3)=1の指標補正により、階数二のPoisson対の被約層内の開へ
代数族が降りる（§2(VI)）。節点・尖点では唯一の特異点が定める直線束で次数重みを補正でき、
mによらず、それぞれのPoisson層とh直線の積の零切断近傍へ降りる（§2(VIII)）。
零制限では全hの族があり、gcd(m,3)=1なら同じ指標法で降りる（§2(VII)）。
型をまたぐ族は§2(IX)で別に選ぶ。各層で先に選んだ式との一致や、節点・尖点型での全hへの延長は結論していない。
固定したactive・中心変数の分解では、
全滑らかな三次式の係数空間と変形直線の積の中で、
零切断全体を含む一つの開集合上に中心元を同時に選べる。
これは係数と無関係な一つのh開集合を得る主張ではない。
一変数一般点での全coherent残余圏の可換復元は論文B-v59が扱い、
有限体拡大後の同値を証明している。
全閉パラメータでのqgrの滑らかさや、可換特殊点を含む相対残余圏の比較は
この一般点の結果とは別の問題である（§7参照）。

## 2. 代数的中心元と係数空間上の選択

### (I) 滑らかな全体三次式のactive偏微分は互いに素

\(S=\mathbb C[x,y,z,u_1,\ldots,u_m]\)、
\(f\in S_3\)、\(V(f)\subset\mathbb P^{m+2}\)滑らか。
もし\(f_x,f_y,f_z\)が非定数因子\(h\)を共有すれば、
射影超曲面\(h=0\)（次元m+1）上に
残りのm個の偏微分\(f_{u_\alpha}=0\)の共通零点がある
（Krullの高さ定理、アフィン錐の次元≥2）。
そこでは全偏微分が零で、Eulerより\(f=0\)。
滑らかさと矛盾する。
ゆえに\(\gcd(f_x,f_y,f_z)=1\)（lem:pg-det-gradient-coprime）。

### (II) 三次の古典的Casimir核は常に一定次元

Jacobian bracketの次数三Casimir \(p\) は
\(d_xp\wedge d_xf=0\)なので、
分数体で\((p_x,p_y,p_z)=a(f_x,f_y,f_z)\)。
前段の互いに素性とUFD性から\(a\in S\)。
両辺の次数は二なので\(a\in\mathbb C\)。
従って
\[
 \ker\mathcal D_{f,0}=\mathbb C f\oplus\mathbb C[u]_3.
\]
\(N_3=\binom{m+5}{3}\)、\(d_m=\binom{m+2}{3}\)、
\(r_m=N_3-d_m-1\)とおくと
\(\operatorname{rank}\mathcal D_{f,0}=r_m\)が
**全ての滑らかな全体三次式fに対して成立**する
（lem:pg-det-classical-kernel）。

### (III) 普遍交換子行列の階数恒等式が特異制限に延長する

滑らかな全体三次式の係数空間
\(\mathcal T_m\subset S_3\)は既約開。
三変数制限 \(g=f(x,y,z,0)\)が滑らかな非空稠密開
\(\mathcal T_m^\circ\)では
一般Hesse中心元を**形式的存在定理なしに**
構成済み（cor:pg-smooth-ternary-explicit）。
PBWの一様開条件の下で、
Weyl基底による有理関数係数の有限行列
\[
 \mathcal D_{f,\hbar}:S_3\longrightarrow S_4^{\oplus3},
 \quad
 p\mapsto\hbar^{-1}([\operatorname{sym}(p),x],
                     [\operatorname{sym}(p),y],
                     [\operatorname{sym}(p),z])
\]
は\(\hbar=0\)で正則。
各固定\(f\in\mathcal T_m^\circ\)について、純中心三次d_m個と
Hesse中心1個が原点近傍で独立となりrank≤r_m。
各\(\hbar\)-曲線上で小行列式の恒等式を延長してからfを動かすので、
Hesse座標をfに関して代数的に同時選択する必要はない。
したがって全\((r_m+1)\)次小行列式は既約・被約な
係数空間で恒等的に零となり、
\(\mathcal T_m\)の**全ての点**に特殊化しても
rank≤r_m（lem:pg-det-universal-rank）。
これは**中心元の分母が特異制限で消えない**
と仮定した議論ではない。rankに関する**正則関数恒等式**
を先に延長している点が重要。

### (IV) Cramer表示と原点での規格化

fの全次数三の単項式のうち、少なくとも一つactive変数を含み、
係数aが非零のものをw_0とする。
純中心三次単項式とw_0を除く残りの単項式w_1,...,w_{r_m}に対する
\(\mathcal D_{f,\hbar}\)の非零\(r_m\times r_m\)
minor M(h)を選ぶ（det M(0)≠0はIIにより保証）。
w_0の列をb(h)、Mの第j列をbに置き換えた行列をM_jとすると
\[
 \boxed{
 \Omega_{f,\hbar}=f(0,0,0,u)+
 a\left[\operatorname{sym}(w_0)
       -\sum_{j=1}^{r_m}\frac{\det M_j(\hbar)}{\det M(\hbar)}
             \operatorname{sym}(w_j)\right].
 }
\]
IIIのrank≤r_mとdet M≠0から、
選んだr_m行が全行空間を張る。
従って**全交換子が厳密に零**。
IIから特殊化は正確にf。
反自己同型によって各係数は\(\hbar^2\)の有理関数。
分母は原点で非零なので\(\hbar=0\)を含むZariski開で
**代数的中心元**となる（thm:pg-universal-determinant）。

### (V) 定階数核・全係数空間・規格化の遷移

`lem:pg-det-divided-kernel` で、零切断全体を含むrank=r_mの開上に
\[
 \mathcal K=\ker\mathcal D,\qquad
 \mathcal C_m=\mathbb C[u]_3\otimes\mathcal O,\qquad
 \mathcal L=\ker(\mathcal D|_{\text{active部分}})
\]
を取り、\(\mathcal K=\mathcal C_m\oplus\mathcal L\)、rank \(\mathcal L=1\) を得る。
可逆小行列による局所分裂により、非被約な底を含む任意の底変更と両立する。
一方、通常の中心は
\[
 Z(\mathcal A_T)_3=\ker(h_T\mathcal D_T),\qquad
 Z(\mathcal A_T)_3/\mathcal K_T
 \simeq\operatorname{Ann}(h_T)\otimes\operatorname{im}\mathcal D_T
\]
であり、\(h_T=0\) では次数三全体へ増える
（`rem:pg-det-center-base-change`）。

係数環 \(B_0=\mathbb C[\boldsymbol c,\Delta^{-1}]\) で、
悪い閉集合のイデアルIと(h)は単位イデアルを生成する。
従って \(p\in I,\ p(0)=1\) を選び、
\(p(h)p(-h)=Q(h^2)\) による一つの偶principal開へ縮められる。
Weyl表示の割った交換子行列は偶なので
\[
 B=B_0[\tau,Q(\tau)^{-1}],\qquad \tau=h^2
\]
へ降りる。\(B[h]/(h^2-\tau)\) はB上忠実平坦であり、定階数条件も降りる。
BはUFDなのでPic(B)=0。Lの大域基底を選び、
法τでの \(f-f_{\mathrm{cent}}\) との単元比を \(B_0^\times\) で補正すると、
\(\Omega_{\mathrm{univ}}\bmod h=f\) を全係数で同時に課せる。
詳細は `thm:pg-det-global-coefficient-lift`。
引用は [Stacks, Tag 0BCH](https://stacks.math.columbia.edu/tag/0BCH)。
固定係数空間での商線束の非自明性は、この構成の障害ではない。

固定単項式の係数と純中心係数を指定したCramer中心元は一意で、
行のminor選択には依存しない。
単項式規格化を変えると
\[
 \Omega_j=a_{ij}\Omega_i+(1-a_{ij})f_{\mathrm{cent}}
\]
というaffine遷移となる。同じ古典極限が保証するのは
\(a_{ij}|_{h=0}=1\) であり、\(a_{ij}=1\) ではない
（`prop:pg-det-normalization-transition`）。

実例は \(f=(x^3+y^3+z^3)/3+xyz+u^3\) である。
S=x³+y³+z³、T=sym(xyz)、τ=h²とすると、
\[
 U=1+\tau/2+7\tau^2/48,\quad
 W=1-5\tau/6+7\tau^2/48,\quad U-W=4\tau/3,
\]
\[
 \Omega_x=u^3+S/3+(W/U)T,\qquad
 \Omega_T=u^3+(U/(3W))S+T
\]
で、\(\Omega_T=(U/W)\Omega_x+(1-U/W)u^3\) となる。
共通開のh≠0で二つの中心イデアルは自然なambientの同一視の下では異なる。
これは抽象的な商代数の非同型を意味しない
（`ex:pg-det-distinct-normalized-ideals`）。

座標変換 \(X=Mx+Cu,\ U=Nu\) と
\(f'=\lambda^{-1}f\circ\Phi\) に対しては
\(h'=\lambda\det(M)h\) が代数を同一視する。
K、純中心部分、商線束も共通定義開で変換と両立するが、
中心平行移動は純中心部分への射影を保たない。
中心三次直線を選ぶことは完全列
\(0\to\mathcal C_m\to\mathcal K\to\mathcal L\to0\) の分裂を選ぶことで、
選択の空間は \(\mathcal Hom(\mathcal L,\mathcal C_m)\) のaffine束となる。
全モジュライへの降下には、座標変換・中心三次配分に同変な分裂、
零切断での \(\mathbb C f\) との一致、およびcocycle条件が必要である。
単一ブロックの層別の具体的選択は次項以降に保持し、
全ての制限型と動くsupportにわたる一つの同変選択は§2(IX)で構成した。
その選択と既存の層別公式との一致、および複数ブロックの配分の変化との整合性は残る。

### (VI) 同変な中心元と中心平行移動の処理

量子交換子の係数をtと書き、
\[
G_0=(\mathrm{GL}_3\times\mathrm{GL}_m)\times\mathbb G_m,\qquad
X=Mx,\quad U=Nu,\quad
f'=\lambda^{-1}f\circ(M^{-1},N^{-1}),\quad
t'=\lambda\det(M)t
\]
とする。`thm:pg-equivariant-levi-center` は、
零切断とg=0の全パラメータ層を含むG_0不変開上に、tについて偶な中心元を選び、
\[
\Phi(\Omega_{f',t'})=\lambda^{-1}\Omega_{f,t},\qquad
\Omega_{f,0}=f,\qquad \rho(\Omega_{f,t})=f_{\mathrm{cent}}
\]
とできることを示す。g=0では次項のPBW中心元sym(f)に一致させる。
これは選択の存在であり、一意性・正準性は主張しない。

証明の要点は次の二つの平均化である。指定閉部分をZ₀=(t=0)∪(g=0)とする。
悪い閉集合のstable ideal IにはZ₀上で1となる元pが存在し、
Reynolds平均後もp∈Iとp|Z₀=1を保つ。μ₂も平均すれば偶な不変principal開が得られる。
そのaffine開ではKの切断をZ₀上のWeyl記号fへ制限する写像が全射である。
fのλ-characterを補正してReynolds平均し、純中心係数を調整する。
商線束中での零点はstable closed setなので、
Z₀を保持したまま再び不変principal開へ縮めてその像を基底にできる。
使うReynolds原理は既知であり、各元が属する有限次元表現上の
最大コンパクト部分群による平均としても説明できる。
この議論は固定係数空間のUFDによる証明とは独立の、同変性を保つ存在証明である。

三変数制限g=f(x,0)が滑らかな開では、中心平行移動も処理できる。
微分写像
\[
\delta_g:\mathbb C^3\longrightarrow\operatorname{Sym}^2(\mathbb C^3)^*,
\qquad v\longmapsto D_vg
\]
は単射である。滑らかな三変数三次式のaffine係数空間上で
この部分束のleft inverse σ_gを取り、Reynolds平均でG_0同変に選ぶ。
fの中心変数について一次の項を \(\sum_i q_i(x)u_i\) と書き、
\[
B_f=(\sigma_g(q_1),\ldots,\sigma_g(q_m)),\qquad
f^\circ(X,u)=f(X-B_fu,u)
\]
と置く。一般の \(X=Mx+Cu,\ U=Nu\) について
\[
B_{f'}=(MB_f-C)N^{-1},\qquad
X+B_{f'}U=M(x+B_fu)
\]
なので、中心を調整した式f^\circはreductive群だけで変換される。
f^\circに対する同変中心元をx+B_fuへ代入することで、
平行移動も含む全ブロック座標群Gに関する同変中心元が得られる。
定義開もこの調整写像で引き戻すのでG不変であり、零切断全体を含む。
詳細は`thm:pg-equivariant-parabolic-center`。
同じ構成は、§2(VIII)の節点・尖点の各軌道で得る正則な同変左逆にも適用する。
この段階では \(\rho\Omega=f_{\mathrm{cent}}\) の規格化は一般に保持しない。

変形変数hを固定するにはt=ηhとし、ηを
\(\eta'=\lambda\det(M)\eta\) で動かす。
すると対応する係数空間の商スタックとh直線の積の開上へ、
中心商の次数別平坦な族が降りる（`cor:pg-equivariant-central-quotient`）。
各閉ファイバーの中心元は非零で左右正則であり、
商のAS-Gorenstein性とHilbert級数は既存の中心商の議論から従う。

商スタックではスカラーを落とす位置に注意する。
\((M,N,C,\lambda)=(aI_3,aI_m,0,a^{-3})\) は係数f,ηを固定するが、
次数dの代数成分にはa^dで作用する。
従って次数付き代数の族はこの \(\mathbb G_m\) を保持する商に載る。
非零ηに制限すると、この商は階数二の被約層内の滑らかな三変数制限の開
\(\mathfrak P_{n,1}^{\mathrm{ell}}\) 上の \(\mathbb G_m\)-gerbeである
（`prop:pg-equivariant-poisson-gerbe`）。
二つのスカラーは、K_sc={(aI_V,a⁻³)} と方程式代表の自由なλ作用として区別する。Ĝ=(GL(V)×Gm,λ)/K_scには1→Gm,λ→Ĝ→PGL(V)→1があり、幾何学的点の安定化群は1→K_sc→G_(f,η)→Aut(X,π)→1となる。詳細は `eq:pg-equivariant-effective-group-sequence` と `eq:pg-equivariant-stabilizer-sequence`。商のgerbe判定は[Stacks Tag 06PD, Lemma 78.27.1](https://stacks.math.columbia.edu/tag/06PD)、同変準連接層の降下は[Tag 06WT, Proposition 96.14.3](https://stacks.math.columbia.edu/tag/06WT)を参照する。

さらにgcd(m,3)=1ならmr−3s=1となる整数を選び、
\[
\theta=(\det N)^r\lambda^s,\qquad
\rho_d^\theta=\theta^{-d}\rho_d
\]
で次数dの線形化を補正できる。
θの中心スカラーへの制限はaなので、G=K_sc×kerθとなる。
補正した代数と中心商は \(\mathfrak P_{n,1}^{\mathrm{ell}}\) とh直線の積の
零切断を含む開へ降りる（`cor:pg-equivariant-character-descent`）。
m=2、n=3ではθ=(det N)²λであり、底Poissonスタックの次元は17である。
指標による中立化と次数線形化の補正は一般的な操作であり、
本研究ではこれを同変な中心商の族に適用した。降下後の次数一束をE_θとすると古典極限はSym(E_θ)とその三次直線による商であり、相対Projは元の普遍三次超曲面族になる。中心三次直線と生成イデアルは降りるが、底スタック上に一つの大域中心生成元を選べるとは限らない（`rem:pg-equivariant-classical-family`）。

17は底の次元であり、固定したh≠0の非可換代数の同型類の像が17次元とは主張しない。
hを保つ変形族全体からは特殊ファイバーと一次括弧により元のPoisson対を回復できる。
3|mでは上の群の全指標のスカラー重みが3の倍数なので、この手段では補正できない。
それだけでgerbeが非中立である、または別の降下法が存在しないとは結論しない。
実際、節点・尖点の各層では群の指標によらない特異点直線を用いて全mで降下できる（§2(VIII)）。

階数二については、§2(IX)の別の構成で全ての制限型を含む一つの共変中心元を得た。
残るのは、この選択と各型で別に選んだ明示式との一致、全hへの延長、
3|Nの場合の別の降下、および複数ブロックでの一般の配分・相対規格化の整合性である。
g=0ではδ_g=0なので上のleft inverseは使えないが、次項のPBW対称化によって
全パラメータで別途解決する。

**同じ方法を広げる際の二つの障害。**
第一に、全中心平行移動との共変性と
\(\rho\Omega=f_{\mathrm{cent}}\) を同時に課すと、Weyl記号P_fは
\(P_f(-Cu,u)=f(-Cu,u)\) を全Cについて満たす。
u≠0でCuは任意のactive座標を動くためP_f=fとなるが、
Fermatの非自明なt²補正がこれに反する。
したがって滑らかなgを含む全G同変性の定理では純中心係数の規格化を外す必要がある。
g=0ではP_f=f自体が中心となるので、この層は上の一般的な障害には抵触しない。

第二に、δ_gが単射である全三次式の開上へ、
gだけに依存する正則なleft inverseを延ばすこと自体が不可能である。
三変数三次式の空間は10次元で、δ_gが非単射となる三次式は、
ある一方向に依存しない式である。その閉集合は
\(\mathbb P^2\)上の階数4のベクトル束からの像なので次元は高々6である。
実際 \(g=x^3+y^3\) では消去方向が一意なので一般ファイバーは零次元となり、次元は6である。
補集合Uの境界の余次元は4である。
U上の正則関数は全アフィン10次元空間へ延長する。
従ってU上のleft inverseの行列成分も全空間へ延長し、
\(\sigma_g\delta_g=I\) が多項式恒等式となるが、g=0で矛盾する。
滑らかな三次式の開では判別式の逆を許すため、この障害はない。
不可約三次式の全開だけでも同様の障害があることを§2(VIII)に記す。
これはgだけに依存する左逆についての障害である。
全fに依存する補空間選択にも別の障害があるが、中心核そのものを扱う構成は可能である。
両者の区別と証明の所在は§2(IX)に記す。

### (VII) 零制限の全パラメータ中心元とsupport平面の層

`thm:pg-equivariant-zero-center` の証明は、g=f(x,0)=0なら
f=xᵀH(u)x/2+b(u)ᵀx+c(u)と書けることを使う。
Hは対称で成分はuの一次式、bは二次式、cは三次式である。
R=C[u]上のJacobian括弧はactive変数についてaffine-linearなので、
中心記号e₀を足した自由階数4のLie代数の包絡代数をe₀−1で割ったものがAとなる。
PBW基底は全t・全係数で存在し、対称化の随伴同変性から

\[
 [x_i,\operatorname{sym}_R(p)]
 =t\operatorname{sym}_R(\{x_i,p\}_f),\qquad
 \Omega^{\mathrm z}_{f,t}=\operatorname{sym}_R(f)
\]

を得る。PBW性と中心性自体にはfの滑らかさは不要である。
滑らかさを加えると、割った交換子の三次核は全tで
K=OΩ⊕C_mとなり、中心元は全ファイバーで非零かつ左右正則になる。
全Gに対するΦΩ'=λ⁻¹ΩはWeyl対称化と中心線形代入の自然性から従う。
この層では全tの定義域・純中心係数固定・全G共変性が両立する。
一般のG_0同変族もこの元に整合させられる。
指定閉部分をZ₀=(t=0)∪(g=0)とし、そのideal J=(t)∩I_g=tI_gを用いると、
Reynolds平均による不変開をQ|Z₀=1として選べる。
Z₀上でWeyl記号fは割った交換子核のλ-characterを持つ切断であり、
その持上げと純中心補正、Z₀を保つ第二縮小により
Ω⁰|g=0=sym(f)を得る（`eq:pg-equivariant-levi-zero-compatibility`）。
補正を要しないのはWeyl記号である。順序付きPBW単項式へ書き換える際に
t依存項が現れることと混同しない。

既知の入力はPBW対称化の随伴同変性である。
[Etingof, MIT lecture notes](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf)
のCorollaries 13.7–13.8, p.75を確認した。
その原理自体の新規性は主張せず、本稿では係数環上の全t構成・全G共変性と商族への適用を記す。
全証明は本文にあり、このノートでは再開に必要な適用範囲を保持する。

**正則性と底変更の区別。** u₁,…,u_mが中心正則列なのはambient Aであり、
A/(u)=C[x₁,x₂,x₃]からKoszul AS-regular性を得る。
中心商BのAS条件はその後に正則なΩを一個割る補題から従う。
Ω mod(u)=0なので、同じu列がBでも正則だとは述べない。
係数fも動く底では次数別局所自由、固定fのC[t]上では次数別有限自由である。
Kはtで割ってから底変更した作用素の核であり、通常の中心ではない。
t=ηhの後にhで割った作用素はηDなので、η=0での核一定性は主張しない。

**幾何学的な範囲。** `prop:pg-equivariant-zero-stratum` の零制限層は
P(W_P)⊂Xで定まり、rank2の被約Poisson層内で余次元10の滑らかな既約閉部分となる。
m≤2ではP²上のm個の中心偏微分二次式に共通零点があるため空で、
m≥3では本文のΣ(u_i x_i²+u_i³)+Σ_{α>3}u_α³が滑らかな例を与える。
次元はbinom(m+5,3)−m²−3m−18である。
ここでの平面はX内にある条件であり、rank4の分離型を判定する
ambient Hessian軌跡内の平面とは別の条件である。

S_m^z=T_m^z×Gm,ηとすると[S_m^z/Gbar]がこのPoisson層を表し、
[S_m^z/G]は中央Gm-gerbeである。
全hの代数族は後者に載り、gcd(m,3)=1なら既存のθで次数線形化を補正して
Poisson層と全A¹_hの積へ降りる。m=3ではgerbe上の全h族までを得る。
全hでのAS-Gorenstein性は示すが、全閉パラメータのqgr滑らかさはこの結論に含まない。

`computations/verify_zero_restriction_center.py --json` はQQ上で
Hの独立6係数、bの3係数、c、tを保持する普遍検算である。
monic規則の唯一の重なりzyx、三つの中心交換子、独立中心並進の三つの関係式とΩ共変性を確認する。
任意mへの適用は中央係数への代入による。一般線形変換・AS条件・滑らかさ・降下の証明は本文にあり、
この計算だけから結論していない。

### (VIII) 非零特異制限：軌道ごとの中心調整と降下

**節点・尖点軌道上の左逆。**
L=GL(W)×Gm,λは三次式にg′=λ⁻¹g∘M⁻¹で作用する。
二次式側の表現はρ₂(M,λ)q=λ⁻¹q∘M⁻¹、方向Wの表現はv↦Mvである。
この二つの表現を区別するとδ_gの同変性は
δ_{g′}(Mv)=ρ₂(M,λ)δ_g(v)となる。
`lem:pg-equivariant-singular-retractions` で扱う標準形と左逆は次の通りである。
係数抽出を[x²]q等と書く。

| 型 | 標準形g | σ_g(q) |
| --- | --- | --- |
| 節点 | x³+y³+xyz | ([x²]q/3, [y²]q/3, [xy]q) |
| 尖点 | y²z−x³ | (−[x²]q/3, [yz]q/2, [y²]q) |

節点のδ像は〈3x²+yz, 3y²+xz, xy〉である。
ζ³=1としてR_ζ=diag(ζ,ζ⁻¹,1)、Sをx,yの交換とすると、
方程式scale込みの全安定化群は
H_nd={(aR,a⁻³):a∈Gm, R∈〈R_ζ,S〉}≅Gm×S₃である。
唯一の特異点[0:0:1]と二つの接線を保つことから、行列はx,yの対角または交換型となり、
三次式の係数比較でzへのshearは消える。上のσの核〈xz,yz,z²〉はこの群に安定である。
尖点でも唯一の特異点と二重接線を保つ行列を係数比較すると、
H_cu={(diag(a,d,a³d⁻²),a⁻³)}≅Gm²を得る。
δ像は〈−3x²,2yz,y²〉で、σの核〈xy,xz,z²〉が安定である。
従って両型でσ_gδ_g=id_Wが成り立ち、σ_gは全安定化群に同変である。

軌道O=L·g_*上では、標準形におけるσ_*を

\[
 \sigma_{(M,\lambda)g_*}
 =M\sigma_*\rho_2(M,\lambda)^{-1}
\]

で移送する。右辺は安定化群の右作用に不変なので、O≅L/H上の正則な写像へ降りる。
これは軌道ごとの構成であり、軌道全体に同時に座標変換Mを選ぶ必要はない。
商と軌道移送の既知入力は
[Milne, *Algebraic Groups*, CUP 2022, 著者PDF](https://www.jmilne.org/math/Books/iAG2022.pdf)
のPropositions 7.12, 7.17, pp.142–143である。
軌道のaffine性を別途使わなくても、この商の普遍性で正則性を示せる。

**全G中心元と定義域。**
全fが滑らかでg=f(x,0)がO_ndまたはO_cuに属する係数層を、それぞれT_m^nd、T_m^cuとする。
上のσを§2(VI)のB_fへ用いれば、同じ変換則B_{f′}=(MB_f−C)N⁻¹が成立する。
拡張した `thm:pg-equivariant-parabolic-center` は各層で、
零切断全体を含むG不変principal開D(Q(f° ,t))と全G共変な中心元を与える。
ここでf°は中心調整した全三次式であり、線形座標変換で得るので滑らかさを保つ。
Q(f°,0)=1で、開は各係数層とt直線の積の中で取る。
中心元の偶性・古典極限・商線束の生成性も元のG₀選択から引き継ぐ。
g=0の場合と違い、全tを定義域とする結論は得ていない。
割った交換子の核と通常の中心の違い、任意底変更に関する注意は従来通りである。

**特異点直線による全mの降下。**
ここでモジュライの主張は本稿の範囲m≥2、n=m+1で述べ、mの合同条件を課さない。
`prop:pg-equivariant-singular-strata` は、S_m^τ=T_m^τ×Gm,η（τ=nd,cu）の商
[S_m^τ/Gbar]を、support平面への三次式の制限が当該型となる階数二の被約Poisson層と同定する。
[S_m^τ/G]はその上の中央Gm-gerbeである。ここでsupport平面はX内に含まれるのではなく、
Xとの平面切断が節点または尖点を持つ。
両層は滑らかで既約であり、階数二の被約層内の余次元はそれぞれc_nd=1、c_cu=2である。
D=binom(m+5,3)とすると底スタックの次元はD−m²−3m−8−c_τで、
n=3、m=2では節点型16、尖点型15となる。
これは固定h≠0での非可換同型類の像の次元ではない。

各gの唯一の特異点が定めるtautological直線をℓ_g⊂Wとする。
その点は座標変換でM倍されるが、代数のpullbackと揃えた直線束の降下データはM⁻¹である。
従って中心スカラー(aI₃,aI_m,0,a⁻³)はℓにa⁻¹、代数の次数d部分にa^dで作用する。
この符号のもとで

\[
 \mathcal A_d^{\mathrm{desc}}=\mathcal A_d\otimes\ell^{\otimes d},
 \qquad
 \mathcal B_d^{\mathrm{desc}}=\mathcal B_d\otimes\ell^{\otimes d}
\]

は重み零となり、積・中心イデアルを保ってPoisson層へ降りる。
重み+1の双対直線L=ℓ∨を使うなら同じ補正はA_d⊗L⁻ᵈである。
中心三次直線もℓ³で補正する。全次数を整合して補正するので、実際の次数付き代数と中心商の降下である。
またL=ℓ∨のframeを加えたスタックは底とfppf局所的に同型になり、gerbe自体も中立となる。
この議論はmの合同条件を使わない。滑らかな制限や零制限で用いた群指標θとは別の中立化である。

重み零の準連接層の降下は
[Bergh–Schnürer, *Decompositions of derived categories of gerbes and of families of Brauer–Severi varieties*](https://doi.org/10.4171/DM/846),
Doc. Math. 26 (2021), 1465–1500、Proposition 4.10, p.1487
（[刊行PDF](https://ems.press/content/serial-article-files/26626?nt=1)）の既知結果を用いる。
重み±1の直線からのgerbe中立化はframeを用いる本文の直接証明であり、同命題の主張として引用しない。
軌道降下・重み零降下自体の新規性は主張しない。本稿での中心元・係数族・商モジュライへの
包括的な適用の初出は未確定である。

t=ηhを代入した族の定義域は各Poisson層とA¹_hの積の零切断近傍である。
型をまたぐ中心元の一致、全hへの延長、全閉ファイバーのqgr滑らかさは別問題である。
下降した三次直線の大域生成元を底上で選べるとも主張しない。

**不可約三次式全域での貼合せ障害。**
`rem:pg-equivariant-stratumwise-centering` の障害は、各軌道でσが存在することと両立する。
不可約ternary cubicの全開U_irr⊂A¹⁰の補集合は、線形形式と二次形式の積の錐である。
その射影化はP²×P⁵の積写像の像で次元7、従って錐の次元は8、余次元は2となる。
正規なA¹⁰から余次元二以上を除いても大域正則関数は変わらない。
もしU_irr上に正則なσ_gがあれば、その行列成分は全A¹⁰へ延長し、
σ_gδ_g=id_Wも多項式恒等式になる。g=0ではδ_0=0なので矛盾する。
この不存在は同変性を仮定しなくても成立する。
したがって滑らか・節点・尖点の各層のσを、不可約三次式全域の単一のσへ貼ることはできない。
この議論自体はgだけに依存する左逆を排除する。
全fに依存するBの障害は§2(IX)で別に証明しており、中心直線の存在定理とは両立する。

**一つの軌道にも残る非分裂：接線とconic。**
g=x²z−xy²ではδ_g=(2xz−y²,−2xy,x²)は単射だが、全安定化群に同変な左逆はない。
安定化群にM_s=diag(s,1,s⁻¹)、λ⁻¹=sと、
M_a:(x,y,z)↦(x,y+ax,z+2ay+a²x)、λ=1が含まれる。
二次式の表現ρ₂の重みは、(x²,xy,xz,y²,yz,z²)の順に
(s⁻¹,1,s,s,s²,s³)、Wの重みは(s,1,s⁻¹)なので、σ(yz)=σ(z²)=0を強制する。
逆代入から得る無限小作用はD_op=−x∂_y−2y∂_zであり、

\[
 D_{\mathrm{op}}(yz)=-(xz+2y^2),\qquad
 D_{\mathrm{op}}(xz+2y^2)=-6xy.
\]

同変性によりσ(xz+2y²)=0、続いてσ(xy)=0となり、σδ_g(e_y)=e_yに矛盾する。
これはδに基づくcenteringの、この固定軌道における障害である。
全G共変なquantum中心元そのものが存在しないとは結論しない。
中心核を直接扱う§2(IX)の方法により、全supportでの共変な中心元の存在は得られる。

**他の分解型で使える直接の左逆。**
triangle g=xyzの安定化群はmonomial行列M=diag(a,b,c)Pとλ=(abc)⁻¹からなり、
Gm³⋊S₃である。conicと横断する直線のg=z(xy+z²)では、
M=diag(a,b,c)またはそのx,y交換との積、ab=c²、λ=c⁻³で、Gm²⋊C₂となる。
前者のδ像は〈yz,xz,xy〉、後者は〈yz,xz,xy+3z²〉であり、いずれも
σ(q)=([yz]q,[xz]q,[xy]q)が同変な左逆となる。
補空間〈x²,y²,z²〉が全安定化群に安定であることが直接の理由である。
同じ軌道移送を適用できるが、現行本文の節点・尖点層のモジュライ命題には追加していない。

**独立検算の範囲。**
`python3 computations/verify_singular_orbit_centering.py --json`
（出力を保存する場合は`--output build/verify_singular_orbit_centering.json`）は、
節点・尖点の独立混合係数、σδ=id、指定安定化群に関する共変性、独立並進を含むB_fの変換則と
中心調整式の恒等式、および接線とconicの左逆条件とLie同変性の不整合を厳密係数で検算する。
実行状態は `validation_paper_a.json` を正本とする。
任意GL変換に関する軌道降下、安定化群の完全分類、quantum中心性・AS条件・モジュライ降下は
この有限計算の検証範囲ではなく、本文の証明と区別する。

**CMRの既知の節点中心公式との具体的対応。**
`rem:pg-cmr-nodal-comparison` はChekhov–Mazzocco–Rubtsovの
*Quantised Painlevé monodromy manifolds, Sklyanin and Calabi–Yau algebras*、
Adv. Math. 376 (2021), 107442、
[DOI 10.1016/j.aim.2020.107442](https://doi.org/10.1016/j.aim.2020.107442)を引用する。
実際に本文を照合した版は[accepted arXiv:1905.02772v2](https://arxiv.org/pdf/1905.02772v2)であり、
式(4.38), p.21、Lemma 4.6・式(4.39), p.22、Table 5, p.41を用いる。
刊行書誌の確認と刊行レイアウトの本文照合を混同しない。

節点の標準形では別の安定化群同変左逆
\(\widetilde\sigma(q)=([yz]q,[xz]q,[xy]q)\)も使える。
\(B=\widetilde\sigma(q)\) として \(f^\circ(X)=f(X-B)\) と置くと、
二次項は \((q_{xx}-3q_{yz})X^2+(q_{yy}-3q_{xz})Y^2+q_{zz}Z^2\) となる。
一次項・定数項も同じ三次式全体の並進で変換する。
従って
\[
 f^\circ=x^3+y^3+xyz+A_1x^2+A_2y^2+A_3z^2
              +\ell_1x+\ell_2y+\ell_3z+\kappa
\]
に対し、\(p=1+t/2,\ s=1-t/2\) として
\[
 q_{\mathrm{CMR}}=p/s,\quad \alpha=\beta=3t/s,\quad\gamma=0,\qquad
 (a_1,b_1,c_1)=-2t(A_1,A_2,A_3)/s,\quad
 (a_2,b_2,c_2)=-t(\ell_1,\ell_2,\ell_3)/s
\]
を代入すれば、CMRの関係式は本稿の対称Jacobian関係式に一致する。
CMRの中心元を \(\Omega_{\mathrm{CMR}}\) とすると、
\[
 Q=s^5\Omega_{\mathrm{CMR}}/(6t)+\kappa,\qquad
 Q^{\mathrm{sw}}-Q=-6A_3\ell_3t^3,\qquad
 \widehat Q=Q-3A_3\ell_3t^3
\]
となる。\(t\) で割る前の全係数は \(t\) で割り切れ、\(Q\) は全係数と \(t\) の多項式で、
\(Q\bmod t=f^\circ\) である。swはx,yと対応する係数を交換し、tを−tへ送る操作である。
最後の純中心補正により、この交換を含む全安定化群への共変性が得られる。
一般の二次項へは \(\widehat Q_{f^\circ,t}(x+B)\) で戻る。

`python3 computations/verify_cmr_nodal_center.py --json` は本改訂の新しい厳密実行でPASSした。
出力は `build/verify_cmr_nodal_center.json` で、一般の独立QQ係数のまま、唯一の語重なりzyx、
三中心交換子、関係式の対応、古典極限、上の交換差と純中心補正、スカラー・μ₃重みを確認した。
検算の定義開は \(sp\ne0\) であり、多項式表示だけから \(t=\pm2\) のPBW性・平坦性は結論しない。
Weyl表示での偶性、安定化群の完全分類、軌道上の正則移送、モジュライ降下はこの計算の対象外である。
節点型の中心元の存在・基準座標での公式は既知として扱い、
本稿の係数・規格化・同変族への適用と区別する。

### (IX) 階数二の全supportにわたる共変な中心元

詳細証明は `intrinsic_rank_two_center.tex` の `thm:pg-intrinsic-rank-two-center` と
`lem:pg-rank-two-bott-vanishing`、降下は `cor:pg-intrinsic-rank-two-descent` に置く。
全三次式Fは滑らか、N>=5、Pは非零分解可能とする。三変数制限の型には条件を課さない。
全supportを動かす底S=T_smooth×C₃^×では、古典核は自然に K₀=OF⊕Sym³Q*、Q=V/W_P と分裂する。

Gr(3,N)上でO(j)とSym³Q*⊗O(j)のH¹は全整数jについて消える。
後者のBott列は (j+N−1,j+N−2,j+N−3,N−1,N−5,…,0) である。
j=0,1,2では重複、j>=3ではH⁰のみ、j<0で重複がなければ第4項が最初の三項を越え、
非零コホモロジーの次数は少なくとも3となる。非零Plücker錐からGrへのGm-torsorの
押出しは全twistの直和なので、H¹(S,K₀)=0を得る。

局所Cramer核は全零h切断の近傍で定階数のベクトル束であり、
各h冪厚化には 0→K₀→K_(r+1)→K_r→0 がある。
H¹の消滅からFを整合する大域形式中心元へ持ち上げられる。
Stiefel開St_(N,3)→C₃^×はSL3-torsorで、補集合の余次元N−2>=2より
Γ(C₃^×,O)=C[Mat_(N,3)]^(SL3) となる。
従って A_N=Γ(T_smooth,O)⊗C[Mat_(N,3)]^(SL3) はHilbert有限生成によりNoetherianであり、
形式中心元の各Weyl係数はA_Nに属する。Plücker錐の射影正規性を追加の入力としない。

次数三・四の有限表示行列はh=0で共通の可換関係式行列となる。
generic PBWから上位小行列式は恒等的に零であり、古典時に独立な関係式列とWeyl列の
固定行列式で、全h=0を含む有限次数Weyl開を取れる。
そのgood locus内の不変principal開D(q)、q|_(h=0)=1を取り、R=A_N[h,q⁻¹]上の
割った交換子を有限行列M、有限核をK=ker Mとする。
Noetherian完備化の完全性から Khat=ker Mhat、Khat/hKhat≅K/hK であり、
形式中心元の剰余類の代表をKから選べば Ω mod h=F を保つ代数解を得る。
K/hKから自由加群のmod hへの写像が単射であるとは仮定しない。
**形式級数全体とその代数解の一致を主張しているのではない。**
P=0での核の階数跳躍はこの有限加群の議論を妨げないが、最終的な族はP≠0で述べる。

H_N=GL(V)×Gm,λの作用は F′=λ⁻¹F∘L⁻¹、P′=λ(Λ³L)P、h′=hである。
引戻しdatumをλでtwistした有理H_N加群KのReynolds平均により
Φ(Ω′)=λ⁻¹Ωを得て、反対代数の対合による平均でWeyl係数をhについて偶にする。
平均化にはKの局所自由性を使わない。
全次数のPBW/AS開とK/Cへの像が非零となる開へ制限すると、
全零h切断を保ったまま K=C⊕OΩ、左右正則な中心元、次数別局所自由な商族を得る。
有限次数のWeyl開だけから全次数PBWを結論するわけではない。

K_sc={(cI,c⁻³)}は(F,P)を固定し、代数の次数dに重みdで作用する。
[S/(H_N/K_sc)]は全階数二の被約Poisson層、[S/H_N]はその上の中央Gm-gerbeである。
gcd(N,3)=1ならNr−3s=1を満たすθ=(det L)^rλ^sを選び、次数dをθ⁻ᵈでtwistする。
H_N=K_sc×kerθとなるためgerbeは中立で、中心三次直線・イデアル・商を含む
実際の次数付き代数族が全被約階数二Poisson層×A¹_hの零切断近傍へ降りる。
N=5ではθ=(det L)²λ³、底の次元17であり、全非零Poisson対を含む。
中心直線の大域生成元、固定h≠0の同型類像の次元は結論しない。
零Poisson構造と変形のh=0切断を区別する。3|Nの別の降下、全hへの延長、
既存層別公式との一致は残る。特にg=0の全h公式sym(F)は、別の強い範囲を持つ選択として保持する。

**補空間を選ぶ方法の限界。** `prop:pg-equivariant-global-centering-obstruction` はm=N−3>=1で、
全f・非零Poisson係数η・hへの依存を許しても、B'=(MB−C)N⁻¹を全零h切断近傍で満たす
正則Bが存在しないことを示す。固定smooth FをStiefel開へ引き戻すと、
このBから正則行列R(A)でR(A)A=I₃が得られ、その成分の全行列空間への延長はA=0で矛盾する。
またU=Hom(Z,W)はsmooth fのアフィン係数空間に自由に作用する。
自由性はgradient正則列の一次係数syzygyの消滅から、任意の底変更後にも従う。
Y=[T_m/U]は代数空間、T_m→YはU-torsorである。
仮にこのtorsorが自明なら、その切断に対応するβのLevi平均はUのaffine変換則を保ち、
全GのBを与えて上記障害に反する。従ってtorsorは非自明である。
Yがアフィンなら加法群torsorのH¹が消えて自明になるので、Yは非アフィンである。
自由商をアフィンとみなして平均化する経路は利用できない。
中心核を直接持ち上げる構成と、補空間選択の非存在は両立する。

指定古典剰余を持つ形式中心元の存在と、相対的・還元群に対応したformalityは既知である。
本稿で区別すべき追加内容は、動く全supportと全smooth Fの係数空間における
同時の**代数的**選択、その全H_N共変性、および上記の被約層への代数族の降下である。
EG Proposition 8.1.1(i)との比較、BWB・不変式・完備化・自由商の確認した一次資料は§7にまとめる。
包括的な初出の確認は未完了である。

## 3. 複数ブロックの中心三次：配分と直線の選択

**全ブロックが零制限の場合の配分独立性。** 固定した正規形で全てのg_s=0なら、
各ブロックの中心元をsym(f_s)と取れるため、独立パラメータのまま
Σ_s sym(f_s)=sym(F)が中心となる。異なるactiveブロックは可換なので、
上の一ブロックの恒等式を各交換子へ適用すればよい。
純中心三次の配分を変えても和は不変であり、この限定した表示での配分の問題は生じない。
任意のブロック分解の変更・全Poissonモジュライへの降下までをこの観察から結論しない。

正規形を
\(F=\sum_s\widetilde f_s(x_s,u)+c(u)\)とし、
純中心三次\(c(u)\)を\(c_1+\cdots+c_k\)へ配分する。
各\(f_s=\widetilde f_s+c_s\)の滑らかさは、
u=0ではXの滑らかさから保証される。
u≠0では\(\mathbb C[u]_3\)は基点自由である。
\(\langle\widetilde f_s,\mathbb C[u]_3\rangle\)の射影線形系に
Bertiniを適用し、\(\widetilde f_s\)の係数が非零のchartでその係数を1に
規格化すると、一般のc_sでf_sが滑らかになる。
k≥2の配分空間は
\(\{(c_s):\sum c_s=c\}\simeq(\mathbb C[u]_3)^{k-1}\)
という既約なアフィン空間で、
各c_sへの射影は全射だから、
k個の滑らかさ条件を同時に満たせる。
k=1ではf_1=Fが既に滑らか。m=0では各純active f_sが
Fの滑らかさから滑らか。
\(\partial_{x_s}c_s=0\)だからPoisson構造は不変。
これは**全Poisson構造**へ一ブロック定理を適用する鍵となる。

### 中心三次束とその底

固定した分解

\[
V=\bigoplus_{s=1}^kW_s\oplus U,\qquad \dim W_s=3,\quad \dim U=m,
\qquad N=3k+m
\]

を使う。各ブロックの三次式を \(f_s(x_s,u)\)、全体を \(F=\sum_sf_s\) とする。係数空間では各 \(V(f_s)\subset\mathbf P(W_s\oplus U)\) と \(V(F)\subset\mathbf P(V)\) の滑らかさを課す。純中心三次の配分もこの表示データに含める。非零Poisson係数 \(\nu_s\in\mathbf G_m\) と共通の変形変数 \(h\) を用い、各ブロックの量子化パラメータを \(t_s=\nu_sh\) とする。

この係数空間と \(h\) 直線の積内で、以下を満たす零切断全体の開近傍 \(S\) を取る。

- 各ブロックの斉次三変数代数はKoszul AS-regular domainであり、中心変数上の相対PBW性が成立する。
- 全体の代数 \(\mathcal A=\bigotimes_{\mathcal O_S[u]}\mathcal A_s\) の次数三・四のWeyl写像が同型である。
- 各ブロックの割った交換子の次数三核 \(\mathcal K_s\) は階数 \(d_m+1\)、\(d_m=\dim\mathbf C[u]_3=\binom{m+2}{3}\) である。

これらは本文の有限rank条件で与えられる。固定した座標分解を保つ座標群について不変な条件なので、不変な開として取れる。任意に選んだCramer分母のprincipal開の不変性を仮定する必要はない。

各 \(\mathcal K_s\) は同じ純中心部分 \(\mathcal C=\mathbf C[u]_3\otimes\mathcal O_S\) を含む。これらを \(\mathcal A_3\) 内で足し合わせ、

\[
\mathcal E=\sum_s\mathcal K_s\subset\mathcal A_3,
\qquad
0\longrightarrow\mathcal C\longrightarrow\mathcal E
\longrightarrow\bigoplus_s\mathcal L_s\longrightarrow0,
\qquad \mathcal L_s=\mathcal K_s/\mathcal C
\]

とする。\(\mathcal E\) は階数 \(d_m+k\) の部分束である。固定した座標では純中心項への射影を使い、\(\mathcal E\simeq\mathcal C\oplus\bigoplus_s\mathcal L_s\) と書ける。異なるactiveブロックのWeyl単項式の支持が異なるため、これは \(\mathcal A_3\) 内でも直和である。全座標群に対して自然なのは上の完全列であり、固定した射影による分裂ではない。

必要なら開をさらに縮め、\(\mathcal E\) を全生成元との割った交換子の核そのものにできる。実際、古典次数三のCasimirは

\[
\ker D_0=\mathbf C[u]_3\oplus\bigoplus_s\mathbf C f_s.
\]

これを示すには、各 \(s\) について \(d_{x_s}p\wedge d_{x_s}f_s=0\) を使う。active偏微分のgcdが1なので比例係数は全変数の多項式であり、全次数を比較すると定数となる。従って \(p-\sum_sc_sf_s\) は純中心三次式である。量子側にはすでに階数 \(d_m+k\) の部分束 \(\mathcal E\) が核として入るので、全体の交換子行列が古典階数を持つ開集合上では等号となる。この開集合も零切断全体を含む。以後 \(\mathcal E\) の形成は非被約な底も含めて任意の底変更と両立する。

### 中心直線を追加した普遍商

直線を表す規約で

\[
p:Y=\mathbf P_{\mathrm{lin},S}(\mathcal E)
 =\operatorname{Proj}_S\operatorname{Sym}(\mathcal E^\vee)\longrightarrow S
\]

とおく。tautological部分束 \(\mathcal N=\mathcal O_Y(-1)\hookrightarrow p^*\mathcal E\subset p^*\mathcal A_3\) を使い、

\[
\mathcal B_Y=p^*\mathcal A/(\mathcal N)
\]

を定める。ここで \((\mathcal N)\) は直線の局所生成元が生成する両側イデアルであり、生成元を単元倍しても変わらない。\(\mathcal N\) は中心に入る。

**\(Y\) の全幾何学的ファイバーで、\(\mathcal N\) の非零生成元は左右正則である。** この構成では無限個の次数の単射条件を開条件として同時に課す必要がない。

証明：一つの幾何学的ファイバーの代数閉体を \(\kappa\) とし、\(0\ne\gamma\in E\) を取る。純中心式だけなら \(\kappa[u]\) 上のPBW自由性から左右正則である。そうでなければ、\(\gamma\) が正のactive次数を持つ一つのブロック \(s\) を選ぶ。そのブロックだけのactive次数でfilterすると、\(\gamma\) の最高記号は

\[
0\ne a_s\in S_{s,t_s}\otimes_\kappa\kappa[u]
\]

に属する。他ブロックの成分と純中心項はこのfiltrationの次数零である。\(S_{s,t_s}\) はdomainなので、その中心多項式拡大における \(a_s\) の左右乗法は単射である。残りのブロックのテンソル積は \(\kappa[u]\) 上自由なので、それとテンソルしても単射が保たれる。最高次数の比較によって元の \(\gamma\) の左右正則性を得る。非可換domainのテンソル積がdomainであるとは仮定していない。

従って各内部次数で

\[
0\longrightarrow\mathcal N\otimes p^*\mathcal A_{d-3}
\longrightarrow p^*\mathcal A_d
\longrightarrow(\mathcal B_Y)_d\longrightarrow0
\]

はベクトル束の局所的に分裂する完全列となる。全ファイバーで単射な有限階数行列には最大小行列式が可逆な近傍があるためである。よって \((\mathcal B_Y)_d\) は有限局所自由であり、商の形成は任意の底変更と両立する。全ファイバーで

\[
\operatorname{Hilb}_{B}(z)=\frac{1-z^3}{(1-z)^N},\qquad
\operatorname{injdim}B=N-1,\qquad
\text{AS parameter}=N-3
\]

となる。ambientのKoszul AS-regular性は既存のPBW・中心一次拡大の議論、商のAS-Gorenstein性は `lem:pg-central-cubic` による。ここからqgrの滑らかさや相対残余圏のsmooth proper性までは結論しない。

### 古典切断と忘却射のファイバー

\(S_0=V(h)\subset S\) 上では

\[
\mathcal E_0=\mathbf C[u]_3\otimes\mathcal O_{S_0}
             +\sum_s\mathcal O_{S_0}f_s.
\]

元の方程式 \(F=\sum_sf_s\) は自然な切断

\[
\sigma_0:S_0\longrightarrow Y_0,\qquad (f_s,\nu_s)\longmapsto[F]
\]

を与え、この切断に沿う \(\mathcal B_Y\) の制限は \(\operatorname{Sym}(V^*)/(F)\) である。**\(h=0\) の全 \(Y_0\) 上で元の \(F\) に戻るわけではない。** 他の直線は一般に \(c(u)+\sum_sa_sf_s\) という別の方程式を定める。元のPoisson対の量子化族を得るには、\(\sigma_0\) を延長する中心直線の族へ普遍商を引き戻す必要がある。その切断の同変な存在・正準性は、普遍商の構成と別問題である。

\(\mathcal E\to\mathcal L_s\) の全てへの射影が零でない直線の開部分を \(Y^\times\subset Y\) とすると、その忘却射の幾何学的二ファイバーは

\[
\mathbf A^{d_m}\times(\mathbf G_m)^{k-1}.
\]

局所的に各 \(\mathcal L_s\) の基底を選び、第一成分を1にすれば、残る \(k-1\) 個の非零係数と \(d_m\) 個の純中心係数が座標となる。従って \(Y^\times\to S\) は滑らかなアフィン射である。基底を選ばない大域記述は、\(\bigoplus_s\mathcal L_s\) 内の全射影非零の射影束の開部分と、その上の \(\mathcal Hom(\mathcal N,\mathcal C)\) のaffine束による。

ここで二ファイバーとは、忘れた表示データへの同型も固定したファイバーである。残余gerbe上でさらに自己同型群により割る非枠付きファイバーとは区別する。

### 中心変数がない場合の相対規格化

\(m=0\) なら \(\mathcal C=0\) で、各 \(\mathcal K_s\) は正準な中心三次直線である。しかし総中心直線の選択は

\[
\mathbf P_{\mathrm{lin}}\left(\bigoplus_s\mathcal K_s\right)
\]

に値を取り、\(k\ge2\) なら一点にはならない。全ブロック成分が非零の部分は \((\mathbf G_m)^{k-1}\)-torsorである。各ブロックの直線だけを保持しても、総和に使う相対同一視は定まらない。

偶な局所基底 \(\Omega_s\bmod h=f_s\) を選んだとき、\(\Omega_s\mapsto a_s\Omega_s\)、\(a_s\in\mathcal O_S^\times\)、\(a_s\equiv1\pmod h\) という変更は各ブロックの中心イデアルを保つ。しかし総和の直線を保つためには、全ての \(a_s\) が共通でなければならない。例えば二ブロックでは

\[
\Omega=\Omega_1+\Omega_2,\qquad
\Omega'=(1+h^2)\Omega_1+\Omega_2
\]

が同じ古典極限と偶性を持つ。\(h\ne0\)、\(1+h^2\ne0\) の開では、自然なambientの同一視の下で生成する中心イデアルは異なる。次数三部分を比較すれば、共通倍数は第二成分から1であり、第一成分から矛盾する。この例は中心商の抽象的な非同型や、同変な選択そのものの不存在を主張しない。

\(m=0\) での \(Y_0^\times\) は、\(Y_0\) のうち滑らかな古典超曲面を定める部分と一致する。実際、全係数が非零なら各 \(f_s\) の滑らかさから \(\sum_sa_sf_s\) は滑らかであり、いずれかが零ならそのブロックの射影空間に特異点を持つ。\(m>0\) では、全active成分の非零性だけでは古典超曲面の滑らかさは保証しない。必要なら \(Y_0\) 上で判別式非零の開を取り、その補集合を \(Y\) から除けば、\(\sigma_0(S_0)\) を含み全ての古典超曲面が滑らかな開が得られる。

\(k=1,m=0\) では \(\mathbf P_{\mathrm{lin}}(\mathcal K_1)=S\) であり、中心商は基底の選択なしに定まる。ただしこの場合 \(n=N-2=1\) なので、論文Aの \(n\ge3\) の定理の内部の特別例ではなく、三生成元代数側の補助的な場合である。\(k=1,m\ge2\) では、直線選択の開 \(\mathbf P(\mathcal K_1)\setminus\mathbf P(\mathcal C)\) は相対次元 \(d_m\) のaffine束となる。

### 表示を保持した商スタックへの降下

各ブロックの座標変換、共通中心変数の変換、中心変数によるactive座標の平行移動、ブロックの置換、および方程式の共通スカラーを保つ表示群を用いる。順序を固定した部分では

\[
X_s=M_sx_s+C_su,\qquad U=Nu,\qquad
f_s'=\lambda^{-1}f_s\circ\Phi^{-1},\qquad
\nu_s'=\lambda\det(M_s)\nu_s,
\]

とし、\(h\) は固定する。この群は選択した表示データの係数空間に作用し、上記のgood openも不変に取れる。\(\mathcal E\)、その射影束、tautological部分束 \(\mathcal N\) は同変である。従って普遍商は

\[
[Y/G]\longrightarrow[S/G]
\]

上の次数付き代数の族として自然に降下する。忘却射は階数 \(d_m+k\) のベクトル束の射影化であり、表現可能な滑らかな射影射である。\(Y^\times\) への制限は表現可能な滑らかなアフィン射となる。必要なのは同変なtautological直線であって、\(\mathcal E\) の同変な基底や \(\sigma_0\) の同変な延長ではない。

この商はブロック分解・純中心三次の配分を表示データとして保持する。これらを全て忘れたPoissonモジュライとの同値を、この構成だけから結論しない。

さらに、共通座標スカラー

\[
M_s=aI_3,\quad N=aI_m,\quad C_s=0,\quad\lambda=a^{-3}
\]

は \((f_s,\nu_s,h)\) と \(Y\) に自明に作用するが、\(\mathcal A_d\) と \(\mathcal B_d\) に \(a^d\)、tautological中心直線に \(a^3\) で作用する。従って元の線形化のままの次数付き代数は、この中心 \(\mathbf G_m\) を保持するgerbeに載る。中心イデアルの同変性だけでは次数重みは消えない。

ただし \(\gcd(m,3)=1\) なら \(mr-3s=1\) を満たす整数を選び、\(\theta=(\det N)^r\lambda^s\) とおくと、\(\theta\) はこの中心 \(\mathbf G_m\) 上で恒等指標になる。各次数 \(d\) の線形化を \(\theta^{-d}\) でtwistすれば中心作用が消え、積と中心イデアルを保ったまま \([Y/(G/\mathbf G_m)]\) へ代数が降りる。この指標はブロックの置換に対しても不変である。\(G\simeq\mathbf G_m\times\ker\theta\) なので、gerbeもこの選択により中立になる。これは単一ブロックの `cor:pg-equivariant-character-descent` と同じ証明である。\(3\mid m\) ではこの群の指標のスカラー重みは全て3の倍数なので同じ指標手段は使えないが、gerbeの非中立性や別の降下法の不存在は結論しない。特に中心変数のない満階数層 \(m=0\) はこの後者の場合に含まれる。

### 元の古典方程式を固定する族の補助底

\(Y^\times\) の普遍商と古典切断 \(\sigma_0\) だけで、元の方程式を持つ量子化族は「\(\sigma_0\) を延長する直線の族への引戻し」と記述できる。これを一つの追加パラメータ空間にしたい場合には、\(Y^\times\) を \(\sigma_0(S_0)\) に沿ってblow upし、\(\sigma_0(S_0)\) の定義イデアルの引戻しが \((h)\) で生成されるchartを取るdilatationが使える。

局所的に \(\ell_s\bmod h=f_s-f_{s,\mathrm{cent}}\) となる \(\mathcal L_s\) の基底を選び、第一active成分を1に規格化する。このとき直線は

\[
\ell_1+\sum_{s=2}^ka_s\ell_s+c(u)
\]

で表され、古典切断への一致条件は \(a_s\equiv1\pmod h\)、\(c\equiv F_{\mathrm{cent}}\pmod h\) である。dilatationの局所座標は

\[
a_s=1+hr_s,\qquad c=F_{\mathrm{cent}}+h c',
\]

であり、\(1+hr_s\) を可逆にする。この空間は底上滑らかで、\(h\ne0\) では \(Y^\times\)、\(h=0\) では相対次元 \(d_m+k-1\) のaffine束となる。その普遍中心商は全ての特殊ファイバーで元の \(F\) に戻る。

ただし、このdilatationが「特殊化した直線が \([F]\) となる」というfunctorそのものを表すのは、試験底で \(h\) が非零因子の場合である。\(h\)-torsionを持つ試験底では割った係数 \(r_s,c'\) は一意でなく、追加データを記録する。特殊ファイバーのaffine方向も直線 \([F]\) 自体の自由度ではなく、持上げの第一係数を記録している。偶な係数を扱う場合には、核が \(\tau=h^2\) へ降りる底で同じ構成を \(\tau\) に対して行い、\(h\) の底へ引き戻せる。

### この構成の文献と確実性

- 本文の入力：`prop:pg-PBW`、`lem:pg-det-divided-kernel`、`thm:pg-universal-determinant`、`lem:pg-central-cubic`、`thm:pg-ad-all-poisson`。
- 射影束の規約とtautological線：Stacks Project [Tag 01OA](https://stacks.math.columbia.edu/tag/01OA)。Stacksの標準規約は一次元商なので、ここでは双対を取って一次元部分束を表す。
- 同変準連接層の商スタックへの降下：Stacks Project [Tag 06WT](https://stacks.math.columbia.edu/tag/06WT)。積・単位・イデアルの射も同変なので代数へ適用できる。
- dilatationに使うblowupの普遍性：Stacks Project [Tag 0806](https://stacks.math.columbia.edu/tag/0806)。上の局所座標で、必要な追加条件と滑らかさを直接確認できる。

中心直線のパラメータ化とtautological商の降下自体は標準的な構成である。ここで個別に証明した点は、複数Jacobianブロックの \(\mathcal E\) 内の全非零元に対する正則性、底変更に耐える平坦商、および複数ブロックの相対規格化自由の明示である。同一の組合せの初出調査は未実施であり、新規性を確定したとは扱わない。

## 4. 特異・零の三変数制限での独立検算

\[
 f=u x^2+v y^2+w z^2+u^3+v^3+w^3
\]
とする。\(g=f(x,y,z,0,0,0)\equiv0\)だが、
各\(2ux=0,\ x^2+3u^2=0\)（巡回も同様）から
全偏微分の非零共通零点がなく、
\(V(f)\subset\mathbb P^5\)は滑らか。
次数3の古典Casimir行列は
\(S_3\to S_4^{\oplus3}\)で378×56、
rank=45、核の次元=11=1+\(\dim\mathbb C[u,v,w]_3\)。
SymPyの有理数演算による実行済みPASSを保持しており、本改訂では再実行していない（§7の計算表）。
再現コード
`computations/verify_singular_cubic_classical_kernel.py`。
この例ではさらに
\([y,z]=2\hbar ux,\ [z,x]=2\hbar vy,\ [x,y]=2\hbar wz\)
に対して**f自身が厳密な中心元**である。
一般特異制限については上記のCramer証明を用いる。
この有限例は一般定理の証明に代わるものではない。


三変数制限が**節点型**となる例
\[
 f=x^3+y^3+xyz+uz^2+u^3
\]
については、次の具体的な計算証明書がある。
$g=f(x,y,z,0)$は$[0:0:1]$にnodeを持つが、
全体$f$の勾配イデアルは零次元で
$V(f)\subset\mathbb P^3$は滑らか。
$\hbar=2/5$（有理数による一つの特殊化）で
次数4の自由非可換語121、関係式の二次倍数102、
関係行列のrank86。
次数3のWeyl交換子行列は20列でrank18、
核は$\mathbb C u^3$と次の中心元により張られる：
\[
 \Omega_{\hbar=2/5}=
 x^3+y^3+u^3
 +\frac{228}{253}\operatorname{sym}(xyz)
 +\frac{722}{759}uz^2
 -\frac{216}{253}u\operatorname{sym}(xy).
\]
この式の3生成元との交換子が関係式のイデアルに入ることは、
分母・行演算まで**有理数演算のみ**で検査する。
再現コード
`computations/verify_nodal_cubic_centre_specialization.py`。
この証明書は今回の監査では再実行していない。
対象は固定した$\hbar=2/5$の非可換代数であり、
一般の$\hbar$に対する代数的存在証明を代替しない。
原点を含む適切なZariski開上の存在は、§2の普遍rank/Cramer論法が与える。

## 5. 短い普遍Hesse中心元：全係数の計算証明

\(g_t=(x^3+y^3+z^3)/3+txyz\)、
\(f=g_t+Axy+Byz+Czx+Dx+Ey+Hz+G\)、
\(A,B,C\in R_1,D,E,H\in R_2,G\in R_3\)。
\(q=\hbar^2\)、\(S=x^3+y^3+z^3\)、
\(T=\operatorname{sym}(xyz)\)、
\(Q=A\operatorname{sym}(xy)+B\operatorname{sym}(yz)
+C\operatorname{sym}(zx)\)、
\(Z_2=Az^2+Bx^2+Cy^2\)、
\(L=Dx+Ey+Hz\)、
\(R_2=B^2x+C^2y+A^2z\)、
\(R_{11}=ACx+ABy+BCz\)と書く。
\[
\begin{aligned}
 U&=1+qt^2/2+q^2t/6-q^2t^4/48,&
 W&=(4-qt^2)(12t+q(t^3-8))/48,\\
 c&=(4-qt^2)(12+qt^2)/48,&
 d&=q(12t+q(2-t^3))/36,\\
 e&=1+q^2t(8-t^3)/144,&
 f_2&=q(4-qt^2)/24,\\
 g_2&=-q(12t+q(t^3+4))/72.
\end{aligned}
\]
\[
 \boxed{\Omega=US/3+WT+cQ+dZ_2+eL+f_2R_2+g_2R_{11}+G.}
\]
\(\Omega_0=f\)。Hesse型の短い式は
\(\hbar^4\)までの有限多項式で**厳密に中心**。
定理 thm:pg-universal-hesse-mixed の証明は
独立不定元\(A,B,C,D,E,H,\hbar,t\)について
全次数4の非可換語339個、関係式の倍数162個、
Q(h,t)上の行列rank144、三交換子の余り0の
**普遍的有理関数恒等式**。
\(\hbar=0\)でのrankも144であり原点を含む開上へ降下。
コード `computations/verify_universal_hesse_mixed_center.py`。
現行スクリプトをそのまま実行し、記載した二つの階数と
三交換子の消滅を全不定元のまま確認したPASSの証拠を保持する。本改訂では再実行していない（§7）。
GL3のHesse変換と中心平行移動は
滑らかな三変数制限の場合の**短い**中心式を与える。

## 6. 内在的な一般次元Hessian補正と再現

定数三重ベクトル\(P\in\Lambda^3V\)と三次式Fに対し
\[
 \mathscr H(P,F)=\frac16\sum P^{ijk}P^{abc}F_{ia}F_{jb}F_{kc}
\]
は座標不変。
正規形では\(\mathscr H(P,F)=
\sum_s\lambda_s^2\det\operatorname{Hess}_{x_s}(f_s)\)。
滑らかな三変数制限のHesse表示では、
純中心項の調整後に
\(\Omega=\operatorname{sym}(F-\hbar^2\mathscr H(P,F)/12
+\hbar^4K_{P,F})\)。
**Hessianの二次補正は座標不変**だが、一般特異制限について
四次で打ち切ることは示していない。
任意の三次ブロックについての二次補正は
`prop:pg-universal-casimir-jet`に記載されている。
二十個の独立係数を持つactive次数三以下の普遍多項式について、
\([\operatorname{sym}(f-\hbar^2H_f/12),x_i]\)を
\(\hbar^4\)を法として厳密計算し、語の反転と\(\hbar\)の符号反転に関する
偶奇性によって\(\hbar^5\)を法とする中心性を得る。
これは全次数の厳密中心元への延長を単独で保証する命題ではない。
対応する現行スクリプトの実行結果は§7に記す。

具体例用のコードとして
`computations/verify_general_dimension_multiblock.py`
（n=3,4,6,7,10の6例でJacobi、Casimir、内在Hessian縮約を検査）と
`computations/build_general_dimension_center.py`
（共通中心を持つ2ブロックのHesse中心式を合成）がある。
これら二本は今回の監査では再実行しておらず、一般次元定理の形式検証でもない。

## 7. 証明監査・再現手順と先行研究

### 証明監査と計算検証の範囲

量子化については、§2のactive gradientの互いに素性、古典Casimir核、
普遍階数恒等式とCramerの規格化、§3のBertini配分を数学的に点検した。
PBWの族への拡張、Koszul AS-regular中央一次元拡大、
中心三次商のAS-Gorenstein性、一ブロックactive次数filtrationによる
中心元の左右正則性も証明を追って確認した。
定階数から底上局所自由性を得る議論、Hesse座標の同時選択を必要としない
稠密性の使い方、Bertiniのアフィンchartへの移行は原稿で明確化している。
全零切断を含む偶principal開、τへの下降、Picard群消滅、
大域基底の単元補正、Ann(h)による通常の中心との差、
規格化遷移・イデアル不一致例・座標変換も独立に読み直して確認した。
全supportの同変選択については、全整数twistのBWB計算、h冪厚化の完全列、
Stiefel開上の正則関数の延長、有限次数Weyl開の一様性、有限核の完備化からの剰余の持上げ、
Reynolds平均と指標による次数補正を独立に読解した。
全f・η・hに依存する補空間選択の障害と、U作用の自由性・非自明torsor・非アフィン商も点検した。
CMRのaccepted versionとの関係式・中心公式の対応は、本文照合と独立な記号計算を区別して扱う。
これは数学的な証明監査であり、定理全体の形式証明器による検証ではない。
正規形・Lie代数・退化幾何等を含むA全体の監査は
`notes/poisson_article_submission_audit.md`を参照する。

本改訂の新しい厳密計算はCMR節点公式の一本であり、実行済み出力を確認した。
それ以外の十三件は以前の実行証拠とコード・証明書のハッシュ照合を引き継ぎ、再実行していない。
全十四件の一覧は `notes/poisson_article_submission_audit.md` に置く。
以下の四つの既存計算の実行証拠は2026-11-13のA-v52監査に由来し、版番号は実行時の記録である。
コマンドはリポジトリのルートで実行し、Python 3とSymPyを用いる。

| コマンド | 最終状態 | 検証の内容と限界 |
| --- | --- | --- |
| `python3 computations/verify_cmr_nodal_center.py --json` | 本改訂でPASS、SymPy 1.14.0 | 独立QQ係数によるCMRのγ=0公式、zyx重なり、三中心交換子、関係式の対応、古典極限、安定化群の生成子に関する補正を検証。Weyl偶性・軌道降下・モジュライ降下は対象外。 |
| `python3 computations/verify_universal_hesse_mixed_center.py` | 既存exit 0・PASSを保持、未再実行 | 339基底語・162関係倍数。階数は\(\hbar=0\)と\(\mathbb Q(\hbar,t)\)でともに144。六混合係数を独立に保ち三交換子が厳密に消滅。 |
| `python3 computations/verify_cubic_casimir_jet.py` | 既存exit 0・PASSを保持、未再実行 | 二十自由係数を保ち、各生成元について125個の語・次数係数が消滅。計算が直接示すのは\(\hbar^4\)を法とした恒等式。 |
| `python3 computations/verify_singular_cubic_classical_kernel.py` | 既存exit 0・PASSを保持、未再実行 | §4の零三変数制限の例。378×56行列の階数45、核は\(\mathbb C f\oplus\mathbb C[u,v,w]_3\)、次元11。 |
| `python3 computations/verify_nonelliptic_quantization.py` | 既存exit 0・PASSを保持、未再実行 | 二つのmonic Diamond系と重なり、六つの普遍中心交換子、古典極限、potential syzygy、分母の範囲、二つの非中心な比較例、17項Fermat恒等式を確認。実行時の再計算結果は保存証明書と完全一致。残余圏のsaturationの計算検証ではない。 |

非楕円型の現在有効な計算証拠は保存JSONである。検証時には
`--write`を付けずに実行し、再計算した結果全体と
`computations/nonelliptic_quantization_certificate.json`の一致を確認した。
公開本文の還元式、中心三次元、重なりの正規形、Fermat恒等式も実装と照合している。

CMRの出力保存コマンドは
`python3 computations/verify_cmr_nodal_center.py --json --output build/verify_cmr_nodal_center.json`。
出力中のstatusはPASS、コードSHA-256は
`f3ca63fcf5e5f66ed6d7aad45c2c853bd162c86074980a8b1e915ee998d3a503`で現行ファイルと一致した。
実行対象、引き継いだ計算と証明書のSHA-256は `validation_paper_a.json` に集約する。
この有限計算はBWB・大域中心元・商モジュライ降下の一般証明を代替しない。

重い記号計算は一本ずつ実行する。
LuaLaTeXによる再生成コマンドは`latexmk papers/paper_a.tex`で、
PDFと中間生成物は`build/`へ出力される。
**A-v59全体の組版・参照検査・PDF確認および計算の最終実施状態は、
リポジトリルートの[`validation_paper_a.json`](../validation_paper_a.json)を参照する。**
本文の証明監査、計算の実行、PDFの確認、配布物の生成・保存は別の状態として扱う。
本ノートからA-v59の組版・視覚確認・Library保存の完了を推定しない。

### 確認した一次文献と本稿の位置

- Mori–Smith, *The classification of 3-Calabi–Yau algebras with 3 generators and 3 quadratic relations*,
  [arXiv:1502.07403v2](https://arxiv.org/abs/1502.07403v2)：
  Theorem 1.4のrank判定、Corollary 2.7のstandard性、Corollary 2.9の3-CY・AS-regular・domainの関係、
  Theorem 4.2(1)の滑らかな三次制限に対する全パラメータの3-CY性を確認した。
- Berger–Taillefer, *Poincaré–Birkhoff–Witt deformations of Calabi–Yau algebras*,
  [刊行PDF](https://ems.press/content/serial-article-files/30423?nt=1), Theorem 1.1(i), p.242、Theorem 3.1, p.246：
  三次元graded CY potentialへの低次数potentialの追加によるPBW変形。
  本稿では中心変数を固定したactive次数二以下の項へ適用する。
- Le Bruyn–Smith–Van den Bergh, *Central extensions of three dimensional Artin–Schelter regular algebras*,
  Math. Z. 222 (1996), 171–212,
  [著者公開PDF](https://sites.math.washington.edu/~smith/Research/Central-extns.pdf), Theorem 3.1.3：
  非楕円量子化節のFermatブロックでは\(Q=I\)、\(l_j=-2s x_j\)、\(\alpha_j=0\)なので、
  三条件を\(\gamma_j=0\)で満たす。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*,
  JEMS 12 (2010), 1371–1416,
  [刊行本文](https://ems.press/content/serial-article-files/31746), Theorem 3.3.2(ii), p.1385、§8.3, pp.1410–1411：
  同次三変数CY potentialの低次変形の非スカラー中心元存在と、rank・射影的閉性による特殊化は既知である。
  本稿では全体の滑らかさによるactive gradientの互いに素性と固定次数の普遍小行列式を用い、
  Cramer表示で原点の規格化を制御する。
  また§9, p.1414は一変数低次項付きRains公式を与える。混合Hesse式もt可逆なら中心平行移動でこの表示へ移る。
  具体式・定数項・自由語関係は `rem:pg-hesse-eg-translation` と `verify_hesse_translation.py` に保持し、
  実行済みの普遍有理恒等式の検算は現行コードのハッシュと共に保持する。固定係数環上での正則な規格化と全係数への延長を、既知の点ごとの存在から区別する。
  **Proposition 8.1.1(i), p.1407、証明pp.1407–1408**は、
  重みa,b,c、d=a+b+cの三生成元potential
  \(\Phi=xyz-yxz+\sum_{j\ge1}\hbar^j\Phi_j\)、\(\deg\Phi_j\le d\)について、
  古典剰余 \((\Phi_1)^{\mathrm{ab}}\) を持つ次数d以下の形式中心元を与える。
  (i)には孤立特異点の仮定がなく、この仮定は(ii),(iii)で追加される。
  証明はR=C[u]を基底とする相対議論を用い、還元群作用に対応するformalityも明記する。
  したがって、指定古典剰余の形式中心元存在や相対・同変な形式構成自体を本稿の新規性とはしない。
  §2(IX)の比較対象は、全smooth Fと動く全support上での代数的な同時選択である。
- Chekhov–Mazzocco–Rubtsov, *Quantised Painlevé monodromy manifolds, Sklyanin and Calabi–Yau algebras*,
  Adv. Math. 376 (2021), 107442、
  [DOI](https://doi.org/10.1016/j.aim.2020.107442)。
  本文確認は[accepted arXiv:1905.02772v2](https://arxiv.org/pdf/1905.02772v2)の
  式(4.38), p.21、Lemma 4.6・式(4.39), p.22、Table 5, p.41。
  節点型の点ごとの中心元と公式は既知。現行稿の具体的な対応・無極な規格化・純中心補正は§2(VIII)を参照する。
- Guo–Lu–Sharpe, *Classical sheaf cohomology rings on Grassmannians*,
  [arXiv:1605.01410v2](https://arxiv.org/pdf/1605.01410v2), §2.2, Theorem 2.3, pp.5–6。
  Grassmann多様体上の束の重みの規約を本文で確認した。
  Theorem 2.4の証明は負の最高重みも明示しており、全整数twistへの適用を確認できる。
- Lurie, *A proof of the Borel–Weil–Bott theorem*,
  [著者公開ノート](https://www.math.harvard.edu/~lurie/papers/bwb.pdf), Theorem 5と証明, p.3。
  PDFに刊行年の記載はない。一般のBWB定理の確認に用いた。
  **Bott原論文やWeyman原書を直接読了したとはしない。**
- Derksen, *Computation of Invariants for Reductive Groups*,
  Adv. Math. 141 (1999), 366–384、
  [著者公開刊行PDF](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.4.pdf)。
  Theorem 2.1, pp.368–369のHilbert有限生成と、p.369のReynolds射影・安定部分加群の性質を確認した。
- Stacks Project [00MA](https://stacks.math.columbia.edu/tag/00MA)・
  [00MB](https://stacks.math.columbia.edu/tag/00MB), Lemmas 10.97.1–10.97.2：
  Noetherian環上の有限加群の完備化の完全性、テンソル積との一致と平坦性。
  [06PH](https://stacks.math.columbia.edu/tag/06PH), Lemma 80.11.7：
  flat・局所有限表示の群による自由作用の商は代数空間で、商写像はfppf torsorとなる。
  [03OY](https://stacks.math.columbia.edu/tag/03OY), §59.22のTheorem 59.22.4：
  準連接層のZariski・fppfコホモロジー比較。アフィン底上の加法群torsorの自明性へ適用する。
- De Laet–Le Bruyn, *The geometry of representations of 3-dimensional Sklyanin algebras*,
  [arXiv:1405.1158v1](https://arxiv.org/abs/1405.1158v1), **§2、p.3**：
  \(3c_3\)の式が本稿の純Hesse中心公式の入力である。
  Theorem 1冒頭の表示には係数と\(z^3\)の誤植があるため、§2の表示・証明と照合する。

PBW/AS-regular性の一般原理と純Sklyanin中心元は既知の入力である。
全混合係数の有限中心公式、普遍rank恒等式への使用、規格化したCramer中心元と
正規形を組み合わせた全Poisson量子化、全support上の同時代数的選択についても、
初出の網羅的確認が完了したとは主張しない。
Pymとの比較は `poisson_article_submission_audit.md` の公開arXiv v1に限り、
刊行版本文・accepted manuscript本文は引き続き未取得である。

### 形式的Poisson構造を経由する方法の注意

Dolgushev, *The Van den Bergh duality and the modular symmetry of a Poisson variety*,
[arXiv:math/0612288v3](https://arxiv.org/abs/math/0612288v3) の
Proposition 1（印刷p.9）とTheorem 3（印刷p.15）は、
標準束が自明な滑らかな複素アフィン多様体の形式星積を扱う。
Theorem 3のunimodularity条件は、その星積のKontsevich classを表す
**形式Poisson構造全体**
\(\pi=\hbar\pi_1+\hbar^2\pi_2+\cdots\)に課される。
一次の\(\pi_1\)のdivergenceが零であることだけでは足りない。
Proposition 1では、先頭項が至る所非零の形式的最高次形式
\(\omega(\hbar)\)が存在し、\(L_\pi\omega(\hbar)=0\)となることが判定条件である。
従ってこの方法を相対係数環・完備双加群へ使うには、
星積の全形式class、基底環、完備化と双対性の仮定を個別に確認する必要がある。
また、形式的中心元の存在から原点近傍の代数的中心元を得ることも別の論点である。
EG Proposition 8.1.1(i)は相対係数環を用いた形式中心の存在を既に与えるので、
この一般原理の適用自体を新しい成果とはしない。
現行の固定正規形の存在証明は外部の形式中心存在を使わず、
全supportの同変選択は既存の代数的定階数核の形式的持上げを有限Noetherian核へ戻す。
これらを省略した形式的CY論法は証明の代用にしない。

### 一般点での復元と残る問題

論文B-v59 `papers/paper_b.tex` は、滑らかな可換三次超曲面を特殊ファイバーに持つ
次数別有限自由な代数的中心三次対について、任意の\(n\ge3\)で
**一変数一般ファイバーの全coherent残余圏**を、有限体拡大後に
滑らかな可換三次超曲面のKuznetsov成分として復元する。
同値はrotationと指定三次周期比較を保ち、可換模型の方程式自体は
元の関数体\(\mathbb C(h)\)上に取れる。
従って「一般次元の非可換Kuznetsov復元が未解決」という一括した記述は使わない。

優先する未解決問題は次の通りである。

1. 複数ブロックの分解・配分を忘れた同変構成。階数二の全supportの共変中心元と、gcd(N,3)=1の全被約層への降下は得た。
   次は§3の中心核の射影束で保持した追加データを忘れる条件を調べる。
   古典核の自然な線と純中心束のコホモロジー、ブロック置換作用から着手する。
   3|Nの全階数二層では、特異点直線に代わる重み一線束の有無を検討する。
   全supportで選んだ中心元と零制限の全h公式・既存層別式との一致、
   固定h≠0での同型類像、全モジュライでの圏の降下は別問題である。
2. 非零の特異な三変数制限に対する短い普遍多項式表示の存在。
   Cramer式の分母と特異型ごとの有限関係式を調べ、単なる可逆な中心元の再規格化で除去できる分母を区別する。
3. 全閉パラメータにおけるqgrの滑らかさ、可換特殊点を含む一変数・多変数底全体での相対残余圏の比較。
   一般点の結果を特殊点へ延長する際のproperness・対角のperfect性・底変更を確認する。

階数二の全supportの証明では、形式的持上げを有限核の代数的持上げに結びつけた。
複数ブロックでも同じ手順が自動的に適用できるとは仮定せず、古典核とコホモロジーを先に確認する。
