# Contributing

Help make the guide more accurate, useful, and easy to inspect. Focused corrections are welcome: source interpretation, evaluation methodology, broken links, unclear instructions, accessibility, and reproducible build problems.

## Propose a useful change

Before a large rewrite, describe the problem and proposed scope in an issue. For a small correction, a focused pull request is enough. Explain what changed, why, and how you checked it.

- Prefer primary sources. Include the exact URL, access date, and the short passage supporting a factual correction.
- Separate explicit requirements from preferred qualifications, and location restrictions from general company language.
- Do not infer publication dates from job-feed update timestamps. Flag closed, unavailable, ambiguous, or unfinished source text.
- Keep projections, observed facts, recommendations, and personal experience distinct.
- Do not add invented metrics, hiring guarantees, unmeasured business savings, or claims that a proposed project has been completed.
- Keep quoted material brief and attributed. Do not upload full copyrighted pages, private correspondence, credentials, or personal application records.

Examples in templates should stay visibly unfilled. Report a contribution's status accurately: submitted, reviewed, and merged are different states.

## Edit and rebuild

The authored guide and presentation template live in `content/`. Evidence summaries live in `evidence/`; reusable worksheets live in `templates/`. Prefer changing these sources and regenerating outputs over manually editing only the built HTML.

```bash
python -m pip install -r requirements-build.txt
python build.py
python tests/check_release.py
```

For content changes, refresh the maintained PDF as well as the generated HTML, Markdown, and toolkit. Inspect the print output and verify that the downloadable copies match the release. Do not assume the standard build regenerates the PDF.

Run `python tests/check_browser.py` after installing `requirements-browser.txt` and Chromium through Playwright; then run `python build.py` again to package the refreshed files. See the README for the complete commands. The release check rejects a PDF whose recorded source hash differs from the current HTML.

For presentation changes, check narrow mobile and desktop widths, keyboard navigation, visible focus, readable tables, and operation with JavaScript disabled. Avoid introducing external runtime dependencies into the portable guide without a clear need and an explicit design discussion.

## Evidence and research updates

Preserve stable source IDs when correcting a record. Explain changes to counts, dates, eligibility summaries, or source-quality warnings. The repository contains analytical summaries and provenance records, not every original research capture. Do not claim to have reverified a source unless you actually retrieved and examined it.

Keep the guide's original research date visible. If updating the research, state the new access/review dates and scope; a refreshed link alone does not establish that all findings remain current.

## Review and attribution

Keep changes small enough to review and respond constructively to questions. Credit collaborators and borrowed material. Disclose material AI assistance when it helps reviewers assess provenance, and verify generated changes yourself.

By contributing original material, you agree to provide it under this repository's MIT license. Only contribute material you have the right to share. Third-party material keeps its applicable license and attribution requirements; identify it explicitly.
