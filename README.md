# nc-cubic：Poisson構造・代数的量子化・可換復元

**2026-11-10・v18。正本はこのGitHubリポジトリのmainのみ。** 最初に `00_research_plan.md`、次に `notes/research_notes.md` を読む。Library保存はpush実失敗時の緊急避難だけとする。

## 最終目標（三本柱）

| 目標 | 主張の内容 | 現状 |
|---|---|---|
| 1. Poisson構造の構造定理 | 滑らかなcubic n-fold (n≥3) の全Poisson構造の正規形・一般階数 | 論文Aの `thm:pg-normal` に証明あり |
| 2. 代数的量子化 | 各固定Poisson構造を、AS-regularな周囲と中心三次商で実現する一パラメータ代数的量子化 | 論文Aの `thm:pg-quantization` に証明あり |
| 3. 非可換cubicの可換復元 | 目標2で得た量子化のgenericファイバーを、rotation付き可換Kuznetsov成分として実現 | 最優先・SM未解決 |

個々のPoisson構造の量子化（目標2）と、Poissonスキーム全成分上の一様相対量子化は別の問題。後者は未解決であり、前者の定理の完成を否定しない。全AS-regular中心三次商の全点での可換復元は目標ではなく、反例がある。\(X^n\subset\mathbb P^{n+1}\) の周囲は \(\mathrm{nc}\mathbb P^{n+1}\)。数学的主張については原稿の証明の存在と外部・独立監査の完了を区別する。

## 現在の中心結果

実在するsmooth proper dg族と自己同値が、一点で滑らかなcubicのKuznetsov成分とrotationに一致すれば、étale局所的に可換cubic族として実現できる。同値双加群の小拡大障害をrotation不変HH²で消去する証明を `papers/reconstruction/etale_realization.tex` に収録した。対象がsmooth properであるという入力は不可欠であり、残余smoothnessそのものを示した定理ではない。

既存の局所rotation逆関手、SMからfull coherent比較と有限型spreadの証明と合わせ、所定の局所量子化がある成分のgeneric可換復元を残余対角perfect性(SM)へ還元する。節点・尖点の五次元例について、可換変形の35係数sliceも厳密に構成した。

**未完成：** 非楕円二成分のSM、全成分を同時に扱う相対量子化族の入力、全点の可換復元、元の底への一意な大域降下。新規性の包括的確認と外部査読・形式証明は未実施。

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

ルート `.latexmkrc` によりLuaLaTeXを用い、全生成PDFをGit対象外の `build/` に出力する。完全なTeXソースを確認できないPDF原本だけは、例外リストに従って `papers/pdf-only/` と `notes/pdf-only/` に暫定保存する。詳しくは `papers/README.md` と `notes/README.md` を参照。

※ PDF原本のうち研究ノート二本は `notes/pdf-only/`、論文系七本は `papers/pdf-only/` に分類した。その他のPDFは生成対象でありGit追跡しない。

## PDFの追跡とソース復旧（2026-11-10）

原則としてTeXと検証コードのみをGitで追跡し、PDFは`latexmk`で`build/`へ生成する。独立した二次ジェットの結果は `papers/independent/poisson_second_jet.tex` に再構成し、以前のPDFの追跡を解除した。現在のPDF原本の例外リストは `papers/pdf-only/README.md` と `notes/pdf-only/README.md` に記録する。対応ソースが未確認の資料を、数学的証明が失われる状態で機械的に削除しない。

## 未照合PDFと関連TeXの整理TODO

追跡中PDF8本と関連TeXの対応候補、全証明の照合・組版・追跡解除の条件は [`TODO_PDF_SOURCES.md`](TODO_PDF_SOURCES.md) に管理する。取り込み済みの別原稿は `sources/candidates/` に暫定配置し、現行の主論文は上書きしない。

原PDF全８本のページ数・対応ソース監査は [`SOURCE_RECOVERY_AUDIT_20261110.md`](SOURCE_RECOVERY_AUDIT_20261110.md)、部分証明の移植は `papers/source_recovery/` と `notes/source_recovery/` を参照する。

## Reye論文の分離

Reye 曲線・停留平面に関する原論文PDF（77頁）、部分復元TeX、計算コード、現行研究ノート・研究方針は独立リポジトリ [uedakazushi/reye](https://github.com/uedakazushi/reye) へ移行した。このリポジトリから Reye 専用資産は除外済み。関連する一般的なPoisson研究や文献引用はここに保持する。
