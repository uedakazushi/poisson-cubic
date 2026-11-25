# Codex実行指示 — poisson-cubic

2026-11-25 / v98。最初に `00_research_plan.md` を読む。GitHub mainが正本。主論文は `papers/poisson-cubic.tex`（古典Poisson論文A-v63）。

## 公表向け監査と担当境界

本repoはPoisson正規形・退化軌跡・Bondal下界・固定および相対Poissonモジュライの古典論を担当する。主原稿はA-v63。量子化の全証明と再現資産は `uedakazushi/cubic-quantization` の独立論文 `papers/cubic-quantization.tex`、可換復元・モジュライは `uedakazushi/nc-cubic` の主論文 `papers/nc-cubic.tex` が正本である。三論文の対象範囲を区別し、数学的内容を削らず、重複した量子化本文を本repoへ戻さない。

全次元正規形の中心はEuler–Koszul表示、Euler–divergence恒等式によるJacobi持上げ、Hessian線形化、支持上の非退化形式からのLie代数構成である。`lem:pg-basepoint-free-lie` は根基の可換イデアル内のsl₂加群と最高根のベクトルから共通零点を構成し、根基と階数2以上の単純因子を排除する。BondalのEuler–divergenceの方法とLie代数の既知定理を適用し、Derdzinski–Gal Theorem Bは独立に証明した結論との比較に用いる。古典論の証明を量子化または非可換比較の結果に依存させない。外部引用には現在の論文名・具体的ラベル・仮定を付け、旧paper A/Bを取得することを再開の前提にしない。

Lean参照版は `uedakazushi/nc-cubic-lean` のcommit `9736787f3a95f52bc3d233ab768a6ab6396d0c24`、対応表は `notes/lean_proof_sources.txt`。参照版を用いた通常の証明の改稿と、Leanの再ビルド・公理依存監査・TeX本文の形式検証を区別する。今回これらの形式検証は実施していない。退化スキーム、Bondal下界、モジュライの結論は参照版の幾何学的主定理の形式化範囲に含まれない。

`prop:pg-triple-lifting-obstruction` は全連結成分正次元・滑らかの条件で任意のr≥2を扱い、持上げ次数は超曲面の次数dに固定する。Pymとの比較は取得済みarXiv v1の番号・頁に限定し、刊行版本文・訂正文・包括的初出は未確認と明記する。

三次四様体のrank4、(3,3)分離型、ambient P⁵のHessian rank≤3軌跡が平面を含む条件の同値では、後二者の同値をBricalli–Favale–Pirola Theorem3.4に帰属する。Hessian可約性だけからrank4を結論しない。相対忘却射のアフィン性、被約rank層、固定Poissonスキームの非被約構造を区別する。

仮定・証明所在・文献比較は `notes/poisson_article_submission_audit.md`、実行状態は `validation_paper_a.json`。現行の有効な証明・計算・原資料を保持し、旧稿・履歴的監査・ログ・PDF・ZIPを蓄積しない。原稿の証明、過去の点検、今回の読解点検・計算・組版を区別する。

## 保存・組版・research-hub

- `main` を正本とし、通常コミットでfast-forward pushする。force push、GitHub Actionsの追加・起動、無用なPRを行わない。Libraryはpush不可能時の緊急保存に限る。
- 主公表原稿は必ず `papers/poisson-cubic.tex` に本文を置く。日本語LuaLaTeX、著者欄は空欄。組版は `latexmk papers/poisson-cubic.tex`、出力は `build/`。VS CodeのLaTeX WorkshopとSyncTeX設定を保つ。
- 設定変更時は research-hub の `papers/paper-template.tex`, `papers/README.md`, `.latexmkrc`, `.vscode/settings.json`, `.vscode/extensions.json` を参照する。
- 証明、厳密計算、ソース確認、LuaLaTeX組版、GitHub保存をそれぞれ別の状態として報告する。検証不能だったことも明記する。
- 研究の区切りには先にこのrepoの原稿・方針・ノート・README・検証状態を現状へ更新・保存し、次にresearch-hubの該当項目（到達点、主張の確実性、未解決課題、次の一手、依存関係、正本・再開先、資料確認日）を更新しmainへ通常pushする。他研究の並行変更を保持する。hubへ反映できない場合は、対象repoの保存状態と未反映理由を別に報告する。
