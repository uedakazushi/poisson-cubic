# 論文Bの集中化と独立成果の現行分担

**2026-11-13 / v6。現行の所在・依存と移管状態を記す。**

## nc-cubicに保持する論文

論文A `papers/paper_a.tex`（A-v51）と全入力を保持する。B `papers/paper_b.tex`（B-v55）は任意のn>=3の一般点可換復元と必要証明に集中し、`papers/generic_recovery/` 内で自立する。この移管作業ではA・Bの本文・共通設定を変更しない。

## 完了単位：点スキーム

現行稿は **nc-cubic2/papers/mixed_cubic_point_schemes.tex**。再開は同リポジトリ `notes/mixed_cubic_point_schemes.md`、検証は `validation_mixed_cubic_point_schemes.json`。

混合中心式の閉公式・自由代数恒等式・Artin PBWと4本のpoint_scheme節を統合。12頁、8TeX入力・47ラベル・22参照・6引用・2文献、未解決・重複なし、全頁表示確認。4コードで自由代数3恒等式、4水準のjet、有理数上の3+12個の長さ24の商、標数11の判別式3例と長さ6の局所商、せん断を検算した。point functor等の形式証明ではない。

専用本文・3入口・文献断片・3コード・3再生成可能証明書・2ノート・旧検査の17ファイルを整理済み。固有ノート内容を統合し、3証明書は再生成とblob一致を確認した。`mixed_test_family.tex` とコードはjet等の独立成果が残るため保持する。

## 完了単位：有限Jacobian復元

現行稿は **nc-cubic2/papers/cubic_jacobian_recovery.tex**。ノートは `notes/cubic_jacobian_recovery.md`、検証は `validation_cubic_jacobian_recovery.json`。

一般次元の低rotation積、有限可積分性、射影的一意性、Fermatの積分解の非一意性、五変数の非可積分な完全交差を含む。元の14数学的環境をバイト一致で保持。6頁、4TeX入力・17ラベル・19参照・7引用・4文献、全頁表示と未解決・重複・overfull・文字欠落0を確認した。

元の証明書blob84f51d6c288c7c2c202e01173ee7c4363a8e3c41を正確に再生成。rank20/24/25、核5/1/0、minor15872、非対称入力の棄却を確認。専用本文・コード・証明書の3ファイルは整理済み。Bの必要な低次数同定・一意性は `gradient_recovery.tex` に保持する。共有文献断片は残る支持節のため保持する。

## 完了単位：一次変形・Plücker障害とTodd補正

現行稿は **nc-cubic2/papers/cubic_first_order_deformations.tex**（v2、13頁）。再開は `notes/cubic_first_order_deformations.md`、検証は `validation_cubic_first_order.json`。

直接的な一次MF比較・Jacobian接空間・Plücker障害・可換点categorical KSは元の22ラベルと全数学的環境を保持する。一般の変数数N>=5の一次消去と、N=5に固有の障害・categorical結論を区別。必要なenhanced比較は `dual_number_window.tex` に証明ごと収録し、相対Koszul・中心元正則性・exact圏とdg商・Hom底変更・Ind生成・rotationを扱う。一般Artin理論全体を移管したものではない。

Todd別証明は9数学的環境・8ラベルを保持し、商環Jac(F)とイデアルJ(F)を区別、JLLZ著者版の図式番号を3.10に訂正。基礎dg圏の一次類とrotation付き全データを混同しない。一次係数を消す系は可換復元族の存在とpure Poisson KS等を仮定する。

6TeX入力・36ラベル・32参照・20引用・9文献、全13頁表示確認、未解決・重複・overfull・文字欠落0。既存2コードの8挿入恒等式、Jacobian rank25/36、商次元10/20、二例のJacobi/Plücker span rank5、非分解可能Xiの負例を保持する。Todd統合時と今回にコードを再実行していない。専用直接比較本文・2コード・Todd本文の4ファイルを整理済み。共有文献と一般Artin原稿は保持する。

## 独立稿を整備済み、元整理は未完了：有限Artin比較

現行稿は **nc-cubic2/papers/cubic_artin_windows.tex**（v1、13頁）。方針と詳細は `notes/cubic_artin_windows.md`、正確な検証範囲は `validation_cubic_artin_windows.json`。移管先mainへの保存確認済みコミットは `8b9d77c57094ed3578cdac3d2120b7168303d6a8`。

一変数の全有限切断R_N=C[h]/h^(N+1)、d>=5変数（次元d-2>=3）についての線束残余/MF比較、正則局所模型のArtin底変更、全Artin切断のsmoothnessが完備底で失われる反例を統合した。任意の局所Artin環や全coherent圏についての主張ではない。

`papers/artin_windows/comparison.tex` は元の比較の主部分17ラベル、定義1・補題5・定理1・証明6を保持。外部参照だった次数別分裂の持上げ、局所cohomology、周期変数の二重次数を本文で説明した。`regular_basechange.tex` は `am:prop:Gamma-basechange` と必要な正則局所の証明を既存局所模型から自立させる。`artin_smoothness_obstruction.tex` は元全文とblob00b88867ab30b64e751160bbb8207b0f405b66daが一致し、全8ラベルと数学的環境を保持する。

**可換MF同値の存在を今回証明したわけではない。** 新しい適用 `ar:cor:conditional` は、W_hと互換なMF比較を別途与えた場合の残余圏への移送である。元の `am:cor:formal-residual` と全次数MF存在入力は元のArtin原稿に保持し、同じラベルのまま条件付き主張に弱める処理をしていない。

7TeX入力・31ラベル・36参照・11引用・5文献を検査し、13頁を組版・全頁表示確認した。未解決・重複・overfull・文字欠落は0。新しい検算コードは既存4次元dg模型の64結合律・16Leibniz則・8単位条件・d²、一般/特殊cohomology次元、6有限切断のrank等をQQ[h]/QQ上で確認する。主定理、Morita同値、全Nの生成性・smoothnessを形式証明したものではない。

**今回は元ソースを削除していない。** Artin比較のam:*は、mixed_test_family、curved_gauge_comparison、kontsevich_second_jet、formal_cubic_mf_reconstruction、three_object_window、geometric_rotation_basechange等が参照する。元の末尾の形式復元系もまだ残る。これらの依存を統合先の現行証明へ接続してから、元の比較・反例を整理する。独立稿の自足性と、他の原稿の依存解消を区別する。

## 残件と具体的着手

1. `relative_formal_models.tex` と `relative_etale_models.tex` の形式的持上げ・同値スタック・smoothnessの入力を明記し、存在定理を自立させる。元のArtin比較末尾の系とam参照を接続し、上記の元重複を整理する。
2. Sklyanin/多ブロック：`sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex`。
3. 対角/bar/Artin sector/Morita：`finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex`等。
4. 混合量子化とjet：`mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex`等。移管先の同時更新と重複を照合する。
5. 元支持節の独立一般化・別証明・反例、ノート・文献・コード。Bと重複する必要証明を二重の新成果として数えない。

旧ノート中の移管済み略称は、上記の現行原稿・ノートの同名結果を指すものとして読む。保存は旧コミットや旧ZIPだけで代用せず、現行証明・入力を保持する。Aの入力を移管しない。全移管の完了と個別原稿の整備を区別する。
