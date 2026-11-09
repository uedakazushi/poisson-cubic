# Rotation と相対saturationへの還元（2026-11-10, v14）

この文書は前回の研究継続bundle `nc-cubic-reconstruction_v14_20261110.zip` の主要な数学的到達点を、GitHub 上で参照可能な形にした研究ノートである。**完全な LuaLaTeX 原稿および PDF はこのファイルに含まれない。** 原稿での証明記載と独立検証を区別する。

## 局所設定
正則局所複素底 `(R,m,k)` 上の次数別自由な量子化 `A` と中心正則三次元 `Omega` を仮定する。特殊ファイバーは滑らかな cubic の斉次座標環。 `B=A/(Omega)` とし、`C_B=thick{O(j)}`、`K_B^lin=<O,...,O(a-1)>^perp` (`a=n-1`) とする。詳細な仮定は `tex/papers/local_projective_model.tex` に従う。

## 1. Rotation 候補の逆関手（証明案を含む）
既存の完全忠実な候補 `rho=L_O o (1)` について、右mutationから `rho^{-1}=(-1) o R_O` を構成する。鍵は特殊ファイバーのSerre traceを底へ持ち上げ、perfect Hom複体の間の双対性写像が剰余で同型であることから局所Nakayamaを適用し、`{}^perp O = O(a)^perp` を得る点である。左右mutationの三角を使い、二つの合成が恒等となることを確認する。残余smoothnessは仮定しない。

**監査項目:** Serre traceの持上げが自然変換として構成されること、上記直交同定の全対象に対する自然性、mutation順序と左右直交の規約を完全なTeX原稿と照合すること。

## 2. Smoothness から全coherent残余圏へ
`Gamma_R=REnd(G)` が `Perf(Gamma_R^op tensor_R^L Gamma_R)` に属すれば、有限例外列とのgluingにより線束生成部分 `C_B` がsmoothとなる。線束生成子 `E` から任意のcoherent対象 `M` への `RHom(E,M)` の底上perfect性と、smooth dg代数上のpseudo-perfect加群のperfect性を使い、`C_B=D^b(qgr B)` および対応する残余圏の一致へ還元する。

**監査項目:** gluing bimoduleのperfect性、全coherent対象への相対Hom有限性、`E` の弱生成性、相対smoothnessとpropernessの各入力を逐条確認する。

## 3. Smooth proper pair の有限型spread
`Gamma_R` のsmooth proper性が確立すれば、dg代数とrotationを表す可逆perfect bimoduleおよび逆同型を有限型開集合にspreadする方針を取る。有限型spreadの存在と、元の量子化からの幾何学的な比較の両立は区別する。

## 4. 条件付きgeneric可換復元
各Poisson既約成分の支配的な滑らかなchartで、相対量子化・残余smoothness・rotation付きpairを構成し、さらに局所実現原理 (ER) が成立すれば、有限分離体拡大上の一般点で滑らかな可換cubicのrotation付きKuznetsov成分として実現できる。**(ER)の独立監査は未完成であり、無条件の可換復元は未証明。**

## 次の核心
非楕円二成分で、実際の有限perfect `Gamma_R^e`-複体 `P` と `P -> Gamma_R` を作ること。特殊ファイバーで擬同型なら、coneのperfect性とNakayamaから局所的な相対smoothnessが従う。ambient Koszul対角を残余対角と同一視してはならない。

## 検証範囲
このMarkdownは研究の要点と未解決事項を記録するもので、TeX原稿全文の代替ではない。最新の原稿に対する独立の数学的査読・Lean検証は実施していない。
