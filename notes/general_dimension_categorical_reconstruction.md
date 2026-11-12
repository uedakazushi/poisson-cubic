# 論文B：一般次元のrotation付き可換復元

**2026-11-12 / B-v41。** 再開時は `00_research_plan.md`、次に `notes/paper_b_proof_audit.md` を読む。

現行主定理 `gdr:thm:generic` は `papers/paper_b.tex` から入力する `papers/support/papers/reconstruction/general_dimension_recovery.tex` にある。方程式の定義体と圏同値の定義体を分ける。新しい一般点の証明と仮定整理は同ディレクトリの `generic_cubic_descent.tex`。

## 現行の結論

代数的・次数別有限自由な中心三次対の滑らかな可換特殊ファイバーと、実際の局所window/proper模型(L)、完備graded MF同値(CF)を仮定する。一般点ambientのAS正則性はflat入力から従う。元の体K=C(h)上のsmooth cubic Yと、有限拡大K'/K上の全coherent残余pair同値を得る。模型は全n>=3で幾何学的に一意。幾何学的一般点で任意の非零対象とその二つのrotationの直和の生成時間は2(n+2)(n+3)-1以下（BFKの既知結果）。

主経路は固定三対象比較→Euler非零性→BFK生成→有限降下→coherent飽和→低Nat底変更→K上の勾配積分。(CF)全体の代替として `gcd:prop:three-object` のenhanced比較でも十分。単なるcohomology次元や積表の一致は代替にならない。

## 残る核心

(L),(CF)の全enhancement・coherent inverse・底変更・periodicityの独立監査は未完。具体的な既知混合多項式の指定には(D)を使うが、一般存在には不要。有限拡大を同値側から取り除くこと、特殊点で正則な模型、同値核の行列、全モジュライへの接着は未証明。

多変数正則局所基底では同じ(L),(CF)の下で分数体上の結論を得る。多変数のKoszul消去の代数部分は証明したが、その事実だけで全族のMF比較が成立したとは扱わない。

## 再現

`latexmk papers/paper_b.tex`（全文組版）、`python3 computations/verify_generic_cubic_descent.py`（可換入力の有限線形代数）。実施範囲は `validation_paper_b.json`。先行研究と証明監査の詳細は `notes/paper_b_proof_audit.md` に集約する。
