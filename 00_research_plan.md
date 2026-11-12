# 研究方針：Poisson三次超曲面の量子化とrotation付き可換復元

**2026-11-12 / v57。再開時は最初に読む。GitHub uedakazushi/nc-cubic のmainが正本。**
現行主原稿は論文A `papers/paper_a.tex`（A-v51）と論文B `papers/paper_b.tex`（B-v41）。

## 目標と達成基準

論文Aでは滑らかなcubic n-foldの全Poisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduli stacksを公表可能にする。論文Bでは実際の代数的中心三次変形の一般点で、rotation付き全coherent残余圏を可換cubicから復元し、仮定・定義体・一意性・有効性を正確にする。原稿に証明があること、今回独立に点検したこと、有限計算・組版・保存を分ける。主依存の全監査と包括的新規性調査が終わるまでは投稿準備完了としない。

## 論文Bの主定理と現在の最短経路

代数的・次数別有限自由な中心三次対、滑らかな可換特殊ファイバー、局所proper/window比較(L)、実際の完備graded MF同値(CF)の下で、**元の体K=C(h)上のsmooth cubic Y**と有限拡大K'/K上の全coherent残余pairのrotation付きMorita同値を得る。一般点AS正則性はflat入力から従い、独立の仮定から外す。幾何学的一意性は全n>=3で成立する。幾何学的一般点の任意の非零Mに対しM⊕ρM⊕ρ²Mは生成時間2(n+2)(n+3)-1以下のstrong generatorとなる（BFKの既知結果）。同じ(L),(CF)を仮定した多変数正則局所基底の分数体にも適用する。

主定理と全依存の入口は `papers/support/papers/reconstruction/general_dimension_recovery.tex`、基礎体降下・AS仮定の除去・定量的生成・固定三対象による代替条件・条件付き多変数拡張の証明は `generic_cubic_descent.tex`（同ディレクトリ）。詳細監査は `notes/paper_b_proof_audit.md`。

**証明の順序**：次数別Koszul持上げ→固定三対象の完備比較→Euler非零性→代数閉包上のBFK生成→perfect核の有限降下→smoothnessによるcoherent飽和→低Natの体拡大→勾配空間の積分で方程式をKへ戻す。

方針の理由：一般点の存在を先に確立すれば、低Natの有限性と体拡大はsmooth proper性から従う。したがって、明示的な低積の全計算や(D)を存在証明の前提に戻す必要はない。特殊ファイバーでの生成性だけをgenericへ持ち上げる方法、および任意Laurent対象へ無限Taylor和を評価する方法は使わない。全MF圏上の同値を先に構成する代わりに、`gcd:prop:three-object` の固定三対象のenhanced比較を閉じる経路を優先する。既存の全MF比較、Stevenson/regradingによる別証明、明示族・相対理論の有効な結果は削除しない。

**残る核心**：(L)の相対dg stabilization/windowと底変更、(CF)のunital curved関手・逆関手・periodicity coherenceの全独立監査。原稿の記載が一般nc cubicの無条件分類を意味するわけではない。方程式はK上に取れるが、同値核もK上に降りること、h=0で正則な模型、特殊点込み相対同値、有限拡大次数、全モジュライへの接着は未証明。

## 優先順位の高い具体作業

1. 論文Bの `am:prop:Gamma-basechange` において、projective mutation模型と三つのstabilizationの比較を照合する。CFのbar構成を固定三対象に制限し、endomorphism準同型・内部shift・指定三次周期図式を点検する。全対象のformal functorの監査と区別し、一般点の最小入力を閉じる。
2. 論文Aの正規形Lie補題、全係数Hesse中心恒等式、PBW/AS条件、全PoissonのCramer特殊化、Bondal・成分数の独立監査と一次資料比較を進める。
3. 論文Bの非可換入力でV=H^0 dgNat(Id,ρ)、U=H^0 dgNat(Id,ρ²)、積μを具体化し、方程式G/Kを実際に算出する。既知の混合λ=1の多項式を指定するには(D)を使う。これは存在定理と別の有効化である。
4. 正則多変数基底上の(L),(CF)とチャート比較を検証する。形式Koszul消去の代数部分が多変数で成立するだけでは、全モジュライ上の一様復元は得られない。

## 論文Aと分離先の現行到達点

論文Aでは全体三次式がsmoothなら三変数制限が特異・零でも、active偏微分のgcd=1、古典Casimir核の一定次元、普遍交換子minorの恒等式、Cramer法と中心三次配分のBertiniにより代数的中心元を構成する。Hesse型では短い多項式公式、一般には原点で正則な有理式である。形式中心元・Kontsevich・Dolgushevをこの量子化存在証明の依存へ戻さない。正規形・PBW/AS・全恒等式の独立監査は未完。

Pois(X)、[Pois(X)/Aut(X)]、relative Poisson stackを区別する。Fermatの成分数はそれぞれサイズ3以上の集合分割、整数分割、floor((n+2)/3)。一般cubicのspace/固定stackは既約とする証明を原稿に保持する。全依存の監査とFermat最大性は別問題。一般次元quadratic envelope・偏極付き圏からのambient復元はAに保持する。詳細は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md`。

Bの明示混合族、全coherent飽和、point schemeとPoisson零点の平坦極限、λ³=-3の有限局所代数、相対Artin障害、有限対角・bar・Morita比較、Poisson一次消滅、非楕円型などの既存有効結果は現行支持節に保持する。全射影化の導来同値を残余同値と混同しない。

17次元非可換cubic族、ambientの1周期性、6/7次元の退化scheme詳細と独立境界研究は `uedakazushi/nc-cubic2` を正本とする。Reye研究は `uedakazushi/reye`。数学的に未照合の候補TeXは無断で削除せず、必要な内容を現行論文かノートへ統合してから整理する。

## 再現と検証状態

`latexmk papers/paper_a.tex` / `latexmk papers/paper_b.tex`。LuaLaTeX・latexmk・LuaTeX-jaを用い、PDFはbuild/へ生成しGit追跡しない。`python3 scripts/check_layout.py`、`python3 scripts/verify_bundle.py` は静的検査であり数学の証明検証ではない。

B-v41の新しい可換計算は `python3 computations/verify_generic_cubic_descent.py --output build/generic_cubic_descent_checks.json`。Q(t)上の3例で可積分空間次元5,1,1と16本の勾配恒等式を実行確認した。非可換低Natの実計算ではない。最新Bの検証状態は `validation_paper_b.json`、Aなど既存検証の詳細は `validation.json`。B全文の再組版・全既存計算再実行・全証明の独立監査は今回未実施。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の常設原則である。

1. 数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して価値を最大化する。方針変更は現在の理由と解決／未解決の境界として書き直し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在を示す。記載、独立監査、有限計算を区別し、誤りの依存先も同期する。
3. 公表用原稿では一次資料を確認し、既知結果との関係を具体的に説明する。未確認の文献情報・新規性を補作せず、外部PDFを大量収録しない。
4. 公表価値のある成果と十分な証明は日本語LuaLaTeXで保持する。原稿は現在の論理順に構成し、既存の有効な結果を軽量化のため削除しない。
5. 研究ノートは現在有効な着想・計算・反例・障害・文献比較を整理する。会話記録や作業日誌を蓄積せず、論文の証明全文を重複させない。
6. 再開は本方針から行い、最新mainだけから現在の結果・未解決点・具体的着手が分かるようにする。旧ZIPや過去の会話を前提にしない。
7. 継続用一式には現行方針・ノート・原稿・必要最小限のコード／入力／証明書を置く。不要な履歴・重複・cacheを除き、数学と検証可能性を容量上限のため損なわない。
8. ユーザーの保存許可により研究の区切りで承諾を求めずmainへ通常のfast-forwardで保存し、遠隔refと変更blobを確認する。GitHub Actions・force pushは禁止。GitHub正本の個別指定に従い、Library保存は実際のpush失敗時のみの緊急避難とする。既存Libraryファイルを明示許可なく削除しない。生成・検証・組版・保存は別々に実施状態を報告する。
