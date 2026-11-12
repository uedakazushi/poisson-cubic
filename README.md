# nc-cubic — Poisson cubic の量子化とrotation付き可換復元

**2026-11-12 / v57。** GitHub mainが正本。研究再開は [00_research_plan.md](00_research_plan.md) から。

| 原稿 | 主題 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | smooth cubicのPoisson正規形・退化・Bondal予想・代数的量子化・Poisson moduli |
| [論文B](papers/paper_b.tex)（B-v41） | 一般次元の中心三次非可換超曲面のrotation付き全coherent可換復元、基礎体上の模型 |

## 論文Bの現在の結論

代数的・次数別flatな中心三次変形と、局所window/proper比較(L)、実際の完備graded MF同値(CF)の下で、元の体K=C(h)上にsmooth cubic模型を取り、有限拡大後に全coherent残余pairとのrotation付き同値を得る。一般点AS正則性はflat入力から導く。模型は全n>=3で幾何学的に一意。BFKの既知結果により、任意の非零対象とその二つのrotationの直和の生成時間は幾何学的一般点で2(n+2)(n+3)-1以下となる。

主経路は固定三対象比較→Euler非零性→既知の軌道生成→有限降下→coherent飽和→低Nat底変更→基礎体上の勾配積分。全MF同値の代わりに固定三対象のenhanced比較でも十分。一般の対角比較(D)は明示式を指定する追加入力であり、一般存在に使わない。同じ(L),(CF)を課した多変数正則局所基底にも分数体上の結論を拡張する。

**未完了**：(L),(CF)の全依存・enhancement・inverse coherenceの独立監査。全nc cubicの無条件復元、同値核の基礎体への降下、特殊点を含む相対同値、全モジュライ上の接着は主張しない。

証明は [一般次元主定理](papers/support/papers/reconstruction/general_dimension_recovery.tex) と [基礎体降下の節](papers/support/papers/reconstruction/generic_cubic_descent.tex)。監査・最短経路・反例・次の具体作業は [notes/paper_b_proof_audit.md](notes/paper_b_proof_audit.md)。B-v41の実施状態は [validation_paper_b.json](validation_paper_b.json)。

## 論文Aと関連研究

論文Aの全Poisson量子化では形式中心元存在に依存しないCramer法を用いる。正規形Lie補題、普遍Hesse中心、PBW/AS条件、退化・成分数の全独立監査と新規性調査は未完。[投稿監査](notes/poisson_article_submission_audit.md)と[中心元ノート](notes/universal_casimir.md)を参照する。

17次元モジュライ、ambient周期性、6/7次元の詳細scheme幾何、独立境界研究は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) が正本。一般次元quadratic-envelope復元はAに保持する。数学的に未照合の候補は `sources/candidates/`、外部に保全したPDFの未照合内容は `notes/source_recovery/`。既存の有効な支持節・反例・計算証明書は保持する。

## 再現

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 computations/verify_generic_cubic_descent.py --output build/generic_cubic_descent_checks.json
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
```

LuaLaTeX、LuaTeX-ja、latexmk、計算にはPython 3とSymPyが必要。PDF・中間物は `build/` に生成しGit追跡しない。新しい計算は既知の可換入力に対するQ(t)上の有限検算であり、非可換低Natの計算ではない。全文組版と証明監査は静的検査とは別。Aなどの既存検証記録は `validation.json` に残し、Bの最新状態と混同しない。

GitHub mainへfast-forwardで保存し、GitHub Actions・force pushを使わない。LibraryはGitHub保存に実際に失敗した場合のみ緊急退避する。
