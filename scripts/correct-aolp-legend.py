#!/usr/bin/env python3
"""Correct only the mean-angle symbol in the supplied vector PDF.

Requires PyMuPDF. Curves, coordinates, tick labels and error bars are retained.
Usage: python scripts/correct-aolp-legend.py input.pdf output.pdf
Use the original PDF from commit 9b82d2a as input; do not digitize its data.
"""
import argparse
import subprocess
from pathlib import Path
import fitz

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('source', type=Path)
parser.add_argument('output', type=Path)
parser.add_argument('--font', type=Path, help='Optional path to DejaVuSans-Oblique.ttf')
args = parser.parse_args()
if args.source.resolve() == args.output.resolve():
    parser.error('Choose a different output path, then review before replacing.')
doc = fitz.open(args.source)
page = doc[0]
targets = [span for block in page.get_text('dict')['blocks']
           for line in block.get('lines', []) for span in line['spans']
           if span['text'] == 'R' and span['size'] == 18.0]
if len(targets) != 3:
    raise SystemExit(f'Expected exactly 3 legend symbols, found {len(targets)}.')
# Use an installed DejaVu Sans face; the original PDF uses Type 3 subsets.
font_path = str(args.font) if args.font else subprocess.check_output(
    ['fc-match', '-f', '%{file}', 'DejaVu Sans:slant=oblique'], text=True).strip()
for span in targets:
    x, y = span['origin']
    page.add_redact_annot(fitz.Rect(x + 1, y - 14, x + 11, y + 1), fill=None)
page.apply_redactions(images=0, graphics=0, text=0)
page.insert_font(fontname='CorrectedMeanAngle', fontfile=font_path)
for span in targets:
    x, y = span['origin']
    page.insert_text((x, y), '\u03b1', fontname='CorrectedMeanAngle', fontsize=18)
    page.draw_line((x + 1, y - 14.5), (x + 10.5, y - 14.5), width=0.7)
doc.save(args.output, garbage=4, deflate=True)
print(f'Corrected 3 legend symbols: {args.output}')
