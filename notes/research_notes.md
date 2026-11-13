# 現在の研究分担と障害

2026-11-14 / v91。論文AはA-v58、論文BはB-v59。最初に[研究方針](../00_research_plan.md)を読む。

## 論文A：正規形から量子化へ

[論文A](../papers/paper_a.tex)に全次元Poisson正規形、Bondalの下界、代数的量子化、固定・相対成分の証明を置く。仮定と今回の確認範囲は[投稿準備監査](poisson_article_submission_audit.md)、中心元の構成と障害は[中心元ノート](universal_casimir.md)を参照する。

三次四様体のrank4 Poissonは(3,3)分離型およびambient Hessian階数≤3軌跡内の平面で判定できる。後二者の同値はBricalli–Favale–Pirolaの既知定理である。可約Hessianだけでは不十分な例、全r>=2の同次数持上げ障害、および文献比較の残る範囲は[幾何ノート](bondal_cubic.md)に整理する。

g=0ではΩ=sym(f)が全パラメータで中心となり、全ブロック群への同変性も備える。support平面がXに含まれる層上でのgerbe族と、gcd(m,3)=1での全hの降下は本文に証明した。節点・尖点の各軌道でも全G同変中心元を得た。一意な特異点直線ℓ_gでA_dをℓ_g^dだけ捻ると中心スカラーの重みが消え、全mでそのPoisson層の零h切断近傍へ代数族が降りる。次の核心は型の境界をまたぐ整合、可約・非被約制限、および複数ブロックの分解・純中心項の配分を変えた一般の整合性である。不可約全域でのδ_g依存の左逆の延長障害と、接する直線＋conic軌道の非分裂は中心元ノートに保持した。全係数空間での中心元の存在と、全Poissonモジュライへの降下を分けて扱う。固定した非零変形パラメータにおける非可換代数の同型類の像の次元、全閉ファイバーのqgrの滑らかさも別の課題である。

## 論文B：一般点復元の有効化と降下

[論文B](../papers/paper_b.tex)の必要証明は `papers/generic_recovery/` 内で完結する。[案内](generic_recovery.md)と[証明監査](paper_b_proof_audit.md)から、適用仮定と証明の所在を確認できる。

Hesse--Sklyanin族では、直接計算した二次jet W_rec=F+h xyz+(h²/3)xyz+O(h³) と、全次数のHesse正規形 W_H=F+[(h+h²/3+h⁵/12)/(1−h⁴/4)]xyz を得た。楕円曲線の比較によってK上の方程式が確定したので、次の中心課題は同値核・拡大次数と、非可換入力からの低rotation積の全行列である。まず三対象stabilizationの有限Hom模型からrotation核と対角を表示し、次数一・二の空間と積を取り出す。証明・計算の所在はBの案内へ集約する。eye無しの積とharmonic-angle中心写像を混ぜないこと、任意のLaurent行列に完備Taylor和を直接評価しないことを再開時の注意とする。同値核のK降下や特殊点を含む代数的相対同値は、方程式の明示化とは別に残る。

## 独立な相対構成・明示模型

点スキーム、有限Jacobian復元、一次変形、Artin window、étale実現、相対復元の現行原稿は[担当境界ノート](paper_b_scope_and_transfer.md)に一覧がある。[nc-cubic2の現行研究ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/relative_reconstruction_models.md)には、有限模型からのrotation積の比較、未決定の同変高次係数、有限bar右逆、二つ以上の無限位数因子の生成性、Artinから完備底への障害を整理している。これらの個別構成に残る条件と、論文Bの一般点存在定理の仮定・結論を混同しない。

証明記載、数学的な点検、有限計算、組版、形式検証、新規性の確認は別の状態である。A/Bについての現行の実行範囲は [Aのvalidation](../validation_paper_a.json)、[Bのvalidation](../validation_paper_b.json)に置く。
