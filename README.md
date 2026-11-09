# nc-cubic：一般次元・各Poisson成分への可換復元

2026年11月9日・v11。最初に `00_research_plan.md`、次に `research_notes.md` を読む。

## 現行の構成

親リポジトリの三論文A（Poisson・量子化）、B（17次元族と偏極付きambient）、C（rotation付き可換復元）と独立の境界研究という構成を保つ。今回の改訂は論文Cの `tex/papers/all_poisson_components.tex` を現在の論理順に書き直したもの。

| 主論文 | 現行入口 |
|---|---|
| A：Poissonと量子化 | `tex/poisson_cubic_quantization.tex` |
| B：17次元族とambient | `tex/generic17_ambient_recovery.tex` |
| C：rotation付き復元 | `tex/rotation_cubic_reconstruction.tex` |

この部分研究bundleには三論文全文は重複収録しない。親リポジトリの証明は変更・削除しない。

- 任意のPoisson錐の非零被約既約成分を、滑らかなスカラーchartで双有理に支配する。
- 必要なら有限étale被覆上でgenericなブロック座標を固定する。
- 形式中心元は有限行列の核を用い、任意の有限jetを保って代数化できる。全次数PBW性は別の入力。
- 残余pairの相対saturationと原稿Cの局所実現原理 (ER) を仮定すると、一つの可換点から成分のgenericへ到達する。
- 錐の特異な頂点上への量子化の降下は、genericな模型の存在より強い別問題である。

相対saturation自体、一般の可換復元の存在、全ファイバーでの同値、モデルの一意な大域降下は未完成。新規性は未確定。

## 独立読解用の論文C抜粋

`tex/exports/componentwise_reconstruction.tex` は同じ現行節を直接inputする独立組版の入口で、新しい第四の主論文ではない。
PDFは `pdf/sections/componentwise_reconstruction.pdf`。この部分研究bundleは一般成分の還元を自己完結して再開する一式であり、親プロジェクト全体を置換しない。

## 再現

Python 3、SymPy、pypdf、LuaLaTeX（LuaTeX-ja、ltjsarticle、標準数学パッケージ）、Pandocを用いる。

```sh
python3 computations/verify_componentwise_reconstruction.py
python3 scripts/build_components.py
python3 scripts/verify_components.py
```

有限特殊化を使わず、記号多項式と自由代数恒等式を検証する。ただし圏論的同値や一般saturationの計算機形式化ではない。生成・組版・ハッシュ照合・Library保存・GitHub反映は別の状態として `validation_components.json` と最終応答で報告する。

既存のA・B・C全体のPDFを今回再生成したとは扱わない。親リポジトリの古いPDFをv11の組版結果と表示しない。GitHubへPDFバイナリが同期されていない場合は、Libraryの現行部分bundleのPDFを参照する。

## 非楕円型Poisson既約成分

論文Aの `tex/papers/nonelliptic_poisson_components.tex` に、滑らかなcubic fivefoldで節点・尖点型ブロックが一般点に残る二つのPoisson既約成分を追加。厳密証明書と再現コードは `computations/nonelliptic_components_certificate.json` と `computations/verify_nonelliptic_components.py`。この結果は一般の可換復元を否定せず、相対saturationの対象に非楕円型を含める必要性を示す。論文Aの統合PDFは未再組版。
