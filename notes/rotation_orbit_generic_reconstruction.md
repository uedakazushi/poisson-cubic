# 次数シフト軌道による一般点復元

**2026-11-11 / v35。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文は `papers/reconstruction/rotation_orbit_generic_reconstruction.tex`。単独入口は `papers/rotation_orbit_generic_reconstruction.tex`。

## 新しい結論と依存

原点のみが特異な斉次超曲面のgraded MFでは、任意の非零対象の全次数シフトが生成する。三次ならE,E(1),E(2)で足りる。非次数付き部分はStevenson Thm6.13。次数の再付与R(U(E))=⊕E(j)とcompact局所化によりgradedへ戻す。非次数付き生成性だけからgraded生成性を即断しない。

(L)は既存の代数的局所proper/window模型。K_R=stab(R)、T_R=K_R⊕K_R(1)⊕K_R(2)のendomorphismが線束生成残余圏を表し、Homの平坦底変更が成立するという入力。(CF)はfo:cor:complete-gradedの実際の完備底有限rank A∞同値であり、両立Artin同値の列だけではない。

(CF)を固定した三対象へ制限してからhを反転する。各固定Hom次数の行列は有限自由な斉次成分なので、形式functorは通常のRhat-multilinear写像として実現される。任意のLaurent係数対象へfunctorを最初から拡張する必要はない。

残余体のspecial stabilizationのEulerベクトルは
`chi_r=Σ_(s+r=0 mod3)(-1)^s binom(N,s)`、r=0,1,2。
二乗和は2*3^(N-1)なので非零。N=5は(-9,9,0)。N=9はchi0=0なので一般次元で自己Euler数だけを使わない。
(L),(CF)により像EのHomは底上perfectでEuler不変。E_L=0なら全chi_r=0となり矛盾する。
従って一般点の像は非零で、三シフトが可換MF全体を生成する。これでLaurent体上の実際のMorita同値とrotation比較を得る。

## 代数性と明示式

Laurent体上で得た逆核は右Gamma-perfectであり、可換側のsmoothnessから包絡代数上compactになる。Toën–Vaquié Lemmas2.8,2.10により有限生成K部分代数へ核とrotation射を降ろす。単位・余単位とrotationのconeは底上perfectで、genericで零なので非空開で零。閉点を取り有限拡大K'/Kへ移す。

これで(L),(CF)下の一変数量子化の線束生成残余pairは幾何学的一般点で可換cubicから復元される。Wの係数がKにない場合は、有限個の係数と判別式を先に有限型部分代数へ降ろし、可換cubic族とそのprojected generatorを同時に特殊化する。

lambda=1では既存(D)の低rotation比較によりW_hと計算済みG_h+v^3が形式GL5同型。Gを固定したまま降下できるので、復元先を既存の明示式に取れる。これは既存の(L),(CF),(D)の全証明を今回独立再検証したという意味ではない。

## 得ていないもの

- 完備底全体のcompact逆核とh=0を含むetale同値。先にhを反転するため不要になったが、証明されたわけではない。
- 有限拡大の次数、同値核の具体的行列、finite-cell数の有効上界。
- K^linと全coherent残余圏の一致、一般lambdaの明示式、多変数の全Poissonモジュライ一般点への一括適用。

P1上の生成子退化反例は有効。新経路は特殊生成性を持ち上げず、一般点で非零性とrotation軌道を使うため、その反例と矛盾しない。

## 再現・一次資料

Stevenson arXiv:1105.4698v3 Thm6.13 (PDF p26)、Dyckerhoff arXiv:0904.4713v5 §2.4/§5.6、Stacks09SM/00FV、Toën–Vaquié math/0503269v5 Lemmas2.8/2.10を確認。新規性の網羅調査は未完了。

`python3 computations/verify_rotation_orbit.py --output build/rotation_orbit_certificate.json` は64個のEulerベクトルと、混合special cubicの32×32行列による41恒等式を検査する。分類定理、一般点のkernel、既存F/Dの実装の検証ではない。
`latexmk papers/rotation_orbit_generic_reconstruction.tex`。

次は(L),(CF),(D)の重要な依存箇所を独立監査し、可能なら三シフト生成の有限cellと同値核を明示化する。generic存在の証明とeffectiveな公式を区別する。
