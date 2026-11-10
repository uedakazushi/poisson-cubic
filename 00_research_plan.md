# 研究方針：非可換cubicの有限代数的復元

**2026年11月11日 / v33。再開時は最初に読む。正本は GitHub `uedakazushi/nc-cubic` の `main`。**
次に `notes/geometric_rotation_basechange.md`、必要に応じて `notes/curved_diagonal.md`、`notes/bar_comparison.md`、`notes/finite_algebraic_recovery.md` を読む。一般背景は `notes/research_notes.md` と論文A/B/C。旧ZIP・会話・Libraryを再開の前提にしない。

## 最終目標と達成基準

構成した代数的な非可換cubicの幾何学的一般ファイバーを、同じKuznetsov成分と指定rotationを持つ滑らかな可換cubicとして実現する。一般次元n>=3、各対象Poisson成分の一般点という目標を保持する。元の可換cubicを固定して復元する必要はなく、全域で一価の有理公式も要求しない。全AS-regular中心三次商の全点復元への拡張は対象外。

達成基準を三つに分ける。
1. 入力の代数的関係式から復元三次式を有限代数計算で得る。
2. その式が全Artin切断で実際のrotation付き残余pairの復元先となることを示す。
3. 非零の一般パラメータにおける代数的な同値双加群・逆・rotation比較を構成する。
第2段階から第3段階を自動的に結論しない。

## 現在選ぶ最短経路

**有限代数的抽出という方針は維持し、標的Natの処理は幾何学的射影核へ切り替える。一般の相対MF核全忠実性(KF)を先行課題にしない。**

既存の形式MF復元とArtin残余比較によって標的は可換cubicのperfect Kuznetsov成分になる。その相対射影核Pとrotation核Qから `Rq_* RHom(P,Q^{*r})` を作れば、これは真の導来Natを計算するperfect複体で、任意の導来底変更に両立する。Toënの相対Morita定理（基底環は任意の可換環）とproper perfect直接像を使う。

座標切断がId→rhoの特殊基底を閉元として持ち上げ、その合成がr=2の特殊基底を持ち上げる。H^(-1)特殊群の消滅だけでH^0の自由性・自然なArtin底変更が従う。H^1の消滅、独立中心v、有限群対称性は不要。一般N>=5の滑らかな可換cubic族についてrankはN,binom(N,2)。**この可換幾何学的定理は追加の(KF)仮定を持たない。**

証明全文：`papers/reconstruction/geometric_rotation_basechange.tex`、単独入口：`papers/geometric_rotation_basechange.tex`。gr:thm:perfect-target、gr:lem:lifts、gr:thm:bc。

非可換への適用では、既存の(F)全Artin残余pair同値と、(D)正則有限対角・乗法的characteristic写像を明示的に入力する。これらの既存証明を全部独立再監査したとは主張しない。この入力下で(BC)は充足し、lambda=1で計算したG_h+v^3と形式W_hは恒等に近い形式線形変換で同型となる（gr:cor:nc、gr:cor:formal-polynomial）。**generic圏同値は未証明。**

### 他の経路を先行させない理由

- 一般(KF)・非正則底の全bar理論：必要な低次数標的は上のperfect核で既に処理できるため、最終目標の前提としては過剰。
- formalityの無限級数そのものの代数性：代数的Gが既にあり、形式比較を得れば方程式側には不要。
- 抽象的な圏同値の代数化：smoothness・有限表示・一様な逆双加群が未確認のまま使うと循環する。
- SM/ER：有効な別経路として保持するが、方程式抽出の先行条件にしない。

## 主要な到達点と保持する数学

**論文A**：一般n>=3のPoisson三変数Jacobianブロック正規形、一般階数、各固定Poisson構造の代数的量子化。`papers/sections/poisson_geometry.tex` の thm:pg-normal/thm:pg-quantization。全係数方向を同時に保つ相対量子化・全モジュライ成分分類とは別。

**論文B**：41次元中心三次対、17係数slice、ambient復元、分離型余次元15、忘却接写像の核7。全nc cubic分類とは言わない。

**論文C**：形式MF復元、Artin相対window、二次星積、有限群同変正規形、有限積分、正則対角の全16積、乗法的bar比較を保持する。一般の特殊生成子持上げは項別自由性だけでは偽であり、反例を保持する。新節は、正の内部次数MFのHomがnilpotent HPLでR-perfectとなる点と、導来特殊化に対するcompact生成性を分けて点検する。旧一般補題を復活させない。

lambda=1の計算済み多項式は
`G_h+v^3=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^12/4374)u^3`。
勾配変換の行列式は `1+h^6/27`。正則行列の分母lcm `(h^3-1)(h^6+162)` を圏のsmoothness判別式と解釈しない。

四代数方程式による正規化はq=h^6、初期Jacobian9、`L=1+127q/5184+O(q^2)`、`C=13/36+1613q/1679616+O(q^2)`。新しい(F),(D)依存の形式同定の範囲で復元先の正規形として使える。個別のformality標識や高次係数の標準的一意性は主張しない。

低次数Jacobian復元、積分不能な完全交差、純Poisson一次消滅、分離Hessian比較、非楕円fivefold、35係数slice、A∞arity、有限bar対角、SM/ER、全Artin smoothでもgeneric非smoothな反例を保持する。独立中心対称性の障害消滅も有効だが、可換標的のBCには不要になった。

## 未解決の核心と次の着手

**第一優先：代数的な有限Morita証明書。** 指定した代数的残余生成子Gamma_Rと可換Y_Gの生成子を固定し、両者の双加群P,Q、両合成の単位・余単位、rotation intertwinerを有限cell/retractで同時に表す。まず既存の形式MF同値が指定生成子へ与える像と有限Homを追跡し、Artin次数に依存しないcell数・shift・高次積の上界を求める。これを有限代数方程式に落とす。各切断で別々の有限式があるだけでは不足。

次にそのデータを一般点へ広げ、生成性と逆性を検査する。非可換側の相対対角perfect性が先に得られるならSM/ERまたはsmooth proper dg代数の有限A_n決定性を使えるが、smoothnessを先取りしない。

一般lambda・独立中心変数を持たない成分・高次元各成分の具体抽出も残る。新しい幾何学的BCは全N>=5に適用できるが、一般の非可換有限積の実計算を自動的に与えない。

## 証明・計算・再現の状態

今回新規に書いて点検したのは射影核、閉基底持上げ、全Artin BCと既存入力下の形式同定の証明。一次資料はToën §2/Thms8.9,8.15、Stacks0B91、BFK5.39、Lin–Zhang2024 Thm3.5/Rem3.6/§5、Lin–Zhang2026 §2.1。Morita原理の新規性は主張しない。包括的新規性調査・外部査読・形式証明は未実施。

`python3 computations/verify_geometric_rotation.py --output build/geometric_rotation_certificate.json` はsector算術56例、有限自由複体のArtin例15件、閉持上げがない反例を厳密検算する。カテゴリカルな定理や非可換全行列の計算ではない。`python3 scripts/verify_geometric_rotation_assets.py` が本文・証明書・主論文統合を点検する。

`latexmk papers/geometric_rotation_basechange.tex` で単独原稿を生成する。現行A/B/C全体の再組版・既存全計算の再実行は未実施。詳細状態はvalidation.json。既存コードと証明書は変更せず保持する。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の一般原則である。
1. 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して研究価値を最大化する。方針は現行の理由・達成点・残る問題として書き直し、変更履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算観察を区別し、仮定・依存・証明所在を明記する。証明の記載・今回の監査・計算・外部査読・形式証明を区別し、誤りは依存する記述も訂正する。
3. 重要文献は一次資料を確認し、未確認の内容・書誌・新規性を推測しない。外部PDFや検索結果を大量収録しない。
4. 価値ある数学と証明全文を日本語LuaLaTeXで保持する。ノートは有効な着想・例・反例・障害を整理し、作業日誌や重複証明にしない。
5. **研究の区切りに承認を求めず、方針・ノート・論文全文・コード・必要な証明書・再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保持し、force push・無断PR・GitHub Actionsを使わない。反映後refと主要blobを照合する。
6. **このプロジェクトのLibrary保存はGitHub反映が実際に失敗した場合のみの緊急避難。** 未同期と復帰手順を明示し、既存Libraryファイルを無断削除しない。
7. 最新一式で再開できる構成とし、旧ZIP・旧稿・ログ・cache・重複物を追加しない。数学・証明・検証可能性を固定容量のため削らない。独立境界研究/未照合PDFはnc-cubic2、Reyeはreyeに保全。
8. 日付・版・参照を揃える。生成・計算・組版・保存・遠隔確認は別々に報告する。PDFはGit追跡せずlatexmkでbuild/へ生成する。
