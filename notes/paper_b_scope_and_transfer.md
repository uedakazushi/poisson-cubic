# 論文Bの集中化と独立成果の現行分担

**2026-11-13 / v2。過去版の履歴ではなく現在の所在を記す。**

## 主リポジトリに残す論文

論文A `papers/paper_a.tex`（A-v51）と、その全入力ソースは変更しない。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3に対する一般点可換復元の主定理と必要な証明だけを読む。必要証明は `papers/generic_recovery/` に自立して収録し、独立成果は本文に戻さない。今回A・Bの原稿と組版設定に変更はない。

## 移管を完了した点スキーム単位

現行原稿は **uedakazushi/nc-cubic2/papers/mixed_cubic_point_schemes.tex**。同リポジトリの `notes/mixed_cubic_point_schemes.md` が、方針・到達点・未解決・一次文献・再現手順の入口である。現在の本文・ノート・コードだけで再開できる。

原稿は混合族の代数と中心三次元の閉公式・自由代数の証明・Artin PBWから始め、点スキームの台、非被約構造、二パラメータ平坦閉包、判別式上の有限環までを一つの論文にまとめた。必要な混合中心式の部分は証明を削らず抽出した。4つのpoint_scheme節の数学的内容を保持し、lambda節のラベル文字列だけを実参照へ修正した。独立の可換復元定理や二次jetを証明の入力にしない。

全文12頁をLuaLaTeX/latexmkで組版し、全頁表示確認を行った。8TeXファイル、47ラベル・22参照・6引用・2文献項目について未解決・重複は0。4本の検算コードを実行し、3個の自由代数恒等式、4水準の有限jet、有理数上の3+12個の長さ24の商、標数11の判別式上の3例、長さ6の局所商、せん断の記号計算を確認した。全幾何学的証明の独立監査やpoint functorの形式化ではない。正確なハッシュと範囲は移管先の `validation_mixed_cubic_point_schemes.json`。

移管先mainの保存確認後、元の4本文・3単独組版入口・文献断片、3個の専用計算スクリプト、3証明書、2ノート、旧配置用検査スクリプトの計17ファイルを本リポジトリから除外した。ノートの固有情報（八重点のHilbert関数、衝突、未解決の境界）は移管先の現行ノートへ統合済み。元の3証明書は移管コードによる再生成とGit blob一致を確認し、再生成可能な出力は移管先build/へ生成する。検算入口は `python scripts/check_mixed_point_schemes.py --calculations`。A・現在のBがこれらのファイルを入力していないことを確認した。

元の `mixed_test_family.tex` とその検算コードは、点スキームに必要な中心式以外に二次jet・同変復元の独立成果が残るため、まだ削除しない。

## 全文保存済みだが統合未完の2節

nc-cubic2の `papers/reconstruction_extensions/first_order_poisson_kernel.tex` と `explicit_jacobian_recovery.tex` は元の全文を保持している。前者の双対数比較・五変数Plücker障害・categorical接空間、後者の有限積分判定・一意性・反例を、対応する独立原稿へ統合する作業が残る。cft:*、am:*等の依存、引用、検算コードを解決するまで元ソースを保持する。

## 残る移管対象と優先順位

1. 一次変形・Plücker障害と有限復元の2節を、既存17次元モジュライ稿との重複を調べて統合する。計算コードと参考文献を揃え、単独原稿として参照・組版・計算を検査する。
2. Artin形式復元・étale実現とSklyanin/多ブロック模型：`papers/support/papers/sections/relative_formal_models.tex`、`relative_etale_models.tex`、`sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex`。rotation障害、相対saturation、全Poisson成分の条件付き結果も照合する。
3. 相対対角・bar・Artin sector・Moritaと有限復元の別構成：`papers/support/papers/reconstruction/` の `finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex` 等。
4. 明示混合量子化・有限jet・同変正規形：`mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex` 等。
5. 元の主証明支持節の独立一般化・別証明・反例、および関連ノート・文献・計算資産。既存の新しいBに残した必要証明と重複する部分は二重の独立成果として扱わない。

各単位で本文・補題・入力の保存、参照と組版・必要計算、移管先main保存を確認してから元のB専用配置を整理する。旧ZIP・過去コミットを取得しないと再開できない構成にはしない。移管全体は未完了であり、点スキーム単位の完了と区別する。
