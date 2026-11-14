# 現在の研究分担と障害

2026-11-14 / v93。論文AはA-v60、論文BはB-v59。最初に[研究方針](../00_research_plan.md)を読む。

## 論文A：正規形から量子化へ

[論文A](../papers/paper_a.tex)に全次元Poisson正規形、Bondalの下界、代数的量子化、固定・相対成分の証明を置く。仮定と今回の確認範囲は[投稿準備監査](poisson_article_submission_audit.md)、中心元の構成と障害は[中心元ノート](universal_casimir.md)を参照する。

三次四様体のrank4 Poissonは(3,3)分離型およびambient Hessian階数≤3軌跡内の平面で判定できる。後二者の同値はBricalli–Favale–Pirolaの既知定理である。可約Hessianだけでは不十分な例、全r>=2の同次数持上げ障害、および文献比較の残る範囲は[幾何ノート](bondal_cubic.md)に整理する。

階数二の全supportで共変な中心元を選ぶ問題は、`intrinsic_rank_two_center.tex` のBott消滅・Stiefel延長・有限核の完備化で解決し、普遍Hessian二次jetも指定できる。gcd(N,3)=1なら全被約階数二Poisson層へ実際の代数族が降り、N=5では全非零Poisson対が対象になる。一般次元でも三次Veroneseは降下する。全階数二層のgerbeの位数はgcd(N,3)であり、3|Nなら重み1の可逆層は存在しない。全fと非零Poisson係数を使う補空間選択は存在せず、自由な中心平行移動の商は非アフィンである。この障害は中心核そのものの持上げを妨げない。

g=0のΩ=sym(f)の全h公式と、節点・尖点の特異点直線ℓ_gによる全mでの降下は、各層の具体的な構成として保持する。節点の中心元にはCMRの既知明示公式を用いる具体的な規格化とパラメータ対応もある。N>=6では零制限の標準中心直線を全support上で一致させることは、P重み2の純中心切断の消滅と非零Hessianによって不可能である。相対障害∂(H_Z/12)と滑らかな例を中心元ノートに整理した。次の核心は複数ブロックの分解・純中心配分を忘れた整合、および三次偏極の族を基準とする別ambientやMorita/qgrの比較である。固定非零hでの同型類像、全閉ファイバーのqgr滑らかさも別の問題として残る。

## 論文B：一般点復元の有効化と降下

[論文B](../papers/paper_b.tex)の必要証明は `papers/generic_recovery/` 内で完結する。[案内](generic_recovery.md)と[証明監査](paper_b_proof_audit.md)から、適用仮定と証明の所在を確認できる。

Hesse--Sklyanin族では、直接計算した二次jet W_rec=F+h xyz+(h²/3)xyz+O(h³) と、全次数のHesse正規形 W_H=F+[(h+h²/3+h⁵/12)/(1−h⁴/4)]xyz を得た。楕円曲線の比較によってK上の方程式が確定したので、次の中心課題は同値核・拡大次数と、非可換入力からの低rotation積の全行列である。まず三対象stabilizationの有限Hom模型からrotation核と対角を表示し、次数一・二の空間と積を取り出す。証明・計算の所在はBの案内へ集約する。eye無しの積とharmonic-angle中心写像を混ぜないこと、任意のLaurent行列に完備Taylor和を直接評価しないことを再開時の注意とする。同値核のK降下や特殊点を含む代数的相対同値は、方程式の明示化とは別に残る。

## 独立な相対構成・明示模型

点スキーム、有限Jacobian復元、一次変形、Artin window、étale実現、相対復元の現行原稿は[担当境界ノート](paper_b_scope_and_transfer.md)に一覧がある。[nc-cubic2の現行研究ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/relative_reconstruction_models.md)には、有限模型からのrotation積の比較、未決定の同変高次係数、有限bar右逆、二つ以上の無限位数因子の生成性、Artinから完備底への障害を整理している。これらの個別構成に残る条件と、論文Bの一般点存在定理の仮定・結論を混同しない。

証明記載、数学的な点検、有限計算、組版、形式検証、新規性の確認は別の状態である。A/Bについての現行の実行範囲は [Aのvalidation](../validation_paper_a.json)、[Bのvalidation](../validation_paper_b.json)に置く。
