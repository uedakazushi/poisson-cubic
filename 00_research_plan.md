# 研究方針：論文Aの保持と一般次元の可換復元論文B

**2026-11-13 / v76。再開時は最初に読む。GitHub mainが正本。**

## 現在の目的と達成基準

論文A `papers/paper_a.tex`（A-v51）はnc-cubicに残す。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3に対する代数的中心三次変形の一般点可換復元と必要な証明だけに集中する。現在の作業は新しい研究成果の追加ではなく、Bから分離した既存成果をnc-cubic2の自立した原稿へ統合すること。A・Bの本文・入力・共通設定は変更しない。

各移管単位で必要な定理・証明・反例・文献・コードを現行原稿に統合し、参照・全文組版・必要な有限検算・移管先main保存を確認する。その後、元側の他の原稿からの依存を整理して重複を除く。独立稿を作ったことと、元ソースを安全に削除できることは別の状態として扱う。

## 論文Bの主結果と必要証明

R=C[h]_(h)上の次数別有限自由な中心三次対で、特殊ファイバーが多項式環と滑らかな三次式になるものを入力とする。現行稿はK=C(h)上の滑らかな三次n次元超曲面と、有限拡大後のrotation・指定三次周期性を保つ全coherent残余圏同値を述べ、smooth proper性・有限線束生成、模型の幾何学的一意性、BFK生成上界を保持する。

証明は `papers/generic_recovery/` に集約する。`main_result.tex` は主定理と短い証明、`local_model.tex` はnoetherian・Koszul・Gorenstein・線束Hom、`window.tex` は相対stabilizationと三対象、`curved_transport.tex` は完備曲率付き移送と逆、`generic_descent.tex` はEuler非零性・局所化・BFK・有限降下、`coherent_saturation.tex` は全coherentへの拡張、`gradient_recovery.tex` は低rotation積と一意性、`field_model.tex` は基礎体上の方程式、`references.tex` は13文献。

必要な自作証明を移管先への参照だけで代用しない。任意の抽象的nc cubicの表示、特殊点込み相対同値、同値核のKへの降下、全射影化の可換導来同値は結論しない。証明記載と全証明の独立監査・形式検証・外部査読を区別する。

## 論文Aに保持する成果

Aは一般次元のPoisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduliを扱う。active偏微分gcd、古典Casimir核、普遍交換子minor、Cramer法による中心元、quadratic envelope・偏極付きambient復元を保持する。Pois(X)、固定商stack、相対stackを区別し、Fermat最大性は未証明。Lie正規形・PBW/AS・普遍中心恒等式等の全独立監査は未完了。研究上の知識は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md` に保持する。

## 独立成果の現行分担

以下の原稿・同名ノート・validationファイルはnc-cubic2にある。

- `papers/mixed_cubic_point_schemes.tex`：12頁。混合中心式・PBW、点加群の台と厚化、平坦閉包と判別式。必要4検算を保持し、元の専用17ファイルを整理済み。
- `papers/cubic_jacobian_recovery.tex`：6頁。低積・有限可積分性・一意性・Fermat例・非可積分な完全交差。全14数学的環境を保持し、元の専用3ファイルを整理済み。Bに必要な低次数同定と一意性はBにも残す。
- `papers/cubic_first_order_deformations.tex`：v2、13頁。直接的な一次MF比較・五変数Plücker障害・categorical KS、双対数window付録、Todd補正付きHKRの別証明。直接比較の22ラベルとToddの9数学的環境・8ラベルを保持。一次消去は変数数N>=5、Plückerとcategorical KS・Todd側はN=5。専用本文・2コードとTodd本文の計4ファイルを整理済み。既に存在する可換模型の一次係数を消すことと、模型の存在自体を区別する。
- **`papers/cubic_artin_windows.tex`：v1、13頁。独立稿を保存済みだが元ソース整理は未完了。** 一変数の全有限切断R_N=C[h]/h^(N+1)での線束残余/MF比較、正則局所模型のArtin底変更、完備化で生成性・smoothnessが失われる既存反例をまとめた。d>=5変数、次元d-2>=3であり、任意の局所Artin環の定理ではない。比較の主部分17ラベルと必要証明を保持し、反例本文は元と完全一致。方針・依存・再現は `notes/cubic_artin_windows.md`、検証は `validation_cubic_artin_windows.json`。保存を確認した内容コミットは `8b9d77c57094ed3578cdac3d2120b7168303d6a8`。

有限Artin稿の `ar:cor:conditional` は、可換MFとの互換な同値を別途入力する移送の系である。元の `am:cor:formal-residual` の全次数MF存在定理を用いた結論を弱めて置き換えたものではない。その系と広い形式・étale理論は元ソースに保持する。元のArtin比較はmixed・formal・window等からも参照されるため、今回は元本文・反例とも削除しない。

現在の全所在と依存の扱いは `notes/paper_b_scope_and_transfer.md` に記す。相対形式/étale、Sklyanin/多ブロック、対角/bar/Morita、混合jet等の全移管は未完了。`mixed_test_family.tex` とそのコードも保持する。

## 次の具体的作業

最優先は、元の `relative_formal_models.tex` と `relative_etale_models.tex` の形式的持上げ、同値スタック、smoothnessの入力を照合し、既存のArtin比較とつながる自立した原稿へ整理すること。`artin_residual_mf_comparison.tex` 末尾の形式復元系を存在定理の証明ごと統合し、mixed・formal等のam参照も整理してから元の比較・反例を除く。独立稿の存在を依存解消の代用にしない。

続いてSklyanin/多ブロック、対角/bar/Morita、混合jetを、移管先で同時に進む原稿との重複も照合して整理する。Aが読むファイルは移管・削除しない。Bの全証明の通読と一次資料の仮定照合は別の課題として保持し、必要証明や未確認引用を省略して短くしない。

## 再現と実施範囲

B-v55は27頁、11TeX入力・102ラベル・94参照・37引用・13文献で、既存の全文組版・表示検査は未解決・重複・文字欠落・overfullが0。今回本文を変更せず再組版していない。状態は `validation_paper_b.json`、依存は `notes/generic_recovery.md`。

今回の有限Artin稿は `python scripts/check_cubic_artin_windows.py --calculations --build` で参照・検算・LuaLaTeXを実行した。7TeX入力・31ラベル・36参照・11引用・5文献、全13頁表示確認、未解決・重複・文字欠落・overfullは0。四次元dg模型についてQQ[h]上の64結合律、16Leibniz則、8単位条件、d²=0、一般/特殊cohomology次元と6有限切断のrankを検算した。Morita同値・全Nの生成性・smoothness・MF比較を計算機形式証明したものではない。

以前の原稿の算術検算は既存記録として保持し、今回再実行していない。Aの再組版、全既存計算、全数学的証明の独立監査は未実施。PDF・中間物・再生成可能出力はbuild/で非追跡。

## 研究一般の原則と保存許可

以下は固有の編集計画とは別の常設原則である。

1. 重要性・新規性・理解・応用・正確性・実現可能性を総合して価値を最大化する。変更は現時点の理由と解決・未解決の境界として整理し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在と記載・監査・検算の差を明示し、誤りなら依存する本文・要約・方針も訂正する。
3. 公表稿は一次資料を確認し、既知結果との関係を示す。文献・新規性を推測で補わず、外部PDFを大量収録しない。
4. 有効な成果と十分な証明を日本語LuaLaTeXで現在の論理順に保持し、軽量化のために数学的内容を削らない。
5. ノートは現在有効な着想・計算・反例・障害・文献比較をまとめ、会話・日誌・重複証明を蓄積しない。
6. 現行方針・ノート・論文・必要資産だけから再開できる一式を保ち、旧ZIPや過去会話を前提にしない。
7. 履歴・重複・cacheを除き、固定容量のために検証可能性を削らない。必要な入力・証明書・再現手順を保持する。
8. 保存許可に従い区切りで承諾を求めずGitHub mainへfast-forward保存し遠隔ref/blobを確認する。Actions・force pushは禁止。Libraryは実際のpush失敗時のみ緊急退避し、既存Libraryを無断削除しない。生成・検算・組版・保存を分けて報告する。
