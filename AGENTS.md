# AGENTS.md — nc-cubic 現行研究・開発指針

**2026-11-12 / v58。** GitHub mainが正本。最初に `00_research_plan.md` を読む。

主原稿はA `papers/paper_a.tex` とB `papers/paper_b.tex` の二本。支持節は `papers/support/papers/`。AはPoisson幾何・量子化、Bは一般点のrotation付き全coherent可換復元。17次元モジュライ・ambient周期性はnc-cubic2に保持する。

## 論文Bの現在の依存と最優先

B-v42の `three_object_window.tex` が代数的入力から(L)を証明する。完備Homの有限縮約→正則局所基底へのproper性降下→実際のdg section/window→剰余Hom比較への導来Nakayama→有限長filtrationによる三対象の像→rotationと中心元からの三次周期性、という順序である。CFをこの証明の入力に戻さない。

主定理の残る比較条件は(CF_3)：完備底上のK,K(1),K(2)から可換MFのE,E(1),E(2)へのunital A∞ quasi-equivalenceで、全Hom・高次積・内部shift・周期比較を保つ。全MF同値(CF)は十分条件。次はformal_cubic_mf_reconstructionとcurved_gauge_comparisonの構成を固定三対象に制限し、実際の関手・逆・収束・周期図式を監査する。ここは全独立監査未完であり、一般nc cubicの無条件復元と呼ばない。

一般点の存在→smoothness→低Nat底変更→K上の勾配積分の順序を維持する。方程式はK=C(h)上、同値核は有限拡大後。幾何学的一意性は全n>=3。生成上界はBFKの既知結果で、新しい一般生成定理と呼ばない。(D)は特定の明示式を指定する条件。低積の有限可積分性だけで圏同値を結論しない。特殊点の生成性だけを一般点へ持ち上げず、形式Taylor和を任意Laurent対象へ評価しない。

Aの量子中心元存在に形式中心元やformalityを必須入力として戻さない。Lie正規形、普遍Hesse、PBW/AS、Bondal・moduli成分の独立監査を継続する。

## 保存と再現

全ての有効な支持節・反例・必要証明書を保持する。主張の仮定・依存・証明所在、記載／独立監査／計算／組版を分ける。数学的内容を整理の名目で削らない。

`python3 computations/verify_three_object_window.py --output build/three_object_window_checks.json` は有限線形代数と添字の検算であり、非可換MFやCF_3の形式検証ではない。`latexmk papers/support/papers/three_object_window.tex` は証明抜粋を生成し、本文外の参照はラベルで表示する。B全文の組版成功を意味しない。最新状態は `validation_paper_b.json`、詳細監査は `notes/paper_b_proof_audit.md`。

日本語LuaLaTeX、出力はbuild/、PDF・中間物はGit非追跡。mainへfast-forwardで保存し遠隔確認。GitHub Actions・force push禁止。LibraryはGitHub保存実失敗時のみ緊急退避し、既存Libraryファイルを無断削除しない。
