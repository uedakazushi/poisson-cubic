# nc-cubic：全coherent残余pairの一般点復元

**2026-11-11 / v37。GitHub mainが正本。** 最初に[研究方針](00_research_plan.md)を読む。

## Bondal予想（論文Aの新しい帰結）

滑らかなcubic n-fold（n>=3）の全Poisson構造についてBondal予想を証明した。一般rank2kの正規形から、j<kではj+1個のJacobian三変数ブロックの平面曲線join（次元2j+1）をD_{2j}に構成する。既存の正規形定理に依存し、その全証明の独立監査・高次元での新規性確認は未完了。本文 `papers/sections/bondal_cubic.tex`、ノート `notes/bondal_cubic.md`。2013年Fano4、2026年Fano5の既存結果を参照。

## 現在の結論

一変数量子化について、既存の(L)局所proper/window模型と(CF)完備MF同値を入力すると、有限拡大K'/C(h)上で**全coherent残余pair**を滑らかな可換cubicのKuから復元できる。lambda=1の明示式にはさらに(D)有限対角比較を用いる。全依存証明の独立監査は未完了。

一般点の三shift生成により線束生成残余のsmoothnessを得た後、Gorenstein環のsection有限性とsmooth対角を用いて線束生成部分=Db(qgr B)を示した。これで一般点におけるK^linと全coherent残余の差を解消した。**射影化全体と可換cubic全体の導来同値は主張しない。**

同値核の具体行列、有限拡大次数、特殊点を含む相対同値、多変数全係数への適用は未完成。

## 原稿と再現

| 内容 | 入口 |
|---|---|
| A：Poisson正規形・量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：統合原稿 | `papers/rotation_cubic_reconstruction.tex` |
| 今回：全coherentへの飽和 | `papers/coherent_residual_saturation.tex` |
| 一般点の三shift生成 | `papers/rotation_orbit_generic_reconstruction.tex` |

[今回の研究ノート](notes/coherent_residual_saturation.md)に証明の依存、監査範囲、再開点を整理した。証明本文は単独稿と論文Cが同じTeXをinputする。既存の証明と計算資産は保持する。

```sh
python3 scripts/verify_coherent_residual_assets.py --rerun-orbit
latexmk papers/coherent_residual_saturation.tex
```

今回、64 Eulerベクトルと32×32行列41恒等式を再実行し、保存証明書と完全一致を確認。新しい飽和定理は数学的証明であって、これらの有限計算で形式検証したものではない。新単独稿5頁を組版・表示確認、現行A/B/C全体と全旧計算の再実行は未実施。詳細はvalidation.json。

## 運用

GitHub mainのみを正本とし、通常のfast-forwardで保存する。PDFは追跡せずbuild/へ生成。GitHub Actions・force pushは禁止。Libraryは実際のGitHub保存失敗時の緊急退避のみ。旧ZIP・会話を再開条件にしない。独立境界/未照合PDFはnc-cubic2、Reyeはreyeに保全されている。
