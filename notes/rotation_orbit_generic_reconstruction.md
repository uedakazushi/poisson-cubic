# 次数シフト軌道による一般点復元

**2026-11-11 / v36。最初に00_research_plan.mdを読む。GitHub mainが正本。**
軌道証明全文は `papers/reconstruction/rotation_orbit_generic_reconstruction.tex`。全coherentへの新しい拡張は `notes/coherent_residual_saturation.md` とその参照先。

## 結論と依存

孤立斉次超曲面のgraded MFでは、非零対象の全次数シフトが生成する。三次ならE,E(1),E(2)で足りる。非次数付き部分はStevenson Thm6.13、gradedへ戻す部分はR(U(E))=⊕E(j)とcompact局所化による。

(L)は代数的局所proper/window模型、K_R=stab(R)、T_R=K_R⊕K_R(1)⊕K_R(2)のendomorphismによる線束残余表示とHom底変更。(CF)はfo:cor:complete-gradedの実際の完備底有限rank A∞同値であり、Artin同値列だけでない。

(CF)を固定三対象へ制限してからhを反転する。固定Hom次数の行列は有限自由斉次成分にあり、形式functorは通常の完備係数多重線形写像になる。任意のLaurent係数対象へ新しい無限Taylor和を評価しない。

Eulerベクトルは `chi_r=Σ_(s+r=0 mod3)(-1)^s binom(N,s)`、二乗和 `2*3^(N-1)`。N=5は(-9,9,0)、N=9はchi0=0なので単独自己Euler数は使わない。proper性から像E_Lの非零性が従い、三shiftが可換MF全体を生成する。Laurent体上の実際のMorita同値とrotation比較を得る。

## 代数性と全coherentへの拡張

体上の逆核は片側perfectで、可換側smoothnessから包絡代数上compact。有限型K部分代数へ核とrotation射を降下し、単位・余単位・rotationのconeを非空開で消して閉点を取ると、有限拡大K'/K上の同値を得る。Wの有限個の係数と判別式も同時に降ろす。

lambda=1では(D)によりW_hと計算済みG_h+v^3が形式GL5同型なので、Gを固定して降下する。

今回のcoherent_residual_saturation.texにより、一般点のAS-regular中心商ではK_lin=K_cohが従う。残余smoothnessから有限例外貼合せで線束部分がsmoothとなり、全coherent対象に対するHom有限性と評価coneの検出で全体へ飽和する。有限拡大からのsmoothnessも対角retractにより降下する。旧定理の線束部分という中間結論を省略せず、この新しい証明を合成する。

## 残る範囲

完備底全体のcompact逆核、h=0を含むetale同値、有限拡大次数、同値行列、有限cellの有効上界、一般lambdaの明示式、多変数全Poissonモジュライへの適用は未完成。全Db(qgr B)とDb(coh Y)の同値は主張しない。

P1上の生成子退化反例は有効であり、現在の証明は一般点の非零性とrotation軌道を使うため矛盾しない。

## 監査・再現

今回Stevenson原PDF p26、Dyckerhoff §2.4、次数の再付与と固定Hom局所化を確認した。旧(L),(CF),(D)全証明を独立再検証したわけではない。
`python3 computations/verify_rotation_orbit.py --output build/rotation_orbit_certificate.json` を再実行し、64 Eulerベクトルと32×32行列41恒等式がPASS、生成JSONは保存blobと完全一致した。分類定理・一般点kernelの形式検証ではない。
`latexmk papers/rotation_orbit_generic_reconstruction.tex`。今回この既存単独稿は再組版していない。
