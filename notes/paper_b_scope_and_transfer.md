# 論文Bの集中化と独立成果の現行分担

**2026-11-13 / v7。現行の所在・依存・移管状態を記す。**

## nc-cubicに保持する論文

A `papers/paper_a.tex`（A-v51）と全入力を保持する。B `papers/paper_b.tex`（B-v55）は任意のn>=3の一般点可換復元と必要証明に集中し、`papers/generic_recovery/` 内で自立する。この移管作業ではA・Bの本文・共通設定を変更しない。

## 元側の専用整理まで完了した三単位

**点スキーム**：nc-cubic2の `papers/mixed_cubic_point_schemes.tex`、ノートは `notes/mixed_cubic_point_schemes.md`、検証は `validation_mixed_cubic_point_schemes.json`。混合中心式・自由代数恒等式・Artin PBWと4本のpoint_scheme節、12頁。8TeX入力・47ラベル・22参照・6引用・2文献、未解決・重複なし、全頁表示確認。4コードの中心性・jet・Groebner長・判別式とせん断の有限検算を保持する。専用17ファイルを除外済み。ノート固有情報と再生成証明書を保存し、混合jet等が残る `mixed_test_family.tex` とコードは保持する。

**有限Jacobian復元**：`papers/cubic_jacobian_recovery.tex`、同名ノート、`validation_cubic_jacobian_recovery.json`。低rotation積・可積分性・一意性・Fermat例・非可積分な完全交差、6頁。全14数学的環境を保持。4TeX入力・17ラベル・19参照・7引用・4文献、組版・表示確認、未解決・重複・overfull・文字欠落0。元証明書84f51d6c288c7c2c202e01173ee7c4363a8e3c41を再生成し、rank20/24/25、核5/1/0、minor15872等を検算。専用本文・コード・証明書の3ファイルを除外済み。Bに必要な低次数同定・一意性は `gradient_recovery.tex` に残し、共有文献も保持する。

**一次変形・Plücker障害とTodd補正**：`papers/cubic_first_order_deformations.tex`（v2、13頁）、同名ノート、`validation_cubic_first_order.json`。直接比較の22ラベル、Toddの9数学的環境・8ラベルを保持。必要な双対数windowは付録で自立。一次比較N>=5とN=5固有の障害・categorical結論を区別する。6TeX入力・36ラベル・32参照・20引用・9文献、組版・全頁表示と未解決等0を確認。既存2コードの8挿入恒等式、Jacobian rank25/36、商10/20、Jacobi/Plücker span5と負例を保持。専用本文・2コード・Todd本文の4ファイルは除外済み。今回これらのコードは再実行しない。共有文献と一般Artin理論は元側に残す。

## 独立稿は保存済み、元依存の整理は未完了：有限Artin比較

現行稿はnc-cubic2の **`papers/cubic_artin_windows.tex`**。方針・証明所在・再現は `notes/cubic_artin_windows.md`、検証は `validation_cubic_artin_windows.json`。

一変数の全有限切断R_N=C[h]/h^(N+1)、d>=5変数での線束残余/MF比較、正則局所模型からの底変更、完備基底で生成性・smoothnessが失われる反例を扱う。任意の局所Artin環や全coherent圏の結果ではない。比較主部17ラベルと必要な局所証明、正則底変更命題を保持する。

`ar:cor:conditional` は互換な可換MF比較を別途与えた場合の移送であり、元の `am:cor:formal-residual` とその全次数MF存在の証明を弱めて置換していない。元末尾の系と広い形式理論は元に残す。am:*はmixed_test_family、curved_gauge_comparison、kontsevich_second_jet、formal_cubic_mf_reconstruction、three_object_window、geometric_rotation_basechange等から参照されるため、元比較の削除は保留する。

反例は移管先 `papers/artin_windows/artin_smoothness_obstruction.tex` の一ファイルを以下のétale稿とも共用する。現在のblobはfe52bb222fdc9a1d2678a10b29bfa9b97ef8f228。数学的主張・証明・8ラベルを保持して外部の文脈参照を二つ除いた。過去の13頁全文組版と有限dg検算は以前のソースの検証であり、共有参照整理後のArtin稿全文は今回再組版していない。現行ファイルでのétale稿の全文組版とは区別する。

## 独立稿の保存を完了、元依存の整理は未完了：étale局所実現

現行稿はnc-cubic2の **`papers/relative_cubic_realization.tex`（v2、10頁）**。ノート `notes/relative_cubic_realization.md`、検証 `validation_relative_cubic_realization.json`、入力案内 `papers/relative_realization/README.md` から再開できる。保存確認済み内容コミットは `68aa33d243d6541531c2ff2c8b2c1c5f60637215`。前回の未反映ZIPを再取得することは再開の前提ではない。

主節etale_realization.texは元のblob746fb290813c5ebad864e8398c07604e8db9a446と完全一致。perfect双加群のExt^2障害、自己同値による不変性、幾何的KSの全射性、HH^1=0によるintertwiner持上げ、対象moduliからのétale局所実現を扱う。任意のn>=3のcubicへ適用するが、実在する相対smooth properな代数的族を仮定する。次数別flatnessだけからその仮定を導くものでも、指定三次周期や群作用coherenceまで追加した変形問題でもない。

Hochschild sector節は全7ラベルと証明を保持し、旧研究予定を適用条件の説明へ直した。反例の証明は上のArtin稿のファイルを共用し、別のコピーを作らない。H^1の底上torsionがあること、cohomology flatな族を反証したわけではないことを保持する。新結果を追加しない。

現行6TeX入力・29ラベル・24参照・16引用・9文献を検査し、全10頁をLuaLaTeXで組版・表示確認した。未解決・重複・overfull・文字欠落0。verify_hochschild_sectors.pyをN=5,...,60で再実行し、元の証明書blob8e7a35337e43b45fc26b04c11414554732213ea4を完全に再生成。これは既知BFK公式の整数計算であり、公式自体や圏論的主張の形式検証ではない。一次資料の以前の確認範囲と未確認点を専用ノートに保持し、今回新たに全監査したとはしない。

**元ソースはまだ削除しない。** `rotation_saturation_reduction.tex` がer:thm:ERを使い、別の未移管節もer/ho/asを参照する。移管元のetale_realization、hochschild_obstructions、artin_smoothness_obstructionと関連コード・文献は、この依存を解消するまで保持する。独立稿の自足性と他の原稿の依存解消を区別する。

## 残件と具体的着手

1. `relative_formal_models.tex` と `relative_etale_models.tex` の全形式持上げ・同値スタック・相対smoothnessの条件を、保存済みのArtin稿とétale稿へ接続する。元Artin末尾の系は必要な全次数存在入力とともに保持する。am/er/ho/asを使うmixed、formal、rotation_saturation等の依存を整理してから元重複を除く。
2. Sklyanin/多ブロック：`sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex`。
3. 対角/bar/Artin sector/Morita：`finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex`等。
4. 混合量子化とjet：`mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex`等。移管先の同時更新と重複を照合する。
5. 元支持節の独立一般化・別証明・反例、ノート・文献・コード。Bの必要証明を二重の独立新成果として数えない。

保存を旧コミットや旧ZIPへのリンクだけで代用せず、現行証明・入力を保持する。Aの入力を移管しない。全移管の完了、個別原稿の保存、元側の重複削除を別々に記録する。
