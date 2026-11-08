# nc-cubic

3次超曲面のPoisson構造と非可換量子化：正規形・退化スキーム・rotation付き残余圏

2026年11月8日・統合第4版 / nc-cubic-v4

## 再開の順序

最初に [00_research_plan.md](00_research_plan.md) を読む。次に [tex/cubic_poisson_rotation.tex](tex/cubic_poisson_rotation.tex) の序論、必要な証明（[tex/papers/](tex/papers/)）、[tex/research_notes.tex](tex/research_notes.tex) を確認する。現在のTeXと研究ノートを研究の正本とし、旧ZIP・会話履歴を再開の前提にしない。

## 構成

- `tex/`：論文・研究ノート・共通設定・文献表のTeXソース。
- `tex/papers/complete_intersections.tex`：Section 2で完全交叉のPoisson存在判定、トーリック・射影斉次多様体の存在、量子化関係式の明示性を論証。
- `tex/papers/poisson_geometry.tex`：Poisson分類、退化、量子化の全証明。
- `tex/papers/rotation_obstruction.tex`、`rotation_models.tex`、`relative_saturation.tex`：可換復元、反例、条件付き構成、相対smoothnessの還元。
- `pdf/`：論文・研究ノート・研究方針の組版済みPDF。
- `computations/`：厳密有限計算と証明書。
- `scripts/`：PDF再生成・bundle検証。

### 重要な状態の区別

**GitHubの `pdf/` 内のPDFは現段階では移動前の旧版です。** 最新のSection 2と相対saturation還元を含むTeX全文は `tex/` にあります。PDFの再組版は今回未実施です。最新の論文PDFとして旧版を引用しないでください。旧内容のSHA256SUMSは削除しました。再生成と検証を完了した後にチェックサムを再作成する設計です。

主張の状態として、AS-regularな中心三次商すべてにrotation付き可換モデルが存在するという一般命題は偽です（Calabi–YauなZhang twist反例）。可換点を含む特定のPoisson量子化族の相対saturation、全パラメータでの可換復元、二つ以上の無限位数Sklyaninブロックの全生成は未解決です。これらと形式・étale局所・明示的ブロックについての肯定的結果を区別します。

## ビルド

Python 3、LuaLaTeX、日本語LaTeX（`ltjsarticle`, LuaTeX-ja, HaranoAji）、pandocが必要です。スクリプトは作業ディレクトリを一時生成し、中間物をリポジトリへ置きません。

```sh
python3 scripts/build.py
python3 scripts/verify_bundle.py --write-hashes
python3 scripts/verify_bundle.py
```

`scripts/build.py --only cubic_poisson_rotation` で個別のTeXを組版できます。検証ではソースの参照閉包、引用・ラベルの一意性、厳密計算、ファイル棚卸とSHA256を確認します。PDFが未再生成の場合、検証が失敗・警告することは意図的です。

主要な成果の証明と文献情報は現行TeXに保持しており、外部文献PDFや旧版ZIPを内包しません。公刊・外部査読・Lean形式化は未実施です。

## 今回の研究進展（v4）

`tex/papers/explicit_hesse_center.tex` で滑らかなHesseブロック `f_t=(x³+y³+z³)/3+txyz`（`t³≠-1`）の三次中心元の閉公式と、零を含むパラメータ開集合の判別式を示した。古典的Smith–Tate / De Laet–Le BruynのSklyanin中心元公式のPoisson変形族への翻訳で、一般混合項の問題は未解決。Fermat型の公式を含み、複数の独立ブロックと中心線形シフトへ拡張できる。証明は原典の中心性＋次数別平坦性に依存する。追加した `computations/verify_hesse_center.py` は複数有限体特殊化の次数四交換子の所属検査であり、普遍的証明の代用ではない。

**出力状態**：v4のTeX原稿はmainに含まれるが、既存の `pdf/` は以前の内容のまま。PDF再組版と新しいSHA256SUMSは未完了で、古いPDFをv4と表示してはならない。

滑らかな任意の三変数三次式もHesse標準形へ線形変換できる（Artebani–Dolgachev, Lemma 1）。従って新しい `tex/papers/explicit_hesse_center.tex` の系では、`g(x)=λ f_t(Mx)` に対して `ħ'=λ det(M) ħ` として `Ω^g_h=λ Ω_{ħ',t}(Mx)` と明示する。一般の中心混合項には拡張していない。

Hesse量子化のpoint schemeの楕円曲線は `θ(h,t)=[t+(h²/3)(1+t³/4)]/(1-h²t²/4)` によるHesse式であり、`Y=V(f_θ+P(u))` が自然な可換cubic候補となる（`θ(0,t)=t`）。分離した中心三次式を伴う一ブロックでは、一般の `t` でも各複素ファイバーのrotation付き同値を証明した。Fermat型 `t=0` では既存の復元模型の係数を回復する。

## 一楕円ブロックの可換復元（v5）

新しい独立論文と証明は `tex/elliptic_cubic_reconstruction.tex` と `tex/papers/elliptic_reconstruction.tex`。研究ノートは `tex/reconstruction_notes.tex`、研究方針は `elliptic_reconstruction_plan.md`。一ブロックの各良い複素ファイバーでのrotation付き可換復元、二次変形、同じ模型を持つ非可換量子化曲線、相対中心商のTHCR表示を証明した。一般混合項・複数無限位数ブロック・相対残余同値は未解決。

再生成: `python3 scripts/build_reconstruction.py`。厳密計算: `python3 computations/verify_reconstruction.py`。今回のv5独立論文PDFはLibraryの `nc-cubic-elliptic-reconstruction_v5_20261109.zip` に収録。**GitHubの既存統合PDFは旧版のまま**で、v5の新しいPDFをGitHubにpushしたとは主張しない。
