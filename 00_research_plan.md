# 研究方針：非可換cubicの有限代数的復元

**2026年11月11日 / v34。再開時は最初に読む。GitHub `uedakazushi/nc-cubic` の `main` が唯一の正本。**
次に `notes/one_sided_morita.md`、`notes/geometric_rotation_basechange.md` を読む。有限計算の詳細は `notes/curved_diagonal.md`、`notes/bar_comparison.md`、`notes/finite_algebraic_recovery.md`。一般背景は `notes/research_notes.md` と論文A/B/C。会話・旧ZIP・Libraryを再開の前提にしない。

## 最終目標と達成基準

構成した代数的nc cubicの幾何学的一般点を、同じKuznetsov成分と指定rotationを持つ滑らかな可換cubicとして実現する。一般n>=3と対象Poisson成分の一般点という目標を保持する。元の可換cubicや全域一価の有理公式は要求しない。任意のAS-regular中心三次商の全点復元とは区別する。

達成基準は、(1)代数的関係からの有限方程式抽出、(2)全Artin切断での実際の残余pairとの比較、(3)幾何学的一般点の代数的同値である。(2)から(3)を自動的に推論しない。

## 現在の最短経路

有限代数的抽出と可換側の幾何学的射影核による(BC)処理を維持する。一般MF核全忠実性(KF)には戻らない。generic段階では、**双方向の核と全逆性を同時に未知量とする代わりに、可換側からnc側への一つのcompact核を作る**。

Cを可換Kuのsmooth proper生成代数、Gammaをnc残余のproper生成代数とする。C,Gammaは周囲の次数付き代数A,Bとは別物。右Gamma-perfectな(C,Gamma)-双加群Pが特殊点で同値を与えるなら、局所底上でも同値となる。逆はQ=RHom_Gamma(P,Gamma)。CのsmoothnessからQは右C-perfect、単位・余単位のconeは底上perfectなので特殊点での消滅から消える。Gammaのsmoothnessは仮定でなく結論。証明：`os:thm:local`。

さらにRがNoether局所G-ringで、通常の導来双加群圏に完備底上のP_hatがあり、右Gamma_hat-perfectで、特殊同値とrotation射を持てば、任意の有限jetを保つetale代数化が得られる。Cのsmoothnessで包絡代数上compactにし、Popescuとperfect加群のfiltered-colimit降下を使う。有限型既約基底では幾何学的一般点の同値が従う。証明：`os:thm:algebraization`, `os:cor:generic`。

**本混合族でP_hatの通常導来圏への実現と右Gamma_hat-perfect性は未証明。** Artin各段階のperfect性、固定rankの自由MF、底上perfectなHomだけでは不足。左C_hat作用とrotationのcoherenceも必要である。新定理をこの入力の構成済みと読み替えない。

一般原理はToën–Vaquié Lemmas2.8,2.10、perfect Nakayama、Popescuに基づく。新規性を主張するのでなく、最終目標に必要な独立の構成を減らす判定として用いる。全文：`papers/reconstruction/one_sided_morita_algebraization.tex`。

## 主要な到達点と依存

**論文A。** n>=3のPoisson三変数Jacobianブロック正規形、一般階数、各固定Poisson構造の代数的量子化。`papers/sections/poisson_geometry.tex` のthm:pg-normal/thm:pg-quantization。全係数方向の一様相対量子化・全モジュライ分類とは別。

**論文B。** 41次元中心三次対、17係数slice、ambient復元、分離型余次元15、忘却接写像の核7。構成した族の商の次元であり、全nc cubic分類とは言わない。

**論文Cの形式比較。** (F)全Artin形式MF/残余window同値と、(D)正則有限対角/乗法的characteristic写像を入力する。可換側のprojected kernel Homはperfectで、座標切断と合成の閉基底持上げにより全Artin低Nat底変更が成立する。N>=5でrankN,binom(N,2)。独立v・対称性・H1消滅・一般KFは不要。`geometric_rotation_basechange.tex`のgr:thm:bc。この幾何学的定理と、ncへの(F),(D)依存を区別する。既存全証明を今回独立再監査したとはしない。

lambda=1の計算済み式は
`G_h+v^3=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^12/4374)u^3`。
(F),(D)下でW_hと形式GL5同型。勾配変換の行列式は1+h^6/27、正則行列の分母lcmは(h^3-1)(h^6+162)。この分母は圏のsmoothness判別式ではない。四代数方程式の正規化はq=h^6、初期Jacobian9、L=1+127q/5184+O(q^2)、C=13/36+1613q/1679616+O(q^2)。標準的なformality係数の一意性は主張しない。

有限積分、全16積、bar/cup比較、相対sector、対角unit、中心対称性、純Poisson一次消滅、分離Hessian、非楕円fivefold、35係数slice、A∞arity、SM/ERは保持する。通常の自己Extの次数制約だけで高次A∞演算は有限arityにならない。項別自由性だけの生成子持上げは偽であり、二周期反例を保持する。全Artinでsmoothでもgeneric非smoothな反例も、ordinary compact核を構成する今回の必要条件を省略する理由にはならない。

## 未解決の核心と具体的着手

最優先は、明示的可換Y_Gの一つの生成子Hについて、全Artin同値の逆像P_mを同じ完備底上の双加群P_hatへ実現し、右Gamma_hat-perfectであることを示すこと。Gamma_hatの有限個のshiftのconeとretractによる一様な有限filtrationを追跡する。左C_hat作用とrotation射をその模型上で保つ。

これが得られれば、逆核、単位・余単位、generic生成性、etale代数化は新定理から従う。これらを独立して全て構成する旧十分条件を先行課題にしない。形式分枝全体の代数化を求めず、特殊同値と必要な有限jetの保存を使う。三次周期性はHH0(C/R)=Rを確認した場合、scalar根で補正できる。

一般lambda・独立中心vのない成分・高次元各成分の具体抽出は未完成。新しい一般判定がそれらの核を自動的に与えるとは言わない。SM/ERは別経路として維持し、nc側のsmoothnessを循環的に仮定しない。

## 検証と再現

新証明は片側smooth対角、随伴、perfect Nakayama、perfect加群降下、Popescuを用いる。Toën–Vaquié printed404–407、Stacks07GC,07M7,068Uを一次資料で確認した。包括的新規性調査・外部査読・形式証明は未実施。

`python3 scripts/verify_one_sided_morita_assets.py` は新本文の参照と主論文統合を点検し、通常のねじった行列代数の206恒等式、relation階数、period補正mod h^8、compact性反例の証明書を再生成する。nc cubicのP_hatを検証するコードではない。

`latexmk papers/one_sided_morita_algebraization.tex` で単独稿を生成する。新単独稿5頁を組版・全頁表示確認した。A/B/C全体の現行再組版、v27全行列と全旧計算の再実行は未実施。既存コード/証明書を保持し、正確な状態はvalidation.jsonで区別する。

## 研究一般の原則と保存許可

以下は本研究固有の計画とは別の一般原則である。
1. 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して研究価値を最大化する。方針は現在有効な理由・到達点・残る問題として書き直し、変更履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算観察を区別し、仮定・依存・証明所在を明記する。証明記載、今回の監査、計算、外部査読、形式証明を分け、誤りは依存する記述も修正する。
3. 重要文献は一次資料を確認し、未確認の内容・書誌・新規性を補作しない。外部PDFや検索結果を大量収録しない。
4. 価値ある数学と証明全文を日本語LuaLaTeXで保持する。ノートは有効な知識・例・反例・障害を整理し、作業日誌や重複証明にしない。
5. **研究の区切りに承認を求めず、方針・ノート・論文全文・コード・必要な証明書・再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保持し、force push・無断PR・GitHub Actionsは使わない。refと変更blobを照合する。
6. **このプロジェクトのLibrary保存は実際のGitHub反映失敗時のみの緊急避難。** 未同期と復帰手順を明示し、既存Libraryファイルを無断削除しない。
7. 最新一式だけで再開できる構成とし、旧ZIP・旧稿・ログ・cache・重複を追加しない。数学と検証可能性を固定容量のため削らない。独立境界/未照合PDFはnc-cubic2、Reyeはreyeに保全。
8. 日付・版・参照を整合させる。生成、計算、組版、保存、遠隔確認は別状態。PDFはGit追跡せずlatexmkでbuild/へ生成する。
