# 研究方針：Poisson三次超曲面の量子化と一般点可換復元

**2026-11-12 / v61。再開時は最初に読む。GitHub uedakazushi/nc-cubic のmainが正本。**
現行主原稿はA `papers/paper_a.tex`（A-v51）とB `papers/paper_b.tex`（B-v45）。

## 目標・到達点・達成基準

Aはsmooth cubicのPoisson正規形、退化、Bondal予想、代数的量子化、固定・相対Poisson moduliを公表可能にする。Bは、次数別有限自由な代数的中心三次変形で特殊ファイバーが多項式環とsmooth cubicである場合に、一般点のrotation付き全coherent残余圏を可換cubicから復元する。

**Bの比較条件は構成定理になった。** 三対象windowで(L)を、`complete_curved_transport.tex` の `cft:thm:complete` で(CF)と(CF_3)を構成する。主定理にはこれらを独立に仮定しない。R=C[h]_(h)、K=C(h)上にsmooth cubic模型Yを取り、有限拡大後にrotationと中心元由来の三次周期比較を保つ全coherent残余圏同値を得る。模型は全n>=3で幾何学的に一意で、BFKの既知定理による三rotation和の生成段数上界2(n+2)(n+3)-1を持つ。正則多変数局所基底の分数体にも同じ結論が成立する。

この結論の対象は指定した**代数的中心三次変形**であり、任意の抽象的nc cubic圏の表示・分類ではない。証明の記載と今回の主要論証の点検、全支持節の独立監査、計算、組版、保存は区別する。包括的新規性調査・外部査読・形式検証は未実施。

## 現在の証明の順序

次数別Koszul持上げ → 代数的三対象window → 完備曲率移送 → 固定Homの局所化 → Euler非零性 → 代数閉包上のBFK生成 → perfect核の有限降下 → coherent飽和 → 低Natの体拡大 → 可積分勾配空間からG/Kを構成。

形式比較では、通常の結合変形をgraded unital formalityで星積へ移す。中心逆像は有限自由な三次式空間上のC_pi=Id+O(m)を逆にして求める。勾配Koszulの完全性と次数からπ=[Ξ,W]、[Ξ,π]=0。曲率はmの倍数ではないが、出力arityは関数k個で2−2k、trivectorを加えると3−2kなので関数は高々一個。arity1,3のnormalized coderivationを積分して、写像・逆ともF_(2r+1)∈m^rを得る。固定次数内の有限自由行列でtwistingの和が収束し、実際の相互逆関手とt多重線形な周期比較を構成する。Artin同値の列の抽象的な逆極限で代用しない。

方程式のKへの降下は一般点の存在とsmooth proper性の後に行う。低Natの明示行列や(D)を一般存在の前提に戻さない。(D)は特定の既知多項式を復元先に指定する比較として残る。

証明の入口は `papers/support/papers/reconstruction/general_dimension_recovery.tex`。局所比較は `three_object_window.tex`、完備比較は `complete_curved_transport.tex`、定義体・生成上界は `generic_cubic_descent.tex`（同ディレクトリ）。詳細は `notes/paper_b_proof_audit.md`。既存の形式二次jet、相対Artin、別生成証明、明示族、障害・反例は現行支持節に保持する。

## 一次非可換方向の消滅と接空間

`papers/support/papers/reconstruction/first_order_poisson_kernel.tex` で、双対数環上の中心三次対に対する一次変形を全次数formalityを使わず直接比較する。HKRで積の一次項を二次係数bivector πへ正規化し、中心性から[π,F]=0、滑らかさ・Koszulからπ=[Ξ,F]となる。曲率 -tF のHochschild複体で η=ε HKR(Ξ)/t の境界がHKR(π)を消す。双対数なのでbar写像はarity1と3のみで実際に逆があり、graded MFの内部shift・中心元由来周期性も保つ。Jacobi条件は一次消滅には不要だが、全次数へ延長する際に必要。一次の可換式は標識によって導分(F)だけ変わり、(S/J(F))_3に値を持つ。次元は binom(N+2,3)-N²、cubic threefoldで10。PoissonのPlücker錐は一般非零点で7次元だが可換零点のZariski接空間は10次元で、cubicの変形10次元と合わせて局所次元17／接空間20という差がある。今回の一次消去は可換点の10方向を対象とし、一般非零点での7次元kernelと同一視しない。17次元非可換族の実際のcategorical forgetful微分はKodaira--Spencer照合が未完である。これは全次数比較の独立検算として価値がある。

## 五変数の二次Hochschild障害の完全なPlücker表示

`first_order_poisson_kernel.tex` に、可換中心三次対(S,F)の一次変形（恒等剰余の次数付き同型を法とする）が `Λ³V ⊕ Jac(F)_3` と表せる命題を加えた。N=5で前者10、後者10、合計20次元。一次変形の積を二次まで延長するHochschild障害は `[π_Ξ,π_Ξ]/2` であり、滑らかなFではその係数二次式のイデアルが五つのPlücker関係式にスキーム論的に一致することを直接証明。非分解可能なΞを標準形 e012+e034 に移し、Jacobi条件を `F_{0i}F_j−F_{0j}F_i=0` と計算、Eulerから `3F F_{0i}=2F_0F_i` を得て滑らかさと矛盾させる。五つのPfaffianの二次写像が五次元の四形式空間へ全射なことからJacobi係数の生成イデアルも同一と示す。

これは既知Poisson構造のGrassmannian記述と整合する独立の二次障害の証明。新規性は未確認。二次の`結合積`障害がPlückerで切り出されることと、中心元も含めた全高次形式局所環の同定を区別する。nc-cubic2では局所次元17とZariski接空間20が別だが、一般非零Poisson点でのcategorical忘却微分とその7次元核は未確認。実例検算は `computations/verify_second_order_plucker.py`。

## 未解決の核心と次の具体的着手

1. **公表可能性の独立監査。** 一次消滅と二次Plücker障害の証明を出発点に、新しい完備移送のnormalized全cochain、非小曲率の評価、matrix延長、periodicityと、既存window・有限降下・coherent飽和を別の観点から再点検する。B全文の参照・引用・組版を実行し、原稿全体を一貫した論理順へ再編する。主定理の証明を構成したことを、全支持節の再監査完了と同一視しない。
2. **有効化。** 非可換入力のV=H^0 dgNat(Id,ρ)、U=H^0 dgNat(Id,ρ²)、積μを有限行列で構成し、G/Kを具体計算する。既知λ=1多項式の特定には(D)を検証する。
3. **降下と相対化。** 同値核のKへの降下障害、h=0で正則な模型、特殊点込み相対同値、有限拡大次数と核の明示、モジュライ上の接着を調べる。幾何学的一意性とK上のformを混同しない。
4. **Aの独立監査。** Lie正規形、普遍Hesse中心、PBW/AS、Cramer特殊化、Bondal・stack成分と一次資料比較を継続する。Aの代数的量子化存在証明にformalityを必須入力として戻さない。

## Aと分離先の現在の内容

Aでは全体三次式がsmoothなら三変数制限が特異・零でも、active偏微分gcd=1、古典Casimir核一定、普遍交換子minor、Cramer法、Bertiniによる中心三次配分から代数的中心元を得る。Hesse型は短い多項式、一般には原点で正則な有理式。全依存の独立監査は未完。Pois(X)、固定商stack、relative stackは別の空間で、Fermat成分数はそれぞれ集合分割、整数分割、floor((n+2)/3)。Fermat最大性は未証明。一般次元quadratic envelope・偏極付きambient復元はAに保持する。詳細は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md`。

Bの混合族、point schemeとPoisson零点の平坦極限、λ³=−3の局所代数、相対Artin障害、有限対角・bar・Morita比較、Poisson一次消滅、非楕円型の有効な証明は保持する。全射影化の導来同値を残余同値と混同しない。17次元モジュライ、ambient周期性、6/7次元scheme詳細、独立境界はnc-cubic2、Reyeはreyeを正本とする。未照合候補は数学的内容を現行論文・ノートへ統合するまで削除しない。

## 再現と実施状態

`latexmk papers/paper_a.tex` / `latexmk papers/paper_b.tex`。静的検査は `python3 scripts/check_layout.py` と `python3 scripts/verify_bundle.py`。B-v43の実施状態は `validation_paper_b.json`、Aなどは `validation.json`。

新しい `computations/verify_complete_curved_transport.py` はSchouten恒等式、CasimirだけではJacobiが従わない負例、非自律・非可換なbar flow模型の10逆行列恒等式と2750余積係数恒等式、arity位数、twisting代入の相互逆性を厳密検算した。実際の非可換MF HomやKontsevich重みの計算ではない。5頁の証明抜粋をLuaLaTeXで組版し表示確認した。B全文・全既存証明書の再実行は未実施。以前の検算コードは保持し、今回再実行したとは記載しない。

## 研究一般の原則と保存許可

以下は具体的計画とは別の常設原則である。

1. 数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合して価値を最大化する。変更は現在の理由と解決／未解決として書き直し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在、記載／独立監査／計算を明記し、誤りなら依存する本文・要約・方針も訂正する。
3. 公表稿は一次資料を確認し、既知結果との関係を具体的に説明する。未確認の文献・新規性を推測で補わず、外部PDFを大量収録しない。
4. 公表価値のある成果と十分な証明は日本語LuaLaTeXで、現在の論理順に保持する。軽量化を理由に有効な数学的内容を削らない。
5. ノートは現在有効な着想・計算・反例・障害・文献比較を整理し、会話・日誌・重複証明を蓄積しない。
6. 本方針を入口とし、最新mainだけで目標・到達点・未解決点・具体的着手を理解できるようにする。旧ZIP・会話を前提にしない。
7. 継続用一式は現行方針・ノート・原稿・必要な最小限のコード／入力／証明書とし、履歴・重複・cacheを除く。数学・検証可能性を容量上限に合わせて削らない。
8. ユーザーの保存許可により区切りで承諾を求めずmainへfast-forward保存し、遠隔ref/blobを確認する。GitHub Actions・force pushは禁止。Libraryは実際のpush失敗時のみ緊急退避、既存Libraryファイルは明示許可なく削除しない。生成・検証・組版・保存を別々に報告する。
