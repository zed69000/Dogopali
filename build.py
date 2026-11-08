#!/usr/bin/env python3
"""Construit le jeu : src/template.html + src/photos.json -> dist/index.html (une seule page autonome)."""
import datetime, pathlib, re, subprocess, sys
root = pathlib.Path(__file__).resolve().parent
t = (root / 'src/template.html').read_text()
photos = (root / 'src/photos.json').read_text()
v = (root / 'version.txt').read_text().strip()
d = datetime.date.today()
t = t.replace('__VERSION__', 'version %s · %d/%d' % (v, d.day, d.month)).replace('__PHOTOS__', photos)
t = t.replace('__VNUM__', v)
out = root / 'dist/index.html'; out.parent.mkdir(exist_ok=True); out.write_text(t)
# manifest of the studio kit (bug reports), read next to the page: keep it with index.html when deploying
(root / 'dist/kit.json').write_text((root / 'src/kit.json').read_text())
js = re.findall(r'<script>(.*?)</script>', t, re.S)[-1]
chk = root / 'dist/.chk.js'; chk.write_text(js)
r = subprocess.run(['node', '--check', str(chk)], capture_output=True, text=True); chk.unlink()
if r.returncode: print(r.stderr); sys.exit(1)
print('OK ->', out, '(version %s)' % v)
