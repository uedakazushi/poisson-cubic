# AGENTS.md — nc-cubic研究継続

**2026-11-11 / v35。mainが唯一の正本。** 00_research_plan.md、notes/rotation_orbit_generic_reconstruction.mdから読む。旧会話・ZIPを再開条件にしない。

## 現在の結論

既存の(L)局所proper/windowと(CF)次数別完備有限rank MF同値の下で、一変数量子化の線束生成残余pairの幾何学的一般点は可換cubicのKu pairと同値になる。明示的lambda=1族では(D)をさらに使い、復元先は既存多項式G_h+v^3。証明全文はpapers/reconstruction/rotation_orbit_generic_reconstruction.tex。

これは(L),(CF),(D)の全独立監査を完了したという主張ではない。一般coherent残余圏や多変数モジュライ全体と混同しない。

## 論理の核心

- K_R=stab(R)、T_R=K_R⊕K_R(1)⊕K_R(2)がwindowからK^linを生成し、Gamma_R=REnd(T_R)はproper。
- 完備functorを固定三対象に制限してからhを反転する。固定Hom成分は有限自由なので通常のA∞写像となる。任意のLaurent対象に形式級数を評価する必要はない。
- Eulerベクトルchi_r=Σ_(s+r=0 mod3)(-1)^s binom(N,s)、二乗和2*3^(N-1)。N=5は(-9,9,0)。N=9ではchi0=0なので一般次元で自己Eulerだけを使わない。
- 一般点の像Eは非零。Stevensonのungraded分類をregradingとcompact局所化でgradedへ戻し、E,E(1),E(2)が生成すると証明する。非零対象単独のgraded生成性は主張しない。
- 一般体上の逆核はcompactになり、有限表示性で有限生成部分代数に降下し、perfect coneを非空開で消して閉点を取る。有限拡大C(h)上の同値を得る。完備底全体のcompact逆核は未構成のままでよい。

## 次の優先事項

(L)のwindow/proper底変更、(CF)のcurved formalityとcomplete-graded比較、明示式の(D)を独立監査する。その後、三シフト生成の有限cellと同値核を明示化する。存在の証明を具体行列の計算と呼ばない。有限拡大の次数、h=0近傍同値、一般lambdaの閉公式、K^lin=全残余、多変数一括適用は未完了。

(KF)や完備逆核を一般点の先行条件に戻さない。片側Morita、Popescu、SM/ERはより強い相対結論の別経路として保持する。旧生成子持上げの反例や全Artin smooth/generic nonsmooth例も削除しない。

## 保存と検証

研究区切りに承認不要で証明全文・方針・ノート・必要なコード/証明書をmainへ通常のfast-forwardで保存する。force push、無断PR、GitHub Actionsは禁止。要約だけを全文pushと呼ばず、remote refと変更blobを照合する。Libraryは実際のpush失敗時のみ緊急退避。既存Libraryファイルの無断削除は禁止。

日本語LuaLaTeX、PDFはbuild/に生成しGit追跡しない。旧ZIP、旧稿、ログ、cacheを追加しない。既存A/B/Cの有効な数学・証明・検証資産を容量のため削除しない。

`python3 scripts/verify_rotation_orbit_assets.py`、`latexmk papers/rotation_orbit_generic_reconstruction.tex`。新計算は64Eulerベクトルと41特殊Koszul行列恒等式であり、generic同値kernelや旧nc全行列を計算したものではない。全A/B/C組版・全旧計算を実行していなければ明記する。生成、証明点検、計算、組版、遠隔保存は別状態。
