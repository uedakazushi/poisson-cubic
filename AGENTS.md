# AGENTS.md — nc-cubic研究継続

**2026-11-11 / v34。GitHub mainが唯一の正本。** 00_research_plan.md、notes/one_sided_morita.md、notes/geometric_rotation_basechange.mdの順に読む。旧ZIP・会話を再開条件にしない。

## 最優先

有限代数的な可換方程式抽出と、可換側のprojected kernelによるBCを維持する。一般MF核全忠実性KFには戻らない。generic段階では可換smooth proper Cからnc proper Gammaへの **一つの形式逆核P_hat** を作る。

新定理：右Gamma-perfectな(C,Gamma)-双加群Pが特殊点で同値なら、底上でも同値。逆Q=RHom_Gamma(P,Gamma)、単位・余単位はperfect Nakayamaで同型。Gammaのsmoothnessは結論。rotationは一射の剰余可逆性で判定でき、HH0(C/R)=Rを確認すれば三次周期性はetale scalar根で補正できる。

P_hatが通常の導来圏に存在し右Gamma_hat-perfectなら、Cのsmoothnessから包絡代数上compactになり、Popescuとperfect dg加群のfiltered-colimit降下で任意の有限jetを保つetale代数化ができる。証明はpapers/reconstruction/one_sided_morita_algebraization.tex。

**具体的nc cubicでこのP_hatの実現・右perfect性・左作用/rotationのcoherenceは未確認。** 固定rank MF、R-perfect Hom、各Artin段階のperfect性だけで満たしたとしない。可換側の一生成子Hの逆像に、一様な有限cell/retract表示を作ることが次の作業。逆核と両逆性を独立に構成する必要はない。

## 既存の依存と禁止する飛躍

v33の幾何学的BCは任意のArtin局所C代数とN>=5の滑らかなcubicに適用できる。ncへの適用は(F)形式MF/Artin残余同値、(D)正則有限対角/乗法的characteristicに依存する。これら全部を今回独立再監査したとは言わない。lambda=1のGとWの形式GL5同型とgeneric圏同値を区別する。

項別自由性だけの生成子持上げ反例を保持する。通常の自己Extの次数制約だけでA∞演算を打ち切らない。SM/ER・smooth proper有限A_n決定性をnc側のsmoothnessなしで使わない。一般lambdaや全Poisson成分の具体核は未構成。

A/Bの全結果、Cの形式MF・window・二次星積・対角・bar・sector・unit・対称性・反例・SM/ERを削除しない。証明全文は現行本文へ統合し、重複する要約だけを保存しない。

## 再現と保存

`python3 scripts/verify_one_sided_morita_assets.py` と `latexmk papers/one_sided_morita_algebraization.tex`。206恒等式等は通常の行列代数模型でありnc compact核の検算ではない。新単独稿5頁を組版・表示確認。A/B/C全体の現行組版と旧全行列再計算は未実施なら明記する。

研究方針の一般原則を守り、区切りごとに承認なしでmainへ全文と再現資産をfast-forward保存する。remote変更を保持、force push・無断PR・GitHub Actions禁止。変更blobを照合する。成功時Libraryへ二重保存せず、実際の失敗時のみ緊急退避。日本語LuaLaTeX、PDFは追跡せずbuild/へ出す。旧ZIP・ログ・cache・重複を除き、数学や証明を容量のため削らない。
