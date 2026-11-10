# 研究方針：cubicのPoisson構造・量子化・可換復元

**2026年11月10日・v21。再開時は最初に本ファイルを読む。**

## 正本と研究の中心

**GitHub uedakazushi/nc-cubic の main を唯一の正本とする。** 次に notes/research_notes.md、論文C papers/rotation_cubic_reconstruction.tex を読む。旧ZIP・会話・Libraryを再開の前提にしない。

最優先は、与えられた非可換cubicから、同じKuznetsov成分とrotationを持つ滑らかな可換cubicを構成すること。**方程式の抽出と圏同値の存在を二つの作業として進める。** 一般の相対smoothnessを先に完了する一本の経路に限定せず、明示例から候補を作る経路と、smoothness・étale実現により存在を保証する経路を照合する。

方針の理由は、一ブロック分離型に既に具体的模型があり、一般次元でもrotationの次数一・二の積が分かれば方程式抽出は有限線形計算になることである。ただし低次数積やHilbert関数の一致は圏同値を保証しない。従来のSM還元・有限bar模型・A∞計算は有効な存在証明の経路として保持する。

## 三つの目標と対象

\(X^n=V(F)\subset\mathbb P^{n+1}_{\mathbb C}\)、\(n\ge3\)、\(N=n+2\) とする。周囲はN個の次数一生成元を持つ \(\mathrm{nc}\mathbb P^{n+1}\) である。

1. **Poisson構造の構造定理。** 三変数Jacobianブロック正規形・逆構成・一般階数。論文A papers/sections/poisson_geometry.tex の thm:pg-normal に証明あり。全既約成分・交叉の完全分類は達成条件ではない。
2. **個々のPoisson構造の代数的量子化。** 各固定 \((X,\pi)\) に対し、\(0\in U\subset\mathbb A^1_h\) 上の次数別平坦な族 \(B_h=A_h/(\Omega_h)\) を構成する。各周囲はKoszul AS-regular、\(\Omega_h\) は中心三次正則元、\(B_0=\mathbb C[z]/(F)\)。同ファイルの thm:pg-quantization に証明あり。全Poisson係数方向を保つ一様相対量子化は、これより強い未解決問題。
3. **構成した非可換cubicの可換復元。** 所定の量子化の少なくとも幾何学的一般ファイバーで、滑らかな \(Y_h\) と
   \[
   (\mathcal K(B_h),\rho_{B_h})\simeq(\operatorname{Ku}(Y_h),\rho_{Y_h})
   \]
   を構成する。必要な有限分離拡大・étale被覆を明示する。**一般混合型では未完成。** 方程式の具体的抽出を中心課題に含めるが、全パラメータに一価の有理閉公式があるとは要求しない。

「証明あり」は原稿に証明がある状態であり、全外部入力の独立監査・形式証明の完了ではない。任意のAS-regular中心三次商の全点復元は、Zhang twistによるrotation付き反例があるため範囲外。Kuだけの同値と、指定rotationを保つ同値を区別する。

## 現在使える具体的結果

### 一ブロック分離型のHessian公式

三変数三次式fの対称Jacobian量子化 \([y,z]=h\,\mathrm{sym}(f_x)\) と巡回式を考える。\(K(v)w=v\times w\) とすると
\[
\det\left(K(v)-\frac h2\operatorname{Hess}(f)\right)
=-3h\left(f+\frac{h^2}{24}\det\operatorname{Hess}(f)\right).
\]
これはMori–Smithの既知の点曲線公式を本稿の規約で表した恒等式である。新規な発見とは称しない。

適切な三次元AS-regular性、滑らかな楕円THCRとなる中心商、独立な中心変数の三次式Pの孤立臨界点を仮定すると、既存の楕円ブロック比較と中心変数追加の定理により、良いファイバーで
\[
Y_h=V\left(f+\frac{h^2}{24}\det\operatorname{Hess}(f)+P(u)\right)
\]
を可換模型として使える。papers/reconstruction/explicit_model_comparison.tex を参照。圏同値の入力は papers/sections/elliptic_reconstruction.tex にあり、行列式の計算成功とは別である。

Hesse形 \(f_t=(x^3+y^3+z^3)/3+txyz\) では
\[
\theta(h,t)=\frac{t+h^2(1+t^3/4)/3}{1-h^2t^2/4},\qquad Y_h=V(f_\theta+P).
\]
特にt=0で復元先の補正は \(+h^2xyz/3\)。中心元の表示を可換化した式では \(-2h^2xyz/3\) であり、差はJacobian環で非零。中心元の可換表示・PBW記号・代数のabelianizationを復元式と同一視しない。

### 一般次元の方程式抽出

対角双加群 \(\Delta\) とrotation双加群Pから
\[
V=H^0\operatorname{RHom}(\Delta,P),\quad
W=H^0\operatorname{RHom}(\Delta,P\otimes^{\mathbf L}P),\quad
\mu:V\otimes V\to W
\]
を計算する。可換cubicでは \(V=J(F)_1,\ W=J(F)_2\) で、積はJacobian環の積。N≥5では次数一・二に非恒等sectorの例外はない。

積の対称性・全射性と \((\dim V,\dim W)=(N,\binom N2)\) を検査し、\(K=\ker(\operatorname{Sym}^2V\to W)\) の基底を \(q_a\) とする。
\[
\sum_a A_{ia}\partial_jq_a=\sum_a A_{ja}\partial_iq_a
\]
というN²未知数の線形系に可逆解があり、Kに共通射影零点がなければ
\[
F_A=\frac13\sum_{i,a}x_iA_{ia}q_a
\]
が滑らかな候補を与える。候補は射影同型を除いて一意だが、固定座標ではscalar倍まで一意とは限らない。

証明は papers/reconstruction/explicit_jacobian_recovery.tex。**検査成功は同値存在の証明ではない。** 任意の非可換表示から上記導来自然変換を有限計算で求める方法も、まだ完成していない。既知の可換入力からの検算を、非可換残余圏の計算と報告しない。

### cubic threefoldの一次消滅

通常のHKRの純bivector部分について
\[
H^0(X,\wedge^2T_X)\longrightarrow HH^2(\operatorname{Ku}(X))
\]
は零である。Todd補正を局所divergenceで処理し、JLLZの作用写像の単射性を適用した証明は papers/reconstruction/poisson_first_order.tex。

量子化のKS類が純Poissonであり、enhanced残余への制限と両立することを確認した上で、可換模型族が存在すればmarked座標変換により \(F_h=F+h^2G_2+O(h^3)\) とできる。全次数の定数性、全奇数次消滅、一般次元、SMは結論しない。G₂は選択した量子化の高次データに依存し得るので、Poisson括弧だけの普遍不変量とはまだ呼ばない。

## 優先順位と次の具体的着手

### 優先1：三次元の最小混合例の二次項

最初の入力を
\[
F_\lambda=(x^3+y^3+z^3)/3+u^3+v^3+\lambda uxy
\]
とする。古典cubicの滑らかさは λ³≠−3 と同値。uxyはFermatのJacobian環で非零なので、単なる一次の座標移動ではない。\(a=\lambda u\)、\(T=\sum_{\sigma\in S_3}x_{\sigma(1)}x_{\sigma(2)}x_{\sigma(3)}\) とすると、対称Jacobian関係に対する三次中心元は
\[
\Omega_{h,\lambda}=\frac{x^3+y^3+z^3}{3}-\frac{h^2}{9}T
+\frac a2(xy+yx)+\frac{h^2a^2}{6}z+\frac{h^4a}{18}z^2+u^3+v^3.
\]
中心性を全パラメータで自由代数の多項式恒等式により証明した。全Artin切断のPBW性と中心商の次数別平坦性も証明した。papers/reconstruction/mixed_test_family.tex を参照。これは非可換側の入力であり、可換復元先ではない。非零hの全AS-regular性や残余SMは、この計算からは結論しない。

対角有限群のcharacterをχとすると、\(J(F_\lambda)_3^\chi=\mathbb C[xyz]\)、\(J(F_\lambda)_3^{\chi^2}=0\) を計算できる。従ってmarked同変復元が存在するという条件下では、最初の非自明な係数は \([G_2]=c(\lambda)[xyz]\) の一変数に絞られる。同変復元の存在やc(λ)自体を求めたわけではない。Hessian由来の未検証案は研究ノートに記載する。

1. 固定した対称量子関係と三次中心元から純Poisson KS条件を確認し、残余への制限との両立を示す。
2. 残余dg模型・rotation双加群の次数一・二の導来自然変換を、まず \(\mathbb C[h]/(h^3)\) 上で求める。分離点ではHessian式と照合する。
3. 可積分線形系から \([G_2]\in J(F_\lambda)_3\) を求める。同変比較が確認できれば未知量はc(λ)一つであり、λ=0でc(0)=1/3を再現する。Hessian由来の候補との一致・不一致を判定する。
4. 同値双加群の持上げ、または下記SM・ER経路で存在を証明する。三次jetの一致のみで圏同値を結論しない。

低次数の候補計算を省いて全m₇,m₁₂等の係数計算だけに集中しない。低次数Homの底変更・有限性にSMが必要な箇所では、その仮定を隠さず有限bar模型へ戻る。

### 優先2：存在証明を同時に進める

現行のétale局所実現ERは、**実在するsmooth proper dg族**とrotationが一点で幾何的pairに一致することを入力とする。幾何的KSの全射、同値双加群のrotation不変障害、HH¹消滅、actual moduliの代数性を使う。証明は papers/reconstruction/etale_realization.tex。これは非幾何的族のsmoothnessの証明ではない。

SM経路ではproper残余dg代数Γの実際の有限perfect対角と増大射を構成する。notes/sm_bar_and_spreading.tex の有限bar-skeletonの右逆判定を使う。線束生成子Λの相対smoothnessとSMの同値は papers/sections/minimal_ainfty_arity.tex にある。

最小A∞模型 \(H=H^0\oplus H^n\) では \(m_k=0\) unless \(k\equiv2\bmod n\)。fivefoldではm₇,m₁₂と \(\delta m_{12}=-[m_7,m_7]/2\) を区別する。現行arity証明書は必要条件の検算であり、実際の係数・有限対角は与えない。

### 優先3：非楕円fivefold・一般成分

節点・尖点二成分の二パラメータ量子化は papers/sections/nonelliptic_quantization.tex に具体式・全次数PBW・周囲の有限対角がある。残余SMと低次数rotation積は未計算。本質的混合項ux²は中心線形shiftだけでは除去できず、Hessian公式を直接適用しない。

35係数可換変形sliceは verify_etale_inputs.py で検算済みだが、量子パラメータから35係数への写像ではない。各Poisson成分のgenericへの拡張には係数chartを保つ相対量子化・必要な底変更・SMまたは直接比較を確認する。rank層と既約成分を同一視しない。

## 保持する成果と障害

- 論文AはPoisson正規形・量子化、Bは17次元族・偏極付きambient復元、Cは可換模型・rotation・障害を扱う。ambient復元とKuからの可換実現を区別する。17次元族の分離型の余次元15、接写像の核7等の証明は既存原稿に保持する。
- BFK sector計算による \(HH^3(\operatorname{Ku}(X))^\rho=0\) は全n≥3。無偏極のHH³はn=7のみ二次元。形式的障害消滅はSMではない。
- Artin切断のperfectnessだけで実際の相対perfectnessを結論しない。現行負例の特殊ファイバー代数はsmoothではなく、今回のSMの反例ではない。
- \(q_i=x_i^2+x_{i+1}x_{i+2}\)（添字mod5）は共通射影零点を持たずHilbert級数 \((1+t)^5\) だが、積分線形系の核は零。正しいHilbert級数と二次完全交差性はJacobian性を保証しない。この例が非可換cubicから生じるとは主張しない。
- 中心商、Serre関手、逆rotation、\(\rho^3\simeq[2]\)、選んだ周期同型のcoherenceは別のデータ。ERは自己同値一つのpairを扱う。
- 独立境界研究・未照合PDF原本8件はnc-cubic2、Reye研究はreyeに保全。原PDFの完全TeX照合は未了。周辺資料の全面再構築を可換復元より優先しない。

## 再現と証明の状態

計算・組版手順は reconstruction/README.md。新しい線形復元、Hessian恒等式、二次比較は厳密有理計算で検証する。論文Cと独立SM/ER節をそれぞれ組版し、全inputの参照・引用・ハッシュを確認する。

初等証明を本文に記載して内部点検したが、外部査読・Lean形式証明ではない。Lin–Zhang、Huybrechts–Rennemo、JLLZ、Calaque–Rossi–Van den Bergh、Mori–Smith、Ueda–Yoshinaga、Hwangの一次資料を参照し、既知結果の応用と具体的計算を区別する。新規性の初出が未確認なら明記する。

## 研究一般の原則と保存規則

1. 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し研究価値を最大化する。方針変更の理由・達成点・未解決点は現在有効な方針として整理し、時系列の履歴を蓄積しない。
2. 証明済み、条件付き、未完成、予想、計算的観察を分け、仮定・依存・証明所在を示す。証明の記載、独立監査、計算実行は別状態。誤りは依存箇所も更新する。
3. 重要な文献は一次資料で適用範囲を確認し、未確認の書誌・新規性を補作しない。外部PDFや検索結果を大量収録しない。
4. 公表価値ある成果と証明全文を日本語LuaLaTeXで保持し、既存成果を削らず論理的に統合する。ノートは着想・計算・例・反例・障害を整理し、日誌や重複証明にしない。
5. **研究の区切りごとに承認を求めず、方針・ノート・証明全文・コード/入力/証明書/再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保持し、force push・PR・GitHub Actionsは使わない。反映後にremote refと主要blobを再取得する。
6. **Library保存はGitHub反映が実際に失敗した場合だけの緊急避難。** 成功時には二重保存しない。退避時は未同期と復帰手順を明示し、既存Libraryファイルは明示指示なしに削除しない。
7. 現行版の自己完結した一式を保つ。旧ZIP・履歴・ログ・キャッシュ・重複物は加えない。数学的内容・検証可能性を固定容量制限のため削らない。
8. 日付・版・参照を揃え、生成・計算・組版・GitHub登録・遠隔確認を区別して報告する。TeXはルート.latexmkrcからLuaLaTeXでbuild/に生成し、PDFをGit追跡しない。未実行・失敗・再現上の制約は明示する。
