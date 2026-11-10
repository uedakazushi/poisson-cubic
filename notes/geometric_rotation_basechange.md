# 射影核による形式復元とgeneric段階への接続

**2026-11-11 / v34。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文は `papers/reconstruction/geometric_rotation_basechange.tex`。generic段階の最新判定は `notes/one_sided_morita.md` とその参照先。

## 幾何学的な結論

可換滑らかなcubic族X/R（RはArtin局所C代数、N>=5）のperfect Kuznetsov成分では、mutation核M_j、射影P=M_0*...*M_(N-4)、rotation核Q=P*M_0*Delta_*O(1)*Pを使い、真のNatを `Rq_* RHom(P,Q^{*r})` で表す。相対Moritaとproper perfect直接像によりperfectかつ導来底変更互換。

各座標sは `M --s--> M(1) -> L_O(M(1))` を与え、r=1の全基底、r=2ではその合成の基底が閉元として持ち上がる。特殊H^(-1)=0から、基底写像のconeのH^(-1),H^0が全nilpotent層で零となり、rankN,binom(N,2)の自由性と自然なH0底変更を得る。一般KF、独立v、mu3対称性は不要。N=7,r=2でH1が二次元でも成立する。

## 非可換側への依存と現在の課題

(F)既存全Artin形式MF/残余同値、(D)正則有限対角/乗法的characteristic写像を入力するとncのBCが従い、lambda=1のG_h+v^3とW_hは形式GL5同型になる。各R_m上の残余pairはV(G mod h^(m+1))のKu pairと同値。既存のF,D全証明やv27全行列を今回独立再監査したとはしない。

これはgeneric同値ではない。有限Morita証明書を両方向に同時構成することは十分だが、現在はより少ない入力でよい。smooth properな可換側からproperなnc側への **一つの右perfect核** が特殊点同値を与えれば、逆と逆性は自動的に構成できる。完備底上のordinary compact核が存在すれば、Popescuでetale代数化できる。詳細はone_sided_morita_algebraization.tex。

残る具体作業は、可換側一生成子の形式逆像を通常の導来双加群圏で実現し、Gamma_hatの有限cell/retractと示すこと。左作用とrotationのcoherenceも必要。全Artinで各々perfectというだけでは代用しない。

生成性を持ち上げる際はHomのR-perfect性、正しい導来特殊化、compact生成性を分ける。項別自由性だけの旧反例は引き続き有効。一般KFの全忠実性は未解決だが、本経路の必須条件ではない。

## 再現

`verify_geometric_rotation.py` はBFK重みの算術56例と、H1が残る有限自由複体を含む15Artin例を検算する。幾何学的核やnc Natの計算コードではない。証明の根拠は本文のMorita・perfect性・coneの議論にある。
