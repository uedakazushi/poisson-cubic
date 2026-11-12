# AGENTS.md — nc-cubic 現行研究・開発指針

**2026-11-12 / v55。GitHub main が正本。** 最初に `00_research_plan.md` を読み、次に現行論文と対応ノートを読む。

## 研究の対象と原稿入口

- **論文A** `papers/paper_a.tex`：滑らかなcubic n-fold（n>=3）のPoisson正規形、退化スキーム、Bondal予想、固定・相対Poisson moduli stacks、全Poisson構造の代数的中心三次元と量子化。中核は`papers/support/papers/sections/poisson_geometry.tex`、`universal_casimir_determinant.tex`、`general_dimension_universal_quantization.tex`。一般次元のquadratic-envelope復元はAに残す。
- **論文B** `papers/paper_b.tex`：中心三次非可換超曲面に対する、局所模型(L)、完備graded MF同値(CF)、generic AS条件の下での全coherent残余圏のrotation付き可換復元。主定理は`papers/support/papers/reconstruction/general_dimension_recovery.tex`。五変数混合族の式の特定には(D)も必要。
- **nc-cubic2**：17次元非可換三次三様体モジュライ、ambient周期性、6/7次元Poisson退化scheme、全次元Poisson pair成分の独立研究。これらをA/Bの無条件の証明と混同しない。

現行主原稿は上記二本のみ。旧論文名 `paper_c.tex` と `rotation_cubic_reconstruction.tex` を再導入しない。
`papers/support/papers/` は両主原稿から `\input@path` 経由で読む現行ソースの置場。独立再生成入口は必要な場合だけ残す。

## 確実性と優先順位

最優先は論文Aの正規形Lie補題、普遍Hesse中心、PBW/AS正則性、Cramer rank 特殊化、Poisson moduli成分とBondal主張の**独立証明監査**および先行研究の一次資料確認。原稿に証明が記載されていることと独立再監査が完了したことを区別する。

次に論文Bの(CF)曲率formality・coherent inverse、(L)相対window/stabilization、(D)明示対角比較を監査する。(L),(CF)を無条件の一般nc cubic結果と呼ばない。有限拡大次数、同値核行列、多変数での同時復元、特殊ファイバーは未完成。

証明済み／追加仮定付き／未完成／予想／有限計算を区別し、主張の仮定・依存・証明の所在・未解決箇所を同期する。数学の有効な成果・反例・必要証明書を整理の名目で削除しない。数学的内容のある `sources/candidates/` は照合完了まで保存し、旧版を新しい正本としない。

## 再現と継続

- `latexmk papers/paper_a.tex` / `latexmk papers/paper_b.tex`：LuaLaTeX、出力は追跡しない `build/`。VS Code/LaTeX Workshop はリポジトリルートから同じ `.latexmkrc` を使う。
- `python3 scripts/check_layout.py`、`python3 scripts/verify_bundle.py`：現在のTeX入口・参照・bibliography・依存ファイルの静的検証。数値証明書と実際の組版・PDF目視、証明全体の独立監査は別々に記録する。
- `python3 scripts/build.py`：A/BのLuaLaTeX組版と source/PDF receipt を作る。組版完了は実際に実行した場合だけ報告する。
- 検証状態は `validation.json`、論文Aの投稿監査は `notes/poisson_article_submission_audit.md`、論文Bは `notes/general_dimension_categorical_reconstruction.md`。

数学的変更の区切りで main に fast-forward push し、遠隔HEADと変更blobを照合。force push・GitHub Actionsは禁止。Libraryへの保存は実際にGitHub pushが失敗した場合だけの緊急避難とし、Libraryの既存ファイルを無断削除しない。日本語LuaLaTeXを標準とし、PDFや組版中間物・cacheはGitで追跡しない。旧ZIP・更新履歴・重複ソースを増やさず、現行一式のみから研究を再開できるよう維持する。
