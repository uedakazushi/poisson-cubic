# 滑らかなcubic n-foldに対するBondal予想

**2026-11-13 / A-v52・nc-cubic-v83。最初に `00_research_plan.md` を読む。**
証明全文は `papers/support/papers/sections/bondal_cubic.tex` の `thm:pg-bondal`。
正規形と射影化の補題は `papers/support/papers/sections/poisson_geometry.tex` にある。
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

## 数学的監査の到達点

正規形からjoinの含有までの証明を独立に追跡し、現行の仮定・結論を弱める必要がある問題は見つからなかった。
確認範囲は以下の通りである。

- `prop:pg-represent`、`prop:pg-jacobi-extension`、`lem:pg-linearize`：Euler列とgradient Koszul複体、divergenceによるJacobiの延長、Hessian条件への線形化。現行本文ではdivergenceの係数NとHessian条件の符号も明示している。
- `lem:pg-quadratic-lie`：基点自由性からVとsupportの双方で非退化なBを選ぶこと、可解根基のscalar作用とtraceによる排除、最高根を用いたrank 2以上の単純因子の排除。
- `thm:pg-normal`：三変数ブロック分解、逆向きのJacobi条件、射影空間とX上の一般階数2k。m=0では全f_s=0がXの真閉集合となる点も確認した。
- `lem:pg-projective-rank` と `thm:pg-bondal`：双ベクトルの像に含まれる直線で割るとrankが2下がり、含まれなければrankが保たれること、およびjoinの各点への適用。

Lie理論の外部入力はEtingof, *Lie Groups and Lie Algebras* の
Proposition 16.9、Definition 21.13／Lemma 21.14、Theorem 25.17、§32.2を
[MIT公開原稿](https://live.ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf)で照合した。
原稿に証明があることに加え、上記の論証を独立に確認したという状態であり、
計算機による一般定理の形式検証や外部査読を完了したという意味ではない。

## 厳密計算と再現方法

リポジトリ根で次を実行する。依存はPythonとSymPyである。

```sh
python3 computations/verify_poisson_article_A.py
```

現行スクリプトを実行し、次の出力を確認した。

```text
PASS: smooth test cubic, 56 Jacobi and 56 Euler-wedge identities
```

対象は共有中心u,vを持つ二ブロックの具体例
F=(x³+y³+z³+a³+b³+c³+u³+v³)/3+uxy+vabである。
有理係数の厳密演算により、gradient理想の零次元性による滑らかさ、
56成分のJacobi恒等式、二つの平面三次曲線のjoin上の
56成分のEuler外積恒等式を確認する。
これは一つの具体例に対する検算であり、任意次元・任意入力に対する上の数学的証明とは区別する。

## 先行研究と初出確認の範囲

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
限定的な一次文献調査では任意次元の全ブロック正規形と同一の定理を確認できていないが、
六次元以上のcubicに対する全退化階数の結論と明示的join構成の初出は未確定である。

## 継続する課題

公表前には、全次元の正規形とjoinによる全退化階数の次元下界について、
近い分類定理と引用先を追加照合して適用仮定・結論・構成の重複を確定する。
既知の三次元分類、一般Fanoの特定退化階数の結果、本稿の明示join構成を区別して序論へ反映する。
高次退化スキームのprimary構造を研究する場合は `prop:pg-deg-ideal` から始め、
台の包含だけから被約性や成分の重複度を推論しない。
