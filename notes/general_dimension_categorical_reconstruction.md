# 論文B：一般次元のrotation付き一般点復元

**2026-11-12 / B-v46。** 最初に `00_research_plan.md`、続いて `notes/paper_b_proof_audit.md` を読む。

代数的・次数別有限自由な中心三次対、滑らかな可換特殊ファイバーという入力から、三対象windowで(L)、完備曲率移送で(CF)と(CF_3)を構成する。比較条件を独立に仮定せず、K=C(h)上のsmooth cubic模型と有限拡大上のrotation付き全coherent残余圏同値を得る。模型は全n>=3で幾何学的に一意。正則多変数局所基底にも同じ一般点定理が成立する。

主定理は `papers/support/papers/reconstruction/general_dimension_recovery.tex`、局所比較は `three_object_window.tex`、形式比較の現行証明は `complete_curved_transport.tex`、模型降下は `generic_cubic_descent.tex`（同ディレクトリ）。全MF比較を固定三対象に制限してから局所化し、任意Laurent対象へ無限Taylor和を評価しない。古い支持節の比較条件は、これらの構成定理から入力する。

(D)と非可換低Natの明示行列は有効化の課題。方程式と同値核の定義体は別であり、K上の模型の一意性、特殊点込み相対同値、全射影化の導来同値、全nc cubicの表示は主張しない。既存の二次jet・明示混合族・相対Artin・point scheme・反例の証明は保持する。

一次の非可換変形をJacobian接空間へ写す直接的な証明は `first_order_poisson_kernel.tex` に置く。これは全次数formalityに依存しない。さらに五変数では二次Hochschild障害のPlücker五式がスキーム論的な障害イデアル全体となることを `first_order_poisson_kernel.tex` に証明した。JLLZの既知η同型から可換点でのcategorical KS接空間完全列は20→10、核10と確定。cubic threefoldでJacob(F)_3は10次元であり、nc-cubic2の17次元族との7方向の対応は未確認。最新検証は `validation_paper_b.json`。証明記載と今回の主要論証点検、全支持節の独立監査、有限計算、全文組版、形式検証、外部査読・包括的新規性調査を区別する。
