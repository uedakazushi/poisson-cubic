# nc-cubic：一般次元・各Poisson成分の可換復元

**2026-11-10・v17。正本はこのGitHubリポジトリのmainのみ。** 最初に `00_research_plan.md`、次に `notes/research_notes.md` を読む。Library保存はpush実失敗時の緊急避難だけとする。

## 現在の中心結果

実在するsmooth proper dg族と自己同値が、一点で滑らかなcubicのKuznetsov成分とrotationに一致すれば、étale局所的に可換cubic族として実現できる。同値双加群の小拡大障害をrotation不変HH²で消去する証明を `papers/reconstruction/etale_realization.tex` に収録した。対象がsmooth properであるという入力は不可欠であり、残余smoothnessそのものを示した定理ではない。

既存の局所rotation逆関手、SMからfull coherent比較と有限型spreadの証明と合わせ、所定の局所量子化がある成分のgeneric可換復元を残余対角perfect性(SM)へ還元する。節点・尖点の五次元例について、可換変形の35係数sliceも厳密に構成した。

**未完成：** 非楕円二成分のSM、全成分での局所量子化入力、全点の可換復元、元の底への一意な大域降下。新規性の包括的確認と外部査読・形式証明は未実施。

## 原稿と再現

| 論文 | 入口 |
|---|---|
| A：Poisson・量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族・ambient | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き復元 | `papers/rotation_cubic_reconstruction.tex` |
| Cの局所rotation・saturation・étale実現の独立組版 | `papers/reconstruction/rotation_saturation_reduction.tex` |

独立組版は第四の主論文ではない。既存三論文と境界研究の証明は保持している。最新のétale実現節は親Cと独立組版で同じソースを読む。

```sh
python3 -m pip install -r reconstruction/requirements.txt
python3 reconstruction/computations/verify_nonelliptic_inputs.py --output /tmp/nc-cubic-center.json
python3 reconstruction/computations/verify_etale_inputs.py --output /tmp/nc-cubic-tangent.json
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

Python 3.10以上、LuaLaTeX、LuaTeX-ja/ltjsarticleと標準数学パッケージが必要。詳細は `reconstruction/README.md`。計算は有理数上の厳密演算であり、圏同値の計算機形式化ではない。

親三論文全体は `python3 scripts/build.py`。今回の検証対象は独立組版と二つの計算証明書であり、親全体を再組版したとは扱わない。

## Hochschild障害の現在有効な公式（論文C）

`papers/reconstruction/hochschild_obstructions.tex` に、BFKの固定sector公式から導かれる三次障害群の全次元の整理を記す。`HH³(Ku(X))^rotation=0` は全 n≥3、無偏極の HH³ は cubic sevenfold でのみ二次元。非楕円cubic fivefoldではHH³=0。これは一次の形式的障害に関する情報であり、残余smoothness (SM) の証明ではない。原稿の再生は `reconstruction/README.md` を参照する。

## 現行のディレクトリとlatexmk

論文A・B・Cと境界研究は `papers/`、研究ノートは `notes/`、計算コードは `computations/` と `reconstruction/computations/` に整理している。正本はGitHub `main` のみ。

```sh
latexmk papers/poisson_cubic_quantization.tex
latexmk papers/generic17_ambient_recovery.tex
latexmk papers/rotation_cubic_reconstruction.tex
latexmk papers/reconstruction/rotation_saturation_reduction.tex
python3 reconstruction/scripts/verify.py
```

ルート `.latexmkrc` によりLuaLaTeXを用い、全生成PDFをGit対象外の `build/` に出力する。ソース未確認のPDF原本だけは `papers/pdf-only/` に保全する。詳しくは `papers/README.md` と `notes/README.md` を参照。

※ PDF原本のうち研究ノート二本は `notes/pdf-only/`、論文系八本は `papers/pdf-only/` に分類した。その他のPDFは生成対象でありGit追跡しない。
