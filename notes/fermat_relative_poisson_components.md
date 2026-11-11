# 研究ノート：固定Fermatと相対Poisson cubicの既約成分の比較

**2026-11-12 / v1。最初に `00_research_plan.md` を読む。**

## 主張の状態・依存

- **論文Aに証明を追加した帰結**：`papers/sections/fermat_relative_poisson_components.tex` の `thm:pg-fermat-relative-count`。既存の滑らかなcubicのPoisson正規形定理 `papers/sections/poisson_geometry.tex` の `thm:pg-normal`、`prop:pg-represent`、`lem:pg-linearize`、およびブロック内在性補題 `papers/sections/nonelliptic_poisson_components.tex` の `ne:blocks` を入力とする。原稿にはこれらの証明があるが、今回それら全体の独立再監査はしていない。
- **固定Fermat**：\(N=n+2\ge5\) 個の添字を各大きさ3以上の非順序ブロックに分割する組 \(\mathcal B=\{B_1,\ldots,B_k\}\) ごとに、\(Z_\mathcal B=\bigoplus_s\widehat{\operatorname{Gr}}(3,\mathbb C^{B_s})\subset\Lambda^3\mathbb C^N\) が既約成分。次元は \(3N-8k\)。Fermat Hessianが全対角形式を張ることから、各 \(\iota_{dz_i}P\) が分解可能でなければならず、異なる三次元ブロックの座標支持は互いに素となる。通常の同じPoisson generic rankで複数の固定Fermat成分が存在する。
- **相対**：smooth cubicを動かす相対Poisson schemeの非零部分では、rank \(2k\) ごとに既約成分が一つ、総数 \(\lfloor N/3\rfloor\)。\(m=N-3k\) として商スタックの次元は \(d_{n,k}=k(3N-8)+\binom{m+2}{3}+k(10+6m+3\binom{m+1}{2})-N^2\)。この計数は大域Poisson正規形定理を前提とする代数的帰結。詳細な相対稿は `uedakazushi/nc-cubic2/papers/poisson_cubic_pair_components.tex` にもあるが、論文Aの証明はそのファイルなしで読める。
- **全次元の対比**：\(n=3,4,5,6,7,8,9,10\) のFermat成分総数は \(1,11,36,92,491,2557,11353,60105\)、相対成分総数は \(1,2,2,2,3,3,3,4\)。固定Fermatで多数に分裂している成分は、cubicを変形すると各rankの一つの相対成分内に連結する。
- **明示的な未解決問題**：Fermatが全smooth cubic中で成分数最大となるか（高次元は未証明）、Poisson schemeのgeneric reducednessと交叉・nilpotent構造、相対モジュライの境界、先行研究上の新規性の完全照合。

## 再現

- `python3 computations/verify_poisson_component_comparison.py`：Python標準ライブラリだけで \(5\le N\le19\) の数値と隣接次元差を厳密整数演算で検算。組合せ式の検算であってPoisson正規形の証明ではない。
- `latexmk papers/poisson_cubic_quantization.tex`：論文Aの一部として日本語LuaLaTeX。新節の試験用単独組版は実行したが、最終main全体の組版は別途確認が必要。

## 文献と再開

主入力は同じリポジトリのPoisson正規形節。一般次元の相対既約性の証明全文も論文Aの新節に配置した。関連する一般計数とscheme問題の詳細は `nc-cubic2` で研究を続けるが、論文Aを読むのに `nc-cubic2` の取得は不要。外部文献の全面的な初出調査は未了。
