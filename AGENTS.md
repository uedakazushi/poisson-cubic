# AGENTS.md — nc-cubic研究継続

**2026-11-11 / v37。GitHub mainが正本。** 00_research_plan.md、notes/coherent_residual_saturation.md、notes/rotation_orbit_generic_reconstruction.mdを先に読む。

## 論文A：Bondal予想の帰結

全滑らかなcubic n-fold (n>=3) のPoisson構造についてBondalのD_{2j}次元下界を、正規形のJacobianブロックから選ぶ平面曲線のjoinで証明。`papers/sections/bondal_cubic.tex` に証明全文、`notes/bondal_cubic.md` に次の監査点。現行の正規形 `thm:pg-normal` に依存する。旧正規形のLie代数補題と射影ランク低下の独立監査が次の優先事項。Fano4/5の既知結果と新規性を区別する。

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
