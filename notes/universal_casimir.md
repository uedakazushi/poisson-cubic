# 全Poisson構造の代数的中心三次元と一般次元量子化：現行研究ノート

**2026-11-14 / v9（論文A-v54・論文B-v57、bundle nc-cubic-v85）。再開時はまず `00_research_plan.md` を読む。**
正本はGitHub `uedakazushi/nc-cubic` の `main`。
現行公表原稿は `papers/paper_a.tex`（論文A）。
主要証明の所在：
`papers/support/papers/sections/universal_casimir_determinant.tex`
（任意のsmoothな全体三次式の代数的Casimir）、
`papers/support/papers/sections/equivariant_central_lifts.tex`
（reductive群と滑らかな三変数制限上の全ブロック座標群に対する同変性）、
`papers/support/papers/sections/poisson_geometry.tex`
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
**形式的中心元、Kontsevich formality、Dolgushevのunimodularity判定は
この存在証明の入力ではない。**

**明示性の限界**：
\(g_s\)が滑らかならHesse標準形による\(\eta_s^4\)までの
短い多項式公式がある。一般の特異・零の\(g_s\)でも、
原点で分母が消えない\(\eta_s^2\)の**有限有理式**がある。
全特異制限に共通する低次数の短い\(\eta_s\)-多項式を
示したわけではない。
全Poissonモジュライへの同変な大域量子化は未構成である。
単一ブロックでは、変数分解を保つreductive群に関する同変性を
全滑らかな全体三次式で得た。三変数制限が滑らかなら、
中心変数によるactive座標の平行移動を含む群についても同変に選べる。
さらにgcd(m,3)=1なら中心スカラーの次数重みを指標で補正でき、
階数二のPoisson対の被約層内の開へ代数族が降りる（§2(VI)）。
固定したactive・中心変数の分解では、
全滑らかな三次式の係数空間と変形直線の積の中で、
零切断全体を含む一つの開集合上に中心元を同時に選べる。
これは係数と無関係な一つのh開集合を得る主張ではない。
一変数一般点での全coherent残余圏の可換復元は論文B-v57が扱い、
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
単一ブロックについては次項の範囲で同変選択を構成した。
特異な三変数制限を含む全座標群への拡張と、
複数ブロックの配分の変化との整合性は残る。

### (VI) 同変な中心元と中心平行移動の処理

量子交換子の係数をtと書き、
\[
G_0=(\mathrm{GL}_3\times\mathrm{GL}_m)\times\mathbb G_m,\qquad
X=Mx,\quad U=Nu,\quad
f'=\lambda^{-1}f\circ(M^{-1},N^{-1}),\quad
t'=\lambda\det(M)t
\]
とする。`thm:pg-equivariant-levi-center` は、
全零切断を含むG_0不変開上に、tについて偶な中心元を選び、
\[
\Phi(\Omega_{f',t'})=\lambda^{-1}\Omega_{f,t},\qquad
\Omega_{f,0}=f,\qquad \rho(\Omega_{f,t})=f_{\mathrm{cent}}
\]
とできることを示す。これは選択の存在であり、一意性・正準性は主張しない。

証明の要点は次の二つの平均化である。悪い閉集合のstable ideal Iには
t=0で1となる元pが存在し、Reynolds平均後もp∈Iとp|_{t=0}=1を保つ。
p(t)p(−t)で偶な不変principal開が得られる。
そのaffine開ではKの切断をt=0のCasimirへ制限する写像が全射である。
fのλ-characterを補正してReynolds平均し、t↦−tで偶化する。
商線束中での零点はstable closed setなので、
再び不変principal開へ縮めてその像を基底にできる。
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
本研究ではこれを同変な中心商の族に適用した。

17は底の次元であり、固定したh≠0の非可換代数の同型類の像が17次元とは主張しない。
hを保つ変形族全体からは特殊ファイバーと一次括弧により元のPoisson対を回復できる。
3|mでは上の群の全指標のスカラー重みが3の倍数なので、この手段では補正できない。
それだけでgerbeが非中立である、または別の降下法が存在しないとは結論しない。

残る核心は、特異・零のgでの同変な中心平行移動の処理と、
複数ブロックでの配分・相対規格化の整合性である。
g=0ではδ_g=0なので、上のleft inverseによる方法はそのまま延長できない。
これは量子化そのものの不存在を意味しない。

**同じ方法を広げる際の二つの障害。**
第一に、全中心平行移動との共変性と
\(\rho\Omega=f_{\mathrm{cent}}\) を同時に課すと、Weyl記号P_fは
\(P_f(-Cu,u)=f(-Cu,u)\) を全Cについて満たす。
u≠0でCuは任意のactive座標を動くためP_f=fとなるが、
Fermatの非自明なt²補正がこれに反する。
したがって全G同変性の定理では純中心係数の規格化を外す必要がある。

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
これは全fの混合係数にも依存する別の同変構成や、
中心直線そのものの延長を排除する議論ではない。

## 3. 複数ブロックの中心三次：配分と直線の選択

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
現行スクリプトをSymPyの有理数演算で**実行してPASS**（§7の計算表）。
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
三交換子の消滅を全不定元のまま確認してPASS（§7）。
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
これは数学的な証明監査であり、定理全体の形式証明器による検証ではない。
正規形・Lie代数・退化幾何等を含むA全体の監査は
`notes/poisson_article_submission_audit.md`を参照する。

以下は2026-11-13のA-v52監査で現行スクリプトを直接実行した結果である。
本改訂ではコードと証明書のハッシュ一致を確認して保持し、これらの重い計算は再実行していない。
コマンドはリポジトリのルートで実行し、Python 3とSymPyを用いる。

| コマンド | 最終状態 | 検証の内容と限界 |
| --- | --- | --- |
| `python3 computations/verify_universal_hesse_mixed_center.py` | exit 0、PASS | 339基底語・162関係倍数。階数は\(\hbar=0\)と\(\mathbb Q(\hbar,t)\)でともに144。六混合係数を独立に保ち三交換子が厳密に消滅。 |
| `python3 computations/verify_cubic_casimir_jet.py` | exit 0、PASS | 二十自由係数を保ち、各生成元について125個の語・次数係数が消滅。計算が直接示すのは\(\hbar^4\)を法とした恒等式。 |
| `python3 computations/verify_singular_cubic_classical_kernel.py` | exit 0、PASS | §4の零三変数制限の例。378×56行列の階数45、核は\(\mathbb C f\oplus\mathbb C[u,v,w]_3\)、次元11。 |
| `python3 computations/verify_nonelliptic_quantization.py` | exit 0、PASS | 二つのmonic Diamond系と重なり、六つの普遍中心交換子、古典極限、potential syzygy、分母の範囲、二つの非中心な比較例、17項Fermat恒等式を確認。再計算した結果は保存証明書と完全一致。残余圏のsaturationの計算検証ではない。 |

非楕円型の実行出力は`build/verify_nonelliptic_quantization.log`。
`--write`を付けずに実行し、再計算した結果全体と
`computations/nonelliptic_quantization_certificate.json`の一致を確認した。
公開本文の還元式、中心三次元、重なりの正規形、Fermat恒等式も実装と照合している。

実行対象と証明書のSHA-256は `validation_paper_a.json` に集約する。

重い記号計算は一本ずつ実行する。
LuaLaTeXによる再生成コマンドは`latexmk papers/paper_a.tex`で、
PDFと中間生成物は`build/`へ出力される。
**A-v54全体の組版・参照検査・PDF確認および計算の最終実施状態は、
リポジトリルートの[`validation_paper_a.json`](../validation_paper_a.json)を参照する。**
本文の証明監査、計算の実行、PDFの確認、配布物の生成・保存は別の状態として扱う。

### 確認した一次文献と本稿の位置

- Mori–Smith, *The classification of 3-Calabi–Yau algebras with 3 generators and 3 quadratic relations*,
  [arXiv:1502.07403v2](https://arxiv.org/abs/1502.07403v2)：
  Theorem 1.4のrank判定、Corollary 2.7のstandard性、Corollary 2.9の3-CY・AS-regular・domainの関係、
  Theorem 4.2(1)の滑らかな三次制限に対する全パラメータの3-CY性を確認した。
- Berger–Taillefer, *Poincaré–Birkhoff–Witt deformations of Calabi–Yau algebras*,
  [arXiv:math/0610112v2](https://arxiv.org/abs/math/0610112v2), Theorem 1.1(i)：
  三次元graded CY potentialへの低次数potentialの追加によるPBW変形。
  本稿では中心変数を固定したactive次数二以下の項へ適用する。
- Le Bruyn–Smith–Van den Bergh, *Central extensions of three dimensional Artin–Schelter regular algebras*,
  Math. Z. 222 (1996), 171–212,
  [著者公開PDF](https://sites.math.washington.edu/~smith/Research/Central-extns.pdf), Theorem 3.1.3：
  非楕円量子化節のFermatブロックでは\(Q=I\)、\(l_j=-2s x_j\)、\(\alpha_j=0\)なので、
  三条件を\(\gamma_j=0\)で満たす。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*,
  JEMS 12 (2010), 1371–1416,
  [arXiv:0709.3593v4](https://arxiv.org/abs/0709.3593v4), §8.3、印刷p.32：
  potentialの中心元をrank一定性と射影的閉性で特殊化する議論は既存の原理である。
  本稿では全体の滑らかさによるactive gradientの互いに素性と固定次数の普遍小行列式を用い、
  Cramer表示で原点の規格化を制御する。
- De Laet–Le Bruyn, *The geometry of representations of 3-dimensional Sklyanin algebras*,
  [arXiv:1405.1158v1](https://arxiv.org/abs/1405.1158v1), **§2、p.3**：
  \(3c_3\)の式が本稿の純Hesse中心公式の入力である。
  Theorem 1冒頭の表示には係数と\(z^3\)の誤植があるため、§2の表示・証明と照合する。

PBW/AS-regular性の一般原理と純Sklyanin中心元は既知の入力である。
全混合係数の有限中心公式、普遍rank恒等式への使用、規格化したCramer中心元と
正規形を組み合わせた全Poisson量子化についても、初出の網羅的確認が完了したとは主張しない。

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
これらを省略した形式的CY論法は、現行の全Poisson量子化定理の証明に用いない。

### 一般点での復元と残る問題

論文B-v57 `papers/paper_b.tex` は、滑らかな可換三次超曲面を特殊ファイバーに持つ
次数別有限自由な代数的中心三次対について、任意の\(n\ge3\)で
**一変数一般ファイバーの全coherent残余圏**を、有限体拡大後に
滑らかな可換三次超曲面のKuznetsov成分として復元する。
同値はrotationと指定三次周期比較を保ち、可換模型の方程式自体は
元の関数体\(\mathbb C(h)\)上に取れる。
従って「一般次元の非可換Kuznetsov復元が未解決」という一括した記述は使わない。

優先する未解決問題は次の通りである。

1. 特異・零のgにおける全G同変選択と、複数ブロックの分解・配分を変えた間の整合。
   全fでのG_0平均、滑らかなgでの中心調整、gcd(m,3)=1での
   階数二の被約Poisson層への代数族の降下は解決済みである。
   次はfの混合係数も使った同変な中心直線の構成と、§3の射影束で保持した
   追加データを忘れる条件を検討する。3|mでの別の降下法、
   固定h≠0での代数の同型類の像の次元、全モジュライでの圏の降下は別の問題である。
2. 特異・零の三変数制限に対する短い普遍多項式表示の存在。
   Cramer式の分母と特異型ごとの有限関係式を調べ、単なる可逆な中心元の再規格化で除去できる分母を区別する。
3. 全閉パラメータにおけるqgrの滑らかさ、可換特殊点を含む一変数・多変数底全体での相対残余圏の比較。
   一般点の結果を特殊点へ延長する際のproperness・対角のperfect性・底変更を確認する。

形式的存在証明への変更は、これらの問題を解くための前提ではない。
