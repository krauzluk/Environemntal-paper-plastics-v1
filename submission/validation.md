# Build and editorial validation

Checked on 20 October 2026 against the original repository commit `9b82d2a`.

- `make package` completed successfully with pdfLaTeX, BibTeX and latexmk.
- The manuscript has 24 pages; the cover letter has one page.
- The source ZIP contains 14 files in one directory. Its CRC check passed, and its bibliography, styles and figures match the current project files.
- The ZIP was extracted into a separate directory and successfully compiled there, with shell escape disabled. It does not depend on the original `figures/` directory.
- Both document logs contain no LaTeX errors, undefined citations or references, or overfull boxes. The local manuscript build reports one warning: the optional `english.apc` file is unavailable. The standard `apacite` package's built-in English defaults are used; see [template provenance](template-provenance.md). A few underfull vertical-box diagnostics arise from float placement.
- All manuscript pages and the cover letter were visually inspected after the main layout changes. Figures are legible, and no clipping or overlapping content was identified. The final bibliography and caption adjustments were compiled and checked again.
- All 40 citation keys used in the original manuscript remain cited, with no additions. The 17 displayed `equation` environments and the one `align` environment are unchanged apart from whitespace. The contents of all three tabular environments are unchanged apart from whitespace.
- The abstract contains 225 whitespace-delimited words. There are five keywords, six numbered figures and three tables. The document uses author–year citations, unnumbered section headings and continuous left-side line numbering.
- The only figure edit replaces three erroneous `R` labels by the angular-mean symbol in `08_class_AOLP_circular.pdf`. A rendered pixel comparison located all changes inside the legend; plotted curves and numerical labels were preserved. The correction is recorded in `scripts/correct-aolp-legend.py`.
- `git diff --cached --check` passed for the project-authored files before committing. The two unmodified upstream style files were excluded from this whitespace check because they retain their original line endings and whitespace.

This validation covers the manuscript files and their build. It does not establish the validity of the radiometric conversion, estimator, measurement uncertainty or experimental conclusions. Those checks require the original measurements and analysis code, which were not present in the repository. The remaining author confirmations and scientific questions are listed in [author-checks.md](author-checks.md).
