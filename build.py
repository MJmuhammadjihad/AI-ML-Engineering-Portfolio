"""Build the portable field guide from authored analysis and reviewed evidence.

Build dependency: Python-Markdown pinned in requirements-build.txt.
No runtime dependency in the HTML.
Raw source captures stay in the research workspace; the toolkit contains
short attributed excerpts and provenance rather than full employer feeds.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent
import markdown

def read_json(path):
    return json.loads((ROOT / path).read_text())

sources = read_json('evidence/source-ledger.json')

jobs_doc = read_json('evidence/reviewed-jobs.json')
jobs = jobs_doc['jobs']
assert len(jobs) == 20 and len({j['sourceId'] for j in jobs}) == 20
assert len({j['employer'] for j in jobs}) == 11
# Original capture hashes and excerpt checks are recorded in the research ledger.
# This public build validates structure without claiming to re-fetch source pages.

e = html.escape
def li(items):
    return '<ul>' + ''.join('<li>' + e(x) + '</li>' for x in items) + '</ul>'

job_cards, job_markdown = [], []
for job in jobs:
    sid = job['sourceId']
    anchor = 'job-' + sid.lower()
    title = f"{sid} · {job['employer']} — {job['title']}"
    contents = [f'<p><strong>{e(job["location"])}</strong> · {e(job["roleFamily"])}</p>',
                f'<p>{e(job["seniorityAssessment"])}</p>']
    md_parts = [f'<a id="{anchor}"></a>', f'### {title}',
                f'**Location:** {job["location"]}. **Family:** {job["roleFamily"]}.',
                job['seniorityAssessment']]
    for warning in job.get('reviewWarnings', []):
        contents.append(f'<p class="warning"><strong>Source warning:</strong> {e(warning)}</p>')
        md_parts.append('**Source warning:** ' + warning)
    for label, key in [('Explicit requirements / eligibility', 'explicitRequirementsOrEligibility'),
                       ('Other listed qualifications', 'listedQualificationSummary'),
                       ('Preferred / nice to have', 'preferredOrNiceToHaveSummary')]:
        values = job.get(key, [])
        if values:
            contents.extend([f'<h4>{e(label)}</h4>', li(values)])
            md_parts.extend([f'**{label}**', '\n'.join('- ' + x for x in values)])
    contents.append(f'<p><strong>Location boundary:</strong> {e(job["locationAndEligibility"])}</p>')
    md_parts.append('**Location boundary:** ' + job['locationAndEligibility'])
    # Keep quotes brief; the entire source description is not redistributed.
    for excerpt in job['evidence'][:2]:
        contents.append(f'<blockquote><p>“{e(excerpt["quote"])}”</p></blockquote>')
        md_parts.append('> ' + excerpt['quote'])
    contents.append(f'<p><strong>Portfolio implication:</strong> {e(job["portfolioImplication"])}</p>')
    md_parts.append('**Portfolio implication:** ' + job['portfolioImplication'])
    contents.append(f'<p><a href="{e(job["url"], quote=True)}">Original employer listing</a> · '
                    f'<a href="{e(job["descriptionSourceUrl"], quote=True)}">Employer-controlled feed</a></p>')
    contents.append(f'<p><small>Captured {e(job["retrievedAt"])}; reviewed {e(job["reviewedOn"])}. '
                    f'{e(job["availabilityLimit"])} Feed update time is not original publication time.</small></p>')
    md_parts.append(f'[Original employer listing]({job["url"]}) · [Employer-controlled feed]({job["descriptionSourceUrl"]})')
    md_parts.append(f'Captured {job["retrievedAt"]}; reviewed {job["reviewedOn"]}. {job["availabilityLimit"]}')
    job_cards.append(f'<details id="{anchor}"><summary>{e(title)}</summary>' + ''.join(contents) + '</details>')
    job_markdown.append('\n\n'.join(md_parts))

source_cards, source_markdown = [], []
for source in sources:
    sid = source['sourceId']
    anchor = 'source-' + sid.lower()
    source_cards.append(f'<li id="{anchor}"><strong>{sid}.</strong> '
        f'<a href="{e(source["url"], quote=True)}">{e(source["title"])}</a>. '
        f'Accessed {e(source["accessed"][:10])}. {e(source["scope"])}'
        f'<details><summary>Capture provenance</summary><p>HTTP {source["httpStatus"]}; '
        f'retrieved {e(source["accessed"])}.</p><p>SHA-256: <code>{source["sha256"]}</code></p></details></li>')
    source_markdown.append(f'<a id="{anchor}"></a>\n\n**{sid}. [{source["title"]}]({source["url"]})** '
        f'Accessed {source["accessed"][:10]}. {source["scope"]}\n\nCapture SHA-256: `{source["sha256"]}`.')

method_note = ('The 20 postings are a purposive sample from 11 employers, including 17 AI/ML roles '
    'and three adjacent software roles. They are evidence of described work and eligibility, '
    'not a representative global survey. One source contains unfinished templates. '
    'Original publication dates were not inferred from feed update timestamps.')
source_note = ('These 25 source pages support the observations and technical guidance. '
    'The project choices, schedule, budgets and readiness gates are authored recommendations. '
    'Duplicate captures were not counted as extra sources. A LinkedIn FAQ returning 404, '
    'a Google hiring page containing only boilerplate, and unavailable Creative Commons legal pages '
    'were not used as evidence. The UCI page itself states the dataset license. '
    'Raw captures are retained in the working research directory; the toolkit includes analytical '
    'summaries, short attributed excerpts and hash ledgers instead of full third-party pages.')
dataset = read_json('evidence/dataset-feasibility.json')
dataset_note = (f'Official dataset archive inspected {dataset["retrievedAt"]}: '
    f'{dataset["dayRows"]} daily rows and {dataset["hourRows"]:,} hourly rows. '
    f'Archive SHA-256: {dataset["archiveSha256"]}. '
    'This inspection established schema feasibility only; no model was trained.')

raw_markdown = (ROOT / 'content/strategy.md').read_text()
body_markdown = re.sub(r'^# .*?\n\n', '', raw_markdown, count=1)
renderer = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'],
                             extension_configs={'toc': {'toc_depth': '2-2'}})
body = renderer.convert(body_markdown)
toc = re.sub(r'^<div class="toc">\s*|\s*</div>$', '', renderer.toc)
template = (ROOT / 'content/report_template.html').read_text()
replacements = {
    '__REPORT_BODY__': body,
    '__TOC__': toc,
    '__JOBS_BODY__': f'<p class="note">{e(method_note)}</p>' + ''.join(job_cards),
    '__SOURCE_BODY__': f'<p>{e(source_note)}</p><ol style="list-style:none;padding-left:0">' + ''.join(source_cards) +
        f'</ol><h3>Dataset feasibility check</h3><p>{e(dataset_note)}</p>' +
        f'<p><a href="{e(dataset["url"], quote=True)}">Official UCI archive</a></p>',
    '__REPORT_DATE__': '7 November 2026',
    '__SAMPLE_COUNT__': '20',
}
for marker, value in replacements.items():
    assert template.count(marker) == 1, marker
    template = template.replace(marker, value)
assert not re.search(r'__[A-Z_]+__', template)

ids = re.findall(r'\bid="([^"]+)"', template)
assert len(ids) == len(set(ids)), 'Duplicate HTML IDs'
for fragment in re.findall(r'href="#([^"]+)"', template):
    assert fragment in ids, ('Unresolved internal link', fragment)

name = 'AI-ML-Hiring-Portfolio-Plan'
(ROOT / 'downloads' / (name + '.html')).write_text(template)
complete_markdown = raw_markdown + '\n\n## Hiring evidence appendix\n\n' + method_note + '\n\n' + '\n\n'.join(job_markdown)
complete_markdown += '\n\n## Source appendix\n\n' + source_note + '\n\n' + '\n\n'.join(source_markdown)
complete_markdown += '\n\n### Dataset feasibility check\n\n' + dataset_note + f'\n\n[Official archive]({dataset["url"]})\n'
(ROOT / 'downloads' / (name + '.md')).write_text(complete_markdown)
(ROOT / 'index.html').write_text(template)
(ROOT / 'evidence/build-validation.json').write_text(json.dumps({
    'reportDate': '2026-11-07', 'postings': len(jobs), 'employers': 11,
    'sourceDocuments': len(sources), 'researchCaptureChecks': 'Verified during original research; public build does not redistribute or re-fetch raw source pages',
    'internalLinkTargetsVerified': True, 'htmlBytes': len(template.encode()),
    'markdownWords': len(complete_markdown.split()), 'markdownBuildDependency': markdown.__version__,
}, indent=2) + '\n')
print(f'Built index.html and downloads: {len(jobs)} postings, {len(sources)} source pages.')

pdf = ROOT / 'downloads' / (name + '.pdf')
if pdf.exists():
    files = [ROOT / p for p in ['README.md', 'START-HERE.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
        'CONTRIBUTING.md', 'SECURITY.md', 'CITATION.cff', 'CHANGELOG.md', 'index.html', 'build.py', 'requirements-build.txt', 'requirements-browser.txt']]
    files += sorted((ROOT / 'content').glob('*'))
    files += sorted((ROOT / 'templates').glob('*'))
    files += sorted((ROOT / 'tests').glob('*.py'))
    files += sorted((ROOT / 'docs').glob('*.md'))
    files += sorted((ROOT / 'assets').glob('*.html'))
    files += sorted((ROOT / 'assets').glob('*.png'))
    files += sorted((ROOT / 'evidence').glob('*.json'))
    files += [ROOT / 'downloads' / (name + suffix) for suffix in ('.html', '.md', '.pdf')]
    manifest = {str(p.relative_to(ROOT)): {'bytes': p.stat().st_size,
                 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
    manifest_path = ROOT / 'downloads/toolkit-manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    files.append(manifest_path)
    with zipfile.ZipFile(ROOT / 'downloads/AI-ML-Hiring-Portfolio-Toolkit.zip', 'w',
                         compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            entry = zipfile.ZipInfo('AI-ML-Engineering-Portfolio/' + str(path.relative_to(ROOT)),
                                    date_time=(2026, 11, 8, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            archive.writestr(entry, path.read_bytes())
    print('Packaged the guide, templates, evidence records, original-source license and third-party notices.')
else:
    print('PDF not found. Render it before packaging the release toolkit.')
