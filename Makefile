.PHONY: all package clean

LATEXMK ?= latexmk
LATEX_FLAGS = -pdf -pdflatex='pdflatex -no-shell-escape %O %S' -interaction=nonstopmode -halt-on-error -outdir=build

all:
	mkdir -p build submission
	$(LATEXMK) $(LATEX_FLAGS) manuscript.tex
	$(LATEXMK) $(LATEX_FLAGS) submission/cover-letter.tex
	cp build/manuscript.pdf submission/manuscript-ema.pdf
	cp build/cover-letter.pdf submission/cover-letter.pdf

package: all
	python3 scripts/package-submission.py

clean:
	$(LATEXMK) -C -outdir=build manuscript.tex
	$(LATEXMK) -C -outdir=build submission/cover-letter.tex
