# 研究方針：Poisson三次超曲面の量子化とrotation付き可換復元

**2026-11-12 / v58。最初に読む。GitHub uedakazushi/nc-cubic のmainが正本。**
現行主原稿は論文A `papers/paper_a.tex`（A-v51）と論文B `papers/paper_b.tex`（B-v42）。

## 目標と達成基準

論文Aではsmooth cubicのPoisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduliを公表可能にする。論文Bでは代数的中心三次変形の一般点で、rotation付き全coherent残余圏を可換cubicから復元し、仮定・定義体・一意性・有効性を明確にする。原稿に証明があること、今回の論証点検、有限計算、組版、保存は区別する。包括的新規性調査と主要依存の全監査が終わるまでは投稿準備完了としない。

## 論文Bの主定理と確立した局所比較

次数別有限自由な代数的中心三次対、滑らかな可換特殊ファイバーを入力する。**局所proper/window比較(L)は追加仮定から外した。** `papers/support/papers/reconstruction/three_object_window.tex` の `tw:thm:window` が、線束生成残余圏を原点のstabilization K_Rの三つのshiftで表示し、proper Hom、剰余・完備化・分数体底変更、rotationと中心元に由来する三次周期比較を与える。一般点AS正則性も代数的入力から従う。

**残る比較条件は(CF_3)**：完備底上の固定三対象 K,K(1),K(2) を、ある滑らかな形式三次式のMF E,E(1),E(2)へ送る実際のunital A∞比較。全Hom複体・高次積・内部shift・周期比較を含む。全MF同値(CF)は十分条件として保持するが、主定理の最小入力ではない。この曲率付き比較の全独立監査は未完了である。

この条件の下で、元の体 K=C(h) 上のsmooth cubic模型 Y と、有限拡大K'/K上のrotation付き全coherent残余圏同値を得る。模型は全n>=3で幾何学的に一意。幾何学的一般点の任意の非零Mについて M⊕ρM⊕ρ²M の生成時間は2(n+2)(n+3)-1以下（BFKの既知結果）。方程式をK上に取れることと同値核のKへの降下は別である。h=0で正則な模型、特殊点込み同値、有限拡大次数、全モジュライへの接着は未証明。

主定理：`general_dimension_recovery.tex`。局所比較：`three_object_window.tex`。基礎体降下・生成上界：`generic_cubic_descent.tex`（すべてpapers/support/papers/reconstruction/）。現在の詳細な監査・障害・参照は `notes/paper_b_proof_audit.md`。

## 証明の最短経路とその理由

代数的三対象window → 固定三対象の(CF_3) → 完備底の固定HomをLaurent体へ局所化 → Eulerノルム2·3^(N−1)による非零性 → 代数閉包上のBFK生成 → perfect核の有限降下 → smoothnessと線束検出によるcoherent飽和 → 低Natの体拡大 → 可積分勾配空間からG/Kを構成する。

(L)の核心は、完備Homの摂動縮約から元の正則局所基底でのproper性を得て、実際のsection--windowのHom比較coneへ導来Nakayamaを使うこと。生成性は T_j=B(j)_{<1-a} の有限filtrationから三角的に証明する。関手はArtin同値の列の逆極限から作らず、生成性を特殊点だけから持ち上げない。rotationは内部切断の境界成分の消滅とevaluation三角で比較する。

一般点の存在を先に得れば、低Natの有限性と体拡大はsmooth proper性から従う。従って明示低積の全計算や(D)を存在の前提に戻さない。全MF比較、Stevenson/regradingの別証明、相対理論、明示族の有効な成果は削除しない。

## 優先順位の高い次の作業

1. **(CF_3)を監査する。** `formal_cubic_mf_reconstruction.tex` と `curved_gauge_comparison.tex` をK,K(1),K(2)へ制限する。π=[Ξ,W]、[Ξ,π]=0とF_(2r+1)∈m^rから、unital bar写像・逆写像・固定次数内の収束・t多重線形性・周期図式を確認する。全対象の形式functorより必要な三対象比較を優先するが、高次積をcohomologyの階数だけで代用しない。
2. 論文AのLie正規形、普遍Hesse中心、PBW/AS、Cramer特殊化、Bondal・stack成分の独立監査と一次資料比較を継続する。
3. 非可換入力でV=H^0 dgNat(Id,ρ)、U=H^0 dgNat(Id,ρ²)、積μを実計算し、G/Kを有効化する。λ=1の既知明示式を指定するには(D)を確認する。これは一般存在の前提ではない。
4. 正則多変数基底の(L)は確立した。同基底の(CF_3)とチャート比較・接着を検証する。形式Koszul消去が多変数で成立するだけでは、全モジュライ上の相対同値にならない。

## 論文Aと分離先の到達点

全体三次式がsmoothなら三変数制限が特異・零でも、active偏微分gcd=1、古典Casimir核一定、普遍交換子minor、Cramer法、中心三次配分のBertiniから代数的中心元を構成する。Hesse型は短い多項式公式、一般には原点で正則な有理式。形式中心元・Kontsevich・Dolgushevをこの存在証明の必須入力へ戻さない。正規形・PBW/AS・普遍恒等式の全独立監査は未完。

Pois(X)、[Pois(X)/Aut(X)]、relative Poisson stackを区別する。Fermatの成分数はそれぞれサイズ3以上の集合分割、整数分割、floor((n+2)/3)。一般cubicのspace/固定stackが既約である証明を保持する。Fermat最大性は未証明。一般次元quadratic envelope・偏極付き圏からのambient復元はAに保持する。詳細は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md`。

論文Bの明示混合族、coherent飽和、point schemeとPoisson零点の平坦極限、λ³=-3の局所代数、相対Artin障害、有限対角・bar・Morita比較、Poisson一次消滅、非楕円型の有効な既存証明を保持する。全射影化の導来同値を残余同値と混同しない。

17次元非可換cubic族、ambient周期性、6/7次元退化scheme詳細、独立境界研究は `uedakazushi/nc-cubic2`、Reyeは `uedakazushi/reye` が正本。数学的に未照合の候補TeXは無断で削除せず、内容を現行論文・ノートへ統合してから整理する。

## 再現と実施状態

`latexmk papers/paper_a.tex` / `latexmk papers/paper_b.tex`。LuaLaTeX・LuaTeX-ja・latexmkを使い、PDF・中間物はbuild/に生成しGit追跡しない。静的検査は `python3 scripts/check_layout.py` と `python3 scripts/verify_bundle.py`。数学的証明の検証とは別である。

今回 `python3 computations/verify_three_object_window.py --output build/three_object_window_checks.json` を実行し、Q(h,u)上の二つの有限複体の16縮約恒等式、2 Schur complement、単元分母、N=5,...,16の12 window添字を確認した。非可換MFの実際のHom、高次積、圏同値の計算ではない。三対象windowの5頁の抜粋をLuaLaTeXで組版した。全文Bと全既存証明書の再実行は未実施。詳細は `validation_paper_b.json`。既存のfield-model検算コード `verify_generic_cubic_descent.py` は保持するが今回は再実行していない。Aなどの既存記録は `validation.json`。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の常設原則である。

1. 重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して研究価値を最大化する。方針変更は現在有効な理由と解決／未解決の境界として書き直し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在を記し、証明記載、独立監査、有限計算を区別する。誤りが分かれば依存する本文・要約・方針も同期して訂正する。
3. 公表稿では一次資料を確認し、既知結果との関係をIntroductionで具体的に説明する。未確認の文献情報・新規性を推測で補わず、外部PDFや検索結果を大量収録しない。
4. 公表価値のある成果と十分な証明は日本語LuaLaTeXで保持し、現在の論理順に構成する。軽量化を理由に有効な証明や成果を削除しない。
5. 研究ノートは現在有効な着想・計算・反例・障害・文献比較を整理する。会話記録や作業日誌を蓄積せず、論文の証明全文を重複させない。
6. 再開は本方針から行い、最新mainだけから目標・到達点・未解決点・具体的着手を理解できるようにする。旧ZIPや会話履歴を前提にしない。
7. 継続用一式には現行方針・ノート・原稿・必要最小限のコード／入力／証明書を置く。履歴・重複・cacheを除き、数学と検証可能性を容量上限に合わせて削らない。
8. ユーザーの保存許可により区切りで承諾を求めずmainへ通常のfast-forwardで保存し、遠隔ref/blobを確認する。GitHub Actions・force pushは禁止。GitHub正本の個別指定に従い、Libraryは実際のpush失敗時のみ緊急退避する。既存Libraryファイルを明示許可なく削除しない。生成・検証・組版・保存を別々に報告する。
