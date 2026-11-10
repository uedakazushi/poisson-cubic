# AGENTS.md — nc-cubic研究継続

**2026-11-11 / v33。GitHub mainが唯一の正本。** 最初に00_research_plan.md、次にnotes/geometric_rotation_basechange.mdを読む。旧ZIP・会話を再開の前提にしない。

## 最優先と到達基準

構成した代数的nc cubicの一般点を、同じKuと指定rotationを持つ可換cubicへ復元する。方程式は有限代数計算で抽出する。形式同値・方程式の代数性・generic圏同値を区別する。

**一般MF核全忠実性(KF)を先行課題にしない。** 既存形式残余同値で可換Kuへ移し、幾何学的射影核Pとrotation核Qから真のNat複体を作る経路を用いる。新本文はpapers/reconstruction/geometric_rotation_basechange.tex。

## 現在使える結果

- 任意のArtin局所C代数上、滑らかなN>=5変数cubicの低Nat標的はperfect kernel Homで計算でき、H0は自由rankN,binom(N,2)。全Artin底変更と積が両立する。座標とその合成の閉基底持上げを使い、独立v・対称性・H1消滅を要求しない。
- 既存入力(F)=全Artin形式MF/残余pair同値、(D)=正則有限対角/乗法的characteristic写像の下で、ncのBCは従う。lambda=1のG_h+v^3とW_hは形式GL5同型。新証明は(F),(D)を独立に再証明したものではない。
- 項別自由性だけでArtin生成性を持ち上げる一般補題は偽のまま。正の内部次数MFのHomのR-perfect性、導来特殊化、compact生成性を別々に確認する。gr:lem:derived-generationは追加条件を明記した有効な形。
- 既存の有限対角、bar比較、中心対称性、相対sector、unitの結果を削除しない。一般KF自体の未解決性を、幾何学的BCの未解決性と混同しない。

## 次の証明

指定nc残余生成子の形式MF像を明示的Gの側で追跡する。有限cell/retractの双加群P,Q、両合成の逆性、rotation intertwinerを同時に構成する。Artin次数に依存しないcell/shift上界を証明して有限代数方程式へ落とす。generic生成性と同値双加群の代数性はまだ未証明。smoothnessを仮定する有限A_n決定性を循環的に使わない。SM/ERは別経路として維持する。

一般lambdaと高次元各Poisson成分の具体抽出は未完成。新しい幾何学的BCの一般性だけで、一般nc積が計算できたとは言わない。

## 保存・再現・正確性

研究方針の一般原則に従う。証明全文、必要なコード/証明書、原稿inputと文献をmainに通常のfast-forwardで自動保存する。force push・無断PR・GitHub Actionsは禁止。要約だけを全文pushと呼ばない。remote refと全変更blobを照合する。成功時のLibrary二重保存は不要、実際のGitHub失敗時のみ緊急退避。既存Libraryファイルは無断削除しない。

日本語LuaLaTeX、latexmkでbuild/へ生成しPDFをGit追跡しない。有効な数学的内容・証明・再現性を容量制限のため削らない。過去版や作業ログ・cacheを追加しない。

`python3 scripts/verify_geometric_rotation_assets.py` と `latexmk papers/geometric_rotation_basechange.tex` を用いる。新計算は有限自由複体とsector算術だけであり、カテゴリカル定理やv27全行列の形式検証ではない。A/B/C全体の組版は未実施なら明示する。生成・計算・組版・保存は別状態。新規性の網羅的確認・外部査読・Lean検証は未実施。
