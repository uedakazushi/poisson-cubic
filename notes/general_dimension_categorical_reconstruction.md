# 論文B：一般次元のrotation付き可換復元（2026-11-12 / B-v40）

## 主定理と再開入口

最初に `00_research_plan.md`、続いて
`papers/paper_b.tex` の主定理 `gdr:thm:generic` を読む。
主定理の全文は `papers/support/papers/reconstruction/general_dimension_recovery.tex`。
次元は `n>=3`、生成変数の個数 `N=n+2`。
`R=C[h]_(h)` 上の次数別有限自由な中心三次対
`(A_R,Omega_R)` と滑らかな剰余 `F` を入力し、
(L) proper/windowと三stabilization、
(CF) 実際の完備係数上の内部shift付きMF同値、
一般ファイバーのnoetherian Koszul AS-regularを条件とする。
その場合 `K'/C(h)` 有限、smooth cubic `Y/K'` が存在して
`(K_B^coh,rho_B) ≅ (Ku(Y),rho_Y)`。
`D^b(qgr B_K)` は線束で生成されsmooth proper。
これは中心三次商を持たない一般の抽象的nc cubicには適用しない。

## 論理の検証地図

1. `local_projective_model.tex` (`lp:thm:main`)：
局所flat、正則局所環、Gorenstein・Koszul・有限proper模型。
`artin_residual_mf_comparison.tex` (`am:thm:comparison`)：
相対stabilization/windowと三shiftの識別。以上が(L)。
2. `formal_cubic_mf_reconstruction.tex`
(`fo:thm:formal-reconstruction`, `fo:cor:complete-graded`)：
標数零、重み零formality、中心Casimirの逆像による形式三次式、
実際の完備graded MF同値(CF)。変数の個数自体は既に任意である。
3. `rotation_orbit_generic_reconstruction.tex`：
(`rog:prop:euler`) の `sum chi_r^2=2*3^(N-1)` は任意 `N`。
(`rog:thm:orbit`) は非零MF対象の三shift生成、そこで
(`rog:thm:laurent`) がLaurent体上で本質的全射、
(`rog:thm:geometric-generic`) が有限体拡大へのperfect核降下。
4. `coherent_residual_saturation.tex`：
(`crs:thm:abstract`, `crs:thm:coherent`, `crs:thm:generic`)。
線束検出、proper Hom、smooth対角から線束部分=全coherent。
一般点でのsmooth性を使い、Artin族の生成子持上げを使わない。
5. `geometric_rotation_basechange.tex`：
低rotation Nat のrank `N,binom(N,2)`、全Artin底変更。
`explicit_jacobian_recovery.tex` / `finite_algebraic_recovery.tex`：
線形可積分性による候補三次式の有限抽出。存在定理とは別。
6. 五変数混合 `lambda=1` の形式模型を特定するには(D)の
finite diagonal/bar/characteristic比較が追加で必要。
Pirozhkov, *A categorical Torelli theorem for hypersurfaces*,
BLMS 56 (2024), 3075--3089, DOI 10.1112/blms.13117：
cubic dimension `n>3` でrotation付き可換模型の一意性。
`n=3` にこの定理を誤って引用しない。

## 状態と最優先の未解決

- **証明本文あり／今回の独立監査未完了**：
(CF)の曲率付きfunctor、中心逆像の導来比較、相対windowのenhancement、
(L)の安定化対象と有限proper Hom、rotationの自然同型。
- **証明本文あり／既存の確認を利用**：Eulerの全次元恒等式、
非零軌道生成、finite descent、coherent飽和。今回原本を読んだが、
全証明の形式検証や独立な全再監査を完了したとは言わない。
- **計算付き／範囲限定**：五変数の明示 `G_h+v^3` と(D)、
point scheme、対角行列。一般次元の閉公式を意味しない。
- **未解決**：全Poisson moduliで一様な多変数復元、
一般非可換cubicの超曲面表示、同値核行列、有限拡大次数、
特殊点の相対同値、射影化全体の導来同値。

## 再現・新規性の点検

`latexmk papers/paper_b.tex`（ルートから）で日本語LuaLaTeX稿を生成。
入力の保存・全件参照確認・式番号のLuaLaTeX実行はそれぞれ別。
現段階ではGitHubソースの整合性検査のみを予定し、
コンパイルや数学的完全検証を実施したと報告しない。
証明の新規性の包括的調査、全依存の一次文献照合は未完了。
既存の原稿各節を削除せず、一般定理→構成→有限計算→応用へ配置変更した。
