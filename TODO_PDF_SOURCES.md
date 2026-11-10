# PDF原本とTeXソースの照合 TODO（2026-11-10）

## 原則と現在の状態

- [x] GitHub `main` を研究の正本とし、論文・研究ノートは原則TeXから再生成する。
- [x] 自動生成PDFは`.gitignore`で無視する。
- [x] 関連が判明したTeXを`sources/candidates/`に追加し、既存の現行TeXを変更しない。
- [ ] **追跡中PDF全9本（論文7・ノート2）の全定理・仮定・証明・計算を、対応する現行TeXと照合する。**
- [ ] 照合後に必要な本文を`papers/`・`notes/`へ統合し、LuaLaTeX組版・参照・計算を確認する。
- [ ] 内容が欠落しないと確認したPDFのみ`git rm --cached`で追跡解除する。Library原本は削除しない。

以下の「関連TeX」は**原PDFを完全再現するソースと認定したものではない**。特にPDFの同名／同主題資料が現行TeXにすべて含まれるとは推論しない。重複する候補ソースは照合が終わるまで保持する。

## 追跡中PDFごとのチェックリスト

- [ ] `papers/pdf-only/ambient/central_cubic_technical.pdf`：中心三次量子化の詳細。関連候補 `papers/sections/poisson_geometry.tex`、`papers/generic17_ambient_recovery.tex`、`sources/candidates/poisson_ambient_bridge_v6.tex`。**第28節の中心チャート貼合せとvery-general正則性の命題・証明は `papers/source_recovery/central_cubic_generic_smoothness.tex` に部分的にTeX化済み（未完全照合）。**中心元の有限公式、AS正則性、一般軌道、正則 locus 等についてPDFの命題・証明と照合する。
- [ ] `papers/pdf-only/ambient/central_pair_formal_moduli.pdf`：中心三次対、全Artin比較、偏極付き復元。関連候補 `papers/generic17_ambient_recovery.tex`、`papers/boundary/pfaffian_brill_noether_technical.tex`、`papers/sections/poisson_geometry.tex`。全Artin次数での同型と局所化、低次数中心の証明を点検する。
- [ ] `papers/pdf-only/boundary/brill_noether.pdf`：Brill–Noether境界。関連候補 `papers/boundary/pfaffian_brill_noether_technical.tex`、`papers/sections/mixed_center_picard.tex`。相対Picard、接錐、6次境界Torelliの定理・証明・仮定を逐一比較する。
- [ ] `papers/pdf-only/boundary/central_quotient_singularities.pdf`：中心商と特異圏。関連候補 `papers/sections/rotation_models.tex`、`notes/research_notes.tex`、`papers/boundary/pfaffian_brill_noether_technical.tex`。有限正則性判別、Brauer・行列因子化・特異圏について未収録の補題を探索する。
- [ ] `papers/pdf-only/boundary/pfaffian_contact.pdf`：Pfaffian/contact型境界。関連候補 `papers/boundary/pfaffian_brill_noether_technical.tex`、`papers/sections/all_poisson_components.tex`。接触同値・高次正規形・計算証明書を対応させる。
- [ ] `papers/pdf-only/boundary/reye_stationary.pdf`：停留平面／Reye曲線。**独立した対応TeXの確証なし・優先度高**。既存の包括TeXでは「Reye」「停留平面」の明示節が未発見。元の論文IVソースを旧bundle等から回収するか、PDFとの厳密照合の上で現行TeXへ復元する。
- [ ] `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`：Sklyanin型の混合量子化・点加群・可換対応。関連候補 `papers/sections/explicit_hesse_center.tex`、`papers/sections/elliptic_reconstruction.tex`、`papers/boundary/pfaffian_brill_noether_technical.tex`、`sources/candidates/elliptic_v5/`。**大部な原PDF全体のTeXは未確認**。全混合項、例外値、点スキーム、同型判定を比較する。
- [ ] `notes/pdf-only/finite_smoothness_notes.pdf`：有限パラメータの正則性・証明監査。関連候補 `notes/research_notes.tex`、`papers/sections/poisson_geometry.tex`、`papers/sections/rotation_models.tex`。**第23節（pp.26–31）のperfectness反例・Artin切断・Hom有限性は `notes/source_recovery/dg_perfectness_counterexamples.tex` に部分的にTeX化済み。その他の節は未照合。**非可換generic smoothnessの条件、有限中心性、行列因子化、反例を保持する。
- [ ] `notes/pdf-only/categorical_boundary_notes.pdf`：圏論的境界・gluing。関連候補 `papers/boundary/pfaffian_brill_noether_technical.tex`、`notes/reconstruction_notes.tex`、`sources/candidates/elliptic_v5/notes.tex`。形式的主張、追加仮定、障害・反例を照合する。

## 今回収録・既収録のTeXに関する確認

- [x] Libraryの大部ソース`nc_cubic_threefold_research_ja_20261030_v18.tex`は`papers/boundary/pfaffian_brill_noether_technical.tex`と**末尾改行1文字を除きバイト一致**（Git blob SHA比較）。よって同じ本文の再追加は不要。
- [x] Libraryの`nc_cubic_v5_elliptic_reconstruction.tex`、`nc_cubic_v5_preamble.tex`、`nc_cubic_v5_refs.tex`は、それぞれ現行の`papers/sections/elliptic_reconstruction.tex`、`notes/reconstruction_preamble.tex`、`notes/reconstruction_references.tex`と本文一致。
- [x] 別原稿`nc_cubic_poisson_ambient_bridge_v6.tex`、一楕円ブロックv5の入口・ノート・依存TeXを`sources/candidates/`に配置。自動的に現行論文へ統合されたわけではない。
- [x] Libraryの以前の包括原稿v16・v17・基礎稿を`sources/candidates/longform/`に照合候補として確保。v18との節見出しは重なるが、本文・証明単位の差分確認は未了。**現行の正本ではなく一時的な照合入力**であり、整理後に有用な内容を現行稿へ取り込み、重複候補を除去する。
- [ ] Libraryの`nc-cubic-3-fold_v21.zip`、`nc-cubic-related-projects_v1.zip`、`nc_cubic_p4_bridge_20261101_v7.zip`等の元のTeXを探索する。現在のLibraryアクセスでは一部ZIPのraw-byte materializationが拒否されたため、**中身を確認したとは扱わない**。
- [ ] 追加候補ファイルの`\input`依存とLuaLaTeXコンパイルを照合する。`sources/candidates/`自体は投稿用の現行ソースではない。

## 2026-11-10 の本文TeX化作業（進行中）

- [x] `notes/pdf-only/finite_smoothness_notes.pdf` の第23節（pp.26–31）のdg加群に関する反例、Artin切断でのperfectness、derived completeなHom有限性を `notes/source_recovery/dg_perfectness_counterexamples.tex` に復元。**元の34ページ全体ではない。**
- [x] `papers/pdf-only/ambient/central_cubic_technical.pdf` に対応する比較原稿第28節（pp.43–44）の二つの中心チャートと一般中心値による正則性を `papers/source_recovery/central_cubic_generic_smoothness.tex` に復元。**外部の非可換Bertini型補題の独立再監査はしていない。**
- [ ] 上の二つのソースを既存原稿へ統合する。TeX化した節以外をPDFから再現できるようにするまでは**両方のPDFを保持**する。
- [ ] TeX化した本文の原PDFとの対応（仮定・式・証明・参照）を最終校訂する。手元のLuaLaTeX試験はdg反例の対応草稿のみで、GitHub収録版と中央チャート版の完全な組版を保証しない。

## PDFを一つ外すためのチェック項目

- [ ] 当該PDFについて章・定理・補題・系・注意・証明・計算の対応表を作り、現行TeXに欠落がないことを確認する。
- [ ] 外部一次資料への参照、仮定、未証明の主張、重要な反例を一致させる。PDFから機械抽出した文章を未確認の「原ソース」と扱わない。
- [ ] 必要なコード・入力・有限証明書と再現手順をGitで保持し、LuaLaTeXで実際にPDFを再生成・検査する。
- [ ] そのPDFを`git rm --cached <path>`で追跡解除し、`.gitignore`の例外を整理する。数学的証明が消えていないことを確認する。
- [ ] `git ls-files '*.pdf'`、ビルドとコード検証、READMEの参照先を再点検して`main`へpushする。

本TODOは「対応候補を確保してから比較・統合する」という作業計画であり、全9本のソース復旧完了を宣言するものではない。
