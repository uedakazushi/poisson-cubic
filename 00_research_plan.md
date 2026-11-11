# 研究方針：非可換cubicの一般点復元

**2026年11月11日 / v35。最初に本ファイルを読む。GitHub `uedakazushi/nc-cubic` の `main` が唯一の正本。**
次は `notes/rotation_orbit_generic_reconstruction.md`。具体式は `notes/curved_diagonal.md`、形式比較は `notes/geometric_rotation_basechange.md`、より強い完備底の条件は `notes/one_sided_morita.md`。一般背景は論文A/B/Cと `notes/research_notes.md`。旧ZIP・会話・Libraryを再開条件にしない。

## 最終目標と現在の達成範囲

構成した代数的nc cubicの幾何学的一般点について、可換cubicのKuznetsov成分と指定rotationを復元する。存在、方程式の明示化、同値核の明示化を区別する。線束生成残余圏K^linと全coherent残余圏を同一視しない。

**現在の統合定理：既存入力(L),(CF)を満たす一変数量子化のK^linは、有限拡大K'/C(h)上で滑らかな可換cubicのKuとrotation付き同値となる。** (L)は代数的局所proper/window模型とそのHom底変更、(CF)は次数別完備底上の実際の有限rank MF A∞同値。単なる両立Artin同値列ではない。この二つは既存本文に証明がある入力であり、今回全証明を独立再監査したという意味ではない。

lambda=1の混合族では既存(D)の有限対角・乗法的低積比較も用い、復元先を計算済みの多項式G_h+v^3に固定できる。**一般点のcompact逆核の存在は新しい軌道生成の証明から従い、追加の未確認仮定として残さない。** 一方、完備底全体のcompact逆核、h=0を含むetale同値、同値行列や有限拡大の次数は未構成である。

## 最短の証明経路

### 存在の経路

1. K_R=stab(R)、T_R=K_R⊕K_R(1)⊕K_R(2)を取る。局所windowの三角的filtrationによりT_RはK^linの代数的生成対象で、Gamma_R=REnd(T_R)はR-proper。全MFの完備底生成性はここで仮定しない。
2. (CF)をこの固定三対象へ制限する。固定Hom次数は有限自由な斉次成分なので形式的Taylor写像は通常のRhat-multilinear写像になる。先にhを反転してL=C((h))へ移す。
3. E=Phi(K_Rhat)の一般点が非零であることをEuler形式で示す。special stabilizationのベクトルは chi_r=Σ_(s+r=0 mod3)(-1)^s binom(N,s)。二乗和2*3^(N-1)は非零。五変数は(-9,9,0)。proper性により特殊・一般でEuler不変。
4. 孤立斉次超曲面の非零graded MFの全次数シフト軌道は生成する。Stevensonの非次数付き分類を、次数の再付与R(U(E))=⊕E(j)とcompact局所化でgradedへ戻す。三次ならE,E(1),E(2)で足りる。これでLaurent体上の像が可換MF全体になる。
5. 体上で得た逆核は片側perfect、可換側smoothnessで包絡代数上compact。Toën–Vaquiéの降下で有限生成C(h)部分代数へ移し、単位・余単位・rotationのconeを非空開で消して閉点を取る。有限代数拡大上の同値を得る。

全文は `papers/reconstruction/rotation_orbit_generic_reconstruction.tex`。rog:thm:orbit、rog:prop:euler、rog:lem:localization、rog:thm:laurent、rog:thm:geometric-generic。

### 明示式の経路

可換側のprojected kernelによる全Artin低Nat底変更と(D)により、計算済み式とW_hを形式GL同型で同定する。この線形変換はL上の通常の変換となる。Gを固定したまま有限体拡大へ降下する。証明はrog:cor:mixed。

従って一般(KF)、完備底全体の逆核、Popescuによる特殊点を含む代数化は、現在のgeneric存在証明の先行条件ではない。これらの有効な結果は、より強い相対同値を目指す別経路として保持する。Artinでの生成性を完備底へ持ち上げる反例と矛盾しない。

## 既存成果の保持と依存

論文A：一般n>=3のPoisson正規形、Jacobianブロック、各固定Poisson方向の代数的量子化。全係数方向の一様相対量子化・全モジュライ分類とは別。
論文B：41次元中心三次対、17係数slice、ambient復元、分離型余次元15、忘却接写像の核7。全nc cubic分類とは言わない。

論文C：形式MF/相対window、有限積分、正則有限対角の全16積、bar/cup/characteristic比較、幾何学的低Nat底変更、片側Morita/Popescu判定を保持する。今回(L)の三つのwindow像と(CF)のcomplete-graded corollaryの使用箇所を点検したが、旧本文と計算全件の独立再検証は未実施。

混合lambda=1の式は
`G_h+v^3=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^12/4374)u^3`。
勾配変換の行列式1+h^6/27、正則行列分母(h^3-1)(h^6+162)、正規形L=1+127q/5184+O(q^2)、C=13/36+1613q/1679616+O(q^2)、q=h^6を保持する。行列分母をsmoothness判別式とみなさない。

相対sector、対角unit、中心対称性、純Poisson一次消滅、分離Hessian、非楕円fivefold、35係数slice、A∞arity、SM/ER、生成子退化と非K-flat性の反例を保持する。新しい一般点の証明は非零性とrotation軌道を使い、項別自由性だけの生成性持上げを復活させない。

## 次の優先課題

1. **統合定理の独立監査。** (L)のregular底windowとproper/Hom底変更、(CF)の曲率formalityとcomplete-graded functor、明示式への(D)を順に再点検し、今回のLaurent局所化と整合することを確認する。新原稿の証明があることと、依存全部の独立監査を区別する。
2. **同値の有効化。** 三シフト生成の有限cellを、明示的混合cubicで求める。得られた逆核の行列・有限拡大次数を計算する。存在の有限表示性だけから計算済みとは言わない。
3. **範囲の拡張。** 一般lambdaの明示式、独立中心vのない成分、同時に全係数を動かす多変数基底、K^linと全coherent残余圏との一致を調べる。一変数量子化の結果から全モジュライ一般点の統一定理を無条件に主張しない。
4. 特殊点h=0を含む相対同値が必要なら、保持した片側compact形式核/Popescu/SM経路を使う。今回の有限体拡大降下は元の形式分枝全体の再現ではない。

## 検証と再現

Stevenson arXiv:1105.4698v3 Thm6.13、Dyckerhoff 0904.4713v5 §2.4/§5.6、Stacks09SM/00FV、Toën–Vaquié math/0503269v5 Lemmas2.8/2.10を一次資料で確認。既知分類とMorita原理の新規性は主張しない。包括的新規性調査・外部査読・形式証明は未実施。

`python3 scripts/verify_rotation_orbit_assets.py` は本文の参照・Cへの統合と、64個のEulerベクトル、混合special cubicの32×32行列による41恒等式の証明書を再生成する。generic核の行列や旧nc全行列の検証ではない。
`latexmk papers/rotation_orbit_generic_reconstruction.tex`。単独稿を7頁に組版・表示確認した。A/B/C現行全体の再組版と既存全計算の再実行は未実施。生成・証明点検・計算・組版・pushはvalidation.jsonで分離する。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の一般原則である。
1. 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して価値を最大化する。方針は現在有効な理由・到達点・残る問題として書き直し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算観察を区別し、仮定・依存・証明所在を明記する。記載、今回の監査、計算、外部査読、形式証明を分け、誤りは依存する記述も修正する。
3. 重要文献は一次資料を確認し、未確認の内容・書誌・新規性を補作しない。外部PDFや検索結果を大量収録しない。
4. 価値ある数学と証明全文を日本語LuaLaTeXで保持する。ノートは有効な知識・例・反例・障害を整理し、作業日誌や重複証明にしない。
5. **研究の区切りに承認を求めず、方針・ノート・論文全文・コード・必要な証明書・再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保持し、force push・無断PR・GitHub Actionsは禁止。refと変更blobを照合する。
6. **Library保存は実際のGitHub反映失敗時のみの緊急避難。** 未同期と復帰手順を明示し、既存Libraryファイルを無断削除しない。
7. 最新一式だけで再開できる構成とし、旧ZIP・旧稿・ログ・cache・重複を追加しない。数学と検証可能性を固定容量のため削らない。独立境界/未照合PDFはnc-cubic2、Reyeはreyeに保全。
8. 日付・版・参照を整合させ、生成・計算・組版・保存・遠隔確認を別々に報告する。PDFはGit追跡せずlatexmkでbuild/へ生成する。
