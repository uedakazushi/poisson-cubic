# nc-cubic — Poisson cubicの量子化とrotation付き可換復元

**2026-11-12 / v58。** GitHub mainが正本。再開は [研究方針](00_research_plan.md) から。

| 原稿 | 主題 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | smooth cubicのPoisson正規形・退化・Bondal・代数的量子化・Poisson moduli |
| [論文B](papers/paper_b.tex)（B-v42） | 三対象window、一般点のrotation付き全coherent可換復元、基礎体上の模型 |

## 論文Bの現在の結論

代数的・次数別有限自由な中心三次対と滑らかな可換特殊ファイバーから、**局所proper/window比較(L)を構成した**。[三対象windowの証明](papers/support/papers/reconstruction/three_object_window.tex)は、完備Homの縮約、正則局所基底への降下、実際のdg section--window、有限長filtration、rotation・周期比較を扱う。生成性を特殊点だけから持ち上げる議論ではない。

主定理の残る条件は **(CF_3)**：固定三対象の実際の形式的A∞比較。全MF比較(CF)は十分条件である。この条件下で、元の体K=C(h)上のsmooth cubic模型、有限拡大上の全coherent残余pair同値、全n>=3の幾何学的一意性、BFKの生成段数上界を得る。方程式と同値核の定義体を区別する。(CF_3)の曲率付き関手・逆・周期図式の全独立監査は未完了で、全nc cubicの無条件復元は主張しない。

[主定理](papers/support/papers/reconstruction/general_dimension_recovery.tex)、[基礎体降下](papers/support/papers/reconstruction/generic_cubic_descent.tex)、[証明監査・次の作業](notes/paper_b_proof_audit.md)、[実際の検証状態](validation_paper_b.json)を参照。正則多変数基底の(L)にも同じ証明が通るが、形式比較と全モジュライへの接着は別課題。

## 関連研究と保存

AのCramer量子化、Lie正規形、PBW/AS、Bondal・stack成分数は [投稿監査](notes/poisson_article_submission_audit.md) に従って独立監査を継続する。17次元モジュライ、ambient周期性、6/7次元のscheme詳細は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) が正本。一般次元quadratic-envelope復元はAに残す。既存の有効な支持節・反例・計算証明書は保持する。

## 再現

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 computations/verify_three_object_window.py --output build/three_object_window_checks.json
latexmk papers/support/papers/three_object_window.tex
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
```

新しい計算はQ(h,u)上の有限複体の符号・分母とwindow添字の検算であり、非可換HomやCF_3の計算ではない。新しい5頁の抜粋と、B全文の組版・全証明の独立監査を区別する。Python 3とSymPy、LuaLaTeX・LuaTeX-ja・latexmkを用いる。

PDF・中間物はbuild/へ生成しGit追跡しない。GitHub Actions・force pushなし。区切りでmainへ通常のfast-forward保存と遠隔確認を行い、Libraryは実際のGitHub保存失敗時のみ緊急退避する。
