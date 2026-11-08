# 再生成・検証手順：generic 17次元族とambient ncP⁴復元

2026-11-03 / v4。最新の研究方針 `research_policy_ja.md` から読む。

## 同梱内容

- `research_policy_ja.md`: 現行の目標・完成基準・優先課題・恒久的研究運用ルール。
- `paper_ja.tex`: 17係数族とambient復元のみに絞った日本語LuaLaTeXの公表用原稿。
- `paper_ja.pdf`: 原稿から実際に組版した13ページのPDF。
- `research_notes_ja.md`: 現行の主張の状態、計算証拠、条件、先行文献の一次参照。
- `verify_17_slice.py`: 31×31の整数行列式による17係数の横断性検算。
- `verify_center_sklyanin.py`: 三変数Sklyanin模型の中心の次数1,2,3を有理数上で計算。
- `validation.json`: 実行済みの組版・検算・ZIP検証と制約。

## 再生成

依存: LuaLaTeX (luatexja, fontspec, amsmath, amsthm, mathtools, hyperref, booktabs), `NotoSerifCJK-Regular.ttc` または TeX Live の `HaranoAjiMincho-Regular`, Python 3, SymPy。

```sh
lualatex -interaction=nonstopmode -halt-on-error paper_ja.tex
lualatex -interaction=nonstopmode -halt-on-error paper_ja.tex
python verify_17_slice.py
python verify_center_sklyanin.py
```

**期待する検算結果:** `verify_17_slice.py` が `-5538243375000` を出して `PASS`。`verify_center_sklyanin.py` は `dim Z(S)_1=0, dim Z(S)_2=0, dim Z(S)_3=1` を出して `PASS`。

外部PDFを収録せず参照元は原稿の参考文献とノートにURL/DOI/定理番号を記載した。組版の一時ファイル、過去bundle、旧原稿、キャッシュはzipに含めない。

## 数学的制約

相対PBW/中心元の全係数証明は論文で書かれた主張であり、今回すべての代数的特殊化や文献の仮定について独立に網羅監査したわけではない。17次元の横断性と低次数中心の具体的証拠はそれぞれのコードで厳密検算した。一般のtails滑らかさ、Ku成分のみからの復元は未解決とする。