# Build from the repository root: latexmk papers/poisson-cubic.tex
# LuaLaTeX by default; PDFs and intermediate files go to ignored build/.
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;

@default_files = ('papers/poisson-cubic.tex');
# Main manuscript: papers/poisson-cubic.tex.
# All TeX inputs use explicit repository-root-relative paths; no TEXINPUTS override.
# Open the repository root in VS Code, or run latexmk there.
