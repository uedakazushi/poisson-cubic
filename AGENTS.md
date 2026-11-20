# Codex実行指示 — poisson-cubic

2026-11-21 / v96。最初に `00_research_plan.md` を読む。GitHub mainが正本。主論文は `papers/poisson-cubic.tex`（旧paper A）。

## 公表向け監査と担当境界

論文AはA-v61。添付の独立査読報告（対象f4c8fb131f346099ed2fb8af29429574861b505e）に基づき、既知結果との差分、Pymとの比較範囲、証明の順序と記号を整理した。中心成果は全次元正規形であり、Lie代数の根基排除を `lem:pg-basepoint-free-lie` として独立させた。EG Theorem 3.3.2(ii)の一ブロック中心元存在、Proposition 8.1.1(i)の所定古典剰余を持つ形式中心元（相対係数・還元群への対応を含む）、§9のRains公式は既知である。Proposition 8.1.1(i)に孤立特異点仮定はない。Hesse混合項はt可逆なら平行移動でその表示へ移る。本稿の追加を指定Casimirへの規格化、係数環上の正則な選択、全ブロック・独立パラメータ・同変降下として記述する。

本文順は、正規形と幾何→固定・相対モジュライ→一ブロックのPBW・中心元→全ブロック→同変化・降下→例。`quantization_foundations.tex`、`algebraic_quantization.tex`、`special_poisson_blocks.tex` が旧一体節の現行支持ファイルである。ambientはA、中心商はBに統一し、ambient復元と完全交叉背景は付録に置く。既存の主定理・必要証明・仮定は保持する。

非連結中心Cに沿う任意のr>=2重消失の持上げは `prop:pg-triple-lifting-obstruction` で独立に証明し、全連結成分正次元・滑らかという条件の下でH¹(I_C^{r−1})=C^{π₀(C)}/Cを得る。持上げ次数は超曲面の定義式の次数dに固定する。分離型では障害δ(g|X)=[(0,1)]が非零。Pymとの比較は確認したarXiv v1の番号・頁に固定し、刊行版本文・関連訂正文は未照合である。未取得資料の内容や包括的な初出を推測しない。

三次四様体ではrank4 Poissonの存在、(3,3)分離型、ambient P⁵のHessian rank<=3軌跡が平面を含む条件が同値である。後二者の同値はBricalli–Favale–Pirola (2025), Theorem 3.4を引用し、Poissonとの同値は本稿の正規形に依存する。Hessianの可約性だけでrank4を結論しない。`ex:pg-reducible-hessian-no-rank-four` と `verify_hessian_split_obstruction.py` が具体的障害を与える。

現行の仮定・証明所在・文献比較は `notes/poisson_article_submission_audit.md`、実行確認は `validation_paper_a.json` に集約する。相対忘却射のアフィン性、被約rank層、中心核と通常の中心の違い、Ω'=aΩ+cによるイデアルの不一致、中心変数を残す複数ブロックの一般の同変構成と中心商の比較の未解決性を保持する。17は構成した底の次元であり、固定h≠0の非可換同型類の像の次元ではない。Bの一般点復元と全閉パラメータでの相対同値を混同しない。


## 研究の正本と担当境界

このrepositoryはPoisson正規形・Bondal下界・代数的中心三次量子化を扱う主論文一本を正本とする。旧paper Bの完備MF移送、一般点のKu比較、coherent飽和、固定有理Hesse模型の定理・証明・計算は `uedakazushi/nc-cubic` の `papers/nc-cubic.tex` および `papers/sections/generic_recovery/` に統合済み。比較を引用する際は同repoの現在の主張を確認し、旧Bの原稿を参照することを必須としない。

現行主原稿の本文と有効な証明・計算・原資料を保持する。古い原稿、歴史的な監査、検証ログやPDF、ZIPを追跡対象に残さない。必要な一次資料の内容と仮定は現行ノートに残し、新規性未確認ならその旨を記す。過去に行われた数学点検、計算、組版を今回再実行したことにしない。

## 保存・組版・research-hub

- `main` を正本とし、通常コミットでfast-forward pushする。force push、GitHub Actionsの追加・起動、無用なPRを行わない。Libraryはpush不可能時の緊急保存に限る。
- 主公表原稿は必ず `papers/poisson-cubic.tex` に本文を置く。日本語LuaLaTeX、著者欄は空欄。組版は `latexmk papers/poisson-cubic.tex`、出力は `build/`。VS CodeのLaTeX WorkshopとSyncTeX設定を保つ。
- 設定変更時は research-hub の `papers/paper-template.tex`, `papers/README.md`, `.latexmkrc`, `.vscode/settings.json`, `.vscode/extensions.json` を参照する。
- 証明、厳密計算、ソース確認、LuaLaTeX組版、GitHub保存をそれぞれ別の状態として報告する。検証不能だったことも明記する。
- 研究の区切りには先にこのrepoの原稿・方針・ノート・README・検証状態を現状へ更新・保存し、次にresearch-hubの該当項目（到達点、主張の確実性、未解決課題、次の一手、依存関係、正本・再開先、資料確認日）を更新しmainへ通常pushする。他研究の並行変更を保持する。hubへ反映できない場合は、対象repoの保存状態と未反映理由を別に報告する。
