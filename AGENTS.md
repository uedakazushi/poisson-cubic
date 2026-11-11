# AGENTS.md — nc-cubic研究継続

**2026-11-12 / v43。GitHub mainが唯一の正本。** 最初に 00_research_plan.md を読む。

## 最優先指示：論文Aを投稿可能な水準へ

現在は論文Aの証明・文献・構成の独立監査と改訂を最優先する。
入口は papers/paper_a.tex、専用文献は papers/support/papers/references_poisson_cubic.tex、
現在有効な研究ノートは notes/poisson_article_submission_audit.md。
最初に prop:pg-represent、lem:pg-linearize、lem:pg-quadratic-lie と thm:pg-bondal を監査する。
次に prop:pg-PBW、lem:pg-formal-center の相対/絶対Calabi–Yau・formality・代数化を
Mori–Smith、Berger–Taillefer、Kontsevich、Dolgushev、Etingof–Ginzburgの一次資料と照合する。
既知のcubic threefold Grassmann分類、Fano四・五次元Bondal予想、
Sklyanin中心公式と本論文の貢献をIntroductionで区別する。
全原稿AのLuaLaTeX組版と必要な整数行列証明書の再実行を経て投稿判定する。
局所的な厳密検算を全定理の形式証明と取り違えない。
論文B/Cの証明・コードを保持し、研究対象の新たな拡張よりAの完成を優先する。

## 論文A：Bondal予想の帰結

全滑らかなcubic n-fold (n>=3) のPoisson構造についてBondalのD_{2j}次元下界を、正規形のJacobianブロックから選ぶ平面曲線のjoinで証明。`papers/support/papers/sections/bondal_cubic.tex` に証明全文、`notes/bondal_cubic.md` に次の監査点。現行の正規形 `thm:pg-normal` に依存する。旧正規形のLie代数補題と射影ランク低下の独立監査が次の優先事項。Fano4/5の既知結果と新規性を区別する。

## Point schemeの現行結果

混合族の全滑らかな係数λ（λ³+3≠0）に拡張。Sklyaninが滑らかなh⁶+27≠0、h非零でPoint(B)=E_h⊔S_{h,λ}。有限部分の環はmonicなx²+λy,y²+λx,z²,v³+1+λxy/3+h²z(λ²/6−2xy/3)で自由rank24。vは単元、明示せん断でh方向の抽象同型。h=0のflat schematic closureはPoisson零点の埋め込みスキーム。λ≠0で12二重点、λ=0で3八重点。証明 `papers/support/papers/reconstruction/point_scheme_lambda_family.tex`、ノート `notes/point_scheme_poisson_zero.md`。Sklyaninの点列scheme/translationは既知入力。特異λ³=−3・退化h⁶=−27と一般nc cubicは未解決。

## 特異境界の有限点の局所型

判別式λ³=-3を越えて孤立point-module可換化環のC[λ,h]自由rank24が証明された。境界h≠0で3×2 +3×6、六重点はC[v]/(v^6)、h=0ではC[v,z]/(v³,z²)。hλ≠0で局所一変数式(v³+(λ³+3)/3)²=0。論文Cの `point_scheme_discriminant_boundary.tex` を使用。Sklyanin部分の退化h⁶=-27と、特異cubicのPoisson零点定理は別扱い。h=0の代数的延長をB0のpoint schemeと同一視しない。証明原稿と有限計算証明書を残す。

## 現行の結論と依存

(L)局所proper/windowと(CF)実際の完備MF同値下の一変数量子化について、有限拡大K'/C(h)上の全coherent残余pairの可換復元を得る。lambda=1の明示式には(D)も必要。既存全依存を独立再監査した意味ではない。

一般点では非零像の三shiftが生成するためLaurent体上の同値が得られ、compact核の有限表示性で有限体拡大へ降下する。完備底全体の逆核を先に作る課題へ戻らない。

新節coherent_residual_saturation.texは、B=A/(w)のGorenstein/section条件から任意MのRHom(O(j),M)が体上perfectであることと全twistによる検出を示す。smoothな線束生成代数の対角によりRHom(G,M)はその代数上perfectとなり、評価coneの直交からC_lin=Db(qgr B)。残余smoothnessと有限例外貼合せで適用し、K_lin=K_cohを得る。一般点以外で無条件の一致を宣言しない。

## 次に進めること

(CF)の曲率formality/coherent inverse全構成、(L)の通常導来stabilization/window、(D)の乗法的比較を独立監査する。今回点検済みなのはStevenson Thm6.13の適用範囲、次数再付与、固定HomのLaurent局所化と、新しい飽和証明。

同値核の行列・有限拡大次数・三shift生成の有効なcell上界は未計算。全Db(qgr B)と可換Db(coh Y)の同値は主張しない。残余同値では貼合せが残る。多変数族・全モジュライ一般点・特殊点を含む相対同値は別課題。

## 保持・検証

論文A/B/Cの有効な証明・コード・必要証明書・反例を保持する。一般KFは未解決だが現行経路の前提でない。項別自由性だけの生成子持上げは偽のまま。smoothness・perfect性・通常導来底変更を区別する。既知の飽和原理を新規成果としない。

`python3 scripts/verify_coherent_residual_assets.py --rerun-orbit` と `latexmk papers/coherent_residual_saturation.tex`。前者はsource参照と旧64 Euler/41 MF恒等式の再現確認であり新定理の形式検証でない。今回新単独稿5頁を組版・表示確認、A/B/C全体は未組版。検証状況はvalidation.jsonに分離する。

## 保存

区切りごとに承認を求めず、証明全文・研究方針・ノート・必要ソースをmainへ通常のfast-forwardで反映する。全文の代わりに要約だけを保存しない。remote headと既存変更を保持し、force push・無断PR・GitHub Actions禁止。refと変更blobを照合する。

成功時はLibraryへ二重保存せず、実際のGitHub失敗時のみ緊急退避する。既存Libraryファイルを無断削除しない。日本語LuaLaTeX、PDFはGit追跡せずbuild/へ生成。旧版ZIP・ログ・cache・重複は追加せず、数学的内容と再現性を容量制限のため削らない。

## papers/の配置規則
papers/直下に置くファイルはpaper_a.tex、paper_b.tex、paper_c.texのみ。補助TeX・参考文献・短い独立原稿はpapers/support/papers/以下に配置する。主原稿はpapers/support/をinput探索先として使用する。新たなpapers/直下のファイルを作らない。
