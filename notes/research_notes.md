# 三次超曲面のPoisson幾何：現行研究ノート

2026-11-21 / v97。最初に [研究方針](../00_research_plan.md) を読む。

## 正規形・退化幾何・モジュライ

[主原稿](../papers/poisson-cubic.tex) は全次元Poisson正規形、Bondal下界、固定・相対成分と退化幾何の証明を保持する。
仮定と先行研究の確認範囲は [主張・文献の監査](poisson_article_submission_audit.md)、Bondal・三次四様体は [幾何ノート](bondal_cubic.md)、成分の区別は [相対成分ノート](fermat_relative_poisson_components.md) に整理する。

三次四様体のrank4 Poissonは(3,3)分離型およびambient Hessian階数≤3軌跡内の平面で判定できる。後二者の同値はBricalli–Favale–Pirolaの既知定理である。Hessianの可約性だけでは不十分である。非連結な滑らかな中心に沿う任意r>=2の同次数持上げ障害では、全連結成分が正次元である条件を保つ。Pymとの不整合は確認したarXiv v1の範囲に限定し、刊行版本文・訂正文は未照合である。

固定Poisスキーム、固定多様体上の商スタック、相対Poissonスタックの成分数を区別する。階数層には被約構造を指定する。非楕円のnodal/cuspidal例の整数小行列証明書は本repoに保持し、量子化した関係行列の行列式は量子化論文の計算資産へ分けた。

## 量子化・非可換幾何との接続

量子化の主原稿は [nc-cubic/papers/cubic-quantization.tex](https://github.com/uedakazushi/nc-cubic/blob/main/papers/cubic-quantization.tex)、中心元の構成・規格化・同変降下と障害のノートは [cubic_quantization.md](https://github.com/uedakazushi/nc-cubic/blob/main/notes/cubic_quantization.md) を正本とする。
可換復元・非可換モジュライの主原稿は同repoの [nc-cubic.tex](https://github.com/uedakazushi/nc-cubic/blob/main/papers/nc-cubic.tex)。量子化の全ブロック存在定理と、良い一ブロック上のモジュライ・比較結果の仮定を混同しない。

独立した点スキーム・有限Jacobian復元・Artin/étale構成の現行入口は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2)。そこで必要な追加仮定を、`nc-cubic.tex` の一般点存在定理から自動的に満たすとは扱わない。個別の相対構成・生成性の障害は [相対構成ノート](https://github.com/uedakazushi/nc-cubic/blob/main/notes/relative_construction_obstacles.tex) に移し、本文にある有効な議論を保持する。

証明記載、内部点検、厳密計算、組版、形式検証、新規性確認は別の状態である。実行範囲は [validation_paper_a.json](../validation_paper_a.json) と [validation.json](../validation.json) を参照する。
