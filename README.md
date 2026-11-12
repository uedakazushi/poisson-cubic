# nc-cubic — Poisson cubicの量子化と一般点可換復元

**2026-11-12 / v59。** GitHub mainが正本。最初に [研究方針](00_research_plan.md) を読む。

| 原稿 | 主題 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | smooth cubicのPoisson正規形・退化・Bondal・代数的量子化・Poisson moduli |
| [論文B](papers/paper_b.tex)（B-v43） | 代数的中心三次変形の一般点可換復元、完備曲率移送、基礎体上の模型 |

## Bの現在の結論

次数別有限自由な代数的中心三次対で、特殊ファイバーが多項式環とsmooth cubicであることを仮定する。[三対象window](papers/support/papers/reconstruction/three_object_window.tex)が(L)を、[完備曲率移送](papers/support/papers/reconstruction/complete_curved_transport.tex)が(CF)と(CF_3)を構成するため、これらを追加仮定とせず一般点復元を得る。

元の体K=C(h)上のsmooth cubic模型と有限拡大後のrotation付き全coherent残余圏同値を構成する。全n>=3の幾何学的一意性とBFKの既知の生成上界を保持し、正則多変数局所基底にも適用する。任意の抽象的nc cubicの表示、同値核のKへの降下、特殊点込み相対同値、全モジュライへの接着は主張しない。

[主定理](papers/support/papers/reconstruction/general_dimension_recovery.tex)、[監査ノート](notes/paper_b_proof_audit.md)、[検証状態](validation_paper_b.json)を参照。構成した証明、全支持節の独立監査、外部査読・新規性調査、計算機形式検証を区別する。

## 再現

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 computations/verify_complete_curved_transport.py --output build/complete_curved_transport_checks.json
latexmk papers/support/papers/complete_curved_transport.tex
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
```

新計算はSchouten恒等式と有限の非自律bar flow・逆・余積・arityの厳密検査であり、非可換MF HomやKontsevich重みの計算ではない。5頁の新抜粋を組版・表示確認したが、B全文と全既存証明書の再実行は未実施。Python 3/SymPy、LuaLaTeX/LuaTeX-ja/latexmkを使う。

Aの独立監査は [投稿監査](notes/poisson_article_submission_audit.md) に従う。17次元モジュライ・ambient周期性・独立境界は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) が正本。既存の有効な証明・反例・計算を削除しない。

PDF・中間物はbuild/で非追跡。mainへfast-forward保存と遠隔確認。GitHub Actions・force pushなし。LibraryはGitHub保存実失敗時のみ緊急退避。
