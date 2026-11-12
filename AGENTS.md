# Codex 実行指示 — nc-cubic（独立成果の nc-cubic2 への移管）

**2026-11-13 / v77。GitHub `main` が正本。最初に `00_research_plan.md`、次に `notes/paper_b_scope_and_transfer.md` を読む。移管先 `uedakazushi/nc-cubic2` の `00_research_plan.md`・`AGENTS.md` と現行TeX・ノートも必ず読む。**

## 役割と達成基準

この担当Codexの主作業は、論文Bから分離した公表価値のある**独立成果を nc-cubic2 の現行論文・研究ノート・再現資産へ安全に統合し、確認できた元側の真の重複だけを整理すること**である。単なるコピー、ファイル数削減、PDF化、体裁の調整を成果と数えない。計画だけで止めず、可能な単位ごとに内容の統合・検証・両リポジトリのGitHub保存まで実行する。

**Chat側の独立した担当**は (1) 論文AのPoisson正規形・量子化の数学的監査、(2) 論文Bの完備MF比較と一般点降下の数学的監査・主定理の改良、(3) 一次資料による先行研究の確認・新規性評価である。Codexはこれらを迂回して論文A・Bを書き換えたり、論文の主定理を勝手に強化・弱化したりしない。Codexは移管中に発見した数学的な矛盾・欠落・反例・文献の問題を、依存先とともに現在有効なノートへ記してChat側へ引き継ぐ。解決せずに正しい証明として出版原稿に混入させない。

## 厳格な境界：論文A・Bと依存を保護する

- `papers/paper_a.tex`（A-v51）、`papers/paper_b.tex`（B-v55）、`papers/generic_recovery/`、`papers/support/papers/common.tex` および**A・Bが再帰的に読む全入力**を、今回の移管タスクでは編集・削除しない。A・Bの本文や必要証明を nc-cubic2 への外部リンクで置き換えない。
- `papers/support/papers/` 配下には、Aの入力、Bの必要証明、独立な支持成果が共存する。パスやファイル名だけで「移管可能」と判定せず、`\\input` / `\\include`、`\\ref` / `\\eqref` / `\\cite`、コードとノートの依存グラフを実際に照合する。保護対象と共有されるファイル・文献・証明書を消さない。
- 移管先 `nc-cubic2` の既存研究（17次元モジュライ・Poisson fourfold・六七次元・PDF研究等）を消さず、既存の対応原稿へ統合する。別の実行者が同じファイルを更新している場合は最新 `main` と突き合わせ、変更を上書きしない。
- 数学的な入力の強さと結論を保持する。特に完備MF比較の**全次数の存在**と「比較同値を別に仮定した条件付き移送」、線束生成残余圏と全coherent残余圏、有限Artin切断と一般のArtin基底、形式同値と代数的同値、相対smooth proper性の仮定を混同しない。
- 論文A・Bに数学的修正が不可欠だと判明したら、元ファイルを変更するのでなく、具体的な問題・反例・仮定・代案・参照箇所をノートに明示する。証明の監査済み・原稿に証明記載・有限計算確認・未検証を区別する。

## 移管対象と着手順（現在の状態に合わせて再確認）

既に移管先の `papers/` に自立原稿がある五単位：`mixed_cubic_point_schemes.tex`、`cubic_jacobian_recovery.tex`、`cubic_first_order_deformations.tex`、`cubic_artin_windows.tex`、`relative_cubic_realization.tex`。前の三単位は元側の専用重複整理まで完了。Artin稿とétale稿は移管先保存済みだが、元側で`am:*`・`er:*`・`ho:*`・`as:*`を参照する箇所が残るため重複削除は未完了。既存の成果を再移植したり、完了した専用ソースを復活させたりしない。

1. **形式・étale・Artinの接続：** 元の `papers/support/papers/sections/relative_formal_models.tex`、`relative_etale_models.tex`、`papers/support/papers/reconstruction/artin_residual_mf_comparison.tex`、`etale_realization.tex`、`hochschild_obstructions.tex`、`artin_smoothness_obstruction.tex` と、その参照元を点検する。既存の `nc-cubic2/papers/cubic_artin_windows.tex` と `relative_cubic_realization.tex` に、残る独立結果・完全な証明・反例・必要文献を適切に統合する。特に `am:cor:formal-residual` の全次数MF存在入力を確認し、`ar:cor:conditional` のみで代用しない。`rotation_saturation_reduction.tex` の `er:*` を含め、元側の参照閉包を確認する。
2. **Sklyanin・多ブロック：** `sklyanin_model_theorems.tex`、`sklyanin_block_models.tex`、`multiblock_generation.tex`、`relative_parameter_boundary.tex` を、移管先の混合形式比較・量子化原稿と照合して、公表価値のある独立主張・証明を現行論理順へ統合する。
3. **対角・bar・Morita：** `finite_algebraic_recovery.tex`、`curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`、`multiplicative_bar_comparison.tex`、`diagonal_kernel_identity.tex`、`relative_artin_sector.tex`、`artin_rotation_obstructions.tex`、`central_symmetry_lifting.tex`、`one_sided_morita_algebraization.tex`、`geometric_rotation_basechange.tex` などを統合する。
4. **混合・jet・その他の残件：** `mixed_test_family.tex`、`explicit_model_comparison.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`mixed_equivariant_normal_form.tex`、未移管のノート・反例・証明書・計算を点検する。移管先の並行作業と重複する部分を統合し、必要なものだけを残す。

この順序は、依存関係または数学的価値から明確な理由がある場合には入れ替えてよい。解決できない問題で作業全体を止めず、その数学的障害を保持して次の独立単位へ進む。ただし「済んだこと」と「安全に削除できたこと」は常に別に判断する。詳しい現在の所在は `notes/paper_b_scope_and_transfer.md` を参照。

## 各単位で必ず通す検証・削除ゲート

1. 元の定理・補題・仮定・証明・式・反例・重要な計算・先行研究の参照と、移管先の現在有効な内容を照合。新規性未確認のものはその状態を明記。外部の旧ZIP・旧コミット・旧PDFの存在を現在の数学的本文の代わりにしない。
2. 移管先の独立原稿に必要な証明・記法・文献を自足させる。論文内は現在の数学的論理順で構成し、旧版対応や移管履歴の一覧を新たに増やさない。ノートは現在有効な未収録の障害・例・着想・証明所在を記す。
3. ラベル・参照・引用・入力閉包、LuaLaTeX/`latexmk` による影響範囲の全文組版、必要な厳密計算と有限証明書の再現を確認。実行できない環境では未実行と明記し、成功と推測しない。TeXを軽量化するため数学的証明を削らない。
4. **先に `nc-cubic2/main` にfast-forward保存し遠隔HEAD/blob確認。その後** `nc-cubic` の元ファイルがA・B・他の未移管原稿・ノート・コードに必要ないことを最新treeで確認してから、真の重複だけを削除し `nc-cubic/main` へ保存。移管先保存失敗・参照未解決・未検証なら元ソースは保持する。
5. 作業ごとの記録は各リポジトリの現行研究方針・必要最小限のvalidation・移管境界ノートを更新し、旧版の記録を追記して蓄積しない。残作業は依存ファイルと具体的な次の手順だけを書く。

## 保存・並行実行・再現

GitHubの両 `main` がそれぞれの正本。作業前とpush前にリモートHEADを再取得する。同時編集があれば最新状態に変更を取り込んでから**通常のfast-forward push**を行い、コミット・遠隔refと実際の対象blobを確認する。force push・GitHub Actions・不要なPR・履歴書換えをしない。別担当の変更を無断で消さない。PDF、SyncTeX、中間物、容易に再生できる出力は `build/` に置き追跡しない。日本語LuaLaTeXと各repoの `.latexmkrc` を使う。Libraryは実際のpush失敗時だけ緊急退避し、既存Libraryファイルを無断削除しない。

## 研究一般の恒久原則と保存許可

研究全体の数学的重要性・新規性・理解の深化・応用・正確性・実現可能性を重視し、目標と方針は柔軟に更新する。証明済み・追加仮定付き・未完成・予想・計算的観察を区別し、誤りが分かれば依存する主張も訂正する。一次資料を確認し、未確認の文献事実を推測で補わない。日本語LuaLaTeXの公表用論文には重要な成果と十分な証明を保持する。研究ノートは現在有効な知識を整理し、作業日誌や重複証明を作らない。研究再開は現行研究方針から行い、現行bundleに必要なソース・証明書・再現手順を保つ。歴史ZIP・古い原稿・キャッシュは収録しない。研究の区切りでユーザーの追加承諾なく保存してよい。本プロジェクトでは上記のGitHub `main` 保存を優先し、Libraryへの保存はpush失敗時に限る。
