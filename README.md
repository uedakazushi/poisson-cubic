# poisson-cubic — 三次超曲面のPoisson構造と代数的量子化

2026-11-21 / v96。再開は [研究方針](00_research_plan.md) から。

| 現行論文 | 内容 |
| --- | --- |
| [主論文](papers/poisson-cubic.tex)（A-v61） | 全次元Poisson正規形・Bondal予想・代数的量子化・固定相対モジュライ（ambient復元は付録） |

主論文は、全次元正規形・Bondalの下界・全Poisson構造の代数的量子化・Fermatと相対モジュライの成分数を中心に整理している。三次四様体の一般階数四の構造を分離型F=f+gで分類し、その正規な退化因子とmodular場を直接計算して純楕円型であることを示す。Bricalli–Favale–Pirolaの既知の分解判定を合わせると、この存在は周囲のP⁵のHessian階数≤3軌跡が平面を含むことと同値になる。Hessianの可約性だけでは不十分な滑らかな具体例も証明する。固定した変数分解の全滑らかな係数空間上でも中心元を同時に選べる一方、規格化のaffine遷移と中心イデアルの不一致例により、モジュライへの降下が別条件であることを明確にしている。

階数二では、supportの三平面を全て動かし、三変数制限の型によらず全座標群に共変な中心元を、普遍Hessianの二次jetまで指定して零h切断近傍に選べる。Grassmann多様体上のBott消滅から中心核へ形式的に持ち上げ、Stiefel開の正則関数の延長と有限加群の完備化で代数的な中心元を得る。gcd(N,3)=1なら次数の線形化を補正して、全被約階数二Poisson対モジュライへ次数別局所自由な中心商族を降ろせる。特に三次三様体N=5では17次元の全非零Poisson対モジュライ×h直線の零切断近傍が対象となる。一般のNでも三次Veronese A_(3d)⊗λ^d は全階数二層へ降下する。元の次数一を保つ線束補正の障害は、位数gcd(N,3)のgerbeとして決定した。固定h≠0で非可換代数の同型類の像が17次元となることや、全hへの延長・一意性は主張しない。

g=0の層では、PBW対称化したΩ=sym(f)が全変形パラメータで全ブロック群に共変な正則中心元となる。この層はm>=3で非空で、support平面P(W_P)⊂Xに対応する。対応するgerbe上では全h直線にわたる中心商族があり、gcd(m,3)=1なら指標補正によりPoisson層自体へ降りる。PBW対称化の既知原理と、その係数族・同変降下への適用を区別する。

節点・尖点の各軌道にも、安定化群に同変な方向微分の左逆を用いて全G同変中心元を構成する。対応するPoisson層の余次元は1,2で、三次三様体では底が16,15次元となる。一意な特異点直線による次数の捻りで、中心変数の個数に関する条件なしに各層の零h切断近傍へ代数族が降りる。これらの層別の明示的構成も保持する。型をまたぐ族は上記の中心核の方法で選ぶ。N>=6では、零制限の標準中心直線へ全層で一致させることは二次jetの相対コホモロジー障害により不可能である。中心商の抽象的同型やqgr比較は別の課題である。全fと非零Poisson係数を用いても補空間の大域同変選択は不可能で、中心平行移動の自由商も非アフィンとなることを証明する。

中心変数のない満support層N=3kでは、順序のないブロック被覆と係数空間のアフィン性を用い、指定二次jetを持つ共変中心元を直接持ち上げる。三次Veroneseとその新次数一の大域中心元・正則中心商が、全被約Poisson層の零h切断近傍へ降りる。三次四様体のrank4では全Poisson対が対象となり、底は4次元である。中心スカラーgerbeの正確な位数gcd(N,3)も、Fermat安定化群の交換子を用いて全非零階数層で決定した。中心変数を残すm>0、k>=2の一般の同時選択は残る。

正規形のLie代数的核心は独立補題 `lem:pg-basepoint-free-lie`、非連結中心の持上げ障害は独立命題 `prop:pg-triple-lifting-obstruction` に整理した。これは各成分が正次元の滑らかな中心と任意の消失次数r>=2について、定義式と同じ次数での持上げを扱う。量子化ではEtingof--Ginzburgの既知の中心元存在・Rainsの公式と、本稿の指定Casimirへの相対規格化、全係数での正則性、全ブロック・同変降下を区別する。節点型の明示中心元はChekhov–Mazzocco–Rubtsovの既知公式との具体対応も示す。本文は幾何から一ブロック、全ブロック、層別降下、階数二の全support、満supportの多ブロック層へ進む。周囲代数A、中心商Bの記法は付録まで統一した。

[Aの監査と文献比較](notes/poisson_article_submission_audit.md) に仮定と証明の所在を、[Aの検証記録](validation_paper_a.json) に組版・厳密計算・確認範囲をまとめた。Bondalの斉次持上げ、Derdzinski--Galの半単純Lie代数上の核計算を既知部分として明記し、完全交叉の低twist消滅は独立に証明した。三次四様体の例はPym arXiv:1507.05668v1の非存在記述と両立せず、同版の非連結曲線に沿う持上げの問題を説明している。刊行版本文・訂正文との照合、初出の網羅確認、中心変数を残す複数ブロックの一般の同変構成、全hへの延長や中心商の比較は残る。

旧論文Bに相当する一般点の全coherent残余圏の可換復元、完備MF移送、指定三次周期、明示Hesse模型と必要証明は [nc-cubic](https://github.com/uedakazushi/nc-cubic) の主原稿へ統合した。このrepoに残す主論文はPoisson正規形・量子化を扱う一本のみである。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現行の入口と担当境界は [nc-cubic2の研究方針](https://github.com/uedakazushi/nc-cubic2)。

LaTeX の読み込み先は実際の `papers/support/papers/` 以下を直接指定する。
リポジトリのルートで `latexmk papers/poisson-cubic.tex` を実行する。
VS Codeではリポジトリ全体を開き、LaTeX Workshopの `latexmk (repository root)` を使用する。
直接 `lualatex` を呼ぶ場合もルートを作業ディレクトリとし、
`lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -output-directory=build papers/poisson-cubic.tex`
を実行できる構成である。出力名は `build/poisson-cubic.pdf`。
 
```sh
python3 scripts/verify_bundle.py
python3 scripts/build.py --only poisson-cubic
python3 scripts/verify_bundle.py --only poisson-cubic --require-pdfs
```

Git checkoutでの追跡対象検査は `python3 scripts/check_layout.py` を用いる。この検査だけはGit管理情報を必要とする。再開はmainの現行ソースと検証資料から行う。

LuaLaTeX・LuaTeX-ja・latexmkと `requirements.txt` のPython依存を用いる。厳密計算のコマンドは各論文のvalidationに記載し、大きな記号計算は一つずつ実行する。PDF・SyncTeX・中間物はbuild/で非追跡。GitHub mainに保存し、Actions・force pushを使用しない。GitHub mainを正本とし、節目ごとの保存に追加承諾は不要とする。GitHub管理後はLibraryへの定常的な二重保存やZIP作成は行わず、push失敗の緊急保存または明示的指示がある場合に限りLibraryを使用する。生成PDF・中間物はGitで追跡しない。既存Libraryファイルは削除しない。
