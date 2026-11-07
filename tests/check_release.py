"""Verify the public release artifacts without fetching mutable external sources."""
import csv
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / 'index.html').read_text()
assert page == (ROOT / 'downloads/AI-ML-Hiring-Portfolio-Plan.html').read_text()
ids = re.findall(r'\bid="([^"]+)"', page)
assert len(ids) == len(set(ids))
assert all(target in ids for target in re.findall(r'href="#([^"]+)"', page))
assert not re.search(r'__[A-Z_]+__', page)
assert not re.search(r'<(?:script|link|img|iframe)[^>]*(?:src|href)=[\"\']https?://', page)
assert 'AI-assisted' in page and 'unfinished' in page
assert (ROOT / 'downloads/AI-ML-Hiring-Portfolio-Plan.pdf').read_bytes().startswith(b'%PDF')
for filename in ('LICENSE', 'THIRD_PARTY_NOTICES.md', 'README.md'):
    assert (ROOT / filename).stat().st_size > 100
for path in (ROOT / 'templates').glob('*.csv'):
    rows = list(csv.reader(path.open()))
    assert rows and all(len(row) == len(rows[0]) for row in rows), path.name
jobs = json.loads((ROOT / 'evidence/reviewed-jobs.json').read_text())['jobs']
assert len(jobs) == 20 and len({j['employer'] for j in jobs}) == 11
assert jobs[16]['sourceId'] == 'H17' and jobs[16]['reviewWarnings']
sources = json.loads((ROOT / 'evidence/source-ledger.json').read_text())
assert len(sources) == 25 and len({s['finalUrl'] for s in sources}) == 25
manifest = json.loads((ROOT / 'downloads/toolkit-manifest.json').read_text())
with zipfile.ZipFile(ROOT / 'downloads/AI-ML-Hiring-Portfolio-Toolkit.zip') as archive:
    assert archive.testzip() is None
    for path, record in manifest.items():
        content = (ROOT / path).read_bytes()
        assert hashlib.sha256(content).hexdigest() == record['sha256'], path
        assert len(content) == record['bytes'], path
        assert archive.read('AI-ML-Engineering-Portfolio/' + path) == content, path
    for name in ('LICENSE', 'THIRD_PARTY_NOTICES.md'):
        assert 'AI-ML-Engineering-Portfolio/' + name in archive.namelist()
stamp = json.loads((ROOT / 'evidence/pdf-provenance.json').read_text())
assert stamp['htmlSha256'] == hashlib.sha256((ROOT / 'index.html').read_bytes()).hexdigest(), 'Refresh the PDF after changing the rendered guide.'
assert stamp['pdfSha256'] == hashlib.sha256((ROOT / 'downloads/AI-ML-Hiring-Portfolio-Plan.pdf').read_bytes()).hexdigest()
print('Release checks passed: links, source structure, CSVs, PDF provenance, license files and every ZIP member.')
