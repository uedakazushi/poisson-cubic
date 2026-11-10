# nc-cubic：有限代数的な可換復元

**2026-11-11 / v34。GitHub mainが正本。** [研究方針](00_research_plan.md)から再開する。

## 現在の最短経路

非可換中心三次対から有限対角の低積と可換式を抽出する。実際の低rotation標的は、既存形式残余同値で可換Kuへ移し、幾何学的射影核で全Artin底変更を証明する。一般MF核比較KFは先行条件にしない。

generic段階の必要データを減らした。**可換smooth proper側からnc proper側への一つの右perfect核**が特殊点で同値なら、逆核と底上の同値が従う。その核が完備底の通常の導来圏でcompactに実現すれば、Popescu降下で指定有限jetを保つetale代数化が得られる。nc側のsmoothnessは仮定でなく結果。

**具体的な混合nc cubicについて、このcompact形式逆核はまだ構成していない。** 各Artin同値や固定rank MFだけでcompact性を推論しない。次は可換側の一生成子の逆像の、一様な有限cell/retract表示を作る。

## 原稿

| 内容 | 入口 |
|---|---|
| A：Poisson・量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き復元の現行統合稿 | `papers/rotation_cubic_reconstruction.tex` |
| 射影核とArtin底変更 | `papers/geometric_rotation_basechange.tex` |
| 片側核の特殊点判定と代数化 | `papers/one_sided_morita_algebraization.tex` |

新しい証明全文は `papers/reconstruction/one_sided_morita_algebraization.tex` をCと単独稿で共有する。[研究ノート](notes/one_sided_morita.md)に未解決条件と着手方法を記載。

既存入力(F),(D)下でlambda=1の計算済みGと形式WはGL5同型。新しい抽象判定を合わせても、generic同値の実現には具体的compact核が必要。旧証明、反例、非可換計算資産を保持している。

```sh
python3 computations/verify_one_sided_morita.py --output build/one_sided_morita_certificate.json
python3 scripts/verify_one_sided_morita_assets.py
latexmk papers/one_sided_morita_algebraization.tex
```

通常のねじった2×2行列代数で206個の恒等式、balanced relation階数、period補正mod h^8、compact性反例を検算。新単独稿5頁を組版・表示確認済み。nc核やカテゴリカル証明の形式検証ではない。A/B/C全体の現行組版、旧全計算の再実行は未実施。詳細は `validation.json`。

mainを正本にfast-forwardのみで保存し、PDFはbuild/へ生成してGit追跡しない。GitHub Actions/force pushは禁止。Libraryは実際のpush失敗時のみ緊急退避。独立境界/未照合PDFはnc-cubic2、Reyeはreyeに保全。
