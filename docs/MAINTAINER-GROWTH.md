# Grow usefulness, then distribution

The goal is a repository people can understand, use, recommend and return to. Stars are one signal of interest; they do not measure learning, code quality or hiring outcomes. The practices below are a small operating plan, not a claim about any platform's ranking algorithm.

## Keep the first visit easy

1. Make the first screen answer: who is this for, what can I use, and where do I start?
2. Keep one prominent link to the live guide and one to the latest toolkit.
3. Ensure every advertised feature is implemented and the public links work.
4. Use a legible share image and a short, specific repository description.
5. Preserve source dates, limitations and the distinction between project briefs and built systems.

### One-time owner settings

These settings are managed in GitHub's interface and are separate from the files in this repository. They require the appropriate repository permissions.

On the repository's **About** panel, select the gear icon and use:

- **Description:** `Build an AI/ML engineering portfolio: project briefs, an interactive planner, evaluation templates, and evidence from 20 job postings.`
- **Website:** `https://mjmuhammadjihad.github.io/AI-ML-Engineering-Portfolio/`
- **Topics:** `ai-engineering`, `machine-learning`, `portfolio`, `career-development`, `mlops`, `rag`, `evaluation`, `python`, `learning-resources`, `roadmap`.

For a repository social preview, open **Settings → General → Social preview**, choose **Edit → Upload an image**, and upload [assets/social-preview.png](../assets/social-preview.png). The 1200 × 630 image is also used by the guide's social metadata. Platform previews may be cached, and their refresh timing is outside this repository's control.

These are optional discoverability improvements, not a requirement to read, use or download the guide.

## Take a small baseline

Record these manually before a meaningful release and once a week afterward. GitHub exposes some traffic data only to users with the necessary repository access and for a limited window; save a dated snapshot if available. Treat missing data as unavailable, not zero.

| Signal | What to record | What it can tell you |
| --- | --- | --- |
| GitHub visits | Views, unique visitors, time window | Whether the repository is being discovered; not whether the guide was read |
| Referring sites and popular paths | Available referrers/pages, same time window | Which sources bring relevant visitors; reporting may omit traffic |
| Clones and release downloads | Counts and observation dates | Interest in taking material away; not unique users or successful setup |
| Stars and forks | Counts and weekly change | A rough interest/return signal; not skill validation or hiring impact |
| Useful issues and contributions | Specific corrections, completed reviews, merged improvements | Where readers invested effort or found friction |
| Reader feedback | Voluntary reports of a tried brief, an evaluation decision or a failed step | Concrete learning about usefulness; do not turn anecdotes into a representative success rate |

Repository visitors and release download events are different populations. Avoid presenting their ratio as a precise conversion rate. This guide has no behavioral analytics or tracking script; browser planning state is local. Do not claim page-level engagement measurements that were not collected.

## Use a two-hour weekly maintenance budget

- **45 minutes:** fix one reader problem or a small evidence/accessibility issue.
- **30 minutes:** review feedback and respond to a focused question with useful context.
- **30 minutes:** write one substantive update if there is a real improvement or finding.
- **15 minutes:** record the available metrics and choose the next problem.

A week without a useful update does not need a promotional post. Larger changes may need more engineering time; reduce promotional activity before rushing verification.

## Share a reason to visit

Use the [share kit](SHARE-KIT.md) as a draft, then adapt it to the audience. Good reasons to share include a new evaluation worksheet, a corrected leakage example, a more accessible interface, a real user finding, or a clearer beginner path.

Read a community's rules before posting. Participate where the topic is relevant, disclose that you maintain the resource, and give a useful explanation alongside the link. Do not buy stars, coordinate reciprocal starring, create fake accounts, mass-message strangers, or repeat the same promotion across unrelated discussions.

## Decide what to improve next

| Observation | A reasonable next step |
| --- | --- |
| People visit but ask what the project contains | Clarify the README opening and show a concrete template or workflow. |
| People download but report setup confusion | Reproduce the failure and improve the first-run instructions. |
| Readers find the guide overwhelming | Shorten the first path, add a direct section link, or make the first action more explicit. |
| A project brief attracts repeated technical corrections | Review the evaluation contract and evidence before broad promotion. |
| A useful contribution arrives | Review it thoughtfully, credit the author accurately, and include it in release notes. |
| Traffic rises after a post | Check whether the audience also produces relevant questions or feedback; avoid attributing all changes to one cause. |

For each experiment, write one hypothesis, one bounded change, an observation window and an actual result. Small samples, external events and multiple simultaneous changes limit causal conclusions. Keep unsuccessful experiments in the notes.

## Release when the improvement is real

Bundle coherent changes, verify the guide/PDF/toolkit together, and write release notes around what readers can now do. Preserve older releases and stable source IDs. Use a new version for substantive content or interaction changes; explain any research refresh and its actual access dates.

A useful release note includes the reader problem, the resulting behavior, the validation performed, and remaining limits. Never claim a star target, readership size or hiring result before observing it.
