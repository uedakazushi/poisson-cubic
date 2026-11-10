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
- [ ] `papers/pdf-only/boundary/central_quotient_singularities.pdf`：中心商と特異圏。関連候補 `papers/sections/rotation_models.tex`、`notes/research_notes.tex`、`papers/boundary/pfaffian_brill_noether_technical.tex`。**中心曲面の完全判別式・特異点・混合パラメータへの変換は `papers/source_recovery/central_fiber_discriminant.tex` に証明付きで移植済み。Azumaya locus、Brauer指数6、非可換tails判別の完全証明は未収録。**有限正則性判別、Brauer・行列因子化・特異圏について未収録の補題を探索する。
- [ ] `papers/pdf-only/boundary/pfaffian_contact.pdf`：Pfaffian/contact型境界。関連候補 `papers/boundary/pfaffian_brill_noether_technical.tex`、`papers/sections/all_poisson_components.tex`。接触同値・高次正規形・計算証明書を対応させる。
- [ ] `papers/pdf-only/boundary/reye_stationary.pdf`：停留平面／Reye曲線。**§2–3と§4.1–4.4の主要結果を `papers/source_recovery/reye_stationary_core.tex` に証明付きで部分復元し、Chern積分275等は厳密検算済み**。§6–7と§13は別TeXへ主証明を再構成済み。残る§5・8–12の全証明、§6–7・§13の依存補題、550本の曲線網羅性・法束、長さ3とcuspの全計算を照合する。77ページの原PDFはその間保持。
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

## 2026-11-10：９本の原本を確定・照合した追加進捗

- [x] GitHubで追跡中のPDF９本に対応する原本（同一バイトサイズのLibrary PDF）をすべて特定し、９本の目次・総ページ数を点検。合計651ページ。照合表は `SOURCE_RECOVERY_AUDIT_20261110.md`。
- [x] 論文VIの中心三次曲面の必要十分判別式 `H(H+1)(27H+28)` と特異点の分類を証明付きで `papers/source_recovery/central_fiber_discriminant.tex` に移植。混合パラメータの因子 `(α³+9)(28α³+243)` への変換も移植。
- [x] 判別式２本、特殊点のHessian、`H=9` のGroebner基底を有理数演算で確認。再現用 `computations/source_recovery/verify_central_fiber_discriminant.py` を追加。
- [ ] 論文VIの非可換tailsへの判別式昇格を証明するAzumaya性・local order・Brauer指数6・特異圏の資料をTeX化する。中心曲面の判別式だけで済ませない。
- [x] 論文IV（Reye）の §2–3、§4.1–4.4 の主要な数学的内容を証明付きで `papers/source_recovery/reye_stationary_core.tex` に復元。LuaLaTeXで8ページを二回組版し、`computations/source_recovery/verify_reye_275.py` でChern数、Porteous積分275、行列式・Hesse恒等式を正確に検証。
- [ ] 論文IVの未移植の中心は §5・8–12 の法束・全Artin変形、550本の網羅性、長さ3のcusp局所模型、および§6–7・§13の依存補題と校訂である。全77ページの再生成性を確認するまで原PDFを保持。
- [ ] 総651ページを一つの現行原稿に機械的に結合するのではなく、原PDFごとの章・定理・証明・依存計算の完全照合後にPDFを追跡解除する。

## PDFを一つ外すためのチェック項目

- [ ] 当該PDFについて章・定理・補題・系・注意・証明・計算の対応表を作り、現行TeXに欠落がないことを確認する。
- [ ] 外部一次資料への参照、仮定、未証明の主張、重要な反例を一致させる。PDFから機械抽出した文章を未確認の「原ソース」と扱わない。
- [ ] 必要なコード・入力・有限証明書と再現手順をGitで保持し、LuaLaTeXで実際にPDFを再生成・検査する。
- [ ] そのPDFを`git rm --cached <path>`で追跡解除し、`.gitignore`の例外を整理する。数学的証明が消えていないことを確認する。
- [ ] `git ls-files '*.pdf'`、ビルドとコード検証、READMEの参照先を再点検して`main`へpushする。

本TODOは「対応候補を確保してから比較・統合する」という作業計画であり、全9本のソース復旧完了を宣言するものではない。

## 2026-11-10：Reye 論文 IV の Hilbert/PT・ruling 移植

- [x] \`papers/source_recovery/reye_stationary_core.tex\` に、原論文IV第6・7節の \(\operatorname{Hilb}_{3m}\) と \(\mathrm{PT}_{0,3}\) のスキーム同型および仮想数275の証明を追加した（以前の275停留点・法束定理を入力）。
- [x] 同TeXに原論文IV命題13.1の普遍停留incidenceの滑らか既約な35次元ベクトル束模型と275点被覆の推移性を追加した。
- [x] 同TeXに原論文IV命題13.13の、rulingを選ぶ等方平面による550本の二成分分解を、原論文第10.4節の網羅性・法束を仮定した形で追加した。
- [ ] 原論文第6節のHilbert関数の独自証明で、飽和化への自然写像の全射性・向きを修正する。現行TeXの平面三次分類はSkjelnes--Smith、Harris--Roth--Starrを使用。
- [ ] 原論文第7節の全PT BPS変換、第8節のprimary GW/PTおよびGV係数への同一視を一次文献の正確な適用条件とともに移す。
- [ ] 原論文第5・9・10節の法束と全Artin同型、550本の網羅性と \(\mathcal O_{\mathbb P^1}(-1)^{\oplus2}\) の全証明を移植。
- [x] 原論文第13.2・13.3節の二点付きincidence全相対位置・単一foldのconormal一意性を移植済み。\(S_{275}\) の証明は別原稿第3・10節の結果を入力とする。特殊階数層は本文で係数比較したが、全行列の独立機械監査は未了。
- [ ] 原論文第12節の長さ3・cusp局所模型・射影regularityを移植。
- [ ] 77ページ原PDFの全章・証明・一次引用とTeXが一致しLuaLaTeXで再生成できることを確認した後にのみ、同PDFのGit追跡を解除する。

## 2026-11-10：Reyeモノドロミーの証明再構成（今回）

- [x] `papers/source_recovery/reye_full_monodromy.tex` を追加。原論文IV第13.1–13.4節の二点付きincidence全相対位置、階数表、conormalによる唯一分岐点、transposition、`S_275`、550本の対角作用を証明付きで再構成。
- [x] `computations/source_recovery/verify_reye_two_point_ranks.py` で一般相対位置5型の二つ目の停留条件の階数を正確な有理数演算で検算。特殊層の表全体は追加の独立監査が必要。
- [x] `computations/source_recovery/verify_reye_fold_conormal.py` で分岐conormalの特異点配置を検算。
- [x] LuaLaTeXによる独立組版（7ページ）・引用参照解決を確認。生成PDFは追跡しない。
- [ ] 原論文第10節の550曲線網羅性・法束、第5・9節の全Artin変形と法束、第11–12節の長さ2・3の射影実現をそれぞれ詳細にTeX化し、対応する原PDFの定理と照合する。
- [ ] 全77ページの独立数学的内容を確実にTeXへ保持した後でのみ`papers/pdf-only/boundary/reye_stationary.pdf`の追跡解除を行う。

## 2026-11-10：Reye 第5・9・10・12節の追加復元

- [x] Reye曲線の法束の完全列、退化写像の一次比較と全局所Artin基底上の埋込み変形を `papers/source_recovery/reye_deformations_degree_one.tex` に整理。
- [x] 定階数4 Hessian直線のkernel二次曲線・全Artin変形対応・法束 `O(-1)^2` を同TeXに整理。
- [x] 正則偶数次対称pencilの平方判別式判定、五次rank4 pencilの `e=0,1,2`、全rank3以下の補題、550本の全網羅と次数1 GW仮想数550を同TeXに整理。
- [x] 長さ3特殊化の横断五変数消去、四次係数 `κΔ/12`、`Δ=4+21AB+27C²`、二変数 `T³+uT+v` のversal cuspを `papers/source_recovery/reye_length_three_cusp_jet.tex` にTeX化。
- [x] 上の有限係数恒等式と具体的F0の滑らかさ、およびrank `e=0,1,2` の例をPython/SymPyで独立検算。コードは `computations/source_recovery/`。
- [ ] GitHub収録版の二つのTeXを `latexmk` で再組版し、参考文献・行列・引用等を確認する（ローカル詳細稿２本の組版とは区別）。
- [ ] 原論文IV第11節の長さ2の全Artin比較・Atiyah F2・PT局所寄与、12.2–12.3節の普遍ordered模型のJacobian階数層・射影regular開性・同じ法束とPT寄与の詳細証明を移植。
- [ ] 原PDF第5・9・10・12節の全命題、補題、注意、証明、数式番号を、現行ソースと節単位で厳密照合する。以上は原本77ページの完全代替ではないためPDFの追跡は維持。
