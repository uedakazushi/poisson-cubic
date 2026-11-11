# 片側compact核と特殊点を含む相対復元

**2026-11-11 / v35。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文は `papers/reconstruction/one_sided_morita_algebraization.tex`。現在の一般点の短い経路は `notes/rotation_orbit_generic_reconstruction.md`。本ノートの判定は、h=0を含むより強い相対同値のための有効な十分条件として保持する。

## 有効な判定

Cを可換Kuのsmooth proper生成代数、Gammaをnc残余のproper生成代数とし、可換側からnc側へ関手を取る。右Gamma-perfectな(C,Gamma)-双加群Pが特殊点で同値を与えれば、局所底で同値となる。逆Q=RHom_Gamma(P,Gamma)はCのsmoothnessで右C-perfectとなり、単位・余単位のconeは底上perfect。特殊点で零なのでperfect Nakayamaを使える。Gammaのsmoothnessは結論であり仮定でない。

rotationについてはL_C tensor_C P→P tensor_Gamma L_Gammaの一つの射と、その特殊点での可逆性で足りる。HH0(C/R)=Rを追加すれば、三次周期性の差はscalar uで、c^3u=1のetale根で補正できる。任意の高次群作用のcoherence全体をこの補正で処理したという主張ではない。

RがNoether局所G-ringで、通常の導来双加群圏に完備底の右Gamma_hat-perfect核P_hatがあり、左作用とrotationの整合性を持てば、Popescuとperfect加群の有限表示性によって任意の有限jetを保つetale代数化を得る。形式分枝全体を再現するとは限らない。

## 現在の一般点の証明との関係

本族で上のP_hatを完備底全体に構成する問題はなお残る。しかしgeneric結論には先にhを反転できる。形式functorが送った原点stabilizationの像はEulerベクトルで一般点でも非零と分かり、三つのrotationシフトが生成する。従ってLaurent体上で初めてinverse kernelを取ればcompactであり、有限代数拡大へ降下できる。

この議論は本節の完備compact性を証明したものではなく、generic目的にはそれを不要にしたものである。特殊点を含む同値、具体的な逆核行列や有限cell数を求める際には、本節の判定を引き続き利用できる。

## 保持する障害

有限自由MF、底上perfectなHom、Artin切断ごとのperfect性だけでP_hatの右Gamma_hat-perfect性を推論しない。Gamma=k[e]/e^2のkは底上perfectでもGamma-perfectでなく、Torは全次数に残る。特殊生成性の無条件持上げの反例も保持する。

## 検証と文献

Toën–Vaquié Lemmas2.8,2.10、Stacks07GC,07M7,068Uへの依存を保持する。`verify_one_sided_morita.py` はねじった2×2行列代数の206恒等式、relation階数、周期補正mod h^8とcompact性反例の検算であり、nc cubicの完備逆核を計算するものではない。この既存計算は今回再実行していない。
