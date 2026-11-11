# nc-cubic：論文Aの投稿準備と一般点可換復元

**2026-11-12 / v46。GitHub mainが正本。** 最初に [研究方針](00_research_plan.md) を読む。

## 現在の最優先課題：論文Aの公表準備

滑らかなcubic hypersurfaceのPoisson正規形・退化軌跡・Bondal予想・代数的量子化を独立論文として推敲する。
原稿 papers/paper_a.tex、専用文献 papers/support/papers/references_poisson_cubic.tex、
現在有効な証明監査と課題 notes/poisson_article_submission_audit.md、独立有限検算 computations/verify_poisson_article_A.py。
IntroductionとAbstractを改訂し、文献・label静的整合性を点検済み。
主定理の全独立監査、全A組版、全旧証明書再実行は未完成。投稿可能判定は行っていない。
論文B/Cの成果は保持し、新規拡張は論文Aの仕上げの後に再開する。

## 量子中心三次元：普遍的な明示式

論文C周辺に既にあったFermat型の全混合中心元の式を、今回、独立中心係数とhを保持したQ(h)上の厳密な自由語計算で**普遍的な多項式中心元**と証明した。全交換子の零余剰・h=0での階数一致を証明書として保存。対角二次混合も中心平行移動で扱える。任意の滑らかな三変数三次制限gに対しては、形式的中心存在補題を仮定し、9×9（中心0個）または30×30（中心2個）のCramer決定式による普遍有理表示を構成した。短いHesse一般型式と形式存在補題の独立監査は未完了。詳細は[現行研究ノート](notes/universal_casimir.md)と論文Aの二節。

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
