# 一般の非可換 cubic threefold — 現行研究継続bundle v3

2026-11-03。最初に `research_policy_ja.md`、次に `paper_ja.pdf`、その後 `research_notes_ja.md` を読む。LuaLaTeXの全原稿は `paper_ja.tex`。`technical_core_ja.pdf` は相対 PBW、中心三次、軌道商17次元、Serre の偶数Veroneseを支える研究上の詳細証明で、旧bundleのアーカイブではなく、現在の主張に必要な技術資料である。

再生成:

```sh
lualatex -interaction=nonstopmode -halt-on-error paper_ja.tex
lualatex -interaction=nonstopmode -halt-on-error paper_ja.tex
```

検証（Python 3 + SymPy）:

```sh
python3 verify_17_slice.py
python3 verify_generic_center_hessian.py
python3 verify_fermat_nc_cubic.py
python3 verify_2jet.py
```

`verify_17_slice.py` は有理数体上の群方向rank=18・結合rank=35を調べる。`verify_generic_center_hessian.py` は smooth Hesse 三次式一例について Hessian contraction rank=3を検算。一般の中心性・Hessian議論は `paper_ja.tex` に証明がある。Fermat、二次ジェットのスクリプトは特定次数・入力のチェックで、全次数の証明ではない。

`validation.json` に実行状況を記録。PDF 組版、ZIP 整合性、検証コードの結果を独立に記録する。一次文献の参照先は本文 bibliography および `research_notes_ja.md` にある。