# 研究方針：cubicのPoisson構造・量子化・可換復元

**2026年11月11日・v27。再開時は最初に本ファイルを読む。**

## 正本・目標・達成基準

GitHub `uedakazushi/nc-cubic` の `main` を唯一の正本とする。次に `notes/curved_diagonal.md`、`notes/finite_algebraic_recovery.md`、一般背景の `notes/research_notes.md`、論文Cを読む。会話・旧ZIP・Libraryを再開の前提にしない。

最優先目標は、構成した代数的な非可換cubicの幾何学的一般ファイバーを、同じKuznetsov成分と指定rotationを持つ滑らかな可換cubicとして実現すること。元の可換cubicへの復元や、全パラメータに一価の有理公式があることは要求しない。任意のAS-regular中心三次商の全点復元にはrotation付き反例があり、その範囲へ広げない。

直接経路は `(A_h,Omega_h) -> 実際の低rotation積 -> その核K_h -> 可換三次式G_h`。formalityの特定の無限級数自体の代数性・収束を先行条件にせず、形式復元は完成底での比較・可積分性の保証に使う。方程式抽出とgenericな圏同値は別の達成基準である。

## 現在の主要な到達点

**1. Poisson・量子化（論文A）。** n≥3の滑らかなcubicのJacobian三変数ブロック正規形・一般階数、各固定Poisson構造の代数的量子化には証明本文がある。`papers/sections/poisson_geometry.tex` の `thm:pg-normal`, `thm:pg-quantization`。全係数方向を保つ一様相対量子化、全モジュライ成分・交叉の完全分類とは区別する。

**2. 17次元族（論文B）。** 41次元中心三次対、17係数slice、ambient復元、分離型の余次元15、忘却接写像の核7を保持する。`papers/generic17_ambient_recovery.tex`。構成した族の商の次元であって全nc cubic分類ではない。

**3. 形式MF復元・Artin残余比較（論文C）。** 一般斉次中心三次形式変形からW_hと定数trivectorを構成し、全有限Artinおよび次数別完備有限rank MFへ比較する証明を保持する。`formal_cubic_mf_reconstruction.tex`, `curved_gauge_comparison.tex`, `artin_residual_mf_comparison.tex`（すべてpapers/reconstruction）。非正則底の絶対特異圏と相対特異圏、perfectと全coherentを区別する。generic生成性・代数的圏同値は未完成。

**4. 有限代数的積分。** 代数的な勾配空間が完成底で滑らかな形式三次式の勾配空間なら、任意の有限jetを保って局所代数的に積分できる。DVR核飽和・Euler積分・可換候補の判別式に証明と実装がある。`finite_algebraic_recovery.tex`, `computations/finite_recovery.py`。人工可換候補の検算は非可換Natの計算ではない。

**5. 実非可換入力の正則な有限対角積。** λ=1の混合中心対について、曲率付き絶対対角の閉行列と全16合成を `Q[h]_(h)` 上で構成した。H⁰のrankは4,6、四境界と六合成の小行列式はh=0で−3。局所自由性により低次数コホモロジーと積は全Artin切断・完備化と両立する。正則化後も核の積分は

`G_h=(x³+y³+z³)/3+h²xyz/3+(1+h⁶/54)uxy−h⁴uz²/18−h²u²z/12+(1+29h⁶/648+h¹²/4374)u³`。

五変数にはv³を加える。勾配変換の行列式は1+h⁶/27。保存行列の455種類の係数の分母lcmは `(h³−1)(h⁶+162)`。この分母を圏のsmoothness判別式と解釈しない。

証明全文は `curved_diagonal_recovery.tex`, `regular_diagonal_recovery.tex`、検算は `computations/verify_regular_diagonal.py`。既存Koszul分解の全次数完全性は依存結果であり、有限次数計算で置換しない。**この積をactual Natまたは指定形式模型W_hの積と同定する比較は未証明。**

**6. 比較に使える有限arity補題。** F,F⁻¹のarityが有界なら、共役は有限支持Hochschild cochainsのdg Lie同型になる。arity上界はL_G(L_F+M−1)。`regular_diagonal_recovery.tex` の `rd:lem:bounded-conjugation`。これだけではcup積保存は従わない。

## 未解決の核心と次の具体的着手

1. **乗法的bar比較を第一優先。** 一入力を標識したbar双加群の比較を構成し、有限対角のYoneda積とcompactly supported Hochschild cup積を同定する。有限arity共役補題と正則な閉行列を入力に使う。形式的dg Lie同型からcup積保存を飛躍させない。
2. **実際のrotation積との比較。** 内部shift・三次周期性・同変化と非恒等sectorを明示し、前項の積を残余dg圏の導来自然変換に移す。GHLRの異なる第二種Hochschild理論を名称だけで同一視しない。包絡代数・外積・対角対象に関する条件を個別に確認する。
3. **generic圏同値。** 比較後、指定生成子の像、有限cone/retract、同値双加群の代数性を調べる。SM（相対対角perfect性）・ER（étale実現）は別経路として維持する。全Artinでのsmoothness・生成性だけからgenericへの結論を出さない。
4. **具体式の範囲拡大。** 一般λの絶対式と二つの形式級数の係数は、比較の検査に役立つ範囲で計算する。相対対角では中心g(u)が消えるため、u³係数を相対結果から補作しない。

方針の重点は、高次級数の逐次計算よりも、実際の有限積とその乗法的比較にある。形式復元・有限積分は得られたが、actual Nat比較とgeneric復元という元の目標の核心は残っている。中間行列のh=0での極は、現在の正則模型では解消した。

## 保持する成果・障害・文献

混合族の二次式 `F_lambda+h²(xyz/3−lambda²u²z/12)`、Jacobian類 `(1/3+lambda³/36)[xyz]`、全Artin PBW・指定中心閉式、有限群による `F_{lambda_*(h⁶)}+h²c_*(h⁶)xyz` 正規形を保持する。h⁶のlambda係数、h⁸のxyz係数、lambda³=−12での高次消滅は未決定。中心元の単純な可換化と復元式を混同しない。

低次数Jacobian復元・射影的一意性、積分不能な正しいHilbert級数の例、純Poisson方向の一次消滅、分離Hessian模型、非楕円fivefoldの節点・尖点成分と35係数slice、A∞arity制約、有限bar対角・SM/ER、全Artin smoothでもgeneric非smoothなdg反例を削除しない。詳細は既存論文Cと `notes/reconstruction.md`, `notes/research_notes.md`。反例を本研究の指定Γの反例と同一視しない。

Kontsevich、Dito、Shoikhet、Căldăraru–Tu、Tu、Chen等の既知入力と本文の比較を区別する。現在のbar比較にはGuan–Holstein–Lazarev–Rasmussen arXiv:2312.16645v5（Theorems4.7,6.14、Remark6.16）、Polishchuk–Positselski arXiv:1010.0982v2（§§3.3,3.5）を参照する。適用条件の確認は未完成。包括的新規性調査・外部査読・形式検証は未完了。

## 検証・再開

`python3 computations/verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json` で全有限行列を再生成する。追跡証明書とJSONとして比較する。大きい全行列はcanonical JSON SHA256で照合できる。`latexmk papers/curved_diagonal_recovery.tex` で単独原稿を生成する。

今回、局所正則化・全合成・rank・積分を厳密計算し、既存finite_recovery証明書も再実行して一致を確認した。単独原稿は10頁に組版・全頁表示確認済み。論文A/B/C全体の現行版再組版・全既存計算の再実行は未実施。各状態はvalidation.jsonに分離して記す。

## 研究一般の原則と保存規則

この節は本研究固有の計画ではなく一般原則である。

1. 数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更は現行の理由・達成点・残る問題として整理し、履歴を蓄積しない。
2. 証明済み、条件付き、未完成、予想、計算的観察を分け、仮定・依存・証明所在を示す。証明の記載、今回の監査、計算、外部査読・形式検証を区別する。誤りは依存する記述も修正する。
3. 先行研究の重要な主張は一次資料で確認し、未確認の内容・書誌・新規性を補作しない。文献PDFを大量収録しない。
4. 公表価値のある成果と十分な証明を日本語LuaLaTeXで保持する。ノートは有効な知識・反例・障害を整理し、作業日誌や重複証明にしない。
5. **研究の区切りごとに承認を求めず、方針・ノート・論文全文・コード・必要な証明書・再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保ち、force push・無断PR・GitHub Actionsを使わない。remote refと主要blobを照合する。
6. **このプロジェクトではLibrary保存はGitHub反映が実際に失敗した場合のみの緊急避難とする。** 通常は二重保存しない。失敗時は未同期と復帰方法を明示し、既存Libraryファイルは無断削除しない。
7. 最新一式から再開できる構成とし、旧ZIP・旧稿・ログ・キャッシュ・重複を追加しない。有効な数学・証明・再現性を容量制限のために削らない。独立境界研究と未照合原PDFはnc-cubic2、Reye研究はreyeに保全されている。
8. 日付・版・参照を揃え、生成・計算・組版・保存・遠隔確認を別々に報告する。PDFはGit追跡せず、latexmkでbuild/へ生成する。
