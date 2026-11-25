# 滑らかな三次超曲面のPoisson幾何

2026-11-25 / v101。再開は [研究方針](00_research_plan.md) から。GitHub mainが正本。

## 公表用論文

[papers/poisson-cubic.tex](papers/poisson-cubic.tex) は **正規形・退化軌跡・モジュライ** を扱う日本語LuaLaTeX論文（A-v66）である。arXiv公開・論文誌投稿を予定し、隣接分野の研究者が通読できる論文として編集する。全次元のPoisson正規形、全階数のBondal下界、固定・相対Poissonスキームと成分、Fermatの非被約零点、非楕円ブロック、三次四様体の純楕円分類、完全交叉の古典的背景を含む。

正規形の証明は [nc-cubic-lean の参照版](https://github.com/uedakazushi/nc-cubic-lean/tree/9736787f3a95f52bc3d233ab768a6ab6396d0c24)を踏まえ、Euler–Koszul表示、Jacobi恒等式の持上げ、三重ベクトルの支持上のLie代数と根ベクトルによる障害を通常の数学的証明として展開した。対応するソースと証明範囲は [参照版との対応](notes/lean_proof_sources.txt) に記す。今回Leanを再ビルドしておらず、TeX本文の形式検証も行っていない。

序論では、次元3以上の射影完全交叉で非零Poisson構造を持つ4型を示し、曲面・Fano三様体・任意次元の構造定理と本稿の全階数正規形を比較する。公開草稿 `uedakazushi/poisson-p4` の147成分という分類案は、人間による検証が未了であることを明記して引用する。全次元分類の優先権は、完全交叉の一つの型の全メンバー・全階数という範囲で「著者の知る限り」と限定しており、包括的に確定していない。

量子化と非可換比較は、次の独立した二論文を正本とする。

| 論文 | 正本 | 内容 |
| --- | --- | --- |
| 三次超曲面の代数的量子化 | [cubic-quantization/papers/cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) | PBW・AS性、代数的中心三次、全ブロックと多パラメータ、同変中心元と降下、二次包絡。 |
| 非可換三次超曲面の可換復元とモジュライ | [nc-cubic/papers/nc-cubic.tex](https://github.com/uedakazushi/nc-cubic/blob/main/papers/nc-cubic.tex) | 完備MF移送・一般点Ku比較、良い一ブロック型のO-markedモジュライ、残余射と降下障害。 |

古典的正規形から量子化へ、量子化から非可換比較へという依存を保つ。後者の一ブロック仮定を量子化全体へ課さず、一般点の比較を全パラメータでの同値と読み替えない。量子化の主原稿と再現資産はcubic-quantization、関連する中心元のノートはnc-cubicを参照し、このrepoでは重複保持しない。

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
python3 scripts/build.py --only poisson-cubic
python3 scripts/verify_bundle.py --only poisson-cubic --require-pdfs
```

`python3 scripts/build.py --only poisson-cubic` は組版と入力/PDF対応を確認する。Git追跡対象の検査は `python3 scripts/check_layout.py`。出力は `build/poisson-cubic.pdf` と同じ場所のSyncTeX。VS Codeではrepo全体を開き、LaTeX Workshopの既存のrepoルート基準レシピを使う。他repoのPDFやauxファイルは組版に不要。

非楕円成分の証明に用いる整数小行列は、PythonとSymPy（`requirements.txt`）で再生成・照合できる。

```sh
python3 computations/verify_nonelliptic_components.py
```

このコマンドは節点型・尖点型の行列を本文の式から作り、有理数上で階数とピボット行を求め、整数上の33次小行列式を保存済みの証明書と照合する。成功すると両例について `PASS`、`rank 33`、それぞれ `det 8916100448256`、`det -4565043429507072` を表示する。`--direct` を付けると、Schouten括弧から直接構成した線形化の階数も追加で照合する。

`papers/build-metadata.tex` はGit管理しない任意入力であり、存在しなくても `latexmk papers/poisson-cubic.tex` でコンパイルできる。`python3 build_pdf.py` はこのファイルがなければ実行時のJST日時から表紙情報と日付入りファイル名を生成し、表紙を確実に再組版して `dist/` にPDFを保存する。既存のmetadataは保ち、同名PDFは上書きしない。本文を改訂して別版を作る場合は `python3 build_pdf.py --new-version` を使う。

生成・証明点検・厳密計算・組版・GitHub保存は別々の状態として報告する。通常コミットでmainへ保存し、Actions・force push・不要なPRは行わない。PDF・中間物は非追跡。GitHub管理後のLibrary二重保存や定常ZIPは行わず、push不能時の緊急保存か明示指示時のみ用いる。既存Libraryファイルは削除しない。研究の区切りにはこのrepoを保存した後にresearch-hubの該当項目を更新する。
