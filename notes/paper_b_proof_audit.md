# 論文B：一般点復元の証明方針と監査

**2026-11-12 / B-v41。** 再開時は `00_research_plan.md` を最初に読む。本ノートは現在の論理構造と有効な障害を整理する。主定理は `papers/support/papers/reconstruction/general_dimension_recovery.tex`、強化の証明は `generic_cubic_descent.tex`（同じディレクトリ）。

## 現行の結論

代数的・次数別有限自由な中心三次対、滑らかな可換特殊ファイバー、実際の局所proper/window比較(L)および完備graded MF比較(CF)を入力する。一般点のambient AS正則性はこの次数別flat入力の帰結である。元の体 K=C(h) 上の滑らかな三次模型 G/K と、有限拡大 K'/K 上の rotation・指定三次周期性付き全coherent残余圏同値を得る。方程式と同値核の定義体を混同しない。

模型はすべての n>=3 で幾何学的に一意。代数閉体上の残余圏では任意の非零 M について M⊕ρM⊕ρ²M の生成時間は 2(n+2)(n+3)-1 以下。これはBFKの既知結果を移す帰結であり、新しい一般生成定理ではない。同じ(L),(CF)を確認した多変数正則局所基底の分数体にも同じ議論が適用される。全モジュライにわたる同時構成・接着は別である。

## 最短の証明経路

1. **代数入力**：次数別Nakayamaでaugmentationと対角のKoszul分解を持ち上げる。一般点AS正則性、中心元の正則性、商の次数別flatnessを導く。`gcd:prop:automatic-as`。この部分の次数・有限性・左右条件を今回点検した。
2. **固定三対象の比較**：stabilizationの三つのshiftのendomorphism代数を完備底上で比較してから局所化する。任意のLaurent対象に無限Taylor和を評価しない。主定理に必要なのは固定三対象のenhanced比較であり、`gcd:prop:three-object` が全MF同値の代替条件を示す。
3. **非零性と生成**：proper HomのEulerベクトルの二乗ノルム 2·3^(N-1) で一般点の像を非零とし、代数閉包上でBFK Theorem 5.15を適用する。Stevenson分類・regradingを経る既存別証明は保持するが、主経路では不要。
4. **有限降下と飽和**：同値核とrotation比較を有限型部分代数へ降ろし、非空開の閉点から有限体拡大を得る。smoothnessの有限体拡大からの降下と、線束Homの有限性・全twistの検出により全coherent残余圏へ拡張する。
5. **方程式だけを元の体へ戻す**：ここで初めて一般点のsmooth proper性を使う。低rotationの導来自然変換と積は有限で、任意の体拡大に可換。二次核Qと可積分行列の線形空間L_QがK上に定義される。幾何学的模型があるためdetが恒等零でなく、無限体Kの点で可逆な行列Aを選べる。G=(1/3)Σx_i(Aq)_i。これは `gcd:thm:field-model` の証明。

**順序が重要**：低積を先に明示計算することや、完備底全体のcompact逆核を先に作ることを、一般点の存在証明の前提にしない。存在→smoothness→低積の底変更→基礎体上の積分、と進む。一般の対角比較(D)は具体的な既知多項式を復元先として指定するために用い、存在の仮定に戻さない。

## 精査した部分とまだ保証していない部分

今回実際に読んだ主依存は、一般次元主定理、local_projective_modelのnoetherian/Koszul/Gorenstein部分、形式的MF復元、curved gaugeのarity・有限flow・twisting、Artin residual/MF比較のstabilization部分、rotation軌道・Euler・有限降下、coherent飽和、低Jacobian復元と局所有限代数化である。

数学的に直接点検した核は、次数別Koszul持上げ、古典symmetrizerによる幾何学的一意性、smooth proper性を入力した低Natの体拡大、可積分線形空間からのK上の模型抽出、生成段数の翻訳、および多変数Koszul消去である。

(CF)では、π=[Ξ,W]、[Ξ,π]=0、F_(2r+1)∈h^r、固定次数内の完備収束、局所化の順序を点検した。しかし全Hochschild formalityから得る実際のunital curved関手、逆関手・periodicity coherenceの全外部入力、(L)の相対dg windowとすべての底変更比較を完全に独立監査したという意味ではない。全38支持入力の全補題を逐一検証したわけでもない。したがって一般の抽象的nc cubicを無条件に可換復元できるとは結論しない。

## 一次文献との関係

- Ballard–Favero–Katzarkov, *Orlov spectra: bounds and gaps*, arXiv:1012.0864v3 (14 October 2013), Section 2 (PDF p.6: algebraically closed characteristic-zero field; level 0 has no cones), Theorem 5.15 (p.41). N変数次数dの上界は2N(N(d−2)+1)−1。PDFの本文とページ画像を確認した。一般非零対象のshift軌道生成は既知であり、新規性を主張しない。
- Lin–Zhang, *Serre algebra, matrix factorization and categorical Torelli theorem for hypersurfaces*, arXiv:2310.09927v2 (4 June 2024), Theorem 3.5・Remark 3.6 (PDF p.9), Theorem 5.1 (=Theorem 1.7, p.11)。本文・ページ画像を確認した。cubicのt=1,2の低積には非恒等sectorが干渉しない。rotation付き一意性にn>3は不要。
- 既存の有限積分・symmetrizer議論は `explicit_jacobian_recovery.tex`、`finite_algebraic_recovery.tex` に証明があり、Ueda–Yoshinaga、Hwangを引用する。今回はその一般点での適用順序を変え、局所完備底で低Natの有限性を先に仮定する経路を避けた。基礎体降下という組合せの包括的新規性調査は未完了。
- 参照先：https://arxiv.org/abs/1012.0864 ; https://arxiv.org/abs/2310.09927 ; https://arxiv.org/abs/2501.08633 。外部PDFはbundleへ収録しない。

## 今後も残す障害・反例

**幾何学的一意性と基礎体上のformは異なる。** C(h)上の Σx_i³ と h x_1³+Σ_(i>1)x_i³ は同じ勾配空間を持つが、Hessian超平面配置とh進付値からC(h)上では射影非同型。三乗根を加えると同型になる。`gcd:ex:forms`。これは同値核の降下障害が実際に非零という例ではなく、勾配空間だけからK上の一意性を主張できない例である。

**特異・Artinの生成性をgenericへ無条件に持ち上げない。** P¹上の cone(O(-1) --hs--> O) の障害は有効。非零性と全rotation軌道という追加構造が必要。

**次元と可積分性は圏同値の証明でない。** 低積が可換・正しい次元でも、候補方程式が得られるにすぎない。今回の基礎体降下は先に幾何学的な圏同値の存在を使っている。

## 次の着手

第一に、`gcd:prop:three-object` の比較を具体化する。am:prop:Gamma-basechange のprojective mutation模型と三つのstabilizationの同定を確認し、CFのbar構成をこの対象集合へ制限して、endomorphism上の準同型・rotation・指定三次周期図式を点検する。ここを閉じることが無条件化への最優先である。

第二に、非可換入力からのV,U,μの有限表示を構成する。これは存在定理の前提ではなく、G/Kを実際の係数へする有効化である。第三に多変数(L),(CF)とチャート間の比較・接着を扱う。特殊点を含む同値、有限拡大次数、同値核行列、最適生成上界は未解決として分離する。

## 計算・組版・保存の状態

`python3 computations/verify_generic_cubic_descent.py --output build/generic_cubic_descent_checks.json` はQ(t)上の3例（5変数Fermat、5変数混合、6変数混合）を厳密計算し、可積分空間次元5,1,1、可逆行列の選択、計16本の勾配恒等式を確認した。非可換圏の低Natや同値核の計算ではない。

現行B全体のLuaLaTeX組版と全既存証明書の再実行は未実施。今回の局所組版・参照確認の実施状態は `validation_paper_b.json` に記す。過去の包括的な `validation.json` と今回のB-v41の実施範囲を混同しない。GitHub main正本、Actions・force pushなし。Libraryは実際のpush失敗時のみ緊急退避。
