# 一般Jacobian三次量子化の普遍中心元

**2026-11-12 / v1。研究を再開するときはまず 00_research_plan.md を読む。**
研究本文・証明は
\`papers/paper_a.tex\` から読み込む
\`papers/support/papers/sections/universal_casimir_determinant.tex\`。
本ノートは結果の状態、有限アルゴリズム、先行した論文C関係の成果、残課題をまとめる。

## 現在の到達点と状態

### 古典Casimirの厳密な核（新しく証明）

任意の中心変数 \`u=(u_1,...,u_m)\` と斉次三次
\`F(x,y,z,u)\` に対し、\`g=F(x,y,z,0)\` が滑らかな平面三次なら、
Jacobian Poisson括弧の全次数3 Casimir空間は厳密に
\`C F ⊕ C[u]_3\`。証明は \`g\` の既約性、Euler公式
\`3g ∂_i p = deg(p) p ∂_i g\` による小次数のCasimir消滅と、
\`u\`-adic最小次数の帰納。論文A
\`lem:pg-det-classical-kernel\` に詳細な証明を掲載。
これは元の量子中心存在補題に依存しない古典結果。

### 有限行列式による普遍的有理公式（形式的中心元存在を入力）

三次Weyl単項式空間の次元
\`N3=binom(m+5,3)\`、純中心三次の次元
\`d=binom(m+2,3)\`、非中心補空間 \`W\` の次元
\`r=N3-d-1\`。
active座標を選び \`a=[x³]F ≠0\` として、
\`W\` は純中心三次と \`x³\` を除いた \`r\` 単項式で張る。
Weyl座標基底を使い
\`D_h(p)= ([sym(p),x],[sym(p),y],[sym(p),z])/h\`
を有限行列にする。
\`D_0|_W\` の非零 \`r×r\` 小行列 \`M\`、対応する
\`D_h(x³)\` 列 \`b\` を選ぶ。第j列をbで置換した小行列を \`M_j\` とする。
すると
\[
 \Omega=F(0,0,0,u)+a\Bigl(x^3-
 \sum_{j=1}^r\frac{\det M_j(h)}{\det M(h)}\operatorname{sym}(w_j)\Bigr)
\]
が \`det M(h)≠0\` 上で厳密な中心三次元となり、
\`Ω_0=F\`。全係数は \`h²\` の有理関数で、\`det M(0)≠0\`。
これは量子中心の全次数での中心性を線形代数から証明するが、
**既存の形式的中心三次元存在補題 lem:pg-formal-center を入力としている**。
相対formality/絶対CY証明の独立監査は未完成。
したがって存在に関する未確認の論理依存を隠さない。
短いGL3不変式による閉多項式公式は得ていない。

固定した行列チャートは \`F\` の係数にも有理的に依存するため
**一般の混合三次係数を同時に扱う普遍決定式**となる。
任意の滑らかな \`g\` では非零小行列を取り直せばよく、
開被覆上で同じ形の式になる。
\`g\` が特異・零なら古典Casimir核の次元が増える可能性があり
この単純な \`r×r\` 公式は無条件ではない。

### 正確な厳密検算

\`computations/verify_universal_casimir_minor.py\` は
Fermat \`F0=(x³+y³+z³)/3 + G(u)\` における
\`D_0|_W\` をSymPy有理数演算で計算する。
辞書式降順のmonomial basis、出力行はx,y,zの順とすると、
- \`m=0\`: \`N3=10,r=9,det M=-72\`;
- \`m=2\`: \`N3=35,r=30,det M=4608\`。

**上の二つは実際にPythonで再計算しPASS。**
この検算は古典的主小行列の非消滅を示し、
量子中心性の計算チェックではない。
量子中心性は存在補題と階数一定性からの論理的帰結である。

## 論文C周辺に既にあった公式

\`papers/support/papers/sections/mixed_center_picard.tex\` の
全混合Fermat型の15方向の表示は、既存の技術原稿の式を引き継ぐ
（今回発見した公式ではない）。
\[
 F=\tfrac{x^3+y^3+z^3}{3}+Axy+Byz+Czx+Dx+Ey+Hz+G(u),
\]
\`A,B,C∈C[u]_1\`, \`D,E,H∈C[u]_2\` とすると、
同資料の候補は
\[
\begin{aligned}
 \Omega_{\mathrm{mixed}}={}&\operatorname{sym}(F)
 -\tfrac{h^2}{9}\sum_{\sigma∈S_3}\sigma(xyz)
 +\tfrac{h^2}{6}(B^2x+C^2y+A^2z)\\
 &+\tfrac{h^4}{18}(Az^2+Bx^2+Cy^2-ACx-AB y-BC z).
\end{aligned}
\]
有限体の15特殊化に対する全交換子の理想所属は
\`computations/verify_mixed_center.py\` により確認されていた。
**普遍係数での独立証明は未完成**。
上式は短い既存候補であり、今回の決定式は条件付きで厳密に中心となる。
両者が一致することを新しい定理としては主張しない。

\`H_F=det Hess_{x,y,z}F\` を直接計算すると
\`H_F=2(4xyz-A²z-B²x-C²y+ABC)\`。
したがってこの候補の \`h²\` 項は
\`-h²H_F/12\` と中心三次項 \`h²ABC/6\` の差しかない。
普遍二次Hessian補正との整合性は**証明できる**。

特異三次曲線の節点/尖点ブロックの公式は
\`papers/support/papers/sections/nonelliptic_quantization.tex\`、
Hesse型の短い既知Sklyanin公式は
\`papers/support/papers/sections/explicit_hesse_center.tex\`。
形式的中心存在の初期研究はEtingof–Ginzburg,
*Noncommutative del Pezzo surfaces and Calabi-Yau algebras*,
JEMS 12 (2010), 1371–1416, Proposition 8.1.1(i)
(doi:10.4171/JEMS/235)。
新しい行列式表現の先行研究上の新規性は未調査。

## 次に取り組む課題

1. 最重要：式 \`lem:pg-formal-center\` の相対formalityと
   完備absolute Calabi–Yau分解を独立監査し、普遍決定式定理の
   形式的存在入力を確定する。
2. 全15混合Fermat型の候補閉公式を、有限体特殊化ではなく
   普遍多項式恒等式として証明し、決定式との一致を確認する。
3. Hesse型一般値tと任意混合方向で
   \`M(h,F)\` の係数を生成し、単純な有理式/多項式の形へ簡約する。
   これにより短いGL3同変な不変式公式を探索する。
4. 古典Casimir核の階数が増える特異ブロックについて
   小行列チャートを細分し、既存の節点・尖点公式へ接続する。
5. 論文A全体のLuaLaTeX組版、計算証明書再実行、文献一次照合を完了する。
