# nc-cubic：有限代数的な可換復元

**2026-11-11 / v33。正本はGitHub main。** [研究方針](00_research_plan.md)から再開する。

## 現在の最短経路

代数的nc中心三次対から有限対角の低積を計算し、その核を積分する方針を維持する。
標的の導来Natは、既存の全Artin残余同値を利用して可換Kuへ移し、**幾何学的射影核で計算する**。
一般の相対MF核全忠実性(KF)を先に証明する必要はない。

新しい定理は、任意のArtin局所C代数上の滑らかなN>=5変数cubicについて、
真の低Natが自由rankN,binom(N,2)で、自然な底変更と積に両立すること。
座標切断とその合成が特殊基底を閉元として持ち上げるため、独立中心変数・有限群対称性は不要。

既存の(F)形式MF/Artin残余同値、(D)正則対角/乗法的characteristic写像を入力すると、
ncの(BC)が従い、lambda=1で計算したG_h+v^3と形式復元式W_hは形式GL5同型になる。
**genericな代数的圏同値は未証明。** 次は指定生成子について、逆双加群とrotation比較を含む有限Morita証明書を構成する。

## 原稿・再現

| 内容 | 入口 |
|---|---|
| A：一般Poisson正規形・固定方向の量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き復元の現行統合稿 | `papers/rotation_cubic_reconstruction.tex` |
| 新しい射影核・Artin底変更の単独稿 | `papers/geometric_rotation_basechange.tex` |

本文の証明は `papers/reconstruction/geometric_rotation_basechange.tex` をCと単独稿で共有する。
[研究ノート](notes/geometric_rotation_basechange.md)に依存と未解決箇所を整理した。
既存の有限対角・bar比較・sector・unit・反例・SM/ERの証明とコードを保持している。

```sh
python3 computations/verify_geometric_rotation.py --output build/geometric_rotation_certificate.json
python3 scripts/verify_geometric_rotation_assets.py
latexmk papers/geometric_rotation_basechange.tex
```

新コードはsector算術56例、有限自由複体のArtin検算15例と閉基底が持ち上がらない反例を検査する。
幾何学的Morita定理や既存の非可換全行列を計算機で検証したものではない。
新単独稿は組版・表示確認済み。A/B/C現行版全体の再組版と全既存計算の再実行は未実施。
詳細は `validation.json`。

## 運用

mainのみを正本とし、旧ZIP・会話を再開条件にしない。PDFはGit追跡せずbuild/へ生成する。
通常のfast-forwardのみ、GitHub Actionsとforce pushは禁止。Libraryは実際のpush失敗時のみ緊急退避。
独立境界研究/未照合原PDFはnc-cubic2、Reyeはreyeに保全されている。本文の有効な数学を削除しない。
