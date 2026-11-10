# nc-cubic：Poisson構造・量子化・可換復元

**2026-11-11 / v27。正本はGitHub main。** 最初に [研究方針](00_research_plan.md)、次に [曲率付き対角の研究ノート](notes/curved_diagonal.md) を読む。

## 現在の到達点

一般次元のPoisson正規形と固定Poisson構造の代数的量子化は論文A、17次元族とambient復元は論文B、rotation付き可換復元は論文Cで扱う。一般混合族のgeneric圏同値は未完成。

最優先の経路は、代数的非可換中心対から実際の低rotation積を有限代数的に計算し、その核を積分して可換方程式を直接得ること。選択したformality級数の収束を先行条件としない。

### 正則な有限対角の積

λ=1の混合入力について、曲率付き絶対対角の分解・高次ホモトピー・四つの閉行列をQ[h]_(h)上で正則に構成し、全16個の順序付き合成を厳密計算した。H⁰のrankは4,6。四境界と六つの実際の積の小行列式はh=0で−3なので、低次数コホモロジーと積は全Artin切断・完備化と両立する。

積の核を積分した五変数候補は

\[
\begin{aligned}
G_h+v^3={}&(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy\\
&-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^{12}/4374)u^3.
\end{aligned}
\]

正則化前後で候補は同じである。保存した有限行列の係数の分母lcmは(h³−1)(h⁶+162)。これは圏のsmoothness判別式ではない。

**未証明：** この有限対角積と実際の残余圏の導来自然変換のrotation積との比較、指定形式Wとの全次数比較、generic rotation付き圏同値。有限arity共役によるdg Lie比較だけではcup積保存を結論しない。

## 原稿と再現

| 内容 | 入口 |
|---|---|
| A：Poisson・量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き可換復元 | `papers/rotation_cubic_reconstruction.tex` |
| 曲率付き対角・局所正則化の単独稿 | `papers/curved_diagonal_recovery.tex` |

証明全文は `papers/reconstruction/curved_diagonal_recovery.tex` と `regular_diagonal_recovery.tex`。有限代数的積分の証明・実装も現行稿に保持する。

Python 3、SymPy、LuaLaTeX、LuaTeX-ja、latexmkを使用する。

```sh
python3 computations/verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json
python3 scripts/verify_regular_assets.py
latexmk papers/curved_diagonal_recovery.tex
```

小証明書は積表・rank・小行列・分母・全行列のcanonical JSON SHA256を持つ。全行列は上記コマンドで再生成できる。既存全体監査は `scripts/verify_bundle.py`、全体組版は `scripts/build.py`。

**今回の検証：** 正則な行列と全積の厳密検算、finite_recoveryの既存証明書との一致、単独稿10頁の組版と全頁表示確認を実施。A/B/C全体の現行再組版と全既存計算の再実行は未実施。詳細は `validation.json`。数学的証明の形式検証や外部査読ではない。

## 保存

mainを正本とし、通常のfast-forwardで反映する。PDFは追跡せずbuild/へ生成。GitHub Actionsとforce pushは使わない。LibraryはGitHub反映が実際に失敗した場合の緊急退避に限る。

独立Pfaffian・Brill–Noether・中心判別式と未照合原PDF8本はnc-cubic2、Reye研究はreyeに保全されている。移転とTeX完全照合は別状態であり、`TODO_PDF_SOURCES.md` と `SOURCE_RECOVERY_AUDIT_20261110.md` を参照。
