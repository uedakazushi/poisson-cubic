# nc-cubic — Poisson cubicの量子化と一般点可換復元

**2026-11-12 / v67。** GitHub mainが正本。最初に [研究方針](00_research_plan.md) を読む。

| 原稿 | 主題 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | smooth cubicのPoisson正規形・退化・Bondal・代数的量子化・Poisson moduli |
| [論文B](papers/paper_b.tex)（B-v50） | 代数的中心三次変形の一般点可換復元、完備曲率移送、基礎体上の模型 |

## 論文Bの五部構成

- **I：一般点復元の構成** — 局所window、完備MF比較、一般点生成、coherent飽和
- **II：可換点と有限復元** — 一次・二次変形、Plücker障害、圏論的接空間、低rotation積
- **III：相対復元と適用条件** — Artin形式復元、étale局所実現、相対smoothness、障害例
- **IV：明示的な可換模型** — 楕円ブロック、混合量子化、中心式、有限curved gauge、二次jet
- **V：point schemeの比較** — 台、非被約構造、混合係数の平坦極限と判別式境界

各部で一般点主定理と個別の追加仮定を区別する。既存の定理・証明・反例・計算は保持する。

## Bの現在の結論

次数別有限自由な代数的中心三次対で、特殊ファイバーが多項式環とsmooth cubicであることを仮定する。[三対象window](papers/support/papers/reconstruction/three_object_window.tex)が(L)を、[完備曲率移送](papers/support/papers/reconstruction/complete_curved_transport.tex)が(CF)と(CF_3)を構成するため、これらを追加仮定とせず一般点復元を得る。

元の体K=C(h)上のsmooth cubic模型と有限拡大後のrotation付き全coherent残余圏同値を構成する。全n>=3の幾何学的一意性とBFKの既知の生成上界を保持し、正則多変数局所基底にも適用する。任意の抽象的nc cubicの表示、同値核のKへの降下、特殊点込み相対同値、全モジュライへの接着は主張しない。

[主定理](papers/support/papers/reconstruction/general_dimension_recovery.tex)、[監査ノート](notes/paper_b_proof_audit.md)、[検証状態](validation_paper_b.json)を参照。構成した証明、全支持節の独立監査、外部査読・新規性調査、計算機形式検証を区別する。

## 一次方向と可換moduli

[双対数上の一次消滅](papers/support/papers/reconstruction/first_order_poisson_kernel.tex) は全次数formalityに依存せず、中心三次対の非可換積の一次項がMF変形として消えることを直接証明する。残る可換三次式の一次係数はJacobian環の次数3に値を持つ。次元はcubic threefoldで10、cubic fourfoldで20。五変数では二次Hochschild障害の係数イデアルが五本のPlücker二次式に一致する（[証明](papers/support/papers/reconstruction/first_order_poisson_kernel.tex)）。JLLZのinfinitesimal categorical Torelliと組み合わせると、可換点の接空間20から$HH^2(\mathrm{Ku}(X))$（次元10）への写像は全射で、核はPoisson一次方向10次元と一致する。局所次元17と一次接空間20を区別する。ただしnc-cubic2の一般17次元族からのcategorical忘却核を7次元と同定したわけではない。

## 再現

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 computations/verify_complete_curved_transport.py --output build/complete_curved_transport_checks.json
python3 computations/verify_first_order_curved_kernel.py
python3 computations/verify_second_order_plucker.py
latexmk papers/support/papers/complete_curved_transport.tex
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
```

新計算はSchouten恒等式と有限の非自律bar flow・逆・余積・arityの厳密検査であり、非可換MF HomやKontsevich重みの計算ではない。5頁の新抜粋を組版・表示確認したが、B全文と全既存証明書の再実行は未実施。Python 3/SymPy、LuaLaTeX/LuaTeX-ja/latexmkを使う。

Aの独立監査は [投稿監査](notes/poisson_article_submission_audit.md) に従う。17次元モジュライ・ambient周期性・独立境界は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) が正本。既存の有効な証明・反例・計算を削除しない。

PDF・中間物はbuild/で非追跡。mainへfast-forward保存と遠隔確認。GitHub Actions・force pushなし。LibraryはGitHub保存実失敗時のみ緊急退避。
