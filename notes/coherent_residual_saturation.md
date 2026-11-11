# 全coherent残余pairへの拡張と依存監査

**2026-11-11 / v36。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文は `papers/reconstruction/coherent_residual_saturation.tex`、単独入口は `papers/coherent_residual_saturation.tex`。

## 今回証明したこと

Aを連結局所有限両側noetherian Koszul AS-regular、global dimensionとGorenstein parameterをN>=5、wを中心正則三次元、B=A/(w)とする。

1. Bは両側AS-Gorensteinでparameter N-3。Burke–Stevenson Lemmas6.1–6.2/Prop4.18より、任意のcoherent有界MについてRHom(O(j),M)は体上perfectで、全twistによるHomの消滅はM=0を検出する。
2. AのKoszul分解をBへ移すとcohomology k,k(-3)が射影商で消え、連続N個の線束から全twistが生成される。G=⊕_{j=0}^{N-1}O(j)でC_lin=thick(G)はproper。
3. C_linがsmoothなら、N_M=RHom(G,M)は生成代数Lambda上perfect。有限cellの評価F(N_M)→MのconeはGと右直交し、全twistによる検出で零。従ってC_lin=D^b(qgr B)。全coherent圏のsmoothnessを前提にしていない。
4. 線束生成残余がsmoothなら、有限例外成分とのadmissibleな貼合せによりC_linがsmooth。これを前項へ適用すればK_lin=K_cohとなる。
5. 有限体拡大でsmoothになったdg代数は元の体でもsmooth。対角のrestrictionはperfectで、lambda:k'→k,lambda(1)=1により元の対角がretractとなる。

これを既存の一般点定理(L),(CF)へ適用すると、K=C(h)上でD^b(qgr B_K)はsmooth properとなり、既存の有限拡大K'/K上のKu同値は全coherent残余pairの同値へ拡張する。lambda=1の明示式にはさらに(D)を使う。これらの既存入力を今回全て再証明したわけではない。

## より定量的な帰結

Lambdaの対角がq段の有限cell/retractで表されれば、全coherent対象も同じq段でGから生成できる。qの具体値や同値核行列を今回得たわけではない。存在と有効計算を区別する。

## 成立しない飛躍

D^b(qgr B)全体とD^b(coh Y)の同値は主張しない。残余は同値でも例外成分との貼合せが異なり得る。次数付きアフィン環Bのglobal dimensionが有限とも言わない。

Gのright-spanning性と、RHom(G,M)の体上perfect性だけでは足りない。dual numbersのG=Lambdaに対してPerf(Lambda)はD^b(mod Lambda)より小さい。smooth対角こそがN_MのLambda-perfect性を与える。

## 今回の監査と未実施項目

Stevenson Thm6.13を原PDF p26で確認し、affine hypersurfaceの全thick部分圏が対象であることを再確認した。次数の再付与とcompact性の使用箇所、固定有限対象のHomを先に制限してLaurent局所化する箇所を点検した。ここに撤回すべき誤りは発見していない。

Kontsevichからのcurved functor全構成、局所windowの全証明、旧nc有限対角行列全部を独立監査したとはしない。次は(CF)のcoherent inverseと(L)の通常の導来stabilizationを重点的に再確認する。同値核の有効化も未完成。

Burke–Stevenson arXiv1507.00830v1 Prop4.18/Lemmas6.1–6.2/Thm6.4、Toën–Vaquié math/0503269v5 Lemma2.8(2)、Perry *Noncommutative homological projective duality* Lemma4.15(3)を一次資料で確認した。新規性の網羅調査・外部査読・形式証明は未実施。

## 再現

`python3 scripts/verify_coherent_residual_assets.py --rerun-orbit` は新原稿の参照、Cへの統合、既存Euler/MF証明書の再生成を点検する。新しい飽和定理は一般の数学的証明であり、このスクリプトで形式検証されるものではない。
`latexmk papers/coherent_residual_saturation.tex` で単独稿を生成する。
