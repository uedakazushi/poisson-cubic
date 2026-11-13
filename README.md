# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

2026-11-14 / v88。再開は [研究方針](00_research_plan.md) から。

| 現行論文 | 内容 |
| --- | --- |
| [論文A](papers/paper_a.tex)（A-v56） | 全次元Poisson正規形・Bondal予想・代数的量子化・固定相対モジュライ（ambient復元は付録） |
| [論文B](papers/paper_b.tex)（B-v58） | 任意のn>=3の中心三次変形の一般点可換復元と必要証明 |

論文Aは、全次元正規形・Bondalの下界・全Poisson構造の代数的量子化・Fermatと相対モジュライの成分数を中心に整理している。三次四様体の一般階数四の構造を分離型F=f+gで分類し、その正規な退化因子とmodular場を直接計算して純楕円型であることを示す。Bricalli–Favale–Pirolaの既知の分解判定を合わせると、この存在は周囲のP⁵のHessian階数≤3軌跡が平面を含むことと同値になる。Hessianの可約性だけでは不十分な滑らかな具体例も証明する。固定した変数分解の全滑らかな係数空間上でも中心元を同時に選べる一方、規格化のaffine遷移と中心イデアルの不一致例により、モジュライへの降下が別条件であることを明確にしている。

単一ブロックの中心元は、全滑らかなfで変数分解を保つreductive群に同変に選べる。三変数制限gも滑らかなら、混合二次項による中心調整で中心平行移動を含む群にも拡張できる。中心変数がm個でgcd(m,3)=1なら、指標θ=(det N)^rλ^s（mr−3s=1）で次数線形化を補正すると中心スカラーの作用が消え、階数二のPoisson対モジュライの被約層内の開へ次数別平坦な中心商族が降りる。特に三次三様体では、17次元のPoisson対の被約モジュライの稠密開とh直線の積の零切断近傍に量子化族を構成する。固定h≠0で非可換代数の同型類の像が17次元となることは主張しない。

正規形のLie代数的核心は独立補題 `lem:pg-basepoint-free-lie`、非連結中心の持上げ障害は独立命題 `prop:pg-triple-lifting-obstruction` に整理した。これは各成分が正次元の滑らかな中心と任意の消失次数r>=2について、定義式と同じ次数での持上げを扱う。量子化ではEtingof--Ginzburgの既知の中心元存在・Rainsの公式と、本稿の指定Casimirへの相対規格化、全係数での正則性、全ブロック・同変降下を区別する。本文は幾何から一ブロック、全ブロック、降下の順に読み進められる。周囲代数A、中心商Bの記法は付録まで統一した。

[Aの監査と文献比較](notes/poisson_article_submission_audit.md) に仮定と証明の所在を、[Aの検証記録](validation_paper_a.json) に組版・厳密計算・確認範囲をまとめた。Bondalの斉次持上げ、Derdzinski--Galの半単純Lie代数上の核計算を既知部分として明記し、完全交叉の低twist消滅は独立に証明した。三次四様体の例はPym arXiv:1507.05668v1の非存在記述と両立せず、同版の非連結曲線に沿う持上げの問題を説明している。刊行版本文・訂正文との照合、初出の網羅確認、同変な量子化の全モジュライ降下は残る。

論文Bの証明は `papers/generic_recovery/` 内で完結する。可換方程式は関数体上、全coherent残余圏のrotation・指定三次周期付き同値は有限拡大上に構成する。固定勾配空間の積分は有限étaleなsymmetrizer代数で記述し、幾何学的に分解不能なら方程式は基礎体上でスカラー倍まで一意である。同値核の基礎体への降下は別の問題である。[Bの証明案内](notes/generic_recovery.md)、[Bの監査](notes/paper_b_proof_audit.md)、[Bの検証記録](validation_paper_b.json) を参照。B-v58では完備移送の主張、windowの比較図式、文献比較を整理し、非可換Hesse族の復元potentialの一次jetを追加した。A-v56と共通preambleは変更していない。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現行の入口と担当境界は [移管境界ノート](notes/paper_b_scope_and_transfer.md)。

```sh
python3 scripts/verify_bundle.py
python3 scripts/build.py --only paper_a
python3 scripts/verify_bundle.py --only paper_a --require-pdfs
python3 scripts/build.py --only paper_b
python3 scripts/verify_bundle.py --only paper_b --require-pdfs
```

Git checkoutでの追跡対象検査は `python3 scripts/check_layout.py` を用いる。この検査だけはGit管理情報を必要とする。再開用ZIPでは上記のソース・組版検査を実行する。

LuaLaTeX・LuaTeX-ja・latexmkと `requirements.txt` のPython依存を用いる。厳密計算のコマンドは各論文のvalidationに記載し、大きな記号計算は一つずつ実行する。PDF・SyncTeX・中間物はbuild/で非追跡。GitHub mainに保存し、Actions・force pushを使用しない。GitHub mainを正本とし、節目ごとの保存に追加承諾は不要とする。現在の利用者指示に従い、研究の区切りでは現行の方針・ノート・原稿・必要な再現資産だけからなる軽量bundleも、承諾を求めずLibraryへ保存する。生成PDF・中間物はGitで追跡しない。Library上の既存ファイルの削除はこの許可に含めない。
