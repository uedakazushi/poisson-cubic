# 研究方針：cubicのPoisson構造・量子化・可換復元

**2026年11月10日・v20。再開時は最初に本ファイルを読む。**

## 正本と最優先事項

**GitHub `uedakazushi/nc-cubic` の `main` だけを正本とする。** 次に `notes/research_notes.md`、`reconstruction/README.md`、現行原稿 `papers/reconstruction/rotation_saturation_reduction.tex` を読む。旧bundle、会話履歴、Libraryを再開の前提にしない。

研究全体の目標は下記の三つに限定する。目標1・2は原稿に定理と証明があり、目標3の可換復元を最優先する。完成のために不要なモジュライ分類や周辺の復元問題を新たな第四の目標にしない。既存の有効な研究成果は論文・ノートに保持する。

## 最終目標は三つだけ

**対象・記法：** \(X^n=V(F)\subset\mathbb P^{n+1}_{\mathbb C}\) は滑らかなcubic、\(n\ge3\)、\(N=n+2\)。周囲の非可換射影空間は \(\mathrm{nc}\mathbb P^{n+1}\)（\(N\)個の次数一生成元をもつAS-regular代数）である。

1. **Poisson構造の構造定理。** 任意の \(\pi\in H^0(X,\wedge^2T_X)\) で \([\pi,\pi]=0\) を満たすものについて、三変数Jacobianブロックによる正規形、その逆構成と一般階数を記述する。**原稿上で定理・証明あり。** `papers/sections/poisson_geometry.tex` の `thm:pg-normal`。Poissonスキームの全既約成分・交叉の完全分類は、この目標の達成条件に含めない。
2. **与えられたPoisson構造の代数的量子化。** 各固定 \((X,\pi)\) に対し、\(0\in U\subset\mathbb A^1_\hbar\) 上の次数付き代数族 \(A\) と中心三次正則元 \(\Omega\) を構成し、\(A_0=\mathbb C[z_1,\ldots,z_N]\)、\(B=A/(\Omega)\)、\(B_0=\mathbb C[z]/(F)\) とする。全ての閉ファイバーの周囲 \(A_\lambda\) はKoszul AS-regular（大域次元 \(N\)）で、\(B\) は所定のPoisson括弧を一次項にもつ次数別平坦な代数的量子化。**個々の構造について原稿上で定理・証明あり。** 同ファイルの `thm:pg-quantization`。Poisson係数空間全体を一括してパラメータ化する *相対的・一様な族* の存在はこれより強い別問題で、現在未完成である。
3. **構成した非可換cubicからの可換復元。** 目標2で構成した \(B_\hbar\) の少なくとも非空Zariski開（必要な有限étale/分離拡大を明示）で、滑らかな可換cubic \(Y_\hbar\) とrotationを保つenhanced同値
   \[
   (\mathcal K(B_\hbar),\rho_{B_\hbar})
   \simeq
   (\operatorname{Ku}(Y_\hbar),\rho_{Y_\hbar})
   \]
   を構成する。**未完成・最優先。** 必要な局所proper模型とrotation、相対étale実現は原稿上で論じられ、残余対角のperfect性(SM)が核心である。任意のAS-regular中心三次商（Poisson量子化族に属さないものを含む）の全点にこの結論を主張してはならない。Zhang twistによる反例と区別する。

**達成判定：** 目標1・2の原稿にある証明を一次資料・数学的論理まで監査し、目標3を上記の量化と底変更条件で無条件に証明すれば、本研究の三目標は達成とする。Poisson既約成分の完全分類、任意の量子化の一意性、全パラメータでの可換復元、可換模型の閉公式、偏極付きambient復元の完成は達成条件に付け加えない。これらの既存成果は削除せず論文・ノートに保持する。

## 現在の到達点と論理

1. 各非零Poisson成分を、滑らかな係数chart T とスカラー h を用いる S=T×A¹ で支配する。必要なら有限étale被覆でブロック座標を固定する。特異な錐の頂点への量子化の降下はgenericな存在の前提ではない。
2. 所定の次数別自由な中心三次量子化が正則局所底上にあれば、properな線束生成残余dg代数 Γ_R が得られる。標準rotationは、残余smoothnessを仮定せず、逆 `(-1) R_O` を持つ。
3. **残余対角のperfect性 (SM)** があれば、全coherent残余圏との同定とsmooth proper pairの有限型開集合へのspreadが従う。
4. **étale局所実現 (ER) は、実在するsmooth proper pairを入力とする定理として証明を収録した。** 同値双加群の小拡大障害はrotation不変HH²に入り、幾何的Kodaira–Spencer写像で消せる。HH¹=0でintertwinerも持ち上がる。actual perfect加群のmoduliの代数性と無限小判定からétale局所実現を得る。証明は `papers/reconstruction/etale_realization.tex`。
5. 従って、**所定の局所量子化が既にある成分ではgeneric可換復元の未解決入力は(SM)に集約される。** 目標2の「固定した各Poisson構造の代数的量子化」と、Poisson成分の係数方向を同時に保つ一様相対量子化とは区別する。後者の全成分版は未完成。

この整理により、(ER)を未証明仮定として重ねて課す必要はなくなった。親原稿のactual/formal変形比較を全て再監査したという意味ではなく、同値双加群を直接持ち上げる独立の論証を用いる。自己同値一つを指定したpairを扱い、選択した `rho^3=[2]` のcoherenceまで入力・結論に含めない。

## Hochschild障害の現在有効な整理

BFKの一次資料の固定sector公式より、滑らかなcubic n-fold (n≥3) のKuについて、`HH³(Ku(X))=0`（n≠7）、n=7のとき`HH³=C²`で、その二方向はrotationの非自明な三乗根固有空間に分かれる。したがって**全次元で `HH³(Ku(X))^rho=0`**。特にn=5の節点・尖点二例では `(dim HH^0,...,dim HH^4)=(1,0,35,0,7)` である。証明は `papers/reconstruction/hochschild_obstructions.tex`。整数sector計算は `reconstruction/computations/verify_hochschild_sectors.py` で再現できる。

この事実は通常のMorita変形の一次障害の候補群を消すが、任意のrotation付き変形のcoherentな障害理論、実在する残余対角の持上げ、代数化は独立である。**残余smoothness (SM) は未証明のまま**であり、本研究の最優先課題を変更しない。

## 優先度1：非楕円二成分の残余smoothness

節点型・尖点型の二つのPoisson既約成分を最優先試験例とする。固定した滑らかなcubic fivefold上の二次元成分であり、全次数PBW ambient・中心混合項を保つ三次正則商・局所proper模型は既に構成されている。純三次ブロックの楕円性を仮定しない。

R=C[r,s]_(r,s)、Γ_R=REnd(G) に対し、実際の有限perfect双加群 P と増大射 `P→Γ_R` を作り、その特殊ファイバーが擬同型であることを示す。Γ_R がR-perfectなので、PもR-perfectであり、coneに局所Nakayamaを適用できる。

具体的着手は、特殊ファイバーの対角を外部線束の有限twisted complexとして記述し、微分・高次homotopy・増大射を量子関係に沿って持ち上げること。ambientのKoszul対角を中心商で両側テンソルしただけのものと残余対角を同一視しない。中心自己交叉の周期的部分をwindowで制御する。通常のpartial_uは量子代数の導分にならないため、可換Jacobian微分をそのまま代入しない。

成功基準は、仮定だけを再掲した還元命題ではなく、有限データ・射・整合式を実際に示すことである。Serre関手、逆rotation、Hom階数表、各Artin切断のsmoothnessだけで(SM)を結論しない。

## 優先度2：得られた成分の復元と一般成分への拡張

(SM)が得られた成分には、現行原稿のgeneric復元定理を適用する。非楕円二成分については、可換特殊ファイバーの35係数変形sliceを厳密に構成した。`verify_etale_inputs.py` は84×49の座標変換行列の階数49と、補空間の35単項式を有理数上で検証する。これは復元先の族の具体化であり、(r,s)から35係数への閉公式や(SM)の証明ではない。

一般成分では、支配的chart上の全次数PBW性・noetherian性・必要なAS条件・底変更を確立する。有限中心行列の形式核は任意の有限jetを保って代数化できるが、これは全次数PBWや残余smoothnessの代替ではない。rank層と既約成分を同一視しない。genericなブロックが節点・尖点型である成分を除外しない。

## 他の現在有効な成果の保持

論文A `papers/poisson_cubic_quantization.tex` はPoisson正規形・退化・量子化、論文B `papers/generic17_ambient_recovery.tex` は17次元中心三次対と偏極付きambient復元、論文C `papers/rotation_cubic_reconstruction.tex` はrotation付き復元と障害を扱う。`reconstruction/` は論文Cの現行証明の独立組版入口であり第四の主論文ではない。

17次元族では分離型の有理商は2次元、法線は6+9=15次元、元の可換cubicのJacobian変形への17次元接写像の核は平面移動6とPoissonスカラー1である。これを量子化後の可換模型への写像と同一視しない。固定したcubic・平面上のスカラー束から楕円Picardへの有理写像障害は、動く模型や分岐対応を否定しない。

Brill–Noether・Pfaffian接触の独立技術原稿、中心曲面判別式の証明と検算は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) にGit blob同一で移管した。PDF-only原本8件はnc-cubic2へGit blob一致で移転済み。TeXとの完全照合は未了。可換復元への直接の依存がない独立境界研究は今後そちらで保守する。Reye 論文・停留平面・275/550計数に関する研究資産は専用リポジトリ https://github.com/uedakazushi/reye を正本とする。原稿にある唯一の証明を軽量化のため削除しない。新規性の包括的文献照合と全既存証明の独立監査は未完了。

## 証明・計算・再現の状態

新しい(ER)の論証は本文に完全に記載して点検したが、外部査読・Lean形式化ではない。基礎入力はToën–Vaquiéのactual perfect object moduli、Lowenの特徴作用と障害、BFKのHochschild計算、Huybrechts–RennemoとJLLZの幾何的接写像、四次元でのHuybrechtsのrotation作用である。Lin–Zhang (2026) の幾何的両側projectorの定理を、非幾何的targetへそのまま適用しない。正確な参照箇所は原稿文献表に置く。

再現は `reconstruction/README.md` に従う。中心性・重なり検算と、変形slice検算を別々に実行する。原稿の全inputを展開して参照とハッシュを検証する。親A/B/C全体の再組版・過去の全計算の再実行は、今回の独立組版の成功から推論しない。

## 研究一般の原則と保存規則

以下は上の個別計画と区別する恒久的原則である。

1. 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更の理由と達成・未解決部分を、現時点で有効な方針として整理する。時系列の履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を分け、仮定・依存・証明所在を示す。証明の記載、今回の監査、計算実行を混同しない。誤りなら依存箇所も直し、有用な反例をノートに残す。
3. 先行研究の重要主張は一次資料で適用範囲を確認し、Introductionで本研究との関係を具体的に示す。未確認の書誌や新規性を補作しない。外部PDFや検索結果を大量に同梱しない。
4. 公表価値ある成果と十分な証明を日本語LuaLaTeXで整理する。既存成果を削らず、論理的な順序へ統合し、未完成を完成定理と扱わない。
5. ノートは現在有効な着想・計算・例・反例・障害・文献比較を保持し、作業日誌や重複証明は置かない。再取得困難な知識は簡潔に残す。
6. **GitHub mainを唯一の正本とし、研究の区切りごとに承認を求めず全文と再現資産を通常のfast-forwardでpushする。** リモート変更を保持し、force push・PR・GitHub Actionsは使わない。push後にremote refと主要ファイルを再取得して検証する。
7. **Library保存はGitHub pushが実際に失敗した場合だけの緊急避難に限定する。** 成功時に保存しない。退避は未同期と復帰手順を明示し、既存Libraryファイルは明示指示なしに削除しない。
8. 現行方針・ノート・全証明・最小限のコード/入力/証明書/再現手順だけを管理する。旧ZIP、旧原稿、履歴、ログ、キャッシュ、重複物は含めない。数学的内容や検証可能性を犠牲にした固定容量制限は設けない。
9. 生成・計算・組版・GitHub登録・遠隔確認は別々に報告する。日付・版を付け、欠落・参照切れ・組版・必要な計算を確認する。未実行・失敗・再現上の制約は正確に記す。

## 現行の研究資産の配置

主論文A/B/Cは `papers/`、現行研究ノートは `notes/`。研究再開時は本方針→`notes/research_notes.md`→`notes/reconstruction.md`→`papers/rotation_cubic_reconstruction.tex` の順で読む。独立組版入口は `papers/reconstruction/rotation_saturation_reduction.tex`。LuaLaTeXの再生成はリポジトリルートで `latexmk papers/rotation_cubic_reconstruction.tex` とする。`build/` の生成PDFはGitに含めず、ソース未照合の原PDFはnc-cubic2で保全し、本リポジトリではPDFを追跡しない。

原PDFはnc-cubic2のノート2件・論文6件に移転済み。nc-cubicの追跡PDFは0件。

## 相対smoothnessの近道と避けるべき推論

可換復元の最短経路は、既存の非楕円（節点・尖点）二パラメータ量子化について、残余dg代数 `Gamma_R` の対角の **実際の有限perfectモデルと射** を構成し、その特殊化で擬同型を確認すること。具体的な判定として、`Gamma_R` の相対bar解消の有限段階 `P_d -> Gamma_R` が導来双加群圏で右逆を持つこととSMは同値である（証明は `notes/sm_bar_and_spreading.tex`）。具体式は `papers/sections/nonelliptic_quantization.tex`、局所proper模型は `papers/sections/local_projective_model.tex`、回復済みの負例は `notes/source_recovery/dg_perfectness_counterexamples.tex`。特に **Artin切断すべてのperfectnessや基底上のHomの有限性だけではSMを結論しない。** 負例は特殊ファイバーの代数自体がsmoothでないので、smooth special fiberを持つ我々の対角の反例ではない。必要な有限証明書の作り方・相対Orlov比較の具体的構成に研究資源を集中する。

### 有限bar模型の明確な目標

`notes/sm_bar_and_spreading.tex` に、proper dg代数の相対対角がsmoothである必要十分条件として、ある有限bar-skeleton `P_d → Gamma_R` の右逆の存在を証明した。またgeneric fiberでのsmoothnessから非空局所化上の相対smoothnessが従うが、**special smoothnessからgeneric smoothnessは未証明**である。次に必要なものは節点・尖点二成分の実際の相対bar右逆、または同等の有限perfect対角証明書である。元の34ページPDFの第18--21節からTeXを回復したが全PDF復元ではない。

## 相対対角の計算対象を縮小した現行方針

局所proper模型の有限$R$-例外列による半直交分解で、相対smoothness (SM) は残余dg代数 `Gamma_R=REnd(G)` と線束生成子のdg代数 `Lambda_R=REnd(⊕_{i=0}^{n+1}O(i))` について同値である（証明：`papers/sections/minimal_ainfty_arity.tex`、既知の相対半直交分解定理Perry Lemma 4.15(3)の適用）。以後は**Homを明示できるLambda側の対角を先に試す**。この同値はSMそのものの証明ではない。

`H^*(Lambda_R)=H^0⊕H^n` なのでstrictly unitalな最小相対A∞模型で `m_k=0`（`k≠2 mod n`）。fivefoldでは最初が `m_7`、次に `m_12`。最初の `[m_7]∈HH^7(H,H)_{-5}` はHochschild類、次に `δm_12=−[m_7,m_7]/2` が必要となる。純粋な次数・指数配置だけで$m_{12}$を消してはならない。計算証明書は `computations/verify_minimal_ainfty_arity.py` と `computations/minimal_ainfty_arity_certificate.json`。

**次の実作業：** 有限コホモロジー模型 `Lambda_R` の相対縮約 `(i,p,h)` を構成し、$m_7$を132本の平面二分木式で求め、Stasheff恒等式および$m_{12}$への障害を確かめる。続いて有限bar-skeletonの増大写像の**実際の右逆**を探す。係数や有限対角証明書はまだ存在を示していない。旧PDFのTeX化や境界研究よりこの計算を優先する。
