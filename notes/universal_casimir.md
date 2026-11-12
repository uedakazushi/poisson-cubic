# 全Poisson構造の代数的中心三次元と一般次元量子化：現行研究ノート

**2026-11-12 / v6。再開時はまず \`00_research_plan.md\` を読む。**
正本はGitHub \`uedakazushi/nc-cubic\` の \`main\`。
現行公表原稿は \`papers/paper_a.tex\`（論文A）。
主要証明の所在：
\`papers/support/papers/sections/universal_casimir_determinant.tex\`
（任意のsmoothな全体三次式の代数的Casimir）、
\`papers/support/papers/sections/poisson_geometry.tex\`
（全Poisson構造の量子化）、
\`papers/support/papers/sections/general_dimension_universal_quantization.tex\`
（全次元・全k変数pencil）、
\`papers/support/papers/sections/hesse_mixed_universal_center.tex\`
（普遍Hesse多項式）。
詳細証明は原稿に置き、本ノートでは主要な結論・依存・障害・再現手順を整理する。

## 1. 解決した核心：全てのsmooth cubicの全Poisson構造を代数的に量子化

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
全Poissonモジュライへの同変な大域量子化や
qgrのsmoothnessも未証明。

## 2. 新しい代数的証明の4段階

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
純中心三次d_m個とHesse中心1個の存在により
\(\mathcal T_m^\circ\)上でrank≤r_m。
したがって全\((r_m+1)\)次小行列式は既約・被約な
係数空間で恒等的に零となり、
\(\mathcal T_m\)の**全ての点**に特殊化しても
rank≤r_m（lem:pg-det-universal-rank）。
これは**中心元の分母が特異制限で消えない**
と仮定した議論ではない。rankに関する**正則関数恒等式**
を先に延長している点が重要。

### (IV) Cramer表示と原点での規格化

fの非零のactive三次単項式係数をa、対応単項式をw_0とする。
残るactive三次単項式w_1,...,w_{r_m}に対する
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

## 3. 複数ブロックに対する中心三次の配分

正規形を
\(F=\sum_s\widetilde f_s(x_s,u)+c(u)\)とし、
純中心三次\(c(u)\)を\(c_1+\cdots+c_k\)へ配分する。
各\(f_s=\widetilde f_s+c_s\)の滑らかさは、
u=0ではXの滑らかさから保証される。
u≠0では\(\mathbb C[u]_3\)は基点自由なのでBertiniにより
一般のc_sでf_sが滑らかになる。
k≥2の配分空間は
\(\{(c_s):\sum c_s=c\}\simeq(\mathbb C[u]_3)^{k-1}\)
という既約なアフィン空間で、
各c_sへの射影は全射だから、
k個の滑らかさ条件を同時に満たせる。
k=1ではf_1=Fが既に滑らか。m=0では各純active f_sが
Fの滑らかさから滑らか。
\(\partial_{x_s}c_s=0\)だからPoisson構造は不変。
これは**全Poisson構造**へ一ブロック定理を適用する鍵となる。

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
同等のSymPy有理数行列を**実際に実行してPASS**。
再現コード
\`computations/verify_singular_cubic_classical_kernel.py\`。
この例ではさらに
\([y,z]=2\hbar ux,\ [z,x]=2\hbar vy,\ [x,y]=2\hbar wz\)
に対して**f自身が厳密な中心元**である。
一般特異制限については上記のCramer証明を用いる。
この有限例は一般定理の証明に代わるものではない。


さらに三変数制限が**節点型**となる例
\[
 f=x^3+y^3+xyz+uz^2+u^3
\]
も調べた。$g=f(x,y,z,0)$は$[0:0:1]$にnodeを持つが、
全体$f$の勾配イデアルは零次元で
$V(f)\subset\PP^3$は滑らか。
$\hbar=2/5$（有理数による一つの特殊化）で
次数4の自由非可換語121、関係式の二次倍数102、
関係行列のrank86。
次数3のWeyl交換子行列は20列でrank18、
核は$\CC u^3$と次の中心元により張られる：
\[
 \Omega_{\hbar=2/5}=
 x^3+y^3+u^3
 +\frac{228}{253}\operatorname{sym}(xyz)
 +\frac{722}{759}uz^2
 -\frac{216}{253}u\operatorname{sym}(xy).
\]
この式の3生成元との交換子が関係式のイデアルに入ることを
分母・行演算まで**有理数演算のみ**で直接計算してPASS。
再現コード
\`computations/verify_nodal_cubic_centre_specialization.py\`。
この確認は固定した$\hbar=2/5$の非可換代数に対する結果で、
$\hbar$の全値にわたる代数的存在証明そのものではない。
全値の存在はSection 2の普遍rank/Cramer論法が与える。

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
\(\hbar^4\)までの有限多項式で\emph{厳密に中心}。
定理 thm:pg-universal-hesse-mixed の証明は
独立不定元\(A,B,C,D,E,H,\hbar,t\)について
全次数4の非可換語339個、関係式の倍数162個、
Q(h,t)上の行列rank144、三交換子の余り0の
**普遍的有理関数恒等式**。
\(\hbar=0\)でのrankも144であり原点を含む開上へ降下。
コード \`computations/verify_universal_hesse_mixed_center.py\`。
当該全不定元での同等の計算は以前ローカル実行してPASS。
GitHubに保存したスクリプトをそのままcloneして
再実行した確認とは区別する。
GL3のHesse変換と中心平行移動は
滑らかな三変数制限の場合の\emph{短い}中心式を与える。

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
\`computations/verify_general_dimension_multiblock.py\` は
n=3,4,6,7,10の6例でJacobi、Casimir、
内在Hessian縮約恒等式の厳密計算を実行してPASS。
\`computations/build_general_dimension_center.py\` は
共通中心を持つ2ブロックのHesse中心式の合成を確認。
いずれも一般次元定理の形式検証ではない。

## 7. 新規性・未解決と次の着手

- **到達**：特異・零の三変数制限まで含めて全Poisson構造の
  代数的中心三次元と量子化を証明した。
  原稿Aの形式的中心元・Kontsevich/Dolgushevルートは
  中心性の存在証明から除いた。
  その旧ルートは有用な代替手段だが、相対CY/formalityの全条件の
  独立監査が完了していないため、完成定理の入力とはしない。
- **先行研究**：Hesse/Sklyanin中心元とPBW/AS正則性は既知。
  Etingof--Ginzburg,
  *Noncommutative del Pezzo surfaces and Calabi-Yau algebras*,
  JEMS 12 (2010), 1371–1416,
  arXiv:0709.3593v4, §8.3（普遍potentialの中心元のrank・特殊化）
  を原PDF p.32で確認。今回の全体滑らかさからの
  active gradient gcdと固定次数rank小行列式の証明とは区別する。
  全般の新規性・初出の網羅調査は未完成。
- **依存の監査**：三変数普遍Hesse中心元の全係数計算証明書、
  Mori–Smithのrank criterion、Berger–TailleferのPBW変形、
  Poisson正規形のLie代数補題、AS-regular中央拡大、
  中心三次商のAS-Gorensteinを継続検証する。
  数学的証明を原稿へ書いたことと全てを今回独立検証したことは違う。
- **残る数学的問題**：Cramer中心元のHesseチャートを越えた
  **モジュライ上の正準化・同変接着**、
  特異制限の短い普遍多項式表示の有無、
  qgrのsmoothness・非可換Kuznetsov復元。
  形式的存在証明の技術的監査は今後の最優先ではない。
- **投稿チェック**：論文A全体のLuaLaTeXビルド・PDF目視、
  参照・式番号、全必要計算の再実行は未完了。
  GitHub mainにソースを保持し、PDFはGit追跡せず
  \`latexmk papers/paper_a.tex\`でbuild/へ生成する。
  GitHubへのpushが実際に失敗した場合だけLibraryを緊急避難先に使う。
