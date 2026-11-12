# AGENTS.md — nc-cubic 現行研究・開発指針

**2026-11-12 / v57。** GitHub mainが正本。必ず `00_research_plan.md` を最初に読む。

## 現行原稿と証明の優先順位

主原稿はA `papers/paper_a.tex` とB `papers/paper_b.tex` の二本のみ。支持ソースは `papers/support/papers/`。AはPoisson構造・量子化、Bは一般点のrotation付き全coherent可換復元を扱う。17次元モジュライとambient周期性はnc-cubic2に保持する。

論文B-v41の主定理は `general_dimension_recovery.tex`、新しい証明の核は `generic_cubic_descent.tex`（いずれもpapers/support/papers/reconstruction/）。監査は `notes/paper_b_proof_audit.md`。一般点AS正則性はflat入力の帰結。方程式の模型はK=C(h)上、圏同値は有限拡大後。幾何学的一意性は全n>=3。BFK Theorem 5.15の既知の生成上界を使い、一般生成定理の新規性を主張しない。

**最短経路**：固定三対象のenhanced比較→Euler非零性→代数閉包上のBFK生成→perfect核の有限降下→coherent飽和→低Nat底変更→K上の可積分勾配空間。全MF同値(CF)の代替となる固定三対象条件 `gcd:prop:three-object` を優先監査する。相対window/stabilizationとrotation・三次周期図式を確認する。

(L),(CF)の全独立監査は未完であり、一般の全nc cubicへ無条件に適用しない。(D)は明示式を指定する追加条件。低積の次元や有限可積分性だけで圏同値を主張しない。特殊点の生成性だけからgeneric生成性を持ち上げない。形式Taylor和を任意のLaurent対象へ評価しない。

論文Aの全Poisson代数中心の存在に、形式中心元・Dolgushev/formalityを必須入力として戻さない。正規形Lie補題、Hesse中心恒等式、PBW/AS、Bondal・moduli成分の独立監査を継続する。

## 保存・再現

全有効結果・証明・反例・必要証明書は保持し、旧名や古い状態説明を積み重ねず現行方針へ整理する。新規性未確認を明示する。日本語LuaLaTeX、rootからlatexmk、PDFはbuild/に生成してGit追跡しない。GitHub Actions・force push禁止。区切りでmainへ通常のfast-forwardで保存し、遠隔ref/blobを確認する。Libraryは実際のGitHub保存失敗時だけ緊急避難、既存Libraryファイルを無断削除しない。

静的検査は `python3 scripts/check_layout.py` と `python3 scripts/verify_bundle.py`。B-v41の新規有限計算は `computations/verify_generic_cubic_descent.py`。Bの最新検証は `validation_paper_b.json`、Aその他の既存検証は `validation.json`。新しい単独抜粋の組版はB全文の組版成功を意味しない。原稿記載、独立監査、計算、組版、保存を区別する。
