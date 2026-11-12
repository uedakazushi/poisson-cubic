# 論文Bの集中化と独立成果の現行分担

**2026-11-13 / v3。現在の所在と残件を記す。**

## nc-cubicに保持する論文

論文A `papers/paper_a.tex`（A-v51）と全入力ソースを維持する。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3に対する一般点可換復元と必要な証明のみを収録する。必要証明は `papers/generic_recovery/` に自立して置き、移管先の未公表証明への参照で代用しない。この移管作業ではA・Bの本文・共通設定を変更していない。

## 完了単位：点スキーム

現行稿は **nc-cubic2/papers/mixed_cubic_point_schemes.tex**。方針・結果・依存・再現は同リポジトリ `notes/mixed_cubic_point_schemes.md`、検証記録は `validation_mixed_cubic_point_schemes.json`。

混合中心三次元の閉公式・自由代数恒等式・Artin PBWの証明と、4本のpoint_scheme節を統合した。全文12頁を組版・表示確認、8TeX入力・47ラベル・22参照・6引用・2文献に未解決・重複なし。自由代数3恒等式、4水準の有限jet、有理数上の3+12個の長さ24の商、標数11の判別式上の3例と長さ6の局所商、せん断を検算した。point functorや既知Sklyanin定理の形式検証ではない。

元の専用本文・3組版入口・文献断片・3計算コード・3再生成可能証明書・2ノート・旧検査の17ファイルを除外済み。ノートの固有情報も移管先に統合し、3証明書は再生成結果のblob一致を確認した。元の `mixed_test_family.tex` とそのコードは、中心式以外の二次jet・同変復元等が残るため保持する。

## 完了単位：有限Jacobian復元

現行稿は **nc-cubic2/papers/cubic_jacobian_recovery.tex**。再開は同リポジトリ `notes/cubic_jacobian_recovery.md`、検証は `validation_cubic_jacobian_recovery.json`。保存を確認した内容コミットは `c84789460fa89a02f4b37fac1d60e893967e4f52`。

任意のn>=3の可換三次超曲面の低rotation積、有限可積分性判定、射影的一意性、Fermatでの積分解の非一意性、五変数の積分不可能な完全交差を含む。元の全14個の定理・証明・例・注意の環境ブロックをバイト一致で保持した。末尾の混合族への具体的研究予定だけをノートへ移し、本文では圏同値の存在と方程式候補の抽出を区別した。

全文6頁を組版・全頁表示確認した。4TeX入力、17ラベル・19参照・7引用・4文献項目、未解決・重複・overfull・文字欠落0。元のコードを有理数上で実行すると証明書blob `84f51d6c288c7c2c202e01173ee7c4363a8e3c41` と完全一致した。移管後は日付・出力先・本文パスのみを修正し数値部分の一致も検査した。可積分性行列rank20,24,25、核次元5,1,0、反例の指定小行列式15872、非対称積の棄却を確認している。これは非可換dg Homや圏同値の検証ではない。

移管先の保存確認後、元の独立本文 `papers/support/papers/reconstruction/explicit_jacobian_recovery.tex`、専用コード、再生成できる証明書の3ファイルを除外する。A・Bの入力には含まれない。主定理で必要な低次数同定と一意性の証明は `papers/generic_recovery/gradient_recovery.tex` に保持する。未移管の二次jet等が参照する同名の命題もこの必要証明で読める。共有の `explicit_jacobian_references.tex` は残る支持節の文献入力に使うので、他単位とともに整理するまで保持する。

## 全文保存済みだが統合未完：一次変形・障害

nc-cubic2の `papers/reconstruction_extensions/first_order_poisson_kernel.tex` は元の全文を保持する。双対数上の曲率付き比較、Jacobian接空間、五変数Plücker障害、categorical接空間を、17次元モジュライ稿との重複と依存を確認して統合する。cft:*、am:*等の依存・文献・検算コードを解決するまで元ソースを保持する。

## その他の残件と着手順序

1. 一次変形・Plücker障害の保存済み節を原稿として閉じ、17次元モジュライとの関係を明示する。
2. Artin形式復元・étale実現とSklyanin/多ブロック模型：`relative_formal_models.tex`、`relative_etale_models.tex`、`sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex`。rotation障害、相対saturation、全Poisson成分の条件付き結果を含む。
3. 相対対角・bar・Artin sector・Moritaの独立構成：`finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex` 等。
4. 明示混合量子化・有限jet・同変正規形：`mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex` 等。
5. 元の主証明支持節に含まれる独立一般化・別証明・反例、および関連ノート・文献・計算資産。現在のBに必要な証明と重複する部分は二重の独立成果として扱わない。

各単位について必要な本文・補題・文献・入力を揃え、組版と計算の必要範囲を検証し、移管先mainの保存を確認してから元を整理する。旧ZIPや過去コミットだけを再開の前提にしない。移管全体の完了と個別単位の完了は区別する。
