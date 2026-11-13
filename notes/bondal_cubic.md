# 滑らかなcubic n-foldに対するBondal予想

**2026-11-14 / A-v55・nc-cubic-v86。最初に `00_research_plan.md` を読む。**
証明全文は `papers/support/papers/sections/bondal_cubic.tex` の `thm:pg-bondal`。
正規形、射影化の補題、分離型三次四様体の分類は
`papers/support/papers/sections/poisson_geometry.tex` にある。
本ノートは証明の要点、確認範囲、先行研究との関係を保持する。

## 現行の結果とjoinの構成

複素数体上の滑らかなcubic n-fold（n>=3）の任意の正則Poisson構造について、
全ての退化軌跡 D_{2j}（0<=2j<n）が次元少なくとも2j+1の既約成分を持つ。
一般階数2kの非零構造には、`thm:pg-normal` の正規形
F=Σ f_s(x_s,u)、N=n+2=3k+mを用いる。
各x_sは三変数で、異なるJacobianブロックは可換、uは中心変数である。

j<kならr=j+1個のブロックを選び、g_s=f_s(x_s,0)と置く。
g_sが非零ならV(g_s)の既約な曲線成分C_sを、g_s=0なら座標平面内の任意の直線C_sを取る。
独立な座標空間にある各曲線のアフィン錐は既約かつ次元2なので、
join J_r=Join(C_1,...,C_r)は既約で次元2r−1である。
その上ではuと他のブロックが零、各g_sも零なのでJ_r⊂Xとなる。

join上のアフィンPoisson階数は高々2rである。
どこかの選択ブロックがrank 0なら既に2r−2以下。
全てrank 2なら、三次Euler等式により各ブロックのEulerベクトルは
ker(dg_s)、すなわちJacobian bivectorの像に含まれる。
全Eulerベクトルは非零であり、その直線を割る射影化でrankが2下がる。
従ってJ_r⊂D_{2r−2}=D_{2j}を得る。j>=kとπ=0ではD_{2j}=Xである。

この証明にはg_sの滑らかさを仮定しない。
結論は退化軌跡の台の次元下界であり、高次退化スキームの被約性・primary分解は含まない。
`prop:pg-deg-ideal` の一般生成イデアルと整合し、
滑らかな平面三次制限を仮定する `lem:pg-critical-cover`、`prop:pg-zero-ci` は証明の入力ではない。

## 分離型三次四様体と一般階数四の分類

滑らかな平面三次式f(x_0,x_1,x_2)、g(y_0,y_1,y_2)に対し、
X=V(f+g)とJacobian括弧の和q_f+q_gは、一般階数四のPoisson構造を与える。
退化因子D=V(f,g)=Join(E_f,E_g)は被約・既約・正規な反標準因子であり、
その特異集合の台は互いに素な二本の楕円曲線E_f、E_gである。
Poisson零点スキームは被約なE_f⊔E_gで、そこではmodularベクトル場が零でない。
従ってPymのDefinition 4.2の意味でpurely elliptic log symplecticである。
構成と一般のf,gについての局所証明は `prop:pg-split-elliptic` にあり、
この命題自体は正規形定理に依存しない。

逆に、滑らかな三次四様体の一般階数四の全Poisson構造は、適当な分離表示でこの形になる。
必要性は `thm:pg-normal` のN=6、k=2、m=0の場合、十分性は上の明示構成による。
正確な同値と依存関係は `cor:pg-cubic-fourfold-elliptic` を参照する。
被約なPoisson零点スキームを退化因子の特異スキームと混同しない。
後者は各楕円曲線の横断方向に長さ8の厚みを持つ
（`rem:pg-split-singular-schemes`）。

## 数学的監査の到達点

正規形からjoinの含有までの証明を独立に追跡し、現行の仮定・結論を弱める必要がある問題は見つからなかった。
確認範囲は以下の通りである。

- `prop:pg-represent`、`prop:pg-jacobi-extension`、`lem:pg-linearize`：Euler列とgradient Koszul複体、divergenceによるJacobiの延長、Hessian条件への線形化。現行本文ではdivergenceの係数NとHessian条件の符号も明示している。
- `lem:pg-quadratic-lie`：基点自由性からVとsupportの双方で非退化なBを選ぶこと、可解根基のscalar作用とtraceによる排除、最高根を用いたrank 2以上の単純因子の排除。
- `thm:pg-normal`：三変数ブロック分解、逆向きのJacobi条件、射影空間とX上の一般階数2k。m=0では全f_s=0がXの真閉集合となる点も確認した。
- `lem:pg-projective-rank` と `thm:pg-bondal`：双ベクトルの像に含まれる直線で割るとrankが2下がり、含まれなければrankが保たれること、およびjoinの各点への適用。
- `prop:pg-split-elliptic`：独立変数のJacobian括弧、完全交叉とSerre条件によるDの正規性、暗黙消去した局所座標でのPfaffianとmodular場の非消滅。明示構成・局所計算を独立に確認した。
- `cor:pg-cubic-fourfold-elliptic` と `rem:pg-split-elliptic-lift-obstruction`：N=6の正規形からの分類、および非連結な曲線に沿う三重消滅をambientへ持ち上げられない障害。

Lie理論の外部入力はEtingof, *Lie Groups and Lie Algebras* の
Proposition 16.9、Definition 21.13／Lemma 21.14、Theorem 25.17、§32.2を
[MIT公開原稿](https://live.ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf)で照合した。
Euler--divergenceの既知前史と半単純Lie代数の核計算は後述のBondal、Derdzinski–Galと照合した。
原稿に証明があることに加え、上記の論証を独立に確認したという状態であり、
計算機による一般定理の形式検証や外部査読を完了したという意味ではない。

## 厳密計算と再現方法

リポジトリ根で次を実行する。依存はPythonとSymPyである。

```sh
python3 computations/verify_poisson_article_A.py
python3 computations/verify_split_cubic_fourfold.py
```

`verify_poisson_article_A.py` は前回の監査で次のPASSを確認済みであり、
現行コードは同一であり、A-v55の今回の検証でも再実行してPASSを確認した。

```text
PASS: smooth test cubic, 56 Jacobi and 56 Euler-wedge identities
```

対象は共有中心u,vを持つ二ブロックの具体例
F=(x³+y³+z³+a³+b³+c³+u³+v³)/3+uxy+vabである。
有理係数の厳密演算により、gradient理想の零次元性による滑らかさ、
56成分のJacobi恒等式、二つの平面三次曲線のjoin上の
56成分のEuler外積恒等式を確認する。
これは一つの具体例に対する検算である。

`verify_split_cubic_fourfold.py` は2026-11-13にSymPy 1.14.0で実行し、終了コード0と全PASSを確認した。
対象はF=(x_0³+x_1³+x_2³+y_0³+y_1³+y_2³)/3という分離型Fermat例である。
次の恒等式を有理係数で厳密に検算した。

- ambient六変数で20個のJacobi恒等式とFのCasimir性。
- x_0=1の射影座標(a,b,c,d,e)で全10括弧、10個のJacobi恒等式、三次方程式への接性。
- H=1+a³+b³+c³+d³+e³=0、b≠0の局所座標(a,c,d,e)で、暗黙微分D_t=∂_t−(t²/b²)∂_bを用いた括弧の整合性と4個のJacobi恒等式。
- この座標順序でPfaffian=b²(c³+d³+e³)、従ってπ²の係数はその二倍。
- modular規約Z^j=Σ_i D_i(π^{ij})で、divergenceとι_{d log Pfaffian}πの一致、およびE_f上のZ=−3b²∂_a≠0。

Fermat例の有限検算を、全ての滑らかなf,gに対する証明や分類定理の計算機証明とは扱わない。
一般の場合の証明は `prop:pg-split-elliptic`、符号は `eq:pg-split-modular` を参照する。
再生成可能な実行ログの置場はbuild/であり、検証・組版の集約記録は `validation_paper_a.json` に置く。

## 先行研究と初出確認の範囲

### Euler--divergenceとLie代数の既知部分

- Bondal, *Non-commutative deformations and Poisson brackets on projective spaces*,
  MPIM Preprint 93-67 (1993)、[一次PDF](https://archive.mpim-bonn.mpg.de/id/eprint/1398/1/preprint_1993_67.pdf)。
  §4、印刷pp.11–12の無番号Theoremは射影空間上のPoisson構造の一意な斉次divergence-free二次持上げを与え、
  直前のLemmaは係数次数と外冪次数が等しい斉次多重ベクトル上で、
  Euler外積D_Eとdivergence Dに対するD_E D+D D_E=dim(V) idを与える。
  本稿の `prop:pg-jacobi-extension` はこの技法を三次超曲面上のJacobiatorへ適用する。
  三次超曲面からの延長、Hessian条件、全ブロック正規形そのものは同文献の定理ではない。
- Derdzinski–Gal, *Curvature spectra of simple Lie groups*,
  Abh. Math. Sem. Univ. Hamburg 83 (2013), no.2, 219–230、
  [DOI](https://doi.org/10.1007/s12188-013-0085-z)、[arXiv:1304.2801](https://arxiv.org/abs/1304.2801)、
  [確認した著者公開PDF](https://people.math.osu.edu/derdzinski.1/preprints/amsuh14.pdf)。
  同PDFの式(1.4), p.2は `eq:pg-lie-H` と係数・符号まで一致する。
  Theorem B, p.3（証明§5, p.7）は半単純Lie代数上の核を記述する。
  複素単純因子ではsl_2のみが全対称二形式を許し、それ以外の核はKilling形式の一次元空間である。
  sl_3はこの核記述の例外ではない。
  本稿で必要な基点自由性からの可解根基の排除は同定理の仮定へ還元する段階であり、同定理自体の結論とは区別する。

**Derdzinski–Galのブロック復元に関する証明上の注意。**
Lemma 7.1(a), p.10にはCartan三形式から単純直和因子の部分空間が決まると記述されている。
ただし、確認した公開PDFの証明(e)にある「kerΔに属する階数3または6以上の写像の像の包含極小元が単純因子」という手順はそのままでは成立しない。
ここでΔ=Φ(C,−)は同論文の作用素で、Killing形式による同一視でkerΛに対応し、核の元を写像μ:g*→gとみている。
sl_2⊕sl_2上で各Killing形式に関して自己共役な階数1、2の写像Σ_1、Σ_2を取ると、
Theorem BによりΣ_1⊕Σ_2はその核に対応するが、像は三次元の混合部分空間である。
許された非零像の最小次元が三なのでこれは包含極小元であり、どちらの単純因子でもない。
これは当該復元手順への反例であり、Lemma 7.1(a)の結論への反例ではない。
本稿は `papers/support/papers/sections/nonelliptic_poisson_components.tex` の
`ne:blocks` にある縮約階数による独立証明を保持し、この手順に依存しない。

### 一般Fano多様体の退化軌跡

- Gualtieri–Pym, *Poisson modules and degeneracy loci*, Proc. Lond. Math. Soc. 107 (2013), 627–654,
  [arXiv:1203.4293](https://arxiv.org/abs/1203.4293)、[DOI](https://doi.org/10.1112/plms/pds090)。
  Conjecture 1.1が次元下界の定式化、Theorem 7.13が偶数次元Fanoの最大・劣最大退化軌跡の結果で、特にFano四次元の全場合を含む。
- Druel–Pereira–Pym–Touzet, *Bondal's conjecture in dimension five*,
  [arXiv:2606.03424](https://arxiv.org/abs/2606.03424)、[著者公開PDF](https://druel.perso.math.cnrs.fr/textes/bondal5d.pdf)。
  Theorem 1.2／4.3は次元2n+1、n>1のFanoについてD_{2n−4}に次元2n−3以上の成分があることを示し、Corollary 1.3がFano五次元の全場合を結論する。
- Darío Martín Aza, *A note on Bondal's conjecture*,
  [arXiv:2604.07217v1](https://arxiv.org/abs/2604.07217v1)、[PDF](https://arxiv.org/pdf/2604.07217)。
  Theorem 1.3の主張（印刷p.2）と証明（印刷p.10）を照合した。
  仮定は複素Fano Poisson多様体と厳密包含D_{2k−2}⊊D_{2k}であり、結論は
  「D_{2k−2}が次元2k−1以上の既約成分を持つ、**または**D_{2k}が次元2k+1以上の既約成分を持つ」
  という選言である。個々の退化軌跡に対する全ての下界を同時に結論する定理ではない。
  同論文§2のrankは外積の最大非零冪を数える規約なので、本稿の通常の双ベクトルrankとの比較では2倍の違いに注意する。
  確認したのはこの定理の仮定・選言・証明の対応であり、同論文の全依存の独立監査ではない。

これらの一般Fanoの結果は、本稿のjoin証明の入力ではない。
正規形の近い既知結果であるLoray–Pereira–TouzetおよびMayanskiyの
cubic threefoldのGrassmann記述とも区別する。
半単純段階の核計算とブロック内在性は上記の既知の記述と区別して位置づける。
確認した一次文献では任意次元の全ブロック正規形と同一の定理を特定できていないが、
六次元以上のcubicに対する全退化階数の結論と明示的join構成の初出は未確定である。

### Pymの公開原稿との不整合と非連結性の障害

一般次数の命題 `prop:pg-triple-lifting-obstruction` は、滑らかな超曲面X内の滑らかな非空Cの全連結成分が正次元のとき、H¹(P^N,I_C²)=C^{π₀(C)}/Cを与える。三重消失を保つ次数dの持上げの障害はこの群に入り、存在時は一意。分離型のδ(g_X)は[(0,1)]で非零である。証明は現行本文にあり、ここで全文を重複しない。

Pym, *Elliptic singularities on log symplectic manifolds and Feigin–Odesskii Poisson brackets*,
Compositio Math. 153 (2017), no.4, 717–744、
[DOI・刊行情報](https://doi.org/10.1112/S0010437X16008174)、
[arXiv:1507.05668v1](https://arxiv.org/abs/1507.05668v1)、[確認したPDF](https://arxiv.org/pdf/1507.05668)。
定義・主張・証明の比較はarXiv v1による。
Definition 4.2とRemark 4.4（p.17）の条件を分離型構成が満たすことを直接確認した。
この構成は同版Theorem 1.3（p.4）の三次四様体での非存在と、
Proposition 5.7（p.30）の二本の楕円平面三次に沿う非正規性の記述とは両立しない。

障害はLemma 5.5（pp.28–29）のambient持上げの議論にある。
C=E_f⊔E_gは非連結で、H¹(P⁵,I_C)≅ℂ、さらにH¹(P⁵,I_C²)≅ℂとなり、使用される消滅は成立しない。
具体的にもg|_Xのambient三次持上げg+λ(f+g)に対し、
E_f沿いの三重消滅はλ=0、E_g沿いではλ=−1を要求する。
各連結成分で選べる持上げを同時には選べないことが本質である。
持上げ列の接続準同型によるδ(g|_X)は、一次元のH¹(P⁵,I_C²)の生成元となる。
詳細は `rem:pg-split-elliptic-lift-obstruction`、
`eq:pg-split-lifting-sequence`、`eq:pg-split-obstruction-class` にまとめている。

**刊行版本文およびaccepted manuscript本文は未取得であり、刊行版・訂正文との最終照合は未了。**
[Oxfordの公開登録](https://ora.ox.ac.uk/objects/uuid:a457621f-f733-41b0-99c7-fa475b8e807e)には
accepted manuscript `ell-log-symp.pdf`（444 KB、受理日2016-07-18）の登録がある。
[具体的な公開ファイルURL](https://ora.ox.ac.uk/objects/uuid:a457621f-f733-41b0-99c7-fa475b8e807e/files/m9ef175dec65308db41a9059fb7ac8247)は特定できたが、通常取得は403である。
[著者の現行論文一覧](https://www.math.mcgill.ca/bpym/papers-bib.html)はDOIとarXivへのリンクを案内し、
[Crossrefの当該DOI登録](https://api.crossref.org/works/10.1112/S0010437X16008174)にも訂正を結ぶrelation・update情報は確認できない。
この範囲で訂正案内を確認できていないという状態であり、訂正文の不存在や刊行版にも同じ記述があることを推測しない。

後続文献については、次の二つを区別する。

- Pym, *Constructions and classifications of projective Poisson varieties*,
  Lett. Math. Phys. 108 (2018), no.3, 573–632、
  [刊行本文・DOI](https://doi.org/10.1007/s11005-017-0984-5)。
  §5.2のTheorem 5.12直後は、元論文が他のいくつかのFano四様体でも非存在を示すと概括する。
  三次四様体の場合の訂正や、非連結な曲線の持上げ障害の指摘ではない。
- Harder, *Mixed Hodge structures in log symplectic geometry*,
  [arXiv:2005.11367v1](https://arxiv.org/abs/2005.11367v1)、[PDF](https://arxiv.org/pdf/2005.11367v1)。
  §4.2、Theorem 4.3（p.17）は特異曲線Cがconnectedであることを明示的に仮定する。
  従って本稿のC=E_f⊔E_gへそのまま適用できず、Pymの三次四様体非存在を訂正する記述でもない。

## 継続する課題

公表前の文献確認では、まずPymの刊行版本文またはaccepted manuscriptを取得し、
Theorem 1.3、Lemma 5.5、Proposition 5.7に相当する箇所と訂正文の有無・内容を照合する。
分離型構成の独立な証明は保持し、文献側の版によって数学的結論を推測で変更しない。
全次元正規形とjoinの初出比較では、Hessianの基点自由性から半単純性への還元を優先して調べる。
Bondalの持上げ、Derdzinski–Galの半単純核計算、三次元分類、一般Fanoの特定退化階数、本稿の幾何学的構成を区別する。
高次退化スキームのprimary構造を研究する場合は `prop:pg-deg-ideal` から始め、
台の包含だけから被約性や成分の重複度を推論しない。
