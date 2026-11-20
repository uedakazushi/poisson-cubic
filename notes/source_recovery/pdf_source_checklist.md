# PDF原本とTeXソースの未照合事項（2026-11-12 / v2）

## PDF追跡解除を優先する運用（nc-cubic2）

旧研究ノートの有限正則性は[現行TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/ambient_finite_smoothness_and_recovery.tex)に整理済みでPDFの追跡を解除した。論文PDFは5件がnc-cubic2に残り、独自結果と証明を保持したまま順次TeXへ統合する。poisson-cubic本体のrotation付き可換復元と独立PDF整理を混同しない。

## 原則と現在の状態

- [x] GitHub `main` を研究の正本とし、論文・研究ノートは原則TeXから再生成する。
- [x] 自動生成PDFは`.gitignore`で無視する。
- [x] 関連が判明したTeXを`sources/candidates/`に追加し、既存の現行TeXを変更しない。
- [ ] **現在保持する論文PDF5本の定理・仮定・証明・計算を、対応する現行TeXと照合する。**
- [ ] 照合後に必要な本文を`papers/`・`notes/`へ統合し、LuaLaTeX組版・参照・計算を確認する。
- [x] 原本PDF8件を当初nc-cubic2へ移転した。その後研究ノート2件とBrill–Noether旧論文1件の追跡を解除し、論文PDF5件を保持する。

以下の「関連TeX」は**原PDFを完全再現するソースと認定したものではない**。特にPDFの同名／同主題資料が現行TeXにすべて含まれるとは推論しない。重複する候補ソースは照合が終わるまで保持する。

## 移転済みPDFごとのTeX照合チェックリスト

- [ ] [`papers/pdf-only/ambient/central_cubic_technical.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_cubic_technical.pdf)：中心三次量子化の詳細。関連候補 `papers/support/papers/sections/poisson_geometry.tex`、[nc-cubic2の17次元モジュライ論](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/nc_cubic_threefold_moduli.tex)、`sources/candidates/poisson_ambient_bridge_v6.tex`。**第28節の中心チャート貼合せとvery-general正則性の命題・証明は `papers/support/papers/source_recovery/central_cubic_generic_smoothness.tex` に部分的にTeX化済み（未完全照合）。**中心元の有限公式、AS正則性、一般軌道、正則 locus 等についてPDFの命題・証明と照合する。
- [ ] [`papers/pdf-only/ambient/central_pair_formal_moduli.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_pair_formal_moduli.pdf)：中心三次対、全Artin比較、偏極付き復元。関連候補 [nc-cubic2の17次元モジュライ論](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/nc_cubic_threefold_moduli.tex)、[nc-cubic2の独立境界TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pfaffian_brill_noether_technical.tex)、`papers/support/papers/sections/poisson_geometry.tex`。全Artin次数での同型と局所化、低次数中心の証明を点検する。
- [x] Brill–Noether旧論文PDFは追跡解除済み。主要な内容は [現行独立境界TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pfaffian_brill_noether_technical.tex) にある。ただし旧PDF全文との証明単位の独立照合ではない。
- [ ] [`papers/pdf-only/boundary/central_quotient_singularities.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/boundary/central_quotient_singularities.pdf)：中心商と特異圏。関連候補 `papers/support/papers/sections/rotation_models.tex`、`notes/research_notes.tex`、[nc-cubic2の独立境界TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pfaffian_brill_noether_technical.tex)。**中心曲面の完全判別式・特異点・混合パラメータへの変換は [nc-cubic2の中心曲面判別式TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/central_fiber_discriminant.tex) に証明付きで移植済み。Azumaya locus、Brauer指数6、非可換tails判別の完全証明は未収録。**有限正則性判別、Brauer・行列因子化・特異圏について未収録の補題を探索する。
- [ ] [`papers/pdf-only/boundary/pfaffian_contact.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/boundary/pfaffian_contact.pdf)：Pfaffian/contact型境界。関連候補 [nc-cubic2の独立境界TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pfaffian_brill_noether_technical.tex)、`papers/support/papers/sections/all_poisson_components.tex`。接触同値・高次正規形・計算証明書を対応させる。
- [ ] [`papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf)：Sklyanin型の混合量子化・点加群・可換対応。関連候補 `papers/support/papers/sections/explicit_hesse_center.tex`、`papers/support/papers/sections/elliptic_reconstruction.tex`、[nc-cubic2の独立境界TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pfaffian_brill_noether_technical.tex)、`sources/candidates/elliptic_v5/`。**大部な原PDF全体のTeXは未確認**。全混合項、例外値、点スキーム、同型判定を比較する。
- [x] 有限正則性ノートPDFは追跡解除済み。[現行LuaLaTeXノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/ambient_finite_smoothness_and_recovery.tex)に有限中心値の判定・偏極付き復元等を整理。dg反例と有限bar検証はpoisson-cubicの独立TeXが正本。
- [x] 圏論的境界の概要ノートPDFは追跡解除済み。現行Pfaffian・Brill–Noether稿と研究方針を参照。

## 今回収録・既収録のTeXに関する確認

- [x] Libraryの大部ソース`nc_cubic_threefold_research_ja_20261030_v18.tex`は旧境界TeXと以前一致していたが、**現行のnc-cubic2大部TeXは主題別に分割・再編集され、もはやバイト一致しない**。同じ数学的本文を再追加せず、現行の節入力を正本とする。
- [x] Libraryの`nc_cubic_v5_elliptic_reconstruction.tex`、`nc_cubic_v5_preamble.tex`、`nc_cubic_v5_refs.tex`は、それぞれ現行の`papers/support/papers/sections/elliptic_reconstruction.tex`、`notes/reconstruction_preamble.tex`、`notes/reconstruction_references.tex`と本文一致。
- [x] 別原稿`nc_cubic_poisson_ambient_bridge_v6.tex`、一楕円ブロックv5の入口・ノート・依存TeXを`sources/candidates/`に配置。自動的に現行論文へ統合されたわけではない。
- [x] Libraryの以前の包括原稿v16・v17・基礎稿を`sources/candidates/longform/`に照合候補として確保。v18との節見出しは重なるが、本文・証明単位の差分確認は未了。**現行の正本ではなく一時的な照合入力**であり、整理後に有用な内容を現行稿へ取り込み、重複候補を除去する。
- [ ] Libraryの`nc-cubic-3-fold_v21.zip`、`nc-cubic-related-projects_v1.zip`、`nc_cubic_p4_bridge_20261101_v7.zip`等の元のTeXを探索する。現在のLibraryアクセスでは一部ZIPのraw-byte materializationが拒否されたため、**中身を確認したとは扱わない**。
- [ ] 追加候補ファイルの`\input`依存とLuaLaTeXコンパイルを照合する。`sources/candidates/`自体は投稿用の現行ソースではない。

## 2026-11-10 の本文TeX化作業（進行中）

- [x] [有限正則性の現行TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/ambient_finite_smoothness_and_recovery.tex) の第23節（pp.26–31）のdg加群に関する反例、Artin切断でのperfectness、derived completeなHom有限性を `notes/source_recovery/dg_perfectness_counterexamples.tex` に復元。**元の34ページ全体ではない。**
- [x] [`papers/pdf-only/ambient/central_cubic_technical.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_cubic_technical.pdf) に対応する比較原稿第28節（pp.43–44）の二つの中心チャートと一般中心値による正則性を `papers/support/papers/source_recovery/central_cubic_generic_smoothness.tex` に復元。**外部の非可換Bertini型補題の独立再監査はしていない。**
- [ ] 上の二つのソースを既存原稿へ統合する。TeX化した節以外をPDFから再現できるようにするまでは**中心三次技術PDFをnc-cubic2で保全**する。
- [ ] TeX化した本文の原PDFとの対応（仮定・式・証明・参照）を最終校訂する。手元のLuaLaTeX試験はdg反例の対応草稿のみで、GitHub収録版と中央チャート版の完全な組版を保証しない。

## 2026-11-10：８本の原本を確定・照合した追加進捗

- [x] nc-cubic2に移転済みのPDF８本に対応する原本（同一バイトサイズのLibrary PDF）をすべて特定し、８本の目次・総ページ数を点検。当初574ページ。照合表は [PDF数学内容一覧](pdf_mathematical_inventory.md)。
- [x] 論文VIの中心三次曲面の必要十分判別式 `H(H+1)(27H+28)` と特異点の分類を証明付きで [nc-cubic2の中心曲面判別式TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/central_fiber_discriminant.tex) に移植。混合パラメータの因子 `(α³+9)(28α³+243)` への変換も移植。
- [x] 判別式２本、特殊点のHessian、`H=9` のGroebner基底を有理数演算で確認。再現用 [nc-cubic2の記号検算コード](https://github.com/uedakazushi/nc-cubic2/blob/main/computations/verify_central_fiber_discriminant.py) を追加。
- [ ] 論文VIの非可換tailsへの判別式昇格を証明するAzumaya性・local order・Brauer指数6・特異圏の資料をTeX化する。中心曲面の判別式だけで済ませない。
- [ ] 旧資料全体を一つの現行原稿に機械的に結合するのではなく、原PDFごとの章・定理・証明・依存計算の完全照合後にTeXへの復元完了を認定する。

## PDFを一つ外すためのチェック項目

- [ ] 当該PDFについて章・定理・補題・系・注意・証明・計算の対応表を作り、現行TeXに欠落がないことを確認する。
- [ ] 外部一次資料への参照、仮定、未証明の主張、重要な反例を一致させる。PDFから機械抽出した文章を未確認の「原ソース」と扱わない。
- [ ] 必要なコード・入力・有限証明書と再現手順をGitで保持し、LuaLaTeXで実際にPDFを再生成・検査する。
- [x] PDFのGit追跡をnc-cubic2に移し、poisson-cubicの追跡例外を撤去した。TeXとの数学的照合は別途必要。
- [ ] `git ls-files '*.pdf'`、ビルドとコード検証、READMEの参照先を再点検して`main`へpushする。

本TODOは「対応候補を確保してから比較・統合する」という作業計画であり、現行5本のソース復旧完了を宣言するものではない。


## 独立した Reye 研究

Reye 論文・停留平面の PDF（77ページ）と TeX・計算コードおよび残課題は [uedakazushi/reye](https://github.com/uedakazushi/reye) へ移した。ここでは非Reyeの現行論文PDF5本だけを扱う。

### SMに関係する部分TeX化の現在の到達点

`notes/sm_bar_and_spreading.tex`（第18--21節、pp.23--25）を日本語LuaLaTeXで4ページに組版し、有限bar段階retract判定、Artin底検出、generic spreadingの証明を再構成した。現行のSMが証明されたことを意味しない。旧34ページの研究ノートPDFは追跡解除済み。有限正則性の要点はnc-cubic2の現行TeXと本repoの証明ノートに集約した。
