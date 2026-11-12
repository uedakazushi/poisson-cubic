# 論文B：三対象windowと一般点可換復元

**2026-11-12 / B-v42。** 再開時は `00_research_plan.md` を読む。主定理は `papers/support/papers/reconstruction/general_dimension_recovery.tex`、局所比較の証明は同ディレクトリの `three_object_window.tex`、基礎体降下・定量的生成は `generic_cubic_descent.tex`。

## 現在の結論と条件

次数別有限自由な代数的中心三次対で、特殊ファイバーが多項式環と滑らかな三次式であることを仮定する。局所proper/window比較(L)と一般点AS正則性は、この代数的入力から導く。残る主定理の比較条件は **(CF_3)**：完備底上の三つのstabilizationを、滑らかな形式三次式のMFに属する E,E(1),E(2) と、全Hom複体・高次積・rotation・中心元からの三次周期性を含めて比較する実際のunital A∞ quasi-equivalence。全MF比較(CF)は十分条件だが必須ではない。

この条件の下で、元の体 K=C(h) 上のsmooth cubic模型、有限拡大後のrotation付き全coherent残余圏同値、全n>=3での幾何学的一意性、BFKによる生成時間2(n+2)(n+3)-1の上界を得る。方程式と同値核の定義体を区別する。特殊点込み相対同値、全nc cubicの表示、同値核のKへの降下は未証明。

## 局所比較(L)を導く論理

1. **完備Homの有限縮約**（`tw:lem:contraction`）。各cohomological degreeが有限自由で、剰余の全cohomologyが有限次元なら、完備底上で有界有限自由複体へ縮約する。体上で ds+sd=1-ip と s²=ps=si=0 を満たすcontractionを選び、δを極大イデアル内の微分の補正とすると J=(1+sδ)^{-1}, L=(1+δs)^{-1}, i'=Ji, p'=pL, s'=sL, d_H=pδJi。固定次数ごとの有限行列で収束する。Crainicの既知摂動公式を本規約へ翻訳したもの。
2. **代数的基底への降下**（`tw:lem:proper-hom`）。有限MFの固定次数Homは有限自由R加群。完備化後に上の縮約を適用し、忠実平坦性から元のHomのcohomologyが有界と分かる。noetherian性から各cohomologyは有限、Rの有限大域次元からperfect。さらに完全な射影複体のcycleはdimension shiftingで射影となるので、通常のHom複体自体が有限自由有界複体とhomotopy同値である。これで剰余への通常tensorも導来tensorを計算する。
3. **実際のdg関手**（`tw:lem:stabilization`）。Chenの余核定理は三角圏の結果として使用し、finite MFとGorenstein-projective加群のexact圏・dg商・有限totalizationを通じてenhancementを構成する。中心曲率でのtotalizationの縮約では残差sws=0を確認。右加群にはA^opを使う。余核の次数別自由性が、ここで必要な剰余・完備化底変更を保証する。
4. **section--window**（`tw:thm:window`）。a=N−3、i=1−a、Ψ=stab((Rω−)_{≥i})。生成線束O(j)上でsectionはB(j)_{≥i}。この対象がambient上perfectであることは有限長商のfiltrationと相対Koszul分解から従う。sourceとtargetのproper Homを用い、剰余の古典Orlov同値のHom比較coneに導来Nakayamaを適用してenhanced完全忠実性を得る。
5. **生成性は有限filtrationから証明**。T_j=B(j)_{<i} は j<a で零、j=a,a+1,a+2 で gr(T_j)=⊕_{r=0}^{j−a}B_r⊗R(j−r)。B_0=Rから三角的にK(a),K(a+1),K(a+2)を得る。(3)=[2]によりK,K(1),K(2)のthick閉包に一致する。特殊点の生成性の一般点への持上げは使わない。
6. **rotation**。Mが残余対象なら (RωM)_i=RHom(O(a−1),M)=0。切断三角とΨ(O)=0からΨρ≃(1)Ψ。像が正負の内部shiftで安定なのでρは自己同値。周期は指定中心元ΩのMF周期から移す。この構成と必要な底変更は自然。任意の別のスカラー倍の周期同型を保存するという主張ではない。

これらは既存のlocal_projective_modelのnoetherian/Koszul/Gorenstein/線束Homの補題を入力する。本文の依存と証明を今回点検して統合したが、Lean等で全証明を形式検証したものでも、外部査読を受けたものでもない。

## 一般点への最短経路

代数的な三対象window → (CF_3)を固定対象へ適用 → 固定HomをLaurent体へ局所化 → Eulerノルム2·3^(N−1)で像の非零性 → 代数閉包上のBFK生成 → perfect核と周期比較の有限降下 → smoothnessと線束検出によるcoherent飽和 → smooth proper性から低Natの体拡大 → 可積分勾配空間からG/Kを抽出する。

低積を最初に実計算すること、完備底全体のcompact逆核を先に構成することは一般点存在の前提にしない。(D)は特定の明示多項式を復元先に指定する別の条件。一般の全MF比較やStevenson/regradingの別証明も現行支持節に保持する。

## 残る核心と具体的着手

最優先は **(CF_3)の曲率付き比較の監査**。`formal_cubic_mf_reconstruction.tex` と `curved_gauge_comparison.tex` の構成を、実際の有限rank K,K(1),K(2)へ制限する。π=[Ξ,W]、[Ξ,π]=0、F_(2r+1)∈m^r の代数的入力と、unital bar写像・逆写像・t多重線形性・周期の自然比較を分けて点検する。固定次数内で収束することと、任意のLaurent対象へ形式級数を評価できることは別である。三対象の高次積を有限次数のEuler表だけで代用しない。

次にV=H^0 dgNat(Id,ρ)、U=H^0 dgNat(Id,ρ²)、積μを非可換入力から具体化する。これはG/Kの有効化であり、一般点存在の必要条件へ戻さない。正則多変数基底の(L)は同じ証明で成立するが、(CF_3)、チャートの接着、特殊点を含む同値は別に検証する。

## 保持する障害・反例

- **生成子の無条件の持上げは偽**。P¹上のcone(O(−1) --hs--> O)の例は有効。ここでは有限filtrationで三対象の像を同定し、その後に一般点の非零性と全rotation軌道を用いる。
- **幾何学的一意性とK上のformは異なる**。C(h)上のΣx_i³とh x_1³+Σ_{i>1}x_i³は同じ勾配空間を持つがK上では射影非同型。Hessian超平面配置とh進付値で判定する。`gcd:ex:forms`。これは同値核の降下障害が非零であることを示す例ではない。
- **積分可能な候補は圏同値を証明しない**。低積が正しい次元・対称性・可積分性を持っても模型候補が得られるだけである。基礎体降下では先に幾何学的同値の存在を用いる。
- **完備化の使い方を限定する**。完備Homの有限縮約は証明したが、Artin同値の列の逆極限が無条件に実際の関手・compact逆核を与えるとは扱わない。

## 一次文献と新規性

Burke--Stevenson, arXiv:1507.00830v1, Proposition 4.18, Lemmas 6.1--6.2, Theorem 6.4（PDF pp.14,18,21の関連箇所）。今回Theorem 6.4とその証明を本文・ページ画像で照合し、windowの向きとVerdier商の関係を確認した。
Chen, *Module factorizations*, arXiv:2402.11613、2025年8月28日付著者版、Theorem 7.2（印刷p.25）を本文・ページ画像で確認した。graded dg自然性は引用元の三角同値だけから宣言せず、本稿のexact圏/dg商の議論で補う。
Crainic, *On the perturbation lemma, and deformations*, arXiv:math/0403266、著者公開PDF `https://www.staff.science.uu.nl/~crain101/pert2.pdf` のTheorem 2.3/Remark 2.4を本文で確認した。同版ip=1+bh+hbと本稿の符号の差をs=−hで調整する（同PDFのweb画像取得は失敗しており、画像確認とは記録しない）。
BFK arXiv:1012.0864v3 Theorem 5.15とLin--Zhang arXiv:2310.09927v2 Theorem 3.5/Remark 3.6/Theorem 5.1は既存の一般点生成・低積・一意性の入力で、今回は再調査していない。包括的新規性調査は未完。既知のperturbation、MF、Orlov原理自体の新規性は主張しない。

## 検証・再現

`python3 computations/verify_three_object_window.py --output build/three_object_window_checks.json` を今回実行し、Q(h,u)上の二つの有限複体について16本の縮約恒等式、二つのSchur complement、原点で単元の分母を厳密検証した。N=5,...,16の12通りのwindow cutoff・三角的filtration・三次周期の添字もPASS。これは有限行列の符号・添字の検査であり、非可換MFの実際のHom模型、(CF_3)、圏同値の計算証明ではない。

以前の `verify_generic_cubic_descent.py` の3例・16勾配恒等式はコードを保持するが、今回は再実行していない。今回の抜粋は `latexmk papers/support/papers/three_object_window.tex` で再生成する。本文外の参照はラベル名で表示する。最新の実施状態は `validation_paper_b.json`。論文B全文と全既存証明書の再実行は未実施。

GitHub mainを正本とし、Actions・force pushなし。Libraryは実際のpush失敗時だけの緊急退避。
