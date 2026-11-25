# 三次超曲面のPoisson幾何：現行研究ノート

2026-11-25 / v101。最初に [研究方針](../00_research_plan.md) を読む。

## 正規形・退化幾何・モジュライ

[主原稿](../papers/poisson-cubic.tex) は全次元Poisson正規形、Bondal下界、固定・相対成分と退化幾何の証明を保持する。
仮定と先行研究の確認範囲は [主張・文献の監査](poisson_article_submission_audit.md)、Bondal・三次四様体は [幾何ノート](bondal_cubic.md)、成分の区別は [相対成分ノート](fermat_relative_poisson_components.md) に整理する。

公表稿はarXiv・論文誌で人間の研究者が通読する論文として構成する。四様体の分類・Hessian判定・持上げ障害は独立した節に置き、固定・相対モジュライの記号は使用前に定義する。計算証明は階数の上界・整数小行列による下界・成分性への推論を本文に置き、固定版の公開計算資料と実行コマンドへつなぐ。文献照合や編集の作業状態はこのノート群と検証記録に保持する。

査読に基づくA-v66では、葉の閉包の一般的滑らかさを超曲面上の値の関係式とともに証明し、相対成分で用いるHessian条件の逆向きを直接示す。階数2のGrassmannianは被約パラメータ空間の主張とし、正規形の内在的ブロックと選択に依存する補空間を区別する。Fermat三様体の葉と零点、Fermat四様体の固定・商成分数を小例で説明する。詳細と確認範囲は主張・一次資料の監査を参照する。

正規形の改稿では、Euler列とgradientのKoszul複体から定数3重ベクトル表示を得て、Jacobiator Jに対するE∧J=FQとdivergenceの恒等式からNJ=3J、従ってJ=0を導く。Hessian条件からは三重ベクトルの支持W上で非退化形式を選んでLie代数を構成し、根基の可換イデアル内のsl₂加群と最高根のベクトルを用いてWをsl₂因子に分解する。Derdzinski–Galの核計算は比較結果であり、必要な排除とブロック復元は本文で証明する。

参照した [nc-cubic-lean のcommit](https://github.com/uedakazushi/nc-cubic-lean/tree/9736787f3a95f52bc3d233ab768a6ab6396d0c24) と本文との対応は [lean_proof_sources.txt](lean_proof_sources.txt) にある。今回Leanは再ビルドしておらず、改稿したTeX本文も形式検証していない。一般階数・退化・Bondal下界・モジュライは参照版の幾何学的主定理の形式化された結論に含まれない。

三次四様体のrank4 Poissonは(3,3)分離型およびambient Hessian階数≤3軌跡内の平面で判定できる。後二者の同値はBricalli–Favale–Pirolaの既知定理である。Hessianの可約性だけでは不十分である。非連結な滑らかな中心に沿う任意r>=2の同次数持上げ障害では、全連結成分が正次元である条件を保つ。Pymとの不整合は確認したarXiv v1の範囲に限定し、刊行版本文・訂正文は未照合である。

固定Poisスキーム、固定多様体上の商スタック、相対Poissonスタックの成分数を区別する。階数層には被約構造を指定する。非楕円のnodal/cuspidal例の整数小行列証明書は本repoに保持し、量子化した関係行列の行列式は量子化論文の計算資産へ分けた。

序論の位置付けは、通常の射影空間内の滑らかな完全交叉・次元3以上の4型を出発点とする。全次元の対角型や特定の退化条件の分類は先行し、本稿の特徴は三次超曲面の全メンバー・全階数を同じ正規形で扱う点にある。限定付きの「最初」という主張と包括的な優先権の確定は区別する。公開 `poisson-p4` 原稿の147成分（141一般階数4、6一般階数2）はPGL商前の被約空間に関する分類案であり、人間による検証は未了である。原典の版・定理番号・確認範囲は [文献比較](poisson_article_submission_audit.md) を参照する。

## 量子化・非可換幾何との接続

量子化の主原稿は [cubic-quantization/papers/cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex)、中心元の構成・規格化・同変降下と障害のノートは [cubic_quantization.md](https://github.com/uedakazushi/nc-cubic/blob/main/notes/cubic_quantization.md) を参照する。
可換復元・非可換モジュライの主原稿は `nc-cubic` の [nc-cubic.tex](https://github.com/uedakazushi/nc-cubic/blob/main/papers/nc-cubic.tex)。量子化の全ブロック存在定理と、良い一ブロック上のモジュライ・比較結果の仮定を混同しない。

独立した点スキーム・有限Jacobian復元・Artin/étale構成の現行入口は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2)。そこで必要な追加仮定を、`nc-cubic.tex` の一般点存在定理から自動的に満たすとは扱わない。個別の相対構成・生成性の障害は [相対構成ノート](https://github.com/uedakazushi/nc-cubic/blob/main/notes/relative_construction_obstacles.tex) に移し、本文にある有効な議論を保持する。

証明記載、内部点検、厳密計算、組版、形式検証、新規性確認は別の状態である。実行範囲は [validation_paper_a.json](../validation_paper_a.json) と [validation.json](../validation.json) を参照する。
