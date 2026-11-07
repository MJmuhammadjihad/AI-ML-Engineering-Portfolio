"""Browser checks for the rendered artifact; no external pages are fetched."""
from pathlib import Path
import json
import hashlib
import shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

# Managed Chrome blocks file:// URLs. Serve the exact artifact on loopback.
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
ORIGIN = f'http://127.0.0.1:{server.server_port}'
URL = ORIGIN + '/index.html'
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
results = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
    for width in (320, 390, 768, 1024, 1440):
        context = browser.new_context(viewport={'width': width, 'height': 1000}, reduced_motion='reduce')
        page = context.new_page()
        errors, external = [], []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('request', lambda req: external.append(req.url) if req.url.startswith(('http:', 'https:')) and not req.url.startswith(ORIGIN + '/') else None)
        page.goto(URL)
        assert page.title().startswith('Build evidence.')
        assert page.locator('.jobs-body > details').count() == 20
        assert page.locator('.source-body > ol > li').count() == 25
        assert page.locator('.report-body > h2').count() == 15
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), f'Overflow at {width}'
        page.keyboard.press('Tab')
        assert page.locator('.skip-link').evaluate('(e) => e === document.activeElement')
        page.keyboard.press('Enter')
        assert page.locator('#main').evaluate('(e) => e === document.activeElement')
        if width <= 900:
            assert not page.locator('#contents').evaluate('(e) => e.open')
            page.locator('#contents > summary').click()
        assert page.locator('.toc a').count() == 15
        page.locator('.toc a').nth(4).click()
        assert 'flagship-1' in page.url
        page.goto(URL + '#job-h17')
        assert page.locator('#job-h17').evaluate('(e) => e.open')
        assert 'unfinished' in page.locator('#job-h17 .warning').inner_text()
        page.goto(URL)
        if width in (390, 1440):
            page.screenshot(path=str(OUT / f'report-{width}.png'))
            page.locator('.report-body > h2').nth(4).scroll_into_view_if_needed()
            page.screenshot(path=str(OUT / f'project-{width}.png'))
        assert not errors, errors
        assert not external, external
        results.append({'viewport': width, 'overflow': False, 'errors': errors, 'externalRequests': external,
                        'navigation': 'passed', 'jobHashExpansion': 'passed'})
        context.close()
    context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
    page = context.new_page()
    page.goto(URL)
    assert page.locator('#contents').evaluate('(e) => e.open')
    assert page.locator('#print-report').is_hidden()
    page.locator('#job-h01 > summary').click()
    assert page.locator('#job-h01').evaluate('(e) => e.open')
    assert page.locator('.report-body > h2').count() == 15
    context.close()
    context = browser.new_context(viewport={'width': 1440, 'height': 1000})
    page = context.new_page()
    page.goto(URL)
    page.pdf(path=str(ROOT / 'downloads/AI-ML-Hiring-Portfolio-Plan.pdf'), format='A4', print_background=True,
             prefer_css_page_size=True)
    context.close()
    browser.close()
server.shutdown()
(ROOT / 'evidence/browser-checks.json').write_text(json.dumps({'viewports':results,'noJavaScript':'passed','pdf':'generated'},indent=2)+'\n')
print('Passed 5 viewport checks, keyboard/navigation, evidence links, no-JS and offline checks; PDF generated.')

(ROOT / 'evidence/pdf-provenance.json').write_text(json.dumps({'htmlSha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(), 'pdfSha256':hashlib.sha256((ROOT/'downloads/AI-ML-Hiring-Portfolio-Plan.pdf').read_bytes()).hexdigest(), 'method':'Chromium print-to-PDF of the complete generated guide; appendix details expanded before printing'},indent=2)+'\n')
