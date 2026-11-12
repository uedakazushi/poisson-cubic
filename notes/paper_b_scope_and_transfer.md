# 論文Bの集中化と独立成果の移管状態

**2026-11-12 / v1。現在の状態だけを記す。**

## 完了した原稿編集

`papers/paper_b.tex`（B-v55）は、任意のn>=3に対する一般点可換復元の主定理と、それを支える証明だけを読み込む。独立結果は本文に含めない。主定理に必要な補題を含む節は必要部分だけ抽出し、`papers/generic_recovery/` に証明ごと収録した。論文Aとその支持ソースは変更しない。

## nc-cubic2に全文を保存した6節

移管先は `uedakazushi/nc-cubic2/papers/reconstruction_extensions/`。次の6ファイルは元の現行本文とGit blobが一致する。

| 節 | Git blob |
|---|---|
| first_order_poisson_kernel.tex | f2875c5e7ed2312d8139dc4e9ca56960e04018f1 |
| explicit_jacobian_recovery.tex | a08e2b1279ee265d27dd6231521e8fbae0edd15b |
| point_scheme_poisson_zero.tex | 75968f92ae40487c3c463f009aa1e0f27e339666 |
| point_scheme_thickening.tex | 345f768a3799660a87b1b0ad86f6f4b7ea9d1c2d |
| point_scheme_lambda_family.tex | 6d631fc215bb99fbe397288425a48941d6097ee6 |
| point_scheme_discriminant_boundary.tex | c4126dd91aeb64f94d3f700aed013491050234ed |

これは本文保存の確認であり、移管先での独立原稿への統合・組版・全数学的監査を完了したという意味ではない。参照先の `cft:*`、`am:*`、`mt:*` と必要文献・コードを整理する必要がある。現在、元ファイルは削除していない。

## 残る移管対象

- Artin形式復元とétale実現、Sklyanin一ブロック・多ブロックの有限係数模型、例外係数の非proper性：`papers/support/papers/sections/relative_formal_models.tex`、`relative_etale_models.tex`、`sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex`。関連するrotation障害・相対saturation・全Poisson成分の条件付き結果も含む。
- 相対対角・bar・Artin sector・Moritaの比較と実効復元：`papers/support/papers/reconstruction/` 内の `finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex` 等。
- 明示混合量子化と有限jet：`mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex` 等。
- 元の主証明支持節に含まれる一般化・別証明・独立例：一変数形式比較の別構成、Stevensonによる軌道生成、任意正則多変数基底の系、有限復元の反例等。Bへ残した必要部分以外も、公表価値のある内容を保持する。
- 関連する研究ノート、参考文献断片、計算コード、再生成できない入力・証明書。既存のnc-cubic2のモジュライ・中心商・混合族と重複を整理して統合する。

## 安全な残件処理

各移管単位について、(1) 全ての定理・証明・例・入力を確認、(2) 移管先の現行論文またはノートへ統合、(3) 参照と組版・計算の必要範囲を検証、(4) 元と数学的内容が対応していることを確認、(5) Aが参照していないことを再確認してから元のB専用配置を整理する。現在は移管全体を完了扱いにしない。元の現行ファイルを残しているので、旧コミットや旧ZIPの取得を再開の前提としない。
