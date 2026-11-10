# 低rotation次数のArtin障害と生成性の訂正

**2026-11-11 / v32。再開時は00_research_plan.mdを最初に読む。**
論文Cに統合する全文はpapers/reconstruction/artin_rotation_obstructions.tex。

体上の五変数三次のgraded MFの導来自然変換
H^{-1},H^0,H^1の次元は内部shift r=1で(0,5,2)、r=2で(0,10,0)。
r=1のH^1は二つの非自明mu3 sector (BFK Thm5.39)。実際の非可換Artin Natではない。

正しいR_m-flatで特殊化と厳密に両立する標的Nat cochain C_mを構成できれば、
r=2は長完全列からH^0自由rank10かつ全Artin底変更。
r=1は第一次ob_1:k^5→k^2の消滅を検査し、さらに高次障害を調べる。
体上の次元と有限対角sourceの自由性だけでは足りない。

**訂正した誤り：** 特殊ファイバーのMorita生成性とHom項別自由性だけでArtin生成性が持ち上がる一般補題は偽。
R=k[eps]/eps^2の有限自由二周期dg圏でG=Rとし、
T=(R --eps--> R --eps--> R)を取ればHom(G,T)は非輪状、Tは非可縮。
G0=kは体上で生成するがGは生成しない。
これは本研究の正の内部次数graded cubic MFへの反例ではない。
相対Artin節の依存主張を訂正し、正しい導来二側bar評価の構成・特殊化を独立の入力とした。

Γ=μ3^(v)を保つ混合族では、H^1のΓ不変部分が零なので、四つの不変な低次数classは全Artinで持ち上がる。第五のvは中心元の閉じた自然変換として持ち上がる。正しいArtin互換導来Nat模型が存在する場合はr=1も自由rank5となる。新定理全文はpapers/reconstruction/central_symmetry_lifting.tex。よって2×5障害の項別計算より、正しい導来bar模型とkernel全忠実性(KF)の確立を優先する。generatorの持上げとKFを混同しない。
