# 滑らかな三次超曲面のPoisson幾何

2026-11-21 / v97。再開は [研究方針](00_research_plan.md) から。GitHub mainが正本。

## 公表用論文

[papers/poisson-cubic.tex](papers/poisson-cubic.tex) は **正規形・退化軌跡・モジュライ** を扱う日本語LuaLaTeX論文（A-v62）である。全次元のPoisson正規形、全階数のBondal下界、固定・相対Poissonスキームと成分、Fermatの非被約零点、非楕円ブロック、三次四様体の純楕円分類、完全交叉の古典的背景を含む。

量子化と非可換比較は、次の独立した二論文を正本とする。

| 論文 | 正本 | 内容 |
| --- | --- | --- |
| 三次超曲面の代数的量子化 | [cubic-quantization/papers/cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) | PBW・AS性、代数的中心三次、全ブロックと多パラメータ、同変中心元と降下、二次包絡。 |
| 非可換三次超曲面の可換復元とモジュライ | [nc-cubic/papers/nc-cubic.tex](https://github.com/uedakazushi/nc-cubic/blob/main/papers/nc-cubic.tex) | 完備MF移送・一般点Ku比較、良い一ブロック型のO-markedモジュライ、残余射と降下障害。 |

古典的正規形から量子化へ、量子化から非可換比較へという依存を保つ。後者の一ブロック仮定を量子化全体へ課さず、一般点の比較を全パラメータでの同値と読み替えない。量子化の証明・計算・現行ノートはnc-cubic内で管理し、このrepoでは重複保持しない。

## 現行資料と未解決点

- [研究ノート](notes/research_notes.md)：幾何とモジュライの入口、現在有効な補助知識。
- [公表向けの仮定・証明・文献比較](notes/poisson_article_submission_audit.md)：既知結果の帰属と一次資料の確認範囲。
- [検証状態](validation_paper_a.json)：読解点検、厳密計算、参照検査、組版を区別する。
- [支持原稿](papers/support/papers/sections/) と [計算資産](computations/)：古典的結果の証明・例・有限検算。

中心的な公表準備課題はPymの刊行版・訂正との比較、包括的な正規形・成分定理の新規性確認である。Pym arXiv:1507.05668v1との不整合には現行本文で独立した構成と非連結中心の持上げ障害を示すが、未取得の刊行版本文については結論を先取りしない。

独立した相対復元・Artin・étale模型のうち以前からnc-cubic2で管理する研究は [同repoの研究方針](https://github.com/uedakazushi/nc-cubic2) を参照する。今回の三論文の証明依存と他研究の担当範囲を混同しない。

## 組版と再現

LuaLaTeX・LuaTeX-ja・latexmk、および `requirements.txt` のPython依存を使う。repoルートから実行する。

```sh
python3 scripts/verify_bundle.py
python3 scripts/verify_article_a_numbering.py
latexmk papers/poisson-cubic.tex
python3 scripts/verify_bundle.py --only poisson-cubic --require-pdfs
```

`python3 scripts/build.py --only poisson-cubic` は組版と入力/PDF対応を確認する。Git追跡対象の検査は `python3 scripts/check_layout.py`。出力は `build/poisson-cubic.pdf` と同じ場所のSyncTeX。VS Codeではrepo全体を開き、LaTeX Workshopの既存のrepoルート基準レシピを使う。他repoのPDFやauxファイルは組版に不要。

生成・証明点検・厳密計算・組版・GitHub保存は別々の状態として報告する。通常コミットでmainへ保存し、Actions・force push・不要なPRは行わない。PDF・中間物は非追跡。GitHub管理後のLibrary二重保存や定常ZIPは行わず、push不能時の緊急保存か明示指示時のみ用いる。既存Libraryファイルは削除しない。研究の区切りにはこのrepoを保存した後にresearch-hubの該当項目を更新する。
