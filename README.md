# Distinguishing microplastic and oil pollutants at the water surface using multi-angle LWIR polarization imaging

Springer Nature `sn-jnl` template with the `sn-apa` bibliography style. Main file: `manuscript.tex`. Compiler: **pdfLaTeX**.

- [Manuscript PDF](submission/manuscript-ema.pdf)
- [Submission source ZIP](submission/ema-source.zip)

Upload the source ZIP to Overleaf and select `manuscript.tex` as the main document. For a local TeX Live installation with `apacite` installed:

```sh
latexmk -pdf -outdir=build manuscript.tex
```

The manuscript text and source comments are retained from commit `dc2b61e`. All figures are the original, unedited files from `9b82d2a`. The original highlights are retained as an unnumbered list. The bibliography has only a technical URL-protection adjustment needed for compilation.

The source ZIP contains the manuscript, `.bib` and `.bbl` bibliography files, Springer class and bibliography style, and figures in one directory. No custom build scripts are required.

Template files are unmodified copies from [the class mirror](https://github.com/iftaken/anor-template/blob/dfeb5372e9211ef50b8d46023e64221f4a8c8de8/sn-jnl.cls) and [the bibliography-style mirror](https://github.com/DanySK/template-latex-springer-nature-sn-jnl/blob/52c1a7e8bd945b754fabf0cc75d6823dd2917f84/sn-apacite.bst). The [official Springer template ZIP](https://www.springernature.com/gp/authors/campaigns/latex-author-support) could not be downloaded here, so identity with that ZIP has not been independently verified.
