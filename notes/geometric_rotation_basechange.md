# 射影核による形式復元と一般点への接続

**2026-11-11 / v35。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文は `papers/reconstruction/geometric_rotation_basechange.tex`。一般点の現在の結論は `notes/rotation_orbit_generic_reconstruction.md`。

## 幾何学的な結論

可換滑らかなcubic族X/R（RはArtin局所C代数、N>=5）のperfect Kuznetsov成分では、mutation核M_j、射影P=M_0*...*M_(N-4)、rotation核Q=P*M_0*Delta_*O(1)*Pを使い、真のNatを `Rq_* RHom(P,Q^{*r})` で表す。相対Moritaとproper perfect直接像によりperfectかつ導来底変更互換。

座標sの `M --s--> M(1) -> L_O(M(1))` とその合成が次数1,2の特殊基底を閉元として持ち上げる。特殊H^(-1)=0より基底写像のconeのH^(-1),H^0が全nilpotent層で零となり、rankN,binom(N,2)の自由性と自然なH0底変更を得る。一般KF、独立v、mu3対称性は不要。N=7,r=2でH1が二次元でも成立する。

## 非可換側への依存と統合結論

既存の全Artin形式MF/残余同値と(D)正則有限対角・乗法的characteristic写像を使うとncのBCが従い、lambda=1のG_h+v^3とW_hは形式GL5同型となる。この節単独の結論は形式的なもので、旧F/Dの全独立監査をしたという意味ではない。

一般点には、別途構成した次数シフト軌道の議論を合成する。実際の完備有限rank functor(CF)を固定三対象へ制限してからhを反転し、Euler非零性と孤立超曲面の軌道生成によってLaurent体上の同値を得る。この形式GL5変換はLaurent体上の通常の変換になるため、Gを固定した同値を有限拡大C(h)上へ降下できる。

完備底全体のcompact逆核とh=0近傍の同値はこの統合結果からは従わない。これらを求めるより強い経路はone_sided_morita_algebraization.tex。一般KFの全忠実性も未解決だが、現在のgeneric経路の前提ではない。

## 再現

`verify_geometric_rotation.py` はBFK重み算術56例と有限自由複体の15Artin例を検査する。幾何学的核やnc Natを計算するコードではない。今回は再実行していない。新しいEuler/Koszul検算は `verify_rotation_orbit.py`。
