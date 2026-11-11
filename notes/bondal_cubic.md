# cubic n-foldに対するBondal予想

**2026-11-11 / v37。最初に00_research_plan.mdを読む。** 主論文Aの証明全文は `papers/sections/bondal_cubic.tex`。

## 確立した帰結（正規形定理に依存）

滑らかなcubic n-fold（n>=3）の任意のPoisson構造について、Bondal予想の全てのD_{2j}（2j<n）が次元少なくとも2j+1の既約成分を持つ。一般階数2kの非零構造の正規形F=Σ f_s(x_s,u)を使う。j<kならr=j+1ブロックを選び、各座標平面の曲線C_s⊂{f_s(x_s,0)=0}のjoin J_r を取る。各C_sは次元1の既約成分（制限三次式が零なら直線）を選ぶ。joinは既約次元2r−1でXに含まれる。

join上のアフィンPoisson階数は高々2r。どこかのブロックrank0なら既に2r−2以下。全rank2なら各ブロックのEulerベクトルはdf_sの核、すなわち各Jacobian bivectorの像に含まれるので、射影化でrankが2下がる。従ってJ_r⊂D_{2r−2}。j>=kとπ=0ではD=X。

この証明は支持集合の次元のみを与え、退化スキームのprimary分解ではない。すべてのPoisson構造の正規形が成立するという現行稿の `thm:pg-normal` に依存し、その全証明の新たな独立監査は未実施。

## 先行研究と次の課題

Gualtieri–Pym (2013)にBondal予想とFano4-fold、Druel–Pereira–Pym–Touzet arXiv:2606.03424 (2026)にFano5-foldの証明がある。Aza arXiv:2604.07217は追加の証拠であり、一般Fanoの全証明とはしていない。六次元以上のcubicについての優先権・新規性の網羅調査は未完了。

次は正規形のLie代数補題 `lem:pg-quadratic-lie` と射影ランク低下補題の独立検証、joinが既存のD_{2j}スキーム計算と整合することの点検。今回の含有・次元計算は数学的証明であり、全正規形の形式検証ではない。
