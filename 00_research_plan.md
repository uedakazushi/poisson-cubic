# 研究方針：cubicのPoisson構造・量子化・可換復元

**2026年11月11日・v28。再開時は最初に本ファイルを読む。**

## 正本・目標・達成基準

GitHub `uedakazushi/nc-cubic` の `main` を唯一の正本とする。次に `notes/bar_comparison.md`、`notes/curved_diagonal.md`、`notes/finite_algebraic_recovery.md` を読み、一般背景は `notes/research_notes.md` と論文Cを参照する。会話・旧ZIP・Libraryを再開の前提にしない。

最優先目標は、構成した代数的な非可換cubicの幾何学的一般ファイバーを、同じKuznetsov成分と指定rotationを持つ滑らかな可換cubicとして実現すること。元の可換cubicへの復元や全パラメータに一価の有理公式があることは要求しない。任意のAS-regular中心三次商の全点復元にはrotation付き反例があり、その範囲へ広げない。

直接経路は `(A_h,Omega_h) -> 実際の低rotation積 -> その核K_h -> 可換三次式G_h`。formalityの特定の無限級数自体の代数性・収束を先行条件にせず、形式復元は完成底での比較・可積分性の保証に使う。方程式抽出とgenericな圏同値は別の達成基準である。

## 現在の主要な到達点

**1. Poisson・量子化（論文A）。** n>=3の滑らかなcubicのJacobian三変数ブロック正規形・一般階数、各固定Poisson構造の代数的量子化には証明本文がある。`papers/sections/poisson_geometry.tex` の `thm:pg-normal`, `thm:pg-quantization`。全係数方向を保つ一様相対量子化、全モジュライ成分・交叉の完全分類とは区別する。

**2. 17次元族（論文B）。** 41次元中心三次対、17係数slice、ambient復元、分離型の余次元15、忘却接写像の核7を保持する。`papers/generic17_ambient_recovery.tex`。構成した族の商の次元であって全nc cubic分類ではない。

**3. 形式MF復元・Artin残余比較（論文C）。** 一般斉次中心三次形式変形からW_hと定数trivectorを構成し、全有限Artinおよび次数別完備有限rank MFへ比較する証明を保持する。`formal_cubic_mf_reconstruction.tex`, `curved_gauge_comparison.tex`, `artin_residual_mf_comparison.tex`（すべてpapers/reconstruction）。非正則底の絶対特異圏と相対特異圏、perfectと全coherentを区別する。既存比較の全証明を今回独立再監査したわけではない。generic生成性・代数的圏同値は未完成。

**4. 有限代数的積分。** 代数的な勾配空間が完成底で滑らかな形式三次式の勾配空間なら、任意の有限jetを保って局所代数的に積分できる。DVR核飽和・Euler積分・可換候補の判別式に証明と実装がある。`finite_algebraic_recovery.tex`, `computations/finite_recovery.py`。人工可換候補の検算は非可換Natの計算ではない。

**5. 実非可換入力の正則な有限対角積。** lambda=1の混合中心対の閉行列と全16合成をQ[h]_(h)上で構成した。H^0のrank4,6、四境界と六合成の小行列式はh=0で-3。局所自由性により低次数コホモロジーと積は全Artin切断・完備化と両立する。核の積分は

`G_h=(x^3+y^3+z^3)/3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^12/4374)u^3`。

五変数にはv^3を加える。勾配変換の行列式は1+h^6/27。保存行列455種類の係数の分母lcmは `(h^3-1)(h^6+162)` であり、圏のsmoothness判別式ではない。証明は `curved_diagonal_recovery.tex`, `regular_diagonal_recovery.tex`、計算は `verify_regular_diagonal.py`。全次数Koszul/PBW完全性は依存結果である。

**6. 乗法的bar比較。** 有界同次射影対角とbarのspecial deformation retractionを入力に、有限対角のYoneda積と有限支持Hochschild cup積を同定する証明を得た。写像は `Q(a)=epsilon_P a Pi`。逆向きJの乗法性の差は `-d(Pi R_phi H R_psi I)`。曲率HPL、bar長の完備化とarity直和の両立、別の有限曲率化との共役を明記する。有限arity共役がdg Lie同型を与えるという既存補題だけからcup保存を推論していない。

**7. MFへの写像と残る(BC)。** 有限支持brace挿入により、実際のgraded MFの内部shift付き導来自然変換への乗法的characteristic写像Thetaを構成する。次数一・二に必要なarityは高々2,4。標的の全Artin底上のH^0が自由rank5,10で、自然な特殊化が体上のNatと同定されThetaに両立する条件(BC)を確認できれば、単元行列式でTheta_1,Theta_2の同型性が従う。**(BC)は本研究の族で未確認。従ってactual Nat同定は未完成。** 全文は `papers/reconstruction/multiplicative_bar_comparison.tex`。

**8. 計算済み候補の代数的正規形。** q=h^6、u=a(q)U+h^2b(q)Z、z=h^4c(q)U+d(q)Zにより候補G_h+v^3を `(x^3+y^3+Z^3)/3+U^3+v^3+L(q)Uxy+h^2C(q)Zxy` へ移す。a,b,c,dの四代数方程式の初期Jacobianは9、初期値は(1,1/36,25/432,1)。`L=1+127q/5184+O(q^2)`、`C=13/36+1613q/1679616+O(q^2)`。指定局所解はetale近傍で代数的。この係数は候補Gの値であり、(BC)未確認のままformalityのW_hの係数と同定しない。

## 未解決の核心と次の具体的着手

1. **標的側の相対kernel/sectorと(BC)を第一優先。** 既存の形式MF同値で標的を可換形式cubicへ移し、Artin底上の対角kernel模型を構成する。gradient Koszulの相対完全性、恒等sectorのrank5,10、非恒等sectorの次数、自然な剰余写像とThetaとの両立を確認する。体上のBFK/Lin--Zhang公式や導来Homの底変更を、そのままH^0底変更の証明にしない。
2. **形式模型との全次数比較。** (BC)が全切断で両立すれば、GとWの低積・勾配空間の同定とsymmetrizer三乗根により形式線形同値を得る。現在は条件付き。有限対角bar比較の同次分裂入力と既存形式MF/残余比較の依存箇所も監査する。
3. **generic圏同値。** 指定生成子の像、有限cone/retract、同値双加群の代数性を調べる。SM（相対対角perfect性）・ER（etale実現）は別経路として維持する。全Artinのsmoothness・生成性だけではgenericへ進めない。
4. **範囲拡大。** 一般lambdaの絶対式、lambda^3=-12の高次項は比較の検査に役立つ範囲で扱う。相対対角では中心g(u)が消えるため、u^3係数を相対式から補作しない。

方針変更の理由は、有限対角から有限支持cup積への乗法性とMFへの写像を明示できたためである。元の目標のうち中間行列の極・有限積分・最初の乗法比較は処理したが、actual Natでの同型性とgeneric復元は残る。GHLRの包絡代数上の第二種理論とtwisted bimodule理論の全面同一視を先取りせず、必要な低次数条件を直接調べる。

## 保持する成果・障害・先行研究

混合族の二次式 `F_lambda+h^2(xyz/3-lambda^2u^2z/12)`、Jacobian類 `(1/3+lambda^3/36)[xyz]`、全Artin PBW・指定中心閉式、有限群による `F_{lambda_*(h^6)}+h^2c_*(h^6)xyz` 正規形を保持する。新しいL,Cは計算済みlambda=1候補の値に限る。中心元の単純な可換化と復元式を混同しない。

低次数Jacobian復元・射影的一意性、積分不能な正しいHilbert級数の例、純Poisson一次消滅、分離Hessian模型、非楕円fivefoldの節点・尖点成分と35係数slice、A∞arity制約、有限bar対角・SM/ER、全Artin smoothでもgeneric非smoothなdg反例を保持する。詳細は既存論文C、`notes/reconstruction.md`, `notes/research_notes.md`。反例を指定nc cubic Gammaの反例としない。

Kontsevich、Dito、Shoikhet、Caldararu--Tu、Tu、Chenの既知入力と本稿の比較を区別する。新節ではNegron arXiv:1304.0527v4 Thm5.3、Tu arXiv:1009.4151v2 Appendix A Lemma A.1、Lowen arXiv:0707.2602 Prop3.11/3.13、GHLR arXiv:2312.16645v5 Thm4.7/6.14, Rem6.16、Lin--Zhang arXiv:2310.09927v2 Thm3.5/Rem3.6を一次資料で確認した。詳細参照は新節のbibliography。既知のcap/HPL/brace原理そのものの新規性を主張しない。包括的新規性調査・外部査読・形式証明は未完了。

## 検証・再開

`python3 computations/verify_bar_comparison.py --output build/bar_comparison_certificate.json` で曲率144件、cap微分288件、cap積360件、乗法性ホモトピー30件、候補の直接代入・Jacobian9・係数を厳密検算する。追跡証明書とJSON比較する。`latexmk papers/multiplicative_bar_comparison.tex` で単独稿を生成する。一般の無限bar証明やcategorical Natの計算とは区別する。

正則対角の全行列は `python3 computations/verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json`、監査は `scripts/verify_regular_assets.py`。その既存証明書・コードを保持し、今回全行列を再実行したとは扱わない。各原稿と計算の正確な状態はvalidation.jsonに記載する。論文A/B/C全体の現行再組版と全既存計算の再実行は未実施。

## 研究一般の原則と保存規則

この節は研究固有の計画とは別の一般原則である。

1. 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して研究価値を最大化する。方針変更は現行の理由・達成点・残る問題として整理し、履歴を蓄積しない。
2. 証明済み、条件付き、未完成、予想、計算的観察を分け、仮定・依存・証明所在を示す。証明の記載、今回の監査、計算、外部査読・形式検証を区別する。誤りは依存する記述も修正する。
3. 重要な先行研究は一次資料を確認し、未確認の内容・書誌・新規性を補作しない。外部PDFや検索結果を大量収録しない。
4. 公表価値ある成果と十分な証明を日本語LuaLaTeXで保持する。ノートは知識・反例・障害を整理し、作業日誌や重複証明にしない。
5. **研究の区切りに承認を求めず、方針・ノート・論文全文・コード・必要な証明書・再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保ち、force push・無断PR・GitHub Actionsを使わない。refと主要blobを照合する。
6. **Library保存はGitHub反映が実際に失敗した場合のみの緊急避難。** 通常は二重保存しない。未同期と復帰方法を明記し、既存Libraryファイルは無断削除しない。
7. 最新一式だけで再開できる構成とし、旧ZIP・旧稿・ログ・キャッシュ・重複を追加しない。価値ある数学・証明・再現性を容量制限のため削らない。独立境界研究・未照合原PDFはnc-cubic2、Reye研究はreyeに保全。
8. 日付・版・参照を揃え、生成・計算・組版・保存・遠隔確認を別々に報告する。PDFはGit追跡せずlatexmkでbuild/へ生成する。
