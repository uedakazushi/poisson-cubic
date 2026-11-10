# nc-cubic：Poisson構造・量子化・可換復元

**2026-11-11 / v29。正本はGitHub main。** 最初に [研究方針](00_research_plan.md)、次に [乗法比較ノート](notes/bar_comparison.md) と [有限対角ノート](notes/curved_diagonal.md) を読む。

## 現在の到達点

**v29：相対Artin sector。** 可換形式五変数cubicの勾配Koszul複体を全Artin切断で調べ、Jacobian環の次数別自由性とrank(次数1,2)=5,10を証明した。非恒等μ3-sectorのH⁰寄与は零。相対stabilized diagonalのkernel作用が同一enhancementで体上BFK比較へ特殊化する条件(KF)を確認すれば、nilpotent検出から既存の(BC)が従う。**(KF)は未証明で、categorical Natやgeneric圏同値の完成を意味しない。** 証明：`papers/reconstruction/relative_artin_sector.tex`、ノート：`notes/relative_artin_sector.md`、検算：`computations/verify_artin_sectors.py`。



一般次元のPoisson正規形と固定方向の代数的量子化は論文A、17次元族とambient復元はB、rotation付き可換復元はC。一般混合族のgeneric圏同値は未完成。

最優先経路は、代数的非可換中心対から実際の低rotation積を有限代数的に計算し、その核を積分して可換方程式を直接得ること。選んだformality級数の収束を先行条件にしない。

### 有限対角からcup積への比較

有界な同次射影対角とbarの分裂比較を入力に、曲率付き有限対角のYoneda積と有限支持Hochschild cup積を同定した。逆向きの写像Jについて、乗法性の差を

`J(phi)J(psi)-J(phi cup psi)=-d(Pi R_phi H R_psi I)`

と明示する。有限支持brace挿入は、graded MFの内部shift付き導来自然変換への乗法的characteristic写像Thetaを与える。**この写像の同型性は未証明。** 全Artin底で標的H^0が自由rank5,10で自然な剰余写像を持つ条件(BC)に還元した。体上の公式から(BC)を推論しない。

### 正則な有限対角と候補式

lambda=1の実際の非可換混合入力から、Q[h]_(h)上の対角・高次ホモトピー・四つの閉行列を構成し、全16合成を計算した。H^0はrank4,6。四境界と六つの積の小行列式はh=0で-3なので、積と全Artin底変更が両立する。五変数候補は

\[
\begin{aligned}
G_h+v^3={}&(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy\\
&-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^{12}/4374)u^3.
\end{aligned}
\]

保存行列の係数分母lcmは(h^3-1)(h^6+162)であり、圏のsmoothness判別式ではない。

この候補はq=h^6のetale近傍で四本の代数方程式により正規化できる。正規形の係数は
`L(q)=1+127q/5184+O(q^2)`、`C(q)=13/36+1613q/1679616+O(q^2)`。
**これは候補Gの係数であり、(BC)未確認のまま形式的圏論模型Wの係数とは言わない。**

## 原稿と再現

| 内容 | 入口 |
|---|---|
| A：Poisson・量子化 | `papers/poisson_cubic_quantization.tex` |
| B：17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き可換復元 | `papers/rotation_cubic_reconstruction.tex` |
| 曲率付き対角・局所正則化 | `papers/curved_diagonal_recovery.tex` |
| 乗法的bar比較・候補の代数的正規形 | `papers/multiplicative_bar_comparison.tex` |

新しい本文は `papers/reconstruction/multiplicative_bar_comparison.tex`。証明はCと単独稿で同じソースをinputする。Python 3、SymPy、LuaLaTeX、LuaTeX-ja、latexmkを使用する。

```sh
python3 computations/verify_bar_comparison.py --output build/bar_comparison_certificate.json
python3 scripts/verify_bar_assets.py
latexmk papers/multiplicative_bar_comparison.tex
```

新検算は有限テスト代数で曲率144件・cap微分288件・cap積360件、乗法性ホモトピー30件、候補の直接代入・Jacobian9・係数を厳密確認する。無限barの一般証明や実際のcategorical Natの検算ではない。

既存正則対角の再生成は `verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json`、監査は `scripts/verify_regular_assets.py`。全体監査は `scripts/verify_bundle.py`、全体組版は `scripts/build.py`。容易に再生成できる全行列の重複保存をせずcanonical JSON SHA256で照合する。

今回の単独稿は8ページで組版・全ページ表示を確認。新計算と既存finite_recovery検算を実行した。v27全行列、A/B/C全体の現行組版、全既存計算の再実行は行っていない。詳細は `validation.json`。外部査読・形式検証とは区別する。

## 保存

mainを正本とし、通常のfast-forwardで反映。PDFは追跡せずbuild/へ生成。GitHub Actionsとforce pushは禁止。LibraryはGitHub反映が実際に失敗した場合の緊急退避のみ。

独立Pfaffian・Brill--Noether・中心判別式と未照合原PDF8本はnc-cubic2、Reyeはreyeに保全。移転とTeX完全照合は別状態であり、`TODO_PDF_SOURCES.md` と `SOURCE_RECOVERY_AUDIT_20261110.md` を参照。
