# 固定FermatのPoisson space・商スタックと相対Poissonモジュライ

**2026-11-14 / v6（論文A-v58、nc-cubic-v90）。再開時は最初に `00_research_plan.md` を読む。**
現行公表原稿は `papers/poisson-cubic.tex`、
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
  `P_n→U_N` は有限型アフィン射であり、閉埋込みは
  `P_n→Tot(E)`。忘却射と閉埋込みを区別する。
  GL(V)の中心スカラーはΛ³VとO_U(-1)に逆の重みで作用するため、
  作用はPGL(V)へ降りる。
  PGL(V)は滑らかで作用groupoidのsource/targetも滑らかなため、
  Stacks Project Theorem 97.17.2, tag 06FI を適用し代数的有限型。
  各幾何学的stabilizerが有限エタールなAut(X,pi)なのでDM。
  零Poissonを含む。
  cubicのモジュライstackへの忘却射を持つ。
  Xへの枠付けを持つ2-fiberはPois(X)、
  Xの同型類上のresidual gerbeに沿った非枠付きfiberは
  [Pois(X)/Aut(X)]。これらを混同しない。

相対表示の任意の底変更への適合性は、幾何学的点での同型だけからは
結論しない。三次代表を選んだ各アフィンチャートで、偏微分の相対Koszul複体を
斉次次数ごとに考える。各ファイバーでは偏微分が正則列をなし、
Jacobian環のHilbert級数は `(1+t)^N`。
正のKoszulホモロジーは零、次数零ホモロジーの次元は一定なので、
各微分の階数は一定となる。被約な基底U_N上で局所的に行列を分割でき、
複体は局所自由なJacobian環の次数部分を分解する局所分裂複体となる。
したがって任意の底変更後も完全性を保つ。
`prop:pg-represent` の表示と `prop:pg-jacobi-extension` のJacobi延長は、
この複体と標数零で可逆なN−3による除法に適合する。
これにより相対Jacobi方程式は自然な非被約Poisson scheme構造を保って貼り合わさる。

## Fermatの三種類の成分数（証明を原稿に記載）

`F_N=Σ_i z_i³`とし、`N=n+2`。
集合`{1,...,N}`の各大きさ≥3の非順序ブロック分割
`mathcal B={B_1,...,B_k}`に対して
`Z_B=Σ_{B∈mathcal B} cone(Gr(3,C^B)) ⊂ Λ³C^N`。
これらが`Pois(X_N)_{red}`の全既約成分。
一般rankは2k、成分の次元は3N-8k。
この記述は `thm:pg-normal` に依存する。
Fermatの対角Hessianから各 `i_{dz_i}P` が分解可能となり、
正規形の異なる3次元支持ブロックは互いに素な座標集合に含まれる。
未使用の座標をブロックへ加えることで上の分割による被覆を得る。
縮約写像の階数と、一般点での支持ブロックの内在性により、
異なる分割が異なる既約成分を与える。

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

ここで成分数・次元の議論は**被約rank層とその閉包**について行う。
局所表示Pの縮約写像 `Λ²V*→V` の階数が3kとなる条件が局所閉層を定める。
`m=N−3k`、`P_k=e_123+e_456+...+e_(3k−2,3k−1,3k)` とすると、
三次式の滑らかなアフィン錐へ引き戻した層は
`GL_N ×^{Stab(P_k)} F_(N,k)^sm` で表される。
安定化子の次元は `8k+3km+m²`、軌道の次元は `k(3N−8)`。
固定P_kに適合する三次式は、異なるactiveブロック間のHessian成分が零となる
線形空間をなし、その次元は

`ell_(N,k)=binom(m+2,3)+k(10+6m+3 binom(m+1,2))`。

その滑らかな部分はFermat三次式を含む非空既約開集合である。
自由なG_m作用 `(F,P)↦(aF,a^(−1)P)` で割って射影的な三次パラメータへ戻すと、
相対rank層の次元は `k(3N−8)+ell_(N,k)−1`。
さらにPGL_Nで割ったstack次元は

`d_(n,k)=k(3N−8)+ell_(N,k)−N²`。

隣接するrank層の次元差は `3(3k−1)(N−3k)+8>0`。
これと縮約階数の半連続性を併用して、異なるrank層の閉包の相互非包含を得る。
G_m商は三次式の代表を選ぶ自由度を除く操作であり、Poisson bivectorの
スカラーを射影化する操作ではない。

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

## 主張の確実性、証明監査と再現

代数性と成分公式の数学的証明は上記の二つの原稿節にある。
固定・相対stackの代数性、忘却射のアフィン性、相対Koszul複体の局所分裂と
任意底変更、G_mのスカラー規約、Fermatの座標分割による被覆、
被約rank層の既約性・次元・閉包の非包含を独立に点検した。
証明は正規形 `thm:pg-normal`、ブロックの内在性 `ne:blocks`、
相対表示 `prop:pg-represent` とJacobi延長 `prop:pg-jacobi-extension` を用いる。
これらを含む論文A全体の依存監査と一次資料の照合範囲は
`notes/poisson_article_submission_audit.md` を参照する。
Stacks Project tag 06FI、Grothendieck–Lefschetz Picard定理
（SGA2 XII Cor 3.7）、Matsumura–Monskyとの関係は
`poisson_moduli_stacks.tex` の証明・引用に記載している。
ここでいう独立点検は数学的な論証の監査であり、形式証明系による検証ではない。

次の二つの計算スクリプトは2026-11-13の監査で実際に実行し、成功した。

- `python3 computations/verify_poisson_stack_component_counts.py`：
  n=3,...,10について集合分割数・整数分割数・floor(N/3)の全表が一致。
  厳密整数演算による計数式の検査であり、Poisson正規形や一般次元の成分分類を
  計算で証明したものではない。
- `python3 computations/verify_nonelliptic_components.py --direct`：
  二つの固定smooth cubic fivefold（node/cusp例）の35列の接空間行列を再計算し、
  ともにrank33、核次元2を確認。
  `computations/nonelliptic_components_certificate.json` の33×33小行列と一致し、
  行列式はそれぞれ `8916100448256=2^24·3^12`、
  `−4565043429507072=−2^33·3^12`。
  直接Schouten計算によるJacobi線形化も両例でrank33だった。
  この直接計算は35個の三重添字と84個の三次単項式からなる
  2940係数を用い、零行は省略する。
  スクリプト内のsmoothness、Poisson plane、射影rank4のwitness、
  determinant curveの検査も成功した。
  この証明書が支えるのは固定した二例の成分と接空間であり、
  全cubicを動かした相対成分性ではない。
  数学的な成分性・一般点での被約性の論証は
  `papers/support/papers/sections/nonelliptic_poisson_components.tex` の
  `ne:main` にある。

再生成・整合性検査はリポジトリのルートで行う。

```sh
python3 scripts/build.py --only poisson-cubic
python3 scripts/verify_bundle.py --only poisson-cubic --require-pdfs
```

後者は入力閉包、数値式番号の規約、ラベル・参照・引用と、
現行ソースに対応するPDF・組版receiptを検査する。
LuaLaTeX組版そのものとPDF表示の点検は別の検証であり、
最終実行状態は `validation_paper_a.json` に集約する。

**射程と未解決事項：** 成分公式は基礎位相空間の分類であって、
Jacobi scheme全体の被約性、成分交叉のイデアル、零点の局所環を決定しない。
非楕円二例の検証を一般の相対schemeの被約性へ拡張してはならない。
相対商stackの粗モジュライの存在・構成や、Fermatの成分数の最大性も未証明。
上の成分公式の初出・新規性の包括的な照合は未完であり、
既知の商stack一般論と正規形からの計数的帰結を区別する。

## 次の優先事項

1. 高次元の正規形・Fermatの分割分類・相対rank成分の先行研究との
   比較を進め、既知の入力と公表上の貢献を具体化する。
2. scheme構造を調べる場合は、少数ブロックの交叉と零Poisson点の
   Jacobiイデアルから着手し、被約成分の分類だけでは決まらない厚みを区別する。
3. Fermatの最大性、一般の固定cubicの成分数、粗モジュライの構成は
   独立した問題として扱う。相対Poisson stack上への量子化の降下については
   [量子化の現行ノート](https://github.com/uedakazushi/nc-cubic/blob/main/notes/cubic_quantization.md) と独立した量子化論文の適用範囲を参照する。
