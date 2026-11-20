# 三次超曲面のPoisson構造と量子化：現行研究ノート

2026-11-21 / v95。主公表原稿はPoisson量子化論文（A-v61）。最初に[研究方針](../00_research_plan.md)を読む。

## 正規形から量子化へ

[論文A](../papers/nc-cubic.tex)に全次元Poisson正規形、Bondalの下界、代数的量子化、固定・相対成分の証明を置く。仮定と今回の確認範囲は[投稿準備監査](poisson_article_submission_audit.md)、中心元の構成と障害は[中心元ノート](universal_casimir.md)を参照する。

三次四様体のrank4 Poissonは(3,3)分離型およびambient Hessian階数≤3軌跡内の平面で判定できる。後二者の同値はBricalli–Favale–Pirolaの既知定理である。可約Hessianだけでは不十分な例、全r>=2の同次数持上げ障害、および文献比較の残る範囲は[幾何ノート](bondal_cubic.md)に整理する。

階数二の全supportで共変な中心元を選ぶ問題は、`intrinsic_rank_two_center.tex` のBott消滅・Stiefel延長・有限核の完備化で解決し、普遍Hessian二次jetも指定できる。gcd(N,3)=1なら全被約階数二Poisson層へ実際の代数族が降り、N=5では全非零Poisson対が対象になる。一般次元でも三次Veroneseは降下する。全階数二層のgerbeの位数はgcd(N,3)であり、3|Nなら重み1の可逆層は存在しない。全fと非零Poisson係数を使う補空間選択は存在せず、自由な中心平行移動の商は非アフィンである。この障害は中心核そのものの持上げを妨げない。

満support N=3kでは `full_support_quantization.tex` に、順序を底に加えない共変中心元と三次Veronese降下を証明した。内在的な有限étaleブロック被覆、還元安定化群によるアフィン軌道、適合係数空間上の有限jetの直接持上げを用いる。中心商の正則性は一ブロックfiltrationで証明し、テンソル積全体のdomain性を仮定しない。全被約rank2k層の底の次元は満supportで2k、三次四様体のrank4では4である。全非零階数層のgerbeの位数gcd(N,3)はFermat安定化群の交換子から求まり、Picard群の消滅を要しない。各主張の証明・仮定と既知のアフィン商の入力は本文に置く。

g=0のΩ=sym(f)の全h公式と、節点・尖点の特異点直線ℓ_gによる全mでの降下は、各層の具体的な構成として保持する。節点の中心元にはCMRの既知明示公式を用いる具体的な規格化とパラメータ対応もある。N>=6では零制限の標準中心直線を全support上で一致させることは、P重み2の純中心切断の消滅と非零Hessianによって不可能である。相対障害∂(H_Z/12)と滑らかな例を中心元ノートに整理した。次の存在問題はm>0、k>=2での分解・純中心配分を忘れた整合である。古典核の完全列 0→Sym³(V/W_P)*→K_0→E_perm→0、古典Fの対角切断、H¹と有限アフィン模型への延長を中心元ノート§3から調べる。三次偏極の族を基準とする別ambientやMorita/qgrの比較も残る。固定非零hでの同型類像、全閉ファイバーのqgr滑らかさも別の問題として残る。

## 独立な相対構成・明示模型

点スキーム、有限Jacobian復元、一次変形、Artin window、étale実現、相対復元の現行原稿は[nc-cubic2](https://github.com/uedakazushi/nc-cubic2)に一覧がある。[nc-cubic2の現行研究ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/relative_reconstruction_models.md)には、有限模型からのrotation積の比較、未決定の同変高次係数、有限bar右逆、二つ以上の無限位数因子の生成性、Artinから完備底への障害を整理している。これらの個別構成に残る条件と、論文Bの一般点存在定理の仮定・結論を混同しない。

証明記載、数学的な点検、有限計算、組版、形式検証、新規性の確認は別の状態である。現在の検証範囲は [Aのvalidation](../validation_paper_a.json) に置く。旧論文Bの現行資料は [nc-cubic-n-fold](https://github.com/uedakazushi/nc-cubic-n-fold) を正本とする。
