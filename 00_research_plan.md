# 研究方針：論文Aの保持と一般次元の可換復元論文B

**2026-11-13 / v73。最初に読む。GitHub mainが正本。**

## 現在の目的と編集方針

論文Aはnc-cubicに残す。論文Bは任意のn>=3の代数的中心三次変形の一般点可換復元と、その証明に必要な結果に集中させる。新しい結果の追加ではなく、完全な証明を備えた公表原稿への整理と独立成果の移管を優先する。

現行入口は `papers/paper_a.tex`（A-v51）と `papers/paper_b.tex`（B-v55）。今回A・Bの本文と入力ソース・共通設定は変更していない。移管先はuedakazushi/nc-cubic2。点スキームと有限Jacobian復元は独立原稿へ統合したが、全移管は未完了であり、残る数学的内容は現行ソースに保持する。

## 論文Bの主結果と証明

R=C[h]_(h)上の次数別有限自由な代数的中心三次対で、特殊ファイバーが多項式環と滑らかな三次式となるものを入力とする。原稿ではK=C(h)上の滑らかな三次n次元超曲面Yと、有限拡大K'/K上のrotation・中心元由来三次周期性を保つ全coherent残余圏同値を証明する。全coherent導来圏のsmooth proper性・有限線束生成、模型の幾何学的一意性、BFK生成上界も保持する。

証明は `papers/generic_recovery/` に集約する。

- `main_result.tex`：一般次元の主定理と短い証明。
- `local_model.tex`：次数別noetherian性、有限Koszul持上げ、Gorenstein型、線束Homとproper残余模型。
- `window.tex`：有限rank MFのproper Hom、dg stabilization、三対象windowとrotation。
- `curved_transport.tex`：完備曲率付き移送、関手と逆、内部shiftと周期性。
- `generic_descent.tex`：Euler非零性、固定対象のLaurent局所化、BFK生成、有限降下。
- `coherent_saturation.tex`：有限Hom・smooth対角・線束による検出から全coherent圏へ。
- `gradient_recovery.tex`：低rotation積の同定と勾配空間による射影的一意性。
- `field_model.tex`：一般点AS正則性、体拡大と低積、可積分性によるG/K、生成上界。
- `references.tex`：証明に用いる13文献。

必要な自作証明をnc-cubic2への参照だけで代用しない。定理は指定された代数的入力に関するもので、任意の抽象的nc cubicの表示、特殊点込み相対同値、同値核のKへの降下、全射影化の可換導来同値を結論しない。証明記載、全独立監査、形式検証、外部査読を区別する。

## 論文Aに保持する成果

Aはsmooth cubicのPoisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduliを扱う。active偏微分gcd、古典Casimir核、普遍交換子minor、Cramer法による中心元構成、一般次元quadratic envelope・偏極付きambient復元を保持する。Pois(X)、固定商stack、相対stackを区別し、Fermat最大性は未証明。Lie正規形・PBW/AS・普遍中心恒等式等の全独立監査は未完了。知識は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md` に保持し、今回変更しない。

## 独立成果の現在の所在

Bに不要な三次三様体の一次接空間・Plücker障害・categorical KS、独立の相対Artin/étale理論、Sklyanin/多ブロック模型、対角/bar/Morita、混合jet、point scheme、有限検査器・反例はnc-cubic2へ証明ごと統合する。公表価値を否定して除外するものではない。

**点スキーム単位は完了。** nc-cubic2の `papers/mixed_cubic_point_schemes.tex` に、中心元の構成と必要証明、4節、文献と4検算コードを統合した。12頁の組版・表示、参照と計算を確認し、元の専用17ファイルを除外済み。ノートは同リポジトリ `notes/mixed_cubic_point_schemes.md`。元の3証明書を正確に再生成できる。

**有限Jacobian復元単位も統合済み。** nc-cubic2の `papers/cubic_jacobian_recovery.tex` は低次数積、可積分性の必要十分条件と有限手順、射影的一意性、Fermat例、積分不可能な完全交差を含む。全14数学的環境をバイト一致で保持し、具体的研究予定は `notes/cubic_jacobian_recovery.md` に置く。6頁の組版・表示と有理数上の検算を実施し、元の証明書と一致を確認した。内容コミットc847894の保存確認後、専用の元本文・コード・再生成可能証明書の3ファイルを除外する。Bに必要な低次数同定・一意性は `gradient_recovery.tex` に残し、共有の文献断片も未移管の支持節用に保持する。

一次変形・障害の節は移管先に全文保存したが統合未完。相対理論、明示模型、混合族の二次jet等も残る。`mixed_test_family.tex` とその検算は点スキーム以外の独立結果を含むので保持する。詳細な所在と残件は `notes/paper_b_scope_and_transfer.md`。既存ノートの旧パスはこの現行所在表で解決し、会話や旧コミットだけを再開の前提にしない。

## 次の課題と具体的着手

最優先は一次変形・Plücker障害の保存済み節を、17次元モジュライ稿と照合して自立させること。cft:*、am:*等の参照が何を入力するか確認し、必要証明・文献・検算をまとめる。その後、Artin/étale、Sklyanin/多ブロック、対角/bar/Morita、混合jetを同じ単位で整理する。移管先mainの保存と必要な検証を終えてから元の重複を除く。Aが読むファイルは移管・削除しない。

短くしたBの全証明の通読と一次資料の仮定照合は別の課題である。組版成功を証明の正しさと混同せず、必要証明の省略や未確認文献の引用済み扱いによって短くしない。

## 再現と確認範囲

B-v55は `latexmk -g -r .latexmkrc papers/paper_b.tex` で全文27頁を生成し、11TeX入力・102ラベル・94参照・37引用・13文献を確認済み。未解決・重複・overfull・文字欠落0、全頁表示確認済み。今回本文を変更せず再組版はしていない。状態とハッシュは `validation_paper_b.json`、依存は `notes/generic_recovery.md`。

移管先の有限Jacobian稿は4TeX入力・17ラベル・19参照・7引用・4文献、未解決・重複0。可積分性行列rank20,24,25、核次元5,1,0、反例minor15872と非対称入力の棄却を検算した。実施範囲は移管先 `validation_cubic_jacobian_recovery.json`、再現は `python scripts/check_cubic_jacobian_recovery.py --calculations`。これは可換多項式の商と線形代数の検算であり、非可換dg Hom・圏同値・全証明の形式検証ではない。

Aの再組版、全既存計算の再実行、全数学的証明の独立監査は今回行わない。PDF・中間物はbuild/に生成しGit追跡しない。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の常設原則である。

1. 重要性、新規性、理解、応用、正確性、実現可能性を総合して価値を最大化する。変更は現在有効な理由と解決・未解決の境界として整理し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在、記載・独立監査・計算を明記し、誤りなら依存する本文・要約・方針を同期して訂正する。
3. 公表稿では一次資料を確認し、既知結果との関係を説明する。文献・新規性を推測で補わず、外部PDFを大量収録しない。
4. 有効な成果と十分な証明を日本語LuaLaTeXで現在の論理順に保持する。軽量化のために数学的内容を削らない。
5. ノートは現在有効な着想・計算・反例・障害・文献比較をまとめ、会話・日誌・重複証明を蓄積しない。
6. 本方針を入口として現行一式だけで目標・到達点・未解決・着手方法を理解できるようにし、旧ZIPや過去会話を前提にしない。
7. 一式には現行方針・ノート・原稿・最小限のコード・入力・証明書を置き、履歴・重複・cacheを除く。検証可能性を固定容量のために削らない。
8. 保存許可により区切りで承諾を求めずGitHub mainへfast-forward保存し、遠隔ref/blobを確認する。Actions・force pushは禁止。GitHub正本の個別指定に従いLibraryは実際のpush失敗時のみ緊急退避、既存Libraryの無断削除はしない。生成・検算・組版・保存は別々に報告する。
