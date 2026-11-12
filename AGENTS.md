# AGENTS.md — nc-cubic 現行研究・開発指針

**2026-11-12 / v66。** mainが正本。最初に `00_research_plan.md` を読む。
A `papers/paper_a.tex`（A-v51）とB `papers/paper_b.tex`（B-v50）が現行主原稿。

## 現在の主定理と次の作業

指定した次数別有限自由な代数的中心三次変形・smoothな可換特殊ファイバーという入力について、三対象windowが(L)を、`complete_curved_transport.tex` が(CF)と(CF_3)を構成する。これらを独立の追加仮定へ戻さない。主定理は元の体上のcubic模型と有限拡大後の全coherent残余pair同値。正則多変数局所基底にも成立する。任意の抽象的nc cubic圏の表示は証明していない。

完備曲率移送は、通常のgraded unital formality、有限三次式空間のC_pi逆写像、勾配Koszul、arity1,3のflow、F_(2r+1)∈m^r、固定次数内のtwistingの収束、相互逆性とt多重線形な周期比較の順序。曲率はm小とは仮定せず、関数入力高々一個というグラフ次数で処理する。普通のcurved Hochschild cohomologyをJacobian環と同一視しない。

一次消滅の独立証明は `first_order_poisson_kernel.tex`。Jacobiを使わず曲率付きHKRのarity3境界で一次の非可換変形を消す。五変数では二次Hochschild障害のJacobi係数イデアルが五本のPlücker二次式と一致する。JLLZ Theorem 4.4(2)とArtin残余比較により、可換点でのcategorical KS写像20→10は全射・核10。これらと一般非零Poisson点の核7を混同しない。残る一次可換変形はJac(F)_3に値を持ち、cubic threefoldでは10次元。nc-cubic2の17次元族への接空間対応は未照合。今後は新結果を増やすより論文Bの編集・証明の独立監査を優先する。既存の完全な証明を削らず、序論・主結果・支持節の整合と先行研究引用を改善する。次は完備移送と既存window・降下・飽和の独立再点検、全文静的検査・組版・公表構成、非可換低Natの有効計算を優先する。原稿の証明を構成したことと全支持節・全計算の再監査完了は別。一般点の存在の前に(D)や低積の実計算を要求しない。(D)は特定の明示式の照合として残す。K上の方程式と同値核の定義体を混同しない。

Aの代数的量子中心にformalityを必須入力として戻さず、Lie正規形・PBW/AS・Hesse・Bondal・成分の監査を継続。17次元モジュライとambient周期性はnc-cubic2に保持する。

論文BはI:主定理を支える比較、II:可換点の変形、III:相対形式・étale、IV:明示量子化、V:point schemeの五部構成。数学的主張・証明・反例を削らず、各部の追加条件と一般点定理の結論を混同しない。今後は新しい研究結果を増やすより、公表本文の推敲と全文引用・組版検証を優先する。

## 保存・再現

有効な既存証明・反例・必要証明書を保持し、状態説明は現行内容に同期する。日本語LuaLaTeX、PDF・中間物はbuild/で非追跡。GitHub mainへfast-forward、遠隔ref/blob確認、Actions・force pushなし。Libraryはpushの実失敗時のみ緊急退避。

`python3 computations/verify_complete_curved_transport.py --output build/complete_curved_transport_checks.json` は有限代数・余積・arityの検算であり、graph積分や圏同値の形式検証ではない。抜粋は `latexmk papers/support/papers/complete_curved_transport.tex`。全Bの組版とは区別する。最新の証明状態は `notes/paper_b_proof_audit.md`、実施検証は `validation_paper_b.json`。
