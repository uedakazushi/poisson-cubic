# 研究方針：論文Aの保持と一般次元の可換復元論文B

**2026-11-13 / v72。再開時は最初に読む。GitHub mainが正本。**

## 現在の目的と編集方針

ユーザーの指定に従い、論文Aは引き続きnc-cubicに残す。論文Bは任意の n>=3 に対する代数的中心三次変形の一般点可換復元と、その証明に必要な結果のみを収める。新しい研究結果の追加ではなく、既存結果の自立した公表原稿への整理と独立成果の移管を優先する。

現行入口は `papers/paper_a.tex`（A-v51）と `papers/paper_b.tex`（B-v55）。A・Bの本文と入力ソース、共通TeX設定は今回変更しない。Bの独立成果の移管先はuedakazushi/nc-cubic2で、点スキーム単位を完了したが全体は未完了。残る数学的内容は現行ソースに保持する。

## 論文Bの主結果と自己完結した証明

入力はR=C[h]_(h)上の次数別有限自由な代数的中心三次対で、特殊ファイバーが多項式環と滑らかな三次式となるもの。原稿では、K=C(h)上の幾何学的に滑らかな三次n次元超曲面Yと、有限拡大K'/K上のrotationおよび中心元由来の三次周期比較を保つ全coherent残余圏同値を証明する。全coherent導来圏のsmooth proper性・有限線束生成、可換模型の幾何学的一意性、BFKによる生成上界を同じ主定理の帰結として保持する。

証明は `papers/generic_recovery/` に集約する。

- `main_result.tex`：一般次元の主定理と短い証明。
- `local_model.tex`：次数別noetherian性、有限Koszul持上げ、Gorenstein型、線束Homとproper残余模型。
- `window.tex`：有限rank MFのproper Hom、dg stabilization、三対象windowとrotation。
- `curved_transport.tex`：完備曲率付き移送、関手と逆関手、内部shiftと周期性。
- `generic_descent.tex`：非零Eulerベクトル、固定対象のLaurent局所化、BFK生成、有限降下。
- `coherent_saturation.tex`：有限Hom・smooth対角・線束による検出から全coherent圏へ。
- `gradient_recovery.tex`：低rotation積の同定と、同じ勾配空間を持つ滑らかな三次式の射影的一意性。
- `field_model.tex`：一般点AS正則性、体拡大と低積、可積分性によるG/K、生成上界。
- `references.tex`：この証明に用いる13文献。

必要な自作の補題・証明は本文内に残し、nc-cubic2の未公表支持節への参照だけで代用しない。定理の対象は上の具体的代数的入力であり、任意の抽象的nc cubicの表示、特殊点込み相対同値、同値核のKへの降下、全射影化の可換導来同値は結論しない。原稿に証明があることと、全証明の独立再監査・形式検証・外部査読は区別する。

## 論文Aの保持する成果と未確認点

Aはsmooth cubicのPoisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduliを扱う。active偏微分のgcd、古典Casimir核、普遍交換子minor、Cramer法による中心元構成を保持する。一般次元のquadratic envelope・偏極付きambient復元もAに残す。Pois(X)、固定商stack、相対stackを区別し、Fermat最大性は未証明として扱う。Lie正規形・PBW/AS・普遍中心恒等式などの全独立監査は未完了。Aの研究上の知識は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md` に保持し、今回書き換えていない。

## 独立成果の分離と現在の所在

三次三様体の一次接空間・Plücker障害・categorical KS、独立の相対Artin/étale復元、Sklyanin・多ブロック模型、有限対角/bar/Moritaの別構成、混合族と二次jet、point scheme、有限復元アルゴリズム・反例はB本文に含めない。これらの公表価値は否定せず、nc-cubic2の現行研究へ証明ごと統合する。

**点スキーム単位は移管・統合済み。** nc-cubic2の `papers/mixed_cubic_point_schemes.tex` に、中心元の構成と必要証明、4つのpoint_scheme節、文献を収録した。全文12頁を組版・表示確認し、参照・引用と4検算コードを検証した。ノートは同リポジトリ `notes/mixed_cubic_point_schemes.md`、検証状態は `validation_mixed_cubic_point_schemes.json`。保存確認後に元の専用本文・組版入口・文献断片・コード・再生成できる証明書・重複ノート・旧検査の17ファイルを除外した。元の3証明書の内容は再生成とblob一致している。

**移管全体は未完了。** 一次変形・障害と有限Jacobian復元の2節は移管先に全文保存済みだが、独立原稿への統合・依存・計算資産が未整理。相対理論、明示模型、混合族の二次jet等も残る。元の `mixed_test_family.tex` は点スキームに不要な独立結果を含むため保持する。詳細は `notes/paper_b_scope_and_transfer.md`。旧版を取得しないと再開できない構成にせず、未移管の本文は現行mainに残す。

## 次の作業と達成基準

最優先は移管の完了であり、新しい数学的主張の追加ではない。次は一次変形・Plücker障害と有限Jacobian復元の保存済み2節の独立原稿化を、既存17次元モジュライ研究との重複を照合しながら進める。cft:*、am:*等の引用先の役割を分け、必要証明・文献・計算を揃える。その後、Artin/étale、Sklyanin/多ブロック、相対対角/bar/Morita、混合jetのまとまりごとに同じ移管単位の検証を行う。Aが読むファイルは移管・削除しない。

短くしたBの全証明の通読と一次資料の仮定の再点検は別の課題として保持する。組版成功は証明の正しさを保証しない。主定理を短くするために必要証明を省略したり、未確認の結果を引用済み扱いにしたりしない。

## 再現と実際の確認

B-v55では既存の `.latexmkrc` を使った `latexmk -g -r .latexmkrc papers/paper_b.tex` により27頁の全文を生成し、11個のTeX入力で102ラベル、94参照、37引用、13文献項目を検査した。未解決・重複・overfull・文字欠落は0、全27頁表示確認済み。今回その原稿は変更せず再組版もしていない。PDFは生成物でGit追跡しない。

点スキームの全文組版と計算は移管先で実施済み。静的検査は8入力・47ラベル・22参照・6引用・2文献項目、未解決・重複0。計算は自由代数3恒等式、有限jet、Groebner商長とせん断、標数11の判別式例を扱い、point functor等の全数学的証明を形式化しない。再現は移管先で `python scripts/check_mixed_point_schemes.py --calculations`。

Bの証明の構成・監査範囲は `notes/generic_recovery.md`、原稿のハッシュと状態は `validation_paper_b.json`。Aの再組版、全既存計算の再実行、全数学的証明の独立監査は今回行っていない。

## 研究一般の原則と保存許可

以下は具体的な編集計画と区別する常設原則である。

1. 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して研究価値を最大化する。方針変更は現在有効な理由と解決・未解決の境界として整理し、履歴を蓄積しない。
2. 証明済み、仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在と、記載・独立監査・有限計算を明記し、誤りなら依存する本文・要約・方針を同期して訂正する。
3. 公表稿は一次資料を確認し、既知結果との関係を説明する。文献や新規性を推測で補わず、外部PDFを大量収録しない。
4. 有効な成果と十分な証明を日本語LuaLaTeXで現在の論理順に保持する。軽量化を理由に数学的内容を削らない。
5. ノートは現在有効な着想・計算・反例・障害・文献比較を整理し、会話や作業日誌や重複証明を蓄積しない。
6. 研究方針を入口とし、現在の一式だけで目標・到達点・未解決・着手方法を理解できるようにする。過去の会話や旧ZIPを前提にしない。
7. 一式は現行方針・ノート・論文・必要最小限のコード・入力・証明書とし、履歴・重複・cacheを除く。検証可能性を固定容量に合わせて削らない。
8. ユーザーの保存許可により区切りで承諾を求めずGitHub mainへfast-forward保存し、遠隔ref/blobを確認する。GitHub Actions・force pushは禁止。GitHub正本という個別指定を優先し、Libraryは実際のpush失敗時のみ緊急退避する。既存Libraryファイルの無断削除はしない。生成・検証・組版・保存は別々に報告する。
