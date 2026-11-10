# AGENTS.md — nc-cubicの研究継続指示

**2026-11-10・v21。GitHub uedakazushi/nc-cubic の main が唯一の正本。** 最初に00_research_plan.md、次にnotes/research_notes.mdとreconstruction/README.mdを読む。旧ZIP・会話・Libraryを再開の前提にしない。

## 目標と優先順位

1. 滑らかなcubic n-fold (n≥3) 上のPoisson構造の構造定理。論文Aのthm:pg-normalに証明あり。
2. 各固定Poisson構造を、Koszul AS-regularな周囲と中心三次正則商で代数的に量子化する。論文Aのthm:pg-quantizationに証明あり。全Poisson係数空間上の一様相対量子化とは区別する。
3. 構成した量子化のgenericファイバーについて、同じKuznetsov成分とrotationを持つ滑らかな可換cubicを構成する。**最優先・一般混合型は未完成。** 任意のAS-regular中心三次商の全点には広げない。Zhang twistによるrotation付き反例がある。

証明の記載、独立監査、計算実行、形式証明を区別する。cubic n-foldの周囲はnc P^(n+1)。価値ある既存成果・証明を軽量化のため削らない。

## 現行の証明方針

**方程式抽出と圏同値の存在を並行して進める。** SMを先に完成する一本の経路に限定しない。一ブロック分離型を明示的基準例とし、三次元の本質的混合項の二次jetへ進む。非楕円fivefoldのSM・一般次元への拡張も維持する。

- papers/reconstruction/explicit_model_comparison.tex：点曲線はf+h² det Hess(f)/24。Mori–Smithの既知公式を本稿の規約に移したもの。適切なAS-regular性・滑らかな楕円中心商・独立な中心変数追加の仮定で可換模型に使う。圏同値は既存er:thm:mainとブロック比較・生成性に依存する。行列式の恒等式だけから同値を結論しない。
- papers/reconstruction/explicit_jacobian_recovery.tex：導来自然変換の次数一・二の積から勾配空間を抽出し、可積分線形系でcubicを求める。一般nc入力では積の対称性を先に検査する。成功は唯一の候補を与えるが、同値の存在は証明しない。ambientの二次関係やpoint schemeをこの積の代わりに入れない。
- papers/reconstruction/poisson_first_order.tex：cubic threefoldの純bivector部分はHH²(Ku)への制限で消える。純Poisson KS類・残余への制限との両立を確認し、可換族の存在を仮定すればF_h=F+O(h²)。全次数の定数性、全奇数次消滅、一般次元、SMへ拡張しない。

次の入力はF_lambda=(x³+y³+z³)/3+u³+v³+lambda*u*x*y（滑らかさはlambda³≠−3）。papers/reconstruction/mixed_test_family.tex に三次中心元の閉式・全パラメータ中心性の自由代数証明書・全Artin切断PBWの証明がある。これは非可換側の入力の完成であり、非零hの全AS性・残余SM・カテゴリカルな積の計算ではない。h³を法としてrotationの低次数積と可換候補の二次類を求め、分離点lambda=0で[G₂]=[xyz]/3を再現する。

同変復元の存在を仮定すると、対角群のcharacterから[G₂]=c(lambda)[xyz]に絞られる。Hessian候補c_H=(12+lambda³)/36は研究ノートに未検証案として置く。計算にこの値を先に組み込まず、圏から独立に求める。

## 維持する存在証明の経路

- ERはpapers/reconstruction/etale_realization.texの実在するsmooth proper dg族を入力とする。障害のrotation不変性、幾何的KS全射、HH¹によるintertwiner持上げ、actual moduliの代数性、étale sectionを確認する。ERで残余smoothnessを先取りしない。
- notes/sm_bar_and_spreading.texの有限bar右逆判定、papers/sections/minimal_ainfty_arity.texの残余Γと線束生成子Λのsmoothness同値を使う。実際の有限perfect双加群と増大射が必要。
- H=H⁰⊕Hⁿの最小A∞模型でm_k=0 unless k=2 mod n。fivefoldのm₇、m₁₂、二次障害を区別する。arity証明書は係数計算やSMではない。低次数復元に役立つかを確認して計算順序を選ぶ。
- 節点・尖点二成分はpapers/sections/nonelliptic_quantization.texの全次数PBW量子化を使う。35係数sliceの検算は復元写像の計算ではない。係数方向も保つ相対量子化は全成分では未完成。
- Artin切断のperfectness、Hom階数、Serre自己同値、周囲の対角からSMを結論しない。現行dg負例の特殊ファイバー代数はsmoothではなく、SM不成立の反例ではない。

## 正確性と先行研究

既知結果・具体的計算・条件付き結果・未完成・予想を分け、仮定と証明所在を明記する。初出未確認なら新規と称しない。重要文献の一次資料を確認する。

rotationの低次数sector計算と、Serre関手だけからrotationを得るgcd条件を混同しない。全次数の自然変換環をJacobian環と同一視しない。正しいHilbert級数だけでは可積分性も圏同値も従わない。

中心元の可換表示と可換模型は異なる。分離Fermat例の二次項はそれぞれ−2h²xyz/3と+h²xyz/3。元のcubicが全量子化で復元されるとは主張しない。一次交換子だけで高次の復元先を決めない。

## 保存・再現・配置

1. 研究の区切りに方針・ノート・論文の証明全文・必要なコード/入力/証明書/再現手順を、承諾を求めずmainへ反映する。remote headを確認し追加変更を保持して通常のfast-forwardのみ。force push、無断PR、GitHub Actionsは使わない。
2. 反映後にremote refと主要blob SHAを再取得する。要約だけの反映を全文保存と呼ばない。生成・数学的監査・計算・組版・遠隔反映を別々に報告する。
3. **Library保存はGitHub反映が実際に失敗した場合だけの緊急避難。** 成功時には二重保存しない。退避時は未同期と復帰手順を明示し、既存Libraryファイルを明示指示なしに削除しない。
4. 主論文はpapers/、ノートはnotes/、計算はcomputations/等。日本語LuaLaTeXを既定とする。ルート.latexmkrcとlatexmkでbuild/へ生成し、**PDFをGit追跡しない。**
5. 新しいinputは参照検査とbuild receiptの全ハッシュに含める。scripts/verify_bundle.py、新しい厳密計算、reconstruction/scripts/build.pyとverify.pyを必要範囲で実行する。親Cと独立SM/ER節の組版を区別し、A/B未組版なら明記する。
6. 独立境界研究・未照合原PDF8件はnc-cubic2、Reye研究はreyeに保全済み。再追加・重複保守しない。可換復元に必要な有効内容は現行本文に保持し、周辺原稿の全面再構築を優先しない。
7. 現在有効な自己完結した一式として更新する。旧ZIP、旧稿、変更履歴、ログ、キャッシュ、重複物を追加しない。数学的内容・検証可能性を損なう固定容量制限を設けない。
