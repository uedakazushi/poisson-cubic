# nc-cubic：Poisson構造・代数的量子化・可換復元

**2026-11-10・v21。正本はGitHub main。** 最初に [研究方針](00_research_plan.md)、次に [研究ノート](notes/research_notes.md) を読む。

## 三つの目標

| 目標 | 内容 | 状態 |
|---|---|---|
| Poisson構造 | 滑らかなcubic n-fold (n≥3) のJacobianブロック正規形・一般階数 | 論文Aに定理・証明あり |
| 代数的量子化 | 各固定Poisson構造をKoszul AS-regularな周囲と中心三次商で実現 | 論文Aに定理・証明あり |
| 可換復元 | 構成した量子化のgenericを、同じKuとrotationを持つ可換cubicとして実現 | 最優先・一般混合型は未完成 |

目標1・2の証明記載と全入力の独立監査完了は区別する。個別量子化と全Poisson係数空間上の一様相対量子化は別問題。任意のAS-regular中心三次商の全点に対するrotation付き復元には反例がある。

## 可換模型を具体的に求める

**方程式抽出と圏同値の存在を並行して進める。** 現在の具体的な基準は次の通り。

- **一ブロック分離型。** 対称Jacobian量子化の点曲線はMori–Smithの既知公式 \(f+h^2\det\operatorname{Hess}(f)/24\)。適切な滑らかな楕円中心商と独立な中心変数Pの仮定で、これにPを加えたcubicを既存のKu比較により可換模型として使える。Hesse形の閉式も保持している。
- **一般次元の候補抽出。** rotationの次数一・二の導来自然変換の積からKを求め、\(\partial_j(Aq)_i=\partial_i(Aq)_j\) を解く。可逆解と共通射影零点の不存在があれば \(F=\sum_i x_i(Aq)_i/3\)。これは存在するときの唯一の候補を与えるが、圏同値の存在までは保証しない。
- **三次元の一次制約。** 純Poisson方向はHH²(Ku)への制限で消える。KS類の純粋性と制限との両立を確認し、可換模型族が存在すれば \(F_h=F+O(h^2)\)。分離Fermat例では二次項は \(+h^2xyz/3\) で、中心元の表示を可換にした \(-2h^2xyz/3\) と異なる。

証明の所在：

| 内容 | 原稿 |
|---|---|
| 低次数積と可積分性、射影的一意性、積分不可能な完全交差 | [explicit_jacobian_recovery.tex](papers/reconstruction/explicit_jacobian_recovery.tex) |
| Todd補正を含む純Poisson方向の一次消滅 | [poisson_first_order.tex](papers/reconstruction/poisson_first_order.tex) |
| Hessian式、分離型模型、中心可換化との二次比較 | [explicit_model_comparison.tex](papers/reconstruction/explicit_model_comparison.tex) |
| 最小混合試験族の三次中心元・全Artin切断PBW | [mixed_test_family.tex](papers/reconstruction/mixed_test_family.tex) |
| 局所rotation・SM・ER | [rotation_saturation_reduction.tex](papers/reconstruction/rotation_saturation_reduction.tex) |

次の主対象は三次元の最小混合族
\(F_\lambda=(x^3+y^3+z^3)/3+u^3+v^3+\lambda uxy\)。
三次中心元の閉公式と全Artin切断のPBW性は証明した。古典cubicはλ³≠−3で滑らかである。対角対称性に両立するmarked復元が存在すれば、二次類はc(λ)[xyz]に絞られる。残余の低次数積とこの係数c(λ)は未計算であり、ここを次に求める。Hessian由来の未検証案は研究ノートに置く。
SM・有限bar対角による存在経路、非楕円fivefoldへの拡張も維持する。

## 原稿・再現

| 論文 | 入口 |
|---|---|
| A：Poisson・量子化 | papers/poisson_cubic_quantization.tex |
| B：17次元族・ambient復元 | papers/generic17_ambient_recovery.tex |
| C：rotation付き可換復元 | papers/rotation_cubic_reconstruction.tex |

Python 3.10以上、SymPy、LuaLaTeX、LuaTeX-ja/ltjsarticleと標準数学パッケージを用いる。
リポジトリルートから次を実行する。

    python3 computations/verify_explicit_jacobian_recovery.py
    python3 computations/verify_explicit_model_comparison.py
    python3 computations/verify_mixed_test_family.py
    python3 scripts/verify_bundle.py
    python3 scripts/build.py --only rotation_cubic_reconstruction
    python3 reconstruction/scripts/build.py
    python3 reconstruction/scripts/verify.py

詳細は [reconstruction/README.md](reconstruction/README.md)。
ルート.latexmkrcでLuaLaTeXを使い、PDFとbuild receiptはGit対象外のbuild/へ生成する。
主論文のbuild receiptは全TeX inputのハッシュを含む。
検算・組版・圏論的証明・遠隔反映は別の状態である。

## 保持する存在結果と未解決点

実在するsmooth proper dg族とrotationが一点で可換cubicのKuと一致すれば、
étale局所的な可換実現を与えるERの証明がある。
これを使う経路では残余対角perfect性SMが必要であり、一般混合型で未証明。
線束生成子によるSMの判定、有限bar右逆判定、A∞arity制約を現行本文に保持する。
一般nc入力の低次数rotation積、一般混合型での同値双加群、
全成分の一様相対量子化、全点復元・一意な大域降下も未完成。

## 資料の配置と保存

mainだけを正本とし、LibraryはGitHub反映が実際に失敗した場合の緊急退避に限る。
GitHub Actions、force pushは使わない。PDFはGit追跡しない。

独立Pfaffian・Brill–Noether・中心判別式研究と未照合原PDF8件は
[nc-cubic2](https://github.com/uedakazushi/nc-cubic2) に保全され、
Reye研究は [reye](https://github.com/uedakazushi/reye) に分離されている。
PDF移転とTeX完全照合の完了は同じではない。
関連資料の参照先は [TODO_PDF_SOURCES.md](TODO_PDF_SOURCES.md)、
[SOURCE_RECOVERY_AUDIT_20261110.md](SOURCE_RECOVERY_AUDIT_20261110.md)。
