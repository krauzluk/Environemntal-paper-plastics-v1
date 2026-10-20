#!/usr/bin/env python3
"""Build a deterministic, flat Springer source archive from an explicit allowlist."""
from pathlib import Path
import re
import zipfile

root = Path(__file__).resolve().parents[1]
source = (root / 'manuscript.tex').read_text()
figures = sorted(set(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', source)))
files = ['cas-refs.bib', 'sn-jnl.cls', 'sn-apacite.bst'] + figures
missing = [name for name in files if not (root/name).is_file()]
if missing:
    raise SystemExit('Missing source files: ' + ', '.join(missing))
if not (root/'build/manuscript.bbl').is_file():
    raise SystemExit('Compile the manuscript with BibTeX first (make all).')
# Use one folder level and include the compiled bibliography for submission engines.
for figure in figures:
    source = source.replace('{' + figure + '}', '{' + Path(figure).name + '}')
payload = {'manuscript.tex': source.encode(),
           'manuscript.bbl': (root/'build/manuscript.bbl').read_bytes()}
for name in files:
    basename = Path(name).name
    if basename in payload:
        raise SystemExit('Archive name collision: ' + basename)
    payload[basename] = (root/name).read_bytes()
target = root/'submission/ema-source.zip'
with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for name, data in sorted(payload.items()):
        entry = zipfile.ZipInfo(name, date_time=(2026, 10, 20, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        archive.writestr(entry, data)
print(f'{target.name}: {len(payload)} files, {target.stat().st_size} bytes')
