# Distinguishing microplastic and oil pollutants at the water surface using multi-angle LWIR polarization imaging

Manuscript preparation for **Environmental Monitoring and Assessment**, 20 October 2026.

The original Elsevier version remains available in git history at commit `9b82d2a`. The default main document is now `manuscript.tex` using Springer Nature `sn-jnl` with author–year citations.

**Before submission:** read [the scientific and author checks](submission/author-checks.md). The repository contains manuscript sources and figures, not raw measurements or analysis code. Successful compilation does not validate the radiometric processing or numerical results. The required confirmation of ethical responsibilities still needs to be inserted after the authors have actually reviewed and confirmed it.

## Files

- [Manuscript PDF](submission/manuscript-ema.pdf)
- [Flat source ZIP](submission/ema-source.zip), prepared for the Springer submission system
- [Cover letter PDF](submission/cover-letter.pdf) and [editable source](submission/cover-letter.tex)
- [Scientific checks and changes](submission/author-checks.md), in Czech
- [Journal options and verified OA conditions](submission/journal-options.md), in Czech
- [Template provenance](submission/template-provenance.md)
- [Build and editorial validation](submission/validation.md)

## Build

Use a current TeX Live installation or Overleaf with pdfLaTeX. Required tools: `pdflatex`, `bibtex`, `latexmk`, Python 3, and GNU Make. LaTeX packages include `apacite`, `natbib`, `amsmath`, `amssymb`, `graphicx`, `booktabs`, `tabularx`, `tikz`, `upgreek`, `lineno`, `placeins`, and the dependencies loaded by `sn-jnl`. On Debian/Ubuntu a suitable installation includes `latexmk texlive-latex-extra texlive-fonts-recommended texlive-pictures texlive-bibtex-extra`.

```sh
make package
```

This compiles both documents with shell escape disabled, copies the PDFs to `submission/`, and builds `submission/ema-source.zip`. The ZIP contains the manuscript, bibliography (`.bib` and compiled `.bbl`), Springer style files, and the referenced figures, all in one directory. It excludes internal notes, build logs, the cover letter, and unused Elsevier files. The `.bbl` accompanies the `.bib` for build compatibility; the main source uses the ordinary bibliography command.

For Overleaf, upload `submission/ema-source.zip`, choose `manuscript.tex` as the main document, and select pdfLaTeX. The cover letter is a separate document. Regenerate the PDFs and ZIP after changing any text or figure.

No new experimental results, inferred sample sizes, or invented declarations were added. Numerical values and the original harmonic estimator were retained pending the checks listed above. Only the angular-mean label in the final AoLP plot was corrected; `scripts/correct-aolp-legend.py` records that vector-only correction and requires PyMuPDF and a DejaVu Sans font. It is not part of the routine manuscript build.
