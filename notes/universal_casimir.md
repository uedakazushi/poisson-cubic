# 普遍Jacobian量子中心三次元：現行研究ノート

**2026-11-12 / v2。** 最初に \`00_research_plan.md\` を読む。
公表用原稿は \`papers/paper_a.tex\`、主要証明は
\`papers/support/papers/sections/fermat_mixed_universal_center.tex\` と
\`papers/support/papers/sections/universal_casimir_determinant.tex\`。
このノートは現行の適用範囲・障害・再現手順を整理し、論文中の証明全文を複製しない。

## 1. 完全に明示した普遍多項式中心元（新たな厳密計算証明）

任意の標数0可換次数付き中心係数環 R について
A,B,C∈R_1、D,E,H∈R_2、G∈R_3 とおく。
F=(x³+y³+z³)/3 +Axy+Byz+Czx+Dx+Ey+Hz+G。
関係式は
[x,y]=h(z²+By+Cx+H),
[y,z]=h(x²+Ay+Cz+D),
[z,x]=h(y²+Ax+Bz+E)。
T=xyz+xzy+yxz+yzx+zxy+zyxとして
\[
\begin{aligned}
\Omega={}&(x^3+y^3+z^3)/3-h^2T/9
+A\operatorname{sym}(xy)+B\operatorname{sym}(yz)+C\operatorname{sym}(zx)\\
&+(D+h^2B^2/6-h^4AC/18)x
 +(E+h^2C^2/6-h^4AB/18)y\\
&+(H+h^2A^2/6-h^4BC/18)z
 +h^4(Az^2+Bx^2+Cy^2)/18+G .
\end{aligned}
\]
**状態：原点h=0を含むPBW開集合上で中心であることを厳密に証明。**
「形式的中心元存在補題」を使わず、次数4の自由語の関係式への普遍的所属を証明した。
係数A,B,C,D,E,Hとhを**一切特殊化せず**、
339個の全自由語、162個の関係ベクトルをQ(h)上で行簡約し、
関係ベクトル階数144、[Ω,x],[Ω,y],[Ω,z]の剰余0を厳密に確認。
h=0の関係ベクトル階数も144であり、Q[h]_(h)上の
次数4商がh-torsion-free（行列のSmith標準形）であることから、
分数体上の恒等式を原点を含む開集合へ降ろせる。
**従来の有限体特殊化15件とは異なり、全係数恒等式の計算証明**である。
今後の査読で必要なら、Q(h)の行簡約を人手で追える
短い関係式分解証明書に落とし込む。

系：任意の対角二次混合 p x²+q y²+r z² も、
中心平行移動 X=x+p,Y=y+q,Z=z+r と明示的なD',E',H',G'の代入で処理できる。
従ってFermat三次制限に対して、中心変数の**全混合項**を網羅する。
中央変数の個数には制限がない。
GL3変換・Poissonパラメータの行列式スケールで、
GL3(Fermat)軌道の全例にも適用できる。
証明所在は論文A thm:pg-fermat-mixed-universal、
cor:pg-fermat-all-mixed。

再現：
\`python3 computations/verify_universal_fermat_mixed_center.py\`
（要SymPy）。
ローカルで同じ有理関数行簡約を実行して
「列339、関係162、h=0およびQ(h)階数144、交換子剰余0」を確認。
GitHubへpush後のファイル内容は確認するが、
pushしたスクリプト自体をGitHub実行環境で走らせたとは主張しない。

古典的なHessianジェットとの関係：
H_F=det Hess_{x,y,z}(F)=2(4xyz-A²z-B²x-C²y+ABC)。
上のh²係数は -h²H_F/12 と純中心項 h²ABC/6 の違いしかない。
これは普遍Hessian二次補正と矛盾しない。

## 2. 全滑らかな三変数三次制限：普遍決定式表示

g=F(x,y,z,0)が滑らかな平面三次なら
\`ker D_{F,0}|_{S_3} = C F ⊕ C[u]_3\`。
証明はgの既約性、Euler公式、
uの最小次数の比較。これは量子中心存在の入力不要な数学的補題で、
論文A lem:pg-det-classical-kernel に証明を記載。
r=binom(m+5,3)-binom(m+2,3)-1。
x³の係数a≠0の線形座標チャートで純中心三次とx³を除いた
r個の三次単項式w_jを選び、
\`D_h(p)=([sym p,x],[sym p,y],[sym p,z])/h\`
のr×r非零小行列Mと列bを取る。
第j列をbへ置き換えたM_jを用いると
\[
 \Omega=F(0,0,0,u)+a\operatorname{sym}
 (x^3-\sum_j (\det M_j/\det M)w_j)
\]
が厳密な中心三次元、Ω_0=F、係数はh²とFの係数の有理関数。
**状態：既存の形式的中心三次元存在補題 lem:pg-formal-center を入力とする条件付き厳密定理**。
この補題の相対formality/絶対CY適用を独立完全監査したわけではない。
Fermat基準点の非零小行列は m=0 で9×9 det=-72、
m=2 で30×30 det=4608。
\`python3 computations/verify_universal_casimir_minor.py\`
をローカルで有理数厳密実行し両者PASS。
この計算は古典的な小行列に関するものだけで量子中心性の直接検算ではない。
gが特異・零の場合には古典的Casimir核の次元が変わる可能性があり、
同じ固定行列式を無条件に適用しない。

## 3. 先行研究との関係

論文C周辺の
\`papers/support/papers/sections/mixed_center_picard.tex\` と
\`computations/verify_mixed_center.py\`には
全15混合方向のFermat式が既に存在した。
新たな貢献は、六つの中央係数を**独立不定元**として扱う
全係数に対する厳密な恒等式証明と、任意中心次数・対角混合への明示的拡張。
有限体検算は現在、追加確認であって証明ではない。
従来の式自体を本研究独自の新発見と扱わない。

既知のHesse型Sklyanin中心式と座標変換は
\`papers/support/papers/sections/explicit_hesse_center.tex\`。
節点・尖点型の中心公式は
\`papers/support/papers/sections/nonelliptic_quantization.tex\`。
Etingof--Ginzburg,
*Noncommutative del Pezzo surfaces and Calabi--Yau algebras*,
J. Eur. Math. Soc. 12 (2010), 1371--1416,
doi:10.4171/JEMS/235, Proposition 8.1.1(i)は
形式的中心元存在に関係。
新しい決定式の先行研究上の新規性・他の短い普遍公式の存在は
十分な文献調査をしていないため未確定。

## 4. 優先する未解決問題

1. **Hesse一般値 t と全混合項：** Fermatだけでなく
   g=(x³+y³+z³)/3+txyz について、
   近似Hessian公式・Hesse中心式・有限行列式を統合した
   短いGL3同変な多項式または有理式を求める。
   機械的な30×30決定式は既にあるが、短い一般式は未構成。
2. **全滑らかなgに対する決定式の無条件化：**
   lem:pg-formal-centerの相対formalityと絶対CY分解を独立監査。
3. **特異gへの延長：** Casimir核が跳ぶ場合は階数別に
   新しいminorsが必要。既存の節点・尖点公式と接続する。
4. 投稿用に「確定」「条件付き」「計算証明」「既知」に主張を分け、
   論文A全体のLuaLaTeX組版・一次文献調査を終える。
