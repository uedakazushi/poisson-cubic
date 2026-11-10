# 射影核による最短経路と有限Morita証明書

**2026-11-11 / v33。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文は `papers/reconstruction/geometric_rotation_basechange.tex`。本ノートは証明を重複せず、依存と再開点を整理する。

## 現在の結論

可換滑らかなcubic族X/R（Rは任意のArtin局所C代数、N>=5）のperfect Kuznetsov成分では、mutation核M_j、射影P=M_0*...*M_(N-4)、rotation核Q=P*M_0*Delta_*O(1)*Pを使い、真のNat複体を `Rq_* RHom(P,Q^{*r})` で表せる。Toënの相対Morita定理とproper perfect直接像によりperfectかつ導来底変更互換。

各座標sは `M --s--> M(1) -> L_O(M(1))` を与える。r=1の全基底、r=2ではその合成から選んだ基底が実際に閉元として持ち上がる。H^(-1)特殊群が零なので、基底写像のconeのH^(-1),H^0が全nilpotent層で零。従ってH0はrankN,binom(N,2)自由、自然なH0底変更も同型。

この幾何学的結論に一般MF核比較KF、独立v、mu3対称性は不要。N=7,r=2はH1特殊群が二次元だが結論は同じ。H1の消滅よりも、必要な基底の実際の閉持上げを使う方が強く短い。

## 非可換への依存

(F) は既存の全Artin形式MF/残余window同値、(D) は正則有限対角と乗法的characteristic写像。幾何学的定理はこれらに依存しないが、ncのBC充足と計算済みGの形式同定は依存する。既存証明全部やv27全行列を今回独立再検証したわけではない。

この依存下でlambda=1のG_h+v^3とW_hは形式GL5同型となり、全R_m上の残余pairはV(G mod h^(m+1))のKu pairと同値になる。これはgeneric同値ではない。正規形L,Cの値は復元先の一つの規格化として使えるが、formalityの選択と無関係な高次係数の標準的一意性は主張しない。

相対Artin比較に使う生成性では、HomがR-perfectとなるnilpotent HPLと、正しい導来特殊化を明記する。項別自由性だけから生成性を持ち上げる旧反例は引き続き有効。一般KFそのものは未解決だが、本経路の必須条件ではない。

## 最終段階へ進む具体作業

指定nc生成子の形式MF像を可換V(G)上へ運び、endomorphismとrotation作用を有限cellデータにする。Artin次数に依存しないcell数とshiftの上界、逆双加群、両合成の単位・余単位、rotation intertwinerを同時に求める。有限証明書の存在を確認せずArtin approximationやsmooth proper dg代数の有限A_n決定性を適用しない。

一般smoothnessを先に解くより、現在の明示的Gと指定生成子に対する有限Morita証明書を直接狙う。対角のfinite perfect証明書が先に得られるならSM/ERへ戻れる。両者のどちらが短いかを実際の生成子像に基づいて判断する。

## 検証

verify_geometric_rotation.py はBFK重みの算術56例と、H1が残る有限自由複体を含む15Artin例を検算する。幾何学的核やnc Natを計算するコードではない。証明の主張は本文のMorita・perfect性・coneの議論に依存する。
