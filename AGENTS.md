# AGENTS.md — nc-cubicの研究継続指示

**2026-11-10・v26。GitHub uedakazushi/nc-cubic の main が唯一の正本。** 最初に00_research_plan.md、次にnotes/research_notes.mdとreconstruction/README.mdを読む。旧ZIP・会話・Libraryを再開の前提にしない。

## 曲率付き絶対対角からの有限積と可換候補（v26）

**実際の非可換入力に対する計算結果、ただし残余rotation積との比較は未証明。** 混合族の λ=1 の指定中心対について、絶対曲率付き対角の閉自己準同型の合成を Q(h) 上で計算した。その対称積の核を積分すると
[
\widetilde F_h=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^{12}/4374)u^3
]
を得る。四変数の積は6×10行列、勾配変換の行列式は 1+h^6/27。これは有限の有理関数体上の計算であり、h=0で正則な中間ホモトピー・実際の残余圏との比較・一般λの式・generic rotation付き圏同値を証明したものではない。相対対角ではu³補正を検出できず、絶対対角を用いる必要がある。

**証明と再現：** papers/reconstruction/curved_diagonal_recovery.tex、computations/curved_diagonal.py、computations/absolute_diagonal.py、computations/verify_curved_diagonal.py、computations/curved_diagonal_certificate.json。研究上の障害は notes/curved_diagonal.md に整理。検算は `python3 computations/verify_curved_diagonal.py --output build/curved_diagonal_certificate.json`、出力と追跡中の証明書を照合する（重い厳密計算）。前回の検算記録と証明書を保持するが、この統合時点で長時間の完全再計算は未実施。

**次の課題：** (1) h=0で極を持つ中間ホモトピーと閉行列をDVR核飽和で正則化する。(2) 曲率付き絶対対角の積と残余dg圏の導来自然変換・rotation積との合成を保つ比較を証明する。(3) 比較が成立した後にgeneric可換模型と圏同値を検証する。SM/ERと指定生成子のgeneric生成性は独立した未解決課題として保持する。

## 目標と優先順位

1. 滑らかなcubic n-fold (n≥3) 上のPoisson構造の構造定理。論文Aのthm:pg-normalに証明あり。
2. 各固定Poisson構造を、Koszul AS-regularな周囲と中心三次正則商で代数的に量子化する。論文Aのthm:pg-quantizationに証明あり。全Poisson係数空間上の一様相対量子化とは区別する。
3. 構成した量子化のgenericファイバーについて、同じKuznetsov成分とrotationを持つ滑らかな可換cubicを構成する。**最優先・一般混合型は未完成。** 任意のAS-regular中心三次商の全点には広げない。Zhang twistによるrotation付き反例がある。

証明の記載、独立監査、計算実行、形式証明を区別する。cubic n-foldの周囲はnc P^(n+1)。価値ある既存成果・証明を軽量化のため削らない。

## 有限代数的復元（最優先）

nc残余圏の実際の低rotation積を有限代数的に構成し、その核から可換方程式を直接積分する。証明全文はpapers/reconstruction/finite_algebraic_recovery.tex、検算はcomputations/verify_finite_recovery.py、障害と用途はnotes/finite_algebraic_recovery.md。人工的可換候補の積をncデータと混同しない。SM/ER・指定生成子のgeneric生成性は圏同値に関する別の課題である。

## 現行の証明方針

**有限な実際の低rotation積を構成し、局所飽和・Euler積分で可換式を直接抽出する。形式MFとArtin比較は完成底での一致に使う。** 証明本文と仮定を確認してから新しい推論を行う。

- formal_cubic_mf_reconstruction.tex：全Hochschild cochainsまで含めたformalityでπ_hと中心Casimir W_hを求める。勾配Koszulの次数論でπ_h=[Ξ_h,W_h], [Ξ_h,π_h]=0。全Artinと次数別完備底上の有限rank MF同値を得る。一ブロックは不要。代数化・generic本質全射は結論しない。
- curved_gauge_comparison.tex：F₀=0で写像と逆写像が有限arityであるbar同型をTwへ延長する。Qのh-adic冪零性を仮定しない。flowはF_(2r+1)=O(h^r)。
- kontsevich_second_jet.tex：混合族の可換式はF_lambda+h²(xyz/3−lambda²u²z/12)、Jacobian係数はc(lambda)=1/3+lambda³/36。低Nat積を完全な10×15行列で決定した。星積eyeと曲率wheelを区別する。半古典πだけで高次Wを決めない。
- artin_residual_mf_comparison.tex：ambient-perfectな相対特異圏、Chen、exact dg商、finite totalization、window i=4−dで線束残余pairをMFと同定する。am:prop:Gamma-basechangeが既存Γ_RのArtin底変更を扱う。絶対D_sgへ置換しない。
- artin_smoothness_obstruction.tex：特殊fiberと全Artinでsmoothでもgenericがnon-smoothとなるrank4のproper dg反例を保持する。既知のP¹生成子退化例に基づく。本研究のnc cubic Γの反例ではなく、cohomology-flatな模型の反例でもない。
- mixed_test_family.tex：指定中心元の閉式、全パラメータ中心性、全Artin PBWを保持。非零hの全AS性はArtin計算だけでは従わない。
- explicit_jacobian_recovery.tex、poisson_first_order.tex、explicit_model_comparison.texの有限積分、一次消滅、分離型Hessian比較の全証明を保持する。候補の一意性と存在、一般次数と三次元の特別な結論を区別する。

mixed_equivariant_normal_form.texのG=H⋊⟨τ⟩同変formalityと二形式級数正規形を維持する。τはx,y交換・h符号反転で、関係式と中心元を保つ。形式可換模型はF_{lambda_*(h⁶)}+h²c_*(h⁶)xyzへ整理できるがgeneric復元は未証明。h⁶のlambda方向a₁、h⁸のxyz方向b₁は有限抽出の検算に必要な場合に計算する。generic圏同値に関する次の課題は、完備MF同値における指定残余生成子の像、genericでの実際の生成性、有限cone/retractまたは対角の証明書を求めること。全Artinで生成することからgeneric生成性を推論しない。λ³=−12でh²類が消える点について、最初に許されるh⁶の係数を調べる。

## 維持する存在証明の経路

- ERはpapers/reconstruction/etale_realization.texの実在するsmooth proper dg族を入力とする。障害のrotation不変性、幾何的KS全射、HH¹によるintertwiner持上げ、actual moduliの代数性、étale sectionを確認する。ERで残余smoothnessを先取りしない。
- notes/sm_bar_and_spreading.texの有限bar右逆判定、papers/sections/minimal_ainfty_arity.texの残余Γと線束生成子Λのsmoothness同値を使う。実際の有限perfect双加群と増大射が必要。
- H=H⁰⊕Hⁿの最小A∞模型でm_k=0 unless k=2 mod n。fivefoldのm₇、m₁₂、二次障害を区別する。arity証明書は係数計算やSMではない。低次数復元に役立つかを確認して計算順序を選ぶ。
- 節点・尖点二成分はpapers/sections/nonelliptic_quantization.texの全次数PBW量子化を使う。35係数sliceの検算は復元写像の計算ではない。係数方向も保つ相対量子化は全成分では未完成。
- Artin切断のperfectness、Hom階数、Serre自己同値、周囲の対角からSMを結論しない。旧dg加群負例の特殊fiber代数は非smoothであるが、新しいartin_smoothness_obstruction.texは特殊fiberも全Artinもsmoothな一般dg反例を与える。どちらも指定nc cubic Γの反例と同一視しない。

## 正確性と先行研究

既知結果・具体的計算・条件付き結果・未完成・予想を分け、仮定と証明所在を明記する。初出未確認なら新規と称しない。重要文献の一次資料を確認する。

rotationの低次数sector計算と、Serre関手だけからrotationを得るgcd条件を混同しない。全次数の自然変換環をJacobian環と同一視しない。正しいHilbert級数だけでは可積分性も圏同値も従わない。

中心元の可換表示と可換模型は異なる。分離Fermat例の二次項はそれぞれ−2h²xyz/3と+h²xyz/3。元のcubicが全量子化で復元されるとは主張しない。一次交換子だけで高次の復元先を決めない。

## 現行版の検証状態

公開コードの二次厳密計算と既存証明書の再検算はPASS。論文Cの従前版は133頁・32 inputsで組版・表示確認済み。現行v26は新inputの追加後に全体組版・receipt検査が未実施。各原稿の組版・receipt・描画の状態はvalidation.jsonを確認する。ソースが変わった場合は共通bibliographyを使うA/B/Cのreceiptを更新し、古いPDFを現行版として提示しない。

## 保存・再現・配置

1. 研究の区切りに方針・ノート・論文の証明全文・必要なコード/入力/証明書/再現手順を、承諾を求めずmainへ反映する。remote headを確認し追加変更を保持して通常のfast-forwardのみ。force push、無断PR、GitHub Actionsは使わない。
2. 反映後にremote refと主要blob SHAを再取得する。要約だけの反映を全文保存と呼ばない。生成・数学的監査・計算・組版・遠隔反映を別々に報告する。
3. **Library保存はGitHub反映が実際に失敗した場合だけの緊急避難。** 成功時には二重保存しない。退避時は未同期と復帰手順を明示し、既存Libraryファイルを明示指示なしに削除しない。
4. 主論文はpapers/、ノートはnotes/、計算はcomputations/等。日本語LuaLaTeXを既定とする。ルート.latexmkrcとlatexmkでbuild/へ生成し、**PDFをGit追跡しない。**
5. 新しいinputは参照検査とbuild receiptの全ハッシュに含める。scripts/verify_bundle.py、新しい厳密計算、reconstruction/scripts/build.pyとverify.pyを必要範囲で実行する。親Cと独立SM/ER節の組版を区別し、A/B未組版なら明記する。
6. 独立境界研究・未照合原PDF8件はnc-cubic2、Reye研究はreyeに保全済み。再追加・重複保守しない。可換復元に必要な有効内容は現行本文に保持し、周辺原稿の全面再構築を優先しない。
7. 現在有効な自己完結した一式として更新する。旧ZIP、旧稿、変更履歴、ログ、キャッシュ、重複物を追加しない。数学的内容・検証可能性を損なう固定容量制限を設けない。
