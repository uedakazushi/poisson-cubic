# AGENTS.md — nc-cubicの継続指示

**正本はGitHub `uedakazushi/nc-cubic` の `main` のみ。研究再開時は必ず `00_research_plan.md` と `research_notes.md` を最初に読む。** `README.md` と `reconstruction/README.md` は再現入口。

## 最優先目標
- 一般次元n≥3、全Poisson既約成分の一般点におけるrotation付き可換復元定理の完成。
- 当面は非楕円（節点・尖点）二成分の残余対角perfect性(SM)を有限証明書 `P→Gamma_R` で示し、局所実現原理(ER)の変形・代数化論を独立監査する。
- 現行成果：`reconstruction/tex/rotation_saturation_reduction.tex` に局所rotationの逆関手、SMからfull coherent比較と有限型spread、SM・ER付きgeneric復元の議論を全文収録。論文A/B/Cと境界研究の既存証明は保持する。

## GitHub正本・再現・保存の永続規則
1. **GitHubからclone/pullするだけで研究を再開・主要原稿を再生成できる状態を常に維持する。** ChatGPT会話・Library・旧ZIP・外部の一時ファイルを前提にしない。
2. 研究の区切りごとに、現在の方針・ノート・公表原稿の**証明全文**・必要なコード/入力/証明書/再生成手順を `main` にpushする。ノートだけのpushを全文保存と呼ばない。
3. commitを作る前に既存リモートheadを確認し、通常のfast-forwardのみで更新する。force push/無断PR/GitHub Actionsは使わない。push後は遠隔refと主要ファイルを再取得し、GitHub反映を検証する。生成・検算・組版・GitHub登録・remote確認は別々に報告する。
4. **ChatGPT Libraryへの保存はGitHub pushが実際に失敗した場合の緊急避難に限る。** 成功した場合は保存しない。退避時は未同期とGitHub復帰手順を明示し、GitHub以外を正本にしない。既存Libraryファイルは明示的指示なしに削除しない。
5. `reconstruction/README.md` の検算・LuaLaTeX再生成を実行し、ソース/PDFの同一性を確認する。親三論文は `python3 scripts/build.py` で組版できる構造を維持する。生成PDF・中間物・旧アーカイブ・履歴を無駄に蓄積せず、必要な証明や検証資産は削らない。
6. 研究成果は現行の論理順に統合し、過去の会話や更新記録だけで代用しない。論文A=Poisson/量子化、B=17次元とambient、C=rotation/可換復元。第四の主論文を不用意に作らない。

## 数学的な正確性
- 証明済み・条件付き・未完成・予想・計算的観察を分け、仮定、依存、証明所在、未解決の核心を示す。原稿内の証明と今回独立監査した証明と実行済み計算を混同しない。
- (A/(\Omega)) が中心三次商AS-regularであるだけでは、smooth proper残余や可換模型を結論しない。全点AS類とPoisson量子化成分の一般点を区別する。rotationの可逆性と `rho^3=[2]` のcoherent同定も区別する。
- 重要な文献は一次資料で仮定・参照箇所を検証し、新規性未確認なら明記。誤りなら依存箇所まで直し、再発防止に必要な反例・障害だけをノートに残す。
- 日本語LuaLaTeXを既定とし、論文は現在有効な証明を削らず整理する。PDFの最新性は実際の組版結果だけで判断する。

これらは永続運用原則であり、具体的研究計画は `00_research_plan.md` に置く。
