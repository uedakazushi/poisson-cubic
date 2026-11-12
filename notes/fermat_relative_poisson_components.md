# 固定FermatのPoisson space・商スタックと相対Poissonモジュライ

**2026-11-12 / v2。再開時は最初に `00_research_plan.md` を読む。**
現行公表原稿は `papers/paper_a.tex`、
定義・代数性の証明は
`papers/support/papers/sections/poisson_moduli_stacks.tex`、
既約成分の証明は
`papers/support/papers/sections/fermat_relative_poisson_components.tex`。
旧資料の取得は不要。

## 定義、代数性と重要な区別

- **space of Poisson structures**：
  `Pois(X)=Z([pi,pi])⊂H⁰(X,Λ²T_X)`。
  quadratic Jacobi equations による有限型アフィンスキームで、
  零Poissonを含み、nilpotent scheme構造は維持する。
- **moduli stack of Poisson structures**（固定X）：
  `PoisStack(X)=[Pois(X)/Aut(X)]`。
  各点のstabilizerがPoisson automorphism group `Aut(X,pi)`。
  `n>=3`のsmooth cubicで `Aut(X)` は有限エタール：
  Pic(X)=Z O_X(1)（SGA2 Exposé XII Cor 3.7）から全自己同型が
  PGL(V)へ延長し、`A(F)=cF` の一次のgradient syzygyを
  smoothness＋Koszulで排除してLie Aut(X)=0。
  よって固定stackは有限型Deligne--Mumford代数的スタック。
  **固定stackの成分数はPois(X)の成分のAut(X)軌道数**であり、
  spaceと同じとは限らない。
- **relative moduli stack of Poisson structures**：
  `PoisRel_n=[P_n/PGL(V)]`、`N=n+2`。
  滑らかな三次式の開 `U_N⊂P(Sym³V*)` 上の
  `E=Λ³V⊗O_U(-1)` の全空間に、
  relative Jacobi二次方程式の零スキーム `P_n` が閉部分として入る。
  局所で `pi=i_{dF}P`。FをaFに替えたらPをP/aに替えるので
  Eは正しく張り合わさる。
  PGL(V)は滑らかで作用groupoidのsource/targetも滑らかなため、
  Stacks Project Theorem 97.17.2, tag 06FI を適用し代数的有限型。
  各幾何学的stabilizerが有限エタールなAut(X,pi)なのでDM。
  零Poissonを含む。
  cubicのモジュライstackへの忘却射を持つ。
  Xへの枠付けを持つ2-fiberはPois(X)、
  Xの同型類上のresidual gerbeに沿った非枠付きfiberは
  [Pois(X)/Aut(X)]。これらを混同しない。

## Fermatの三種類の成分数（証明を原稿に記載）

`F_N=Σ_i z_i³`とし、`N=n+2`。
集合`{1,...,N}`の各大きさ≥3の非順序ブロック分割
`mathcal B={B_1,...,B_k}`に対して
`Z_B=Σ_{B∈mathcal B} cone(Gr(3,C^B)) ⊂ Λ³C^N`。
これらが`Pois(X_N)_{red}`の全既約成分。
一般rankは2k、成分の次元は3N-8k。
この記述は `thm:pg-normal` に依存し、その全証明の独立監査は未完了。

**space** の成分数：
`Σ_{k=1}^{floor(N/3)} S_≥3(N,k)`、
ここで`S_≥3(N,k)`は大きさ≥3のk個の非順序部分集合への分割数。
指数母関数は
`Σ_N S_≥3(N,k)t^N/N! = (e^t-1-t-t²/2)^k/k!`。

**固定stack** の成分数：
`p_≥3(N)=[q^N]∏_{b≥3}(1-q^b)^(-1)`。
理由はFermatのHessian判別式が`∏z_i`なので、
どの射影自己同型も座標超平面を置換するmonomial行列であり、
`Aut(X_N)≅(μ_3^N/μ_3)⋊S_N`。
S_Nはブロックサイズの多重集合が同じ分割に推移的に作用し、
サイズ多重集合が異なる成分は混同されない。
**これを space の集合分割数と同一視してはいけない。**

**relative stack** の成分数：
`floor(N/3)`。
正規形による一般rank2k層は一つずつ既約。
k増加で縮約写像のrankは上がり、閉包関係では
小rank層は大rank層を含まず、逆向きは既約層の次元の
厳密減少によって排除される。
PGL(V)は連結だから成分を置換しない。
零Poisson切断は既存のrank2成分の閉包に入る。

| n | N | Fermat space | fixed stack | relative stack |
|---:|---:|---:|---:|---:|
| 3 | 5 | 1 | 1 | 1 |
| 4 | 6 | 11 | 2 | 2 |
| 5 | 7 | 36 | 2 | 2 |
| 6 | 8 | 92 | 3 | 2 |
| 7 | 9 | 491 | 4 | 3 |
| 8 | 10 | 2557 | 5 | 3 |
| 9 | 11 | 11353 | 6 | 3 |
| 10 | 12 | 60105 | 9 | 4 |

一般のsmooth cubicではspaceもfixed stackも一つの成分だけを
持つ（論文A cor:pg-generic）。固定stackの成分数は複素構造に
依存する。Fermatが全smooth cubicで最大と証明したわけではない。

## 主張の確実性と再現

- 原稿に代数性と成分公式の数学的証明を記載した。
  この作業で全一次資料を網羅調査した意味ではない。
  元のPoisson正規形・Fermatの分割分類・相対rank層の
  依存証明全体を独立に再監査したわけではない。
- Stacks Project tag 06FI の定理文、
  Grothendieck–Lefschetz Picard（SGA2 XII Cor 3.7）、
  Matsumura–Monskyの自己同型群の既知結果を照合。
- `python3 computations/verify_poisson_stack_component_counts.py` は
  n=3,...,10に対し集合分割数・整数分割数・floor(N/3)
  の全表を厳密整数演算で検算。
  計数式の検査でありPoisson正規形の証明ではない。
- `python3 scripts/verify_article_a_numbering.py` は式番号、
  `eqref`、`bibitem`の静的整合性検査（LuaLaTeX組版ではない）。
- `latexmk papers/paper_a.tex` で論文AをLuaLaTeX組版する。
  最新v48の全原稿の組版・PDF目視確認は今回未実施。

## 次の優先事項

現在のPoisson stack定義とFermat・relative成分公式を
論文AのIntroductionに適切に置いたので、
本稿の主結果の全依存監査（とくに正規形のLie補題）、
モジュライ成分のscheme構造・交叉の扱い、
全一次文献照合とLuaLaTeX組版を行う。
