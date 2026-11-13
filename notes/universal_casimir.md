# 全Poisson構造の代数的中心三次元と一般次元量子化：現行研究ノート

**2026-11-13 / v7（論文A-v52・論文B-v57、bundle nc-cubic-v83）。再開時はまず `00_research_plan.md` を読む。**
正本はGitHub `uedakazushi/nc-cubic` の `main`。
現行公表原稿は `papers/paper_a.tex`（論文A）。
主要証明の所在：
`papers/support/papers/sections/universal_casimir_determinant.tex`
（任意のsmoothな全体三次式の代数的Casimir）、
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
一変数一般点での全coherent残余圏の可換復元は論文B-v57が扱い、
有限体拡大後の同値を証明している。
全閉パラメータでのqgrの滑らかさや、可換特殊点を含む相対残余圏の比較は
この一般点の結果とは別の問題である（§7参照）。

## 2. 代数的証明の4段階と依存関係

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

## 3. 複数ブロックに対する中心三次の配分

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

## 7. A-v52の監査・再現手順と先行研究

### 証明監査と計算検証の範囲

量子化については、§2のactive gradientの互いに素性、古典Casimir核、
普遍階数恒等式とCramerの規格化、§3のBertini配分を数学的に点検した。
PBWの族への拡張、Koszul AS-regular中央一次元拡大、
中心三次商のAS-Gorenstein性、一ブロックactive次数filtrationによる
中心元の左右正則性も証明を追って確認した。
定階数から底上局所自由性を得る議論、Hesse座標の同時選択を必要としない
稠密性の使い方、Bertiniのアフィンchartへの移行は原稿で明確化している。
これは数学的な証明監査であり、定理全体の形式証明器による検証ではない。
正規形・Lie代数・退化幾何等を含むA全体の監査は
`notes/poisson_article_submission_audit.md`を参照する。

以下は2026-11-13に**現行スクリプトを直接実行した状態**である。
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

実行対象のSHA256：

```text
83ee2cef8ab984b2bb92bfef9f1947b5f58a1ca1bbd0adf466c3af8dca736229  computations/verify_universal_hesse_mixed_center.py
d7faf1134403d3e99a569af9e64c399cc4703200b58cfa33e6faba72b7a850e2  computations/verify_cubic_casimir_jet.py
703d8951c3dff91c2bc3cc3dada11c32056f6f070e297cfc1e305b234c170c5b  computations/verify_singular_cubic_classical_kernel.py
b0c00fa02004e778c516d5e93e7c7ecf9d103dbce607897a10fdbe271d2b5966  computations/verify_nonelliptic_quantization.py
```

重い記号計算は一本ずつ実行する。
LuaLaTeXによる再生成コマンドは`latexmk papers/paper_a.tex`で、
PDFと中間生成物は`build/`へ出力される。
**A-v52全体の組版・参照検査・PDF確認および計算の最終実施状態は、
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

1. Cramer中心元のチャートを越えた正準化・同変接着と、相対Poissonモジュライ上の大域量子化。
   まず二つの非零小行列式の共通開上で、規格化の違いと中心元の差を比較する。
2. 特異・零の三変数制限に対する短い普遍多項式表示の存在。
   Cramer式の分母と特異型ごとの有限関係式を調べ、単なる可逆な中心元の再規格化で除去できる分母を区別する。
3. 全閉パラメータにおけるqgrの滑らかさ、可換特殊点を含む一変数・多変数底全体での相対残余圏の比較。
   一般点の結果を特殊点へ延長する際のproperness・対角のperfect性・底変更を確認する。

形式的存在証明への変更は、これらの問題を解くための前提ではない。
