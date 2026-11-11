# nc-cubic：有限方程式と一般点の可換復元

**2026-11-11 / v35。GitHub mainが正本。** [研究方針](00_research_plan.md)から再開する。

## 現在の到達点

既存の局所proper/window模型(L)と次数別完備MF同値(CF)を入力する範囲で、一変数量子化の**線束生成残余pair**は、有限拡大K'/C(h)上で滑らかな可換cubicのKuznetsov pairと同値になる。

完備底全体のcompact逆核を先に作らず、固定生成子の像をLaurent体へ移す。Eulerベクトルで非零性を検出し、孤立斉次超曲面の非零対象の次数シフト軌道が生成することを使う。三次では三つのshiftで足りる。体上のcompact核は有限代数拡大へ降下できる。

lambda=1混合族では既存(D)の低積比較も使い、復元先を既存の明示的多項式G_h+v^3に固定できる。N=5のEulerベクトルは(-9,9,0)。一般Nでも三成分二乗和2*3^(N-1)は非零。

**範囲の注意：** 既存(L),(CF),(D)の全証明の独立再監査ではない。全coherent残余圏との一致、多変数全モジュライ、同値核の具体行列、拡大次数、h=0を含む相対同値は別課題。一般点の存在証明と有効な計算を区別する。

## 原稿と再現

| 内容 | 入口 |
|---|---|
| A：Poisson正規形・固定方向の量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族とambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き復元・統合稿 | `papers/rotation_cubic_reconstruction.tex` |
| 軌道生成と一般点復元・単独稿 | `papers/rotation_orbit_generic_reconstruction.tex` |

新本文は `papers/reconstruction/rotation_orbit_generic_reconstruction.tex` をCと単独稿で共有する。[研究ノート](notes/rotation_orbit_generic_reconstruction.md)に依存と残る問題を整理した。

```sh
python3 computations/verify_rotation_orbit.py --output build/rotation_orbit_certificate.json
python3 scripts/verify_rotation_orbit_assets.py
latexmk papers/rotation_orbit_generic_reconstruction.tex
```

検算は64個のEulerベクトルと、混合special cubicの32×32行列の41恒等式。生成分類、形式functor、generic kernelの計算機証明ではない。新単独稿7頁を組版・全頁表示確認した。現行A/B/C全体の再組版と旧計算全件の再実行は未実施。正確な状態はvalidation.json。

## 運用

通常のfast-forwardのみ。GitHub Actionsとforce pushは禁止。PDFは追跡せずbuild/へ生成する。Library保存は実際のpush失敗時の緊急退避だけ。旧ZIP・会話を再開の前提にしない。

既存の有限対角、bar比較、幾何学的BC、片側Morita/Popescu、SM/ERと反例を保持する。独立境界研究/未照合原PDFはnc-cubic2、Reyeはreyeに保全。
