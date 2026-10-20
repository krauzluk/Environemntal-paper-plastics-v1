# Template and build provenance

Prepared on 20 October 2026.

Official template landing page: https://www.springernature.com/gp/authors/campaigns/latex-author-support

The publisher page identifies the December 2024 journal package. Its download link resolved to:

https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/18782940/data/v12

The official binary download could not be retrieved in this environment: the command-line request timed out and the browser download route also failed. The class and bibliography style were therefore obtained from public mirrors. They have not been claimed to be a byte-for-byte verified copy of that current ZIP.

- `sn-jnl.cls`: https://github.com/iftaken/anor-template/blob/dfeb5372e9211ef50b8d46023e64221f4a8c8de8/sn-jnl.cls . The mirror describes its template as version 3.1, December 2024. The class retains the old internal `2019/11/18 v0.1` identifier; that identifier alone is not evidence of the package release date.
- `sn-apacite.bst`: https://github.com/DanySK/template-latex-springer-nature-sn-jnl/blob/52c1a7e8bd945b754fabf0cc75d6823dd2917f84/sn-apacite.bst . That mirror's sample manuscript is marked version 3, October 2023. This is the compatible Springer APA bibliography style. Its equivalence to the style in the December 2024 ZIP was not independently checked.

Both files retain their upstream notices and have not been edited. Journal-specific formatting is contained in `manuscript.tex`. In particular, the manuscript enables continuous left line numbering with `lineno`, leaves headings unnumbered, uses the `sn-apa` class option, and renders DOI identifiers as complete links. Redundant `url` fields were removed from DOI-bearing bibliography entries to avoid duplicate links in this style. Citation identities were retained.

The standard `apacite` LaTeX dependency was absent from the minimal build environment and was locally supplied from https://github.com/open-source-uc/latex-template-msc/blob/master/apacite.sty (v6.03, 2013/07/21, blob `11a4c757b786aaa7ad3fc3a425961a8ae1ce04dc`). It is an environment dependency, not a project source file. A normal TeX Live installation should provide the complete package through `texlive-bibtex-extra`. The local build uses the package's built-in English defaults because the optional `english.apc` file is absent; the warning is recorded in the validation report.

If strict identity with the current publisher bundle is required, replace the two vendored files from the official ZIP and run `make package` again. This is a remaining provenance limitation, not a claim that the manuscript uses an independently verified complete publisher download.
