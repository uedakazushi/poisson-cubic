# nc-cubic：論文Aの投稿準備と一般点可換復元

**2026-11-12 / v52。GitHub mainが正本。** 最初に [研究方針](00_research_plan.md) を読む。

## 現在の最優先課題：論文Aの公表準備

滑らかなcubic hypersurfaceのPoisson正規形・退化軌跡・Bondal予想・代数的量子化を独立論文として推敲する。
原稿 papers/paper_a.tex、専用文献 papers/support/papers/references_poisson_cubic.tex、
現在有効な証明監査と課題 notes/poisson_article_submission_audit.md、独立有限検算 computations/verify_poisson_article_A.py。
IntroductionとAbstractを改訂し、文献・label静的整合性を点検済み。
主定理の全独立監査、全A組版、全旧証明書再実行は未完成。投稿可能判定は行っていない。
論文B/Cの成果は保持し、新規拡張は論文Aの仕上げの後に再開する。

## 論文Aから独立させた六・七次元の詳細幾何

論文Aは**任意次元の構造定理と量子化・モジュライ**に集中する。
六・七次元固有の退化スキームのprimary分解、embedded components
（横断長8・64、被約化との差の長さ49）、
Calabi--Yau四次元完全交叉のHodge数などは
[独立草稿](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/poisson_cubic_six_seven_geometry.tex)
にまとめた。一般の退化スキームの式と証明は論文Aに残し、
移管先でも必要な背景・証明を本文に収録する。
移管元の6/7次元専用節と数値計算節は論文Aから除外したが、
数学的内容は移管先に保持した。
先行研究上の新規性とprimary分解の独立監査は未完了であり、
副次的研究として継続する。

## Poisson構造のspaceと二つのmoduli stacks

論文Aでは、固定XのJacobi零スキームPois(X)を
**space of Poisson structures**、
その自己同型商[Pois(X)/Aut(X)]を
**moduli stack of Poisson structures**、
Xも変形した組(X,pi)の商[P_n/PGL(V)]を
**relative moduli stack of Poisson structures**
と定義する。n>=3の滑らかなcubicではAut(X)が有限エタールで、
二つのstackは有限型Deligne--Mumford代数的スタック。
証明はpapers/support/papers/sections/poisson_moduli_stacks.tex。

**Fermatでの成分数は三種類を区別する。**
N=n+2、F_N=Σz_i³なら、spaceの成分は
各ブロックのサイズ>=3の集合分割Bごとの
Z_B=Σ_{B_s∈B}cone(Gr(3,C^{B_s}))で与えられる。
固定stackでは座標置換のためサイズの整数分割によって
同一視され、成分数は
p_>=3(N)=[q^N]∏_{b>=3}(1-q^b)^(-1)。
relative stackの成分数はfloor((n+2)/3)。
例えばn=10ではspace=60105、固定stack=9、relative stack=4。
一般cubicでは固定space・stackとも既約。
定理の証明は
papers/support/papers/sections/fermat_relative_poisson_components.tex、
現行研究ノートはnotes/fermat_relative_poisson_components.md。

**論文Aの全表示数学式は自動の数値式番号へ統一した。**
原稿入口はpapers/paper_a.tex、全TeX入力・式番号・参照・引用の
静的検査はscripts/verify_article_a_numbering.py。
最新原稿全体のLuaLaTeX組版とPDF目視は未実施であり、
静的検査だけで組版が成功したとはしない。

## 全Poisson構造の代数的中心元・量子化（論文A v50）

**滑らかな三次超曲面の全Poisson構造について、形式的存在定理を使わず
代数的な中心三次元を構成できることを証明した。**
三変数制限g=f(x,y,z,0)が特異・零でも、
全体fが滑らかならactive偏微分の最大公約因子は1。
古典Casimir核はC f⊕C[u]_3で一定次元となる。
普遍Hesse公式の成立する係数空間の稠密開上から
量子交換子行列の高次小行列式の恒等的消滅を得て、
**全ての滑らかな全体f**へrank上界を特殊化する。
原点で可逆な小行列のCramer比から
厳密な中心三次元をh²の有理関数係数で得る。
この証明は形式的中心元、Kontsevich formality、
Dolgushevのunimodularityを使用しない。

一般次元の正規形F=Σ f_s(x_s,u)では、
純中心三次c(u)を一般的に各blockへ配分することで
全f_sを滑らかな三次超曲面に選べる（Bertini）。
Poisson構造は変化せず、各blockでCramer中心を構成できる。
中心元Ω=ΣΩ_sは厳密に中心、ambientはKoszul AS-regular、
中心三次商はAS-Gorenstein。
独立パラメータη_sにより固定Fのk次元Poisson線形族を
**全方向について同時に代数的量子化**できる。

Hesse型に対しては以前得たη_s⁴までの短い**多項式**公式があり、
任意の特異gに対しては原点で正則な**有理式**Cramer表示がある。
特異gに短い多項式公式まで得たとは主張しない。

- [全体三次のCramer中心元の証明](papers/support/papers/sections/universal_casimir_determinant.tex)
- [全Poisson構造の量子化定理](papers/support/papers/sections/poisson_geometry.tex)
- [全次元・独立k変数同時量子化](papers/support/papers/sections/general_dimension_universal_quantization.tex)
- [現行研究ノート](notes/universal_casimir.md)
- [三変数制限g=0の厳密検算](computations/verify_singular_cubic_classical_kernel.py)

数学的に残るのは、普遍Hesseの記号計算証明書・正規形Lie補題・
PBW/AS条件の全独立監査、モジュライ上の量子化族の接着、
先行研究の初出・新規性比較および全LuaLaTeX組版。
**代数的中心元の存在そのものはこれらと区別して証明済み**とする。

## 量子中心三次元：全Hesse型の普遍多項式公式

論文Aで、`g_t=(x³+y³+z³)/3+txyz`の**任意のtと全中心混合係数**に対する、`h²`の高々二次の係数を持つ**厳密な普遍中心三次元**を構成した。独立係数A,B,C,D,E,Hとh,tを不定元のまま扱い、Q(h,t)上の339自由語・162関係の階数144と三交換子の剰余0を厳密計算した。h=0の階数も144なので原点近傍で成立する。Hessianと四次補正を使ったコンパクト公式あり。

中央平行移動とArtebani–DolgachevのHesse標準形により、**任意の滑らかな三変数三次制限と全混合項**に適用できる。したがってこの範囲では形式的中心元存在補題を使わず代数的量子化を構成でき、元座標のCramer決定式表示も無条件となった。非滑らかな制限を含む全Poisson構造の代数的中心元は上記のCramer法で証明済み。
形式的存在証明の監査はもはや主定理の依存ではない。公式・状態・再現手順は[現行研究ノート](notes/universal_casimir.md)、証明は`papers/paper_a.tex`、検証コードは`computations/verify_universal_hesse_mixed_center.py`。

## 正則三次超曲面のambientは1周期的

標準5次元Koszul AS正則Z代数に次数3の左右正則な正規族があれば、ambientは必ず1周期的。正規族から3周期、Koszul–Frobenius双対性から5周期を得て、2×3−5=1で構成する。一般には最小周期がgcd(N,d)を割る。中心性や周期同型の可換性は不要。証明全文は `papers/support/papers/ambient_cubic_periodicity.tex`、仮定・未解決の区別・再現手順は `notes/ambient_cubic_periodicity.md`。既知の一般論からの系として扱い、新規性は未確認。ambientの1周期性と、商イデアルを保つ1周期構造・中心三次元による表示・任意の抽象的nc cubicの超曲面表示の存在を区別する。単独稿は `latexmk papers/paper_a.tex` で再生成できる。この結果の保存は、上の論文A最優先方針を変更しない。

## Bondal予想（論文Aの新しい帰結）

滑らかなcubic n-fold（n>=3）の全Poisson構造についてBondal予想を証明した。一般rank2kの正規形から、j<kではj+1個のJacobian三変数ブロックの平面曲線join（次元2j+1）をD_{2j}に構成する。既存の正規形定理に依存し、その全証明の独立監査・高次元での新規性確認は未完了。本文 `papers/support/papers/sections/bondal_cubic.tex`、ノート `notes/bondal_cubic.md`。2013年Fano4、2026年Fano5の既存結果を参照。

## Point schemeとPoisson零点（二パラメータでの新定理）

F_λ=(x³+y³+z³)/3+u³+v³+λuxy の混合量子化について、λ³+3≠0、h⁶+27≠0 の範囲で、h非零のpoint schemeはSklyanin楕円曲線 E_h と長さ24の有限平坦成分S_{h,λ}の非交和。h=0のスキーム論的平坦閉包はPoisson零点スキームD0と一致。λ≠0では12個の二重点、λ=0では3個の八重点へ衝突（各局所環 C[x,y,z]/(x²,y²,z²)）。全文 `papers/support/papers/reconstruction/point_scheme_lambda_family.tex`、単独組版 `papers/support/papers/point_scheme_lambda_family.tex`、計算 `computations/verify_lambda_point_scheme.py`。一般nc cubicへ無条件に適用しない。

## 特異境界の局所代数

λ³=-3で元の可換cubicは特異でも、point-moduleの孤立部分を記述する可換化環はC[λ,h]上自由rank24。h≠0の境界では3二重点と3六重点（局所環C[t]/t^6）。h=0では六重点はC[t,z]/(t^3,z²)になり局所型が変わる。λ境界の局所模型はhλ≠0で(v³+(λ³+3)/3)²=0。証明 `papers/support/papers/reconstruction/point_scheme_discriminant_boundary.tex`、単独原稿 `papers/support/papers/point_scheme_discriminant_boundary.tex`、検証 `computations/verify_lambda_discriminant.py`。Poisson零点との一致はsmooth cubic領域以外には主張しない。

## 現在の結論

一変数量子化について、既存の(L)局所proper/window模型と(CF)完備MF同値を入力すると、有限拡大K'/C(h)上で**全coherent残余pair**を滑らかな可換cubicのKuから復元できる。lambda=1の明示式にはさらに(D)有限対角比較を用いる。全依存証明の独立監査は未完了。

一般点の三shift生成により線束生成残余のsmoothnessを得た後、Gorenstein環のsection有限性とsmooth対角を用いて線束生成部分=Db(qgr B)を示した。これで一般点におけるK^linと全coherent残余の差を解消した。**射影化全体と可換cubic全体の導来同値は主張しない。**

同値核の具体行列、有限拡大次数、特殊点を含む相対同値、多変数全係数への適用は未完成。

## 原稿と再現

| 内容 | 入口 |
|---|---|
| A：Poisson正規形・量子化 | `papers/paper_a.tex` |
| B：17次元族・ambient復元 | `papers/paper_b.tex` |
| C：統合原稿 | `papers/paper_c.tex` |
| 今回：全coherentへの飽和 | `papers/support/papers/coherent_residual_saturation.tex` |
| 一般点の三shift生成 | `papers/support/papers/rotation_orbit_generic_reconstruction.tex` |

[今回の研究ノート](notes/coherent_residual_saturation.md)に証明の依存、監査範囲、再開点を整理した。証明本文は単独稿と論文Cが同じTeXをinputする。既存の証明と計算資産は保持する。

```sh
python3 scripts/verify_coherent_residual_assets.py --rerun-orbit
latexmk papers/coherent_residual_saturation.tex
```

今回、64 Eulerベクトルと32×32行列41恒等式を再実行し、保存証明書と完全一致を確認。新しい飽和定理は数学的証明であって、これらの有限計算で形式検証したものではない。新単独稿5頁を組版・表示確認、現行A/B/C全体と全旧計算の再実行は未実施。詳細はvalidation.json。

## 運用

GitHub mainのみを正本とし、通常のfast-forwardで保存する。PDFは追跡せずbuild/へ生成。GitHub Actions・force pushは禁止。Libraryは実際のGitHub保存失敗時の緊急退避のみ。旧ZIP・会話を再開条件にしない。独立境界/未照合PDFはnc-cubic2、Reyeはreyeに保全されている。

**新しい証明付き低次結果：** 論文AではWeyl中心元の偶性と、普遍Hessian二次補正による mod h⁵ 中心性を追加した。計算証明書は computations/verify_cubic_casimir_jet.py。全次数の形式的中心元の相対CY/formality監査はなお優先課題。

## papers/の構成
papers/直下にはpaper_a.tex、paper_b.tex、paper_c.texの三つのみを置く。その他の既存原稿・参考文献・分割節はpapers/support/papers/以下に保存。リポジトリrootからlatexmk papers/paper_a.tex等で組版する。
