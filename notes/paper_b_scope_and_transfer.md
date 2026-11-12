# 論文Bの集中化と独立成果の現行分担

**2026-11-13 / v4。現在の所在と残件を記す。**

## nc-cubicに保持する論文

論文A `papers/paper_a.tex`（A-v51）とその入力ソースを保持する。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3に対する一般点可換復元と必要な証明のみを収録する。必要証明は `papers/generic_recovery/` に自立して置き、移管先の未公表証明への参照で代用しない。今回A・Bの本文・共通設定は変更していない。

## 完了単位：点スキーム

現行稿は **nc-cubic2/papers/mixed_cubic_point_schemes.tex**。方針・結果・依存・再現は同リポジトリ `notes/mixed_cubic_point_schemes.md`、検証記録は `validation_mixed_cubic_point_schemes.json`。

混合中心三次元の閉公式・自由代数恒等式・Artin PBWの証明と、4本のpoint_scheme節を統合した。全文12頁を組版・表示確認、8TeX入力・47ラベル・22参照・6引用・2文献に未解決・重複なし。自由代数3恒等式、4水準の有限jet、有理数上の3+12個の長さ24の商、標数11の判別式上の3例と長さ6の局所商、せん断を検算した。point functorや既知Sklyanin定理の形式検証ではない。

元の専用本文・3組版入口・文献断片・3計算コード・3再生成可能証明書・2ノート・旧検査の17ファイルを除外済み。ノートの固有情報も移管先に統合し、3証明書は再生成結果のblob一致を確認した。`mixed_test_family.tex` とそのコードは、二次jet・同変復元等の独立成果が残るため保持する。

## 完了単位：有限Jacobian復元

現行稿は **nc-cubic2/papers/cubic_jacobian_recovery.tex**。再開は `notes/cubic_jacobian_recovery.md`、検証は `validation_cubic_jacobian_recovery.json`。保存確認済み内容コミットは `c84789460fa89a02f4b37fac1d60e893967e4f52`。

一般次元の低rotation積、有限可積分性判定、射影的一意性、Fermatでの積分解の非一意性、五変数の積分不可能な完全交差を含む。元の全14個の数学的環境ブロックをバイト一致で保持し、具体的研究予定はノートへ移した。全文6頁を組版・表示確認、4TeX入力・17ラベル・19参照・7引用・4文献、未解決・重複・overfull・文字欠落0。

元の計算証明書blob `84f51d6c288c7c2c202e01173ee7c4363a8e3c41` を正確に再生成した。可積分性rank20,24,25、核5,1,0、反例minor15872、非対称入力の棄却を検算。専用本文・コード・再生成可能証明書の3ファイルは除外済み。主定理に必要な低次数同定・一意性の証明は `papers/generic_recovery/gradient_recovery.tex` に残す。共有の文献断片は未移管の支持節が使うため保持する。

## 完了単位：一次変形・Plücker障害

現行稿は **nc-cubic2/papers/cubic_first_order_deformations.tex**。研究再開は `notes/cubic_first_order_deformations.md`、検証は `validation_cubic_first_order.json`。保存確認済みの内容コミットは `880b648df35fe4a52e80c03eec3d5e811bc20a66`。

元の `first_order_poisson_kernel.tex` の一次曲率付き消去、Jacobian接空間、五変数Plücker障害、可換点でのcategorical KS完全列を保持する。全22ラベルと、定理3・命題1・系2・証明6・注意4の環境を保持した。全次数比較への導入参照を除き、Koszul原像の小議論を既存注意に記し、HKRとtwistingの引用を加えた。基礎dg圏とrotationの忘却を述べる一語句を訂正したため、本文全体のバイト一致ではない。

圏論的結論に必要な比較は、元の一般Artin比較の証明から双対数基底に必要な部分を `dual_number_window.tex` に自立的に構成した。相対Koszul、中心元正則性、exact圏とdg商による余核、線束Homと底変更、MF Homの有限摂動、Ind圏の生成性、rotationと周期性を付録に収録する。これは一般Artin理論全体の移管完了ではなく、元の `artin_residual_mf_comparison.tex` は保持する。

全文10頁を移管先と同一の.latexmkrcで組版し全頁表示確認した。5TeX入力・28ラベル・24参照・13引用・8文献、未解決・重複・overfull・文字欠落0。元と完全一致の2コードで、8挿入恒等式、Jacobian次数3のrank25/36・商次元10/20、Fermatと混合例のJacobi係数二次式20本/56本のspan rank5、Plücker式を加えてもrank5、非分解可能Xiの負例を確認した。これは一般のMF関手や全証明の形式検証ではない。

保存確認後、元の専用本文と2検算コードの計3ファイルを除外する。Todd補正による別証明 `poisson_first_order.tex` の導入に残っていたfpk節番号だけを記述的説明に置き換え、証明本文は保持する。旧ノート中のfpkラベル・2コードのパスは、移管先の同名現行ファイルを指すものとして読む。A・Bはこれらを入力しない。

## 残件と着手順序

1. Artin形式復元・étale実現：`relative_formal_models.tex`、`relative_etale_models.tex`、`artin_residual_mf_comparison.tex`、rotation障害、相対saturation、全Poisson成分の条件付き結果。双対数の付録に収めていない一般基底・底変更の成果を保持する。
2. Sklyanin/多ブロック模型：`sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex`。
3. 相対対角・bar・Artin sector・Moritaの独立構成：`finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex` 等。
4. 混合量子化・有限jet・同変正規形と一次消滅の別証明：`mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex`、`poisson_first_order.tex` 等。
5. 元の支持節に残る独立一般化・別証明・反例と関連ノート・文献・計算資産。Bに必要な証明と重複する部分を二重の独立成果として扱わない。

各単位で必要な本文・補題・文献・入力を揃え、組版と計算の必要範囲、移管先main保存を確認してから元を整理する。旧ZIPや過去コミットだけを再開の前提にしない。移管全体は未完了であり、三単位の完了と区別する。
