# AGENTS.md — nc-cubicの継続指示

**GitHub `uedakazushi/nc-cubic` の `main` だけが正本。** 最初に `00_research_plan.md`、次に `notes/research_notes.md`、`reconstruction/README.md` を読む。旧ZIP・会話・Libraryを再開の前提にしない。

## 研究目標（三つに限定）

1. **Poisson構造の構造定理**：任意の滑らかなcubic \(X^n\)、\(n\ge3\) 上のPoisson構造のJacobianブロック正規形・一般階数。論文Aの `papers/sections/poisson_geometry.tex`、定理 `thm:pg-normal` に証明あり。
2. **個別Poisson構造の代数的量子化**：\(X^n\subset\mathbb P^{n+1}\) とそのPoisson構造に対し、非可換 \(\mathbb P^{n+1}\) を表すKoszul AS-regular代数と中心三次正則商を代数的な一パラメータ族で構成する。論文Aの `thm:pg-quantization` に証明あり。各固定Poisson構造についての存在と、全Poisson係数空間上の一様相対量子化を混同しない。
3. **構成した非可換cubicのrotation付き可換復元**：目標2の量子化のgenericファイバーに対する可換cubicのKuznetsov成分とのenhanced pair同値。最優先、未完成。残余対角perfect性(SM)の証明を最初に狙う。

目標1・2を「完成」と呼ぶときは**原稿に定理・証明がある**という意味。文献・論理の徹底的独立監査はまだ必要。全AS-regular三次商の全点復元は反例があり範囲外。Poissonスキームの全成分の完全分類、ambientの一意復元、閉公式等は最終達成条件に含めない。これらの既存の価値ある成果は維持し、破棄しない。

## 最優先の研究

三目標のうち目標3のrotation付き可換復元を最優先する。固定Poisson構造ごとに目標2が保証する量子化族のgenericファイバーを扱い、可能なら各Poisson既約成分のgeneric点へ相対化する。
現在、実在するsmooth proper pairに対するétale局所実現(ER)は `papers/reconstruction/etale_realization.tex` に、同値双加群の障害消去による証明がある。これは残余smoothnessを証明する定理ではない。

当面は節点・尖点二成分の残余対角perfect性(SM)を、有限perfect双加群と実際の射 `P→Gamma_R` で示す。量子化が得られた成分では、SMからfull coherent比較、pairのspread、ER、generic可換復元へ進む。Poisson係数方向も同時に動かす相対量子化入力は全成分に対して未完成で、目標2の個別存在定理とは区別する。

現行の独立組版入口は `papers/reconstruction/rotation_saturation_reduction.tex`。局所rotationの逆、gluing、full coherent比較、spreadの既存の全証明を保持する。三論文A/B/Cと独立境界研究を削除・要約で代替しない。

## 永続的な保存・再現規則

1. 研究の区切りには、方針・ノート・公表原稿の**証明全文**・必要なコード/入力/証明書/再現手順をmainへpushする。要約だけのpushを全文保存と呼ばない。
2. 事前にremote headを確認し、追加変更を保持して通常のfast-forwardだけで更新する。force push、無断PR、GitHub Actionsは使わない。push後にremote refと主要ファイルのblob SHAを再確認する。
3. **ChatGPT Libraryへの保存は、GitHub pushが実際に失敗した場合の緊急避難に限る。** 成功時には保存しない。退避時は未同期と復帰方法を明示する。既存Libraryファイルの削除は明示指示なしに行わない。
4. `reconstruction/README.md` の検算・組版・検証を実行する。新しいTeX inputは全てbuild receiptのハッシュと参照検査に含める。PDFはソースから再生成し、不要なバイナリ・旧版・ログ・キャッシュは蓄積しない。
5. 親論文A/B/C全体の組版は `python3 scripts/build.py`。未実行なら独立組版の成功と混同しない。生成・数学的監査・計算・組版・GitHub反映・遠隔確認を区別して報告する。

## 現在の障害理論の追加データ
- `papers/reconstruction/hochschild_obstructions.tex` にBFK sector公式から `HH³(Ku(X))^rho=0`（全n≥3）を導出し、非楕円cubic fivefoldで `HH³=0` を示した。形式的第一障害の消滅をSMの証明と混同しない。
- `reconstruction/computations/verify_hochschild_sectors.py` に有限次元の整数sector検算を記録。既知の外部定理の証明やHochschild群の形式化とは呼ばない。

## 数学的な正確性

証明済み、条件付き、未完成、予想、計算的観察を区別し、仮定と所在を示す。証明の記載と今回の独立監査を混同しない。

SMなしにERを適用しない。perfect対象moduliの代数性だけで可換模型を結論しない。ERでは障害のrotation不変性、幾何的KSの全射、HH¹消滅によるintertwinerの持上げ、代数性、無限小smoothness、étale sectionを全て確認する。

中心三次商やambientの対角だけから残余smoothnessを結論しない。自己同値性と、指定した `rho^3=[2]` のcoherenceは別である。35係数sliceの計算はSMや復元写像の閉公式を証明しない。

一次資料で仮定・参照箇所を確認し、新規性未確認なら明記する。誤りがあれば依存する本文・要約・方針も直す。日本語LuaLaTeXを既定とし、現在有効な証明を論理的な順序で保持する。

## 永続的なディレクトリ・ビルド・PDF規則（2026-11-10）

1. 主要公表原稿は `papers/`、研究ノートは `notes/` に置く。公表前の未完成結果も証明全文を保持する。再開はルート `00_research_plan.md` から始める。
2. 原稿やノートを移動するときは全 `\\input`、引用・参照、検算・ビルドスクリプト、検証台帳のパスを同時に直す。旧パスに重複するファイルを残さない。
3. 組版はルート `.latexmkrc` と `latexmk papers/rotation_cubic_reconstruction.tex` などを使い、LuaLaTeXで `build/` にPDFと中間生成物を作る。生成PDFはGitで追跡しない。例外の `papers/pdf-only/` は完全な原稿TeXを未確認の原本だけで、内容を失わないよう保持する。
4. 再現テストは `python3 scripts/verify_bundle.py`、`python3 reconstruction/scripts/build.py`、`python3 reconstruction/scripts/verify.py`。実行していない組版や数学的形式検証を成功したと報告しない。
5. 正本はGitHub `main`、LibraryはGitHub push実失敗時のみの緊急退避。GitHub Actions、force pushは使わない。

※ PDF原本のうち研究ノート二本は `notes/pdf-only/`、論文系六本は `papers/pdf-only/` に分類した。その他のPDFは生成対象でありGit追跡しない。

## 主目標に集中するための分離規則（2026-11-10）

- [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) に移した独立境界TeX（Pfaffian/Brill–Noether）と中心判別式・検算の全文を、本リポジトリで重複保守しない。必要な数式・補題は主論文A/Cに自立して記載する。
- **可換復元（SM）最優先**。移管後の詳細なPDF全面TeX化や周辺モジュライの完全分類より、非楕円二成分の実際の残余対角有限perfect証明書を優先する。
- `notes/sm_bar_and_spreading.tex` に有限bar段階のretract判定・generic spreadingの完全な証明を記載した。**generic smoothness が既に判明すれば**局所化上の相対smoothnessが得られるが、特殊ファイバーのsmoothnessだけからgenericを結論しない。有限barの右逆を実際に持ち上げることを優先する。
- `notes/source_recovery/dg_perfectness_counterexamples.tex` にArtin切断や特殊ファイバーのperfect性だけから相対perfectnessが従わない反例を保持する。ただし特殊ファイバーdg代数自体がsmoothでないため、これをSM失敗の反例とは扱わない。
- 例外的に追跡中のPDF原本は転送・全定理照合を確認するまで保持する。GitHubに反映したと報告するのは遠隔コミットとblobを再取得できた場合だけ。

## A∞経路の現行研究指示（2026-11-10）

- 可換復元のSMは線束生成子 `Lambda_R` の相対smoothnessと同値。既知の半直交分解smoothness定理を適用して証明した `papers/sections/minimal_ainfty_arity.tex` を最初に参照する。残余Gammaの非明示的な対角の代わりにLambdaの有限bar対角を計算する。
- `H=H^0⊕H^n`、strictly unital minimal A∞の演算arityは `k=2 (mod n)`。fivefoldで最初が$m_7$、次は$m_{12}$。$m_7$のHochschild類、二次障害$[m_7,m_7]$を分けて計算する。
- `computations/verify_minimal_ainfty_arity.py` と証明書は対象指数の必要条件のみを検算する。実際の$m_7$係数やSM成立を計算済みと主張しない。
- 係数を求めるには、`papers/sections/nonelliptic_quantization.tex` の具体的二パラメータ代数と、`papers/sections/local_projective_model.tex` のHom/底変更を使って相対dg縮約$(i,p,h)$を選ぶことが最初の課題。高次積すべてを$m_7$だけで代替してはならない。
