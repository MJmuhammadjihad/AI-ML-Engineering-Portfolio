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
            page.locator('#portfolio-planner').scroll_into_view_if_needed()
            page.screenshot(path=str(OUT / f'planner-{width}.png'))
            page.locator('.report-body > h2').nth(4).scroll_into_view_if_needed()
            page.screenshot(path=str(OUT / f'project-{width}.png'))
        assert not errors, errors
        assert not external, external
        results.append({'viewport': width, 'overflow': False, 'errors': errors, 'externalRequests': external,
                        'navigation': 'passed', 'jobHashExpansion': 'passed'})
        context.close()
    # Verify calculations, role ordering, opt-in persistence and actual export.
    context = browser.new_context(viewport={'width': 1440, 'height': 1000}, accept_downloads=True)
    page = context.new_page()
    page.goto(URL)
    assert page.locator('#plan-estimate').inner_text() == '24 weeks'
    page.locator('#plan-role').select_option('ai')
    assert page.locator('#plan-milestones > li').nth(1).get_attribute('data-milestone') == 'evidence'
    page.locator('#plan-hours').select_option('3')
    page.locator('#plan-days').select_option('5')
    assert page.locator('#plan-estimate').inner_text() == '58 weeks'
    page.locator('[data-gate="foundation"]').check()
    assert page.locator('#plan-progress').inner_text() == '1 of 5 gates marked'
    assert page.evaluate("localStorage.getItem('ai-ml-portfolio-plan-v1')") is None
    page.locator('#remember-plan').check()
    page.reload()
    assert page.locator('#plan-role').input_value() == 'ai'
    assert page.locator('#plan-estimate').inner_text() == '58 weeks'
    assert page.locator('[data-gate="foundation"]').is_checked()
    with page.expect_download() as pending:
        page.locator('#export-plan').click()
    download = pending.value
    assert download.suggested_filename == 'my-ai-ml-portfolio-plan.md'
    exported = Path(download.path()).read_text()
    assert '58 weeks' in exported and '3 hours/day' in exported
    assert '- [x] Own a small Python/data tool' in exported
    assert exported.index('Evidence Desk') < exported.index('Demand Replay')
    assert 'self-assessed' in exported and 'not independently verified' in exported
    page.once('dialog', lambda dialog: dialog.dismiss())
    page.locator('#reset-plan').click()
    assert page.locator('[data-gate="foundation"]').is_checked()
    page.once('dialog', lambda dialog: dialog.accept())
    page.locator('#reset-plan').click()
    assert page.locator('#plan-progress').inner_text() == '0 of 5 gates marked'
    assert page.locator('#plan-role').input_value() == 'ai'
    page.locator('#remember-plan').uncheck()
    assert page.evaluate("localStorage.getItem('ai-ml-portfolio-plan-v1')") is None
    page.reload()
    assert page.locator('#plan-estimate').inner_text() == '24 weeks'
    page.locator('#plan-role').select_option('ml')
    assert page.locator('#plan-milestones > li').nth(1).get_attribute('data-milestone') == 'demand'
    context.close()
    # Storage failures and malformed saved data must not break the guide.
    for mode in ('blocked', 'malformed', 'invalid-schema'):
        context = browser.new_context()
        if mode == 'blocked':
            context.add_init_script("Object.defineProperty(window, 'localStorage', {get() { throw new DOMException('Blocked for test', 'SecurityError'); }});")
        else:
            value = '{bad json' if mode == 'malformed' else json.dumps({'version':1,'role':'ai','hours':-5,'days':999,'checks':{'foundation':True}})
            context.add_init_script('localStorage.setItem("ai-ml-portfolio-plan-v1", ' + json.dumps(value) + ');')
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(URL)
        assert page.locator('#plan-estimate').inner_text() == '24 weeks'
        assert page.locator('#export-plan').is_visible()
        assert not page.locator('[data-gate="foundation"]').is_checked()
        if mode == 'blocked':
            assert page.locator('#remember-plan').is_disabled()
            assert 'unavailable' in page.locator('#storage-note').inner_text()
        assert not errors
        context.close()
    context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
    page = context.new_page()
    page.goto(URL)
    assert page.locator('#contents').evaluate('(e) => e.open')
    assert page.locator('#print-report').is_hidden()
    assert page.locator('#planner-controls').is_hidden()
    assert page.locator('#planner-static').is_visible()
    assert page.locator('#plan-milestones > li').count() == 5
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
    context = browser.new_context(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
    page = context.new_page()
    page.goto(ORIGIN + '/assets/social-preview.html')
    assert page.evaluate('document.documentElement.scrollWidth == 1200')
    assert page.evaluate('document.documentElement.scrollHeight == 630')
    page.screenshot(path=str(OUT / 'social-preview.png'))
    context.close()
    browser.close()
server.shutdown()
(ROOT / 'evidence/browser-checks.json').write_text(json.dumps({'viewports':results,'noJavaScript':'passed','planner':{'calculations':'passed','rolePriority':'passed','optInPersistence':'passed','markdownExport':'passed','resetConfirmation':'passed','storageFailureFallback':'passed','malformedStateFallback':'passed'},'socialCard':'1200x630 generated','pdf':'generated'},indent=2)+'\n')
print('Passed responsive, keyboard, planner/state/export, metadata, no-JS and offline checks; PDF and share card generated.')

(ROOT / 'evidence/pdf-provenance.json').write_text(json.dumps({'htmlSha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(), 'pdfSha256':hashlib.sha256((ROOT/'downloads/AI-ML-Hiring-Portfolio-Plan.pdf').read_bytes()).hexdigest(), 'method':'Chromium print-to-PDF of the complete generated guide; appendix details expanded before printing'},indent=2)+'\n')
