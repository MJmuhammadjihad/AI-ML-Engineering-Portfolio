# AI & ML Engineering Portfolio

Research and recommendations prepared **7 November 2026** for learners starting from zero, with a planning budget of six study hours per day and a global job-search goal. Adapt the plan to your actual education, work authorization, hardware and budget. The default assumes a normal laptop, no GPU, and a free-first build. Estimates are planning budgets after prerequisite skills, not promises of learning speed or employment.

> **Research provenance:** This guide was prepared with AI assistance, source review and a direct dataset-schema inspection. It proposes projects; it does not claim the publisher has built these systems, measured their performance or obtained employment through them. The dated source records and limitations are included for review.

## 1. The recommendation

Build **two complementary flagship projects**, give one a **serious reliability release**, and make **one useful contribution to an existing project**. Start with a small Python/data tool so you can actually own the work. Publish the evidence in a form that a hiring team can inspect and that you can explain without depending on generated answers.

| Order | What to build | What an employer can inspect | Where it belongs |
| --- | --- | --- | --- |
| Foundation | A CSV quality-checking CLI | Your Python, error handling, tests, Git habits, and ability to finish a small tool | A learning repository; pin only while it is your strongest work |
| Flagship 1 | **Demand Replay:** a leakage-aware next-day demand forecast and API | Data contracts, prediction-time reasoning, simple baselines, temporal evaluation, and reproducible model delivery | A pinned GitHub repository, case study, and short demo |
| Flagship 2 | **Evidence Desk:** a bounded documentation assistant with citations and abstention | Retrieval, LLM integration, evaluation design, grounded answers, failure analysis, cost and latency | A pinned GitHub repository, evaluation report, and short demo |
| Reliability release | A monitored, bounded, recoverable version of one flagship | Timeouts, schema failures, observability, load testing, release controls, rollback, and an incident report | A tagged release and case study inside the flagship repository |
| Collaboration | A verified correction, regression test, or small bug fix in a tool you actually use | Reproduction, review response, communication, and working within someone else's codebase | Link to the real issue/PR and a precise contribution summary |

**Default sequencing:** foundation → Demand Replay → Evidence Desk → reliability release. This puts data and evaluation discipline before LLM orchestration. If your eligible target roles clearly emphasize AI product engineering, you can build Evidence Desk before the forecasting flagship once the software/evaluation prerequisites are met. The choice follows the target work, not a trend.

Do not create a separate repository for every component. Two coherent, reproducible systems with documented decisions provide more inspectable evidence than a large collection of unfinished interfaces. The separate [First Principles learning roadmap](https://github.com/MJmuhammadjihad/AI-ML-Engineering-Roadmap) is a related resource. A roadmap or documentation application can show interface design, packaging and delivery; it does not by itself establish independently trained models, valid ML experiments or professional production experience.

## 2. What the research actually supports

### Method and limits

The hiring review examined **20 distinct postings from 11 employers**: 17 directly about AI/ML and three adjacent entry-level software roles. The employer-controlled feeds were captured on 6 November 2026 and reviewed on 7 November. The employers are Databricks, Datadog, Elastic, Anthropic, Reddit, Pinterest, Roblox, Duolingo, Airbnb, Scale AI, and Affirm. A separate appendix preserves titles, locations, exact evidence, requirements, warnings, and URLs.

This is a **purposive capability sample**, heavily weighted toward large technology companies and accessible English-language job boards. It is not a representative global labor-market survey. It cannot estimate the share of employers requiring a degree, your chances of getting hired, the availability of worldwide remote jobs, or the best project for every country. A captured job description is also not a guarantee that the vacancy remains open. One posting contains unfinished template text; ambiguous conditions from that text must not be used as eligibility evidence.

The review also uses first-party technical guidance, employer interview guidance, official dataset/documentation pages, GitHub/LinkedIn documentation, and broader labor-market reports. Evidence is linked below. The project selection, time budgets, readiness gates, and publishing cadence are recommendations in this guide, not an experimentally validated hiring formula.

### The clearest hiring signals

| Observed evidence | What it means for your portfolio | Boundary |
| --- | --- | --- |
| Databricks describes production GenAI deployment, evaluation, and optimization; its “all levels” FDE posting also explicitly asks for at least four years of relevant experience. [H01](#job-h01) | Show a complete, evaluated workflow and customer-facing explanation. | “All levels” does not mean suitable for a beginner. |
| Databricks welcomes infrastructure engineers without an ML background while emphasizing software testing and deployment. [H02](#job-h02) | Strong software fundamentals are a useful bridge into applied AI. | “No ML background” is not “no engineering experience.” |
| Anthropic's demo-engineering role says accuracy and honesty matter alongside polish and mentions evaluation/validation harnesses and graceful fallbacks. [H05](#job-h05) | A beautiful demo should expose reliable behavior, limits, and failure handling. | This is an experienced engineering role, not a promise that a demo qualifies you. |
| Reddit describes ownership from problem definition and feature engineering through training, deployment, and monitoring. [H06](#job-h06) | Build the chain around the model, with a reproducible baseline and a service/replay. | The posting also requests production experience. |
| Scale AI asks for extending evaluations, investigating failure modes, flagging regressions, and owning work through release/debugging. [H13](#job-h13) | Publish experiments, failures, regression checks, and the release decision. | A portfolio replay should not be described as professional production ownership. |
| Pinterest's master's graduate role explicitly asks for critical validation of AI-generated suggestions. [H09](#job-h09) | Explain your AI assistance and demonstrate independent debugging and judgment. | This particular role also has an explicit master's requirement. |
| Affirm's early-career SWE role accepts equivalent practical experience or a related bachelor's degree. [H18](#job-h18) | Junior software work can be a relevant adjacent route while you develop ML depth. | Its location and authorization conditions still apply. |

The practical conclusion is to demonstrate **problem definition, data judgment, evaluation, readable software, delivery, and independent explanation**. Framework familiarity is useful when it supports those behaviors. A framework list alone gives a reviewer little evidence.

### Eligibility comes before portfolio matching

Several reviewed student/new-graduate roles are restricted by degree, enrollment, graduation date, or location. Pinterest's master's graduate role, Roblox's PhD early-career role, Duolingo's new-PhD role, and the Datadog internship illustrate different restrictions; they do not establish a universal degree rule. [H09](#job-h09) [H10](#job-h10) [H11](#job-h11) [H20](#job-h20)

“Remote” is also scoped: the reviewed Pinterest role is US-based, while Affirm's MLE role specifies Canadian eligibility details. Airbnb's China role explicitly requires English and Mandarin. Scale AI's public-sector role requires an active security clearance. These are not gaps you can fix by adding another notebook. [H07](#job-h07) [H16](#job-h16) [H12](#job-h12) [H14](#job-h14)

If you are not enrolled in a qualifying degree, filter student-only roles out of your primary list. Include eligible junior software/backend, data-platform, QA automation, or applied-AI implementation roles where the work and requirements match your actual skills. This is a search strategy to test in your market, not a claim that those jobs are easy or available everywhere.

### Demand and the future

The retrieved US BLS data-scientist page projects 35% employment growth in 2025–2035; its software developer/QA/tester group projects 10%. These are broad US occupational projections, with openings including replacement needs. They are not forecasts of globally accessible junior AI-engineering vacancies or individual job chances. [S01](#source-s01) [S02](#source-s02)

WEF's 2025 report summarizes expectations from more than 1,000 employers across 55 economies and highlights AI/big data alongside analytical thinking and other broader capabilities. Those are surveyed expectations through 2030. Stanford's 2026 economy chapter describes uneven labor effects, including pressure in young-worker hiring pipelines; it does not prove that a particular applicant will be helped or displaced by AI. [S03](#source-s03) [S04](#source-s04)

**Planning principle:** as tools change, keep investing in understanding the problem, constructing valid tests, tracing data, measuring constraints, integrating systems, and communicating decisions. If code generation improves, those capabilities help you check and own its output. If budgets tighten, a measured baseline and a smaller dependable solution become valuable. These are conditional planning arguments, not predictions of a winning framework or a hiring boom.

## 3. Choose the job family before choosing extra tools

| Target | Main engineering question | Portfolio emphasis | Additional preparation |
| --- | --- | --- | --- |
| Applied AI / AI product engineer | Can you turn a model capability into a bounded, useful workflow? | Evidence Desk, evaluations, API integration, user feedback, cost/latency, failure handling | Python or TypeScript, HTTP, SQL, basic frontend, auth/secrets, retrieval and LLM failure modes |
| ML engineer | Can you make predictions that remain valid and useful after training? | Demand Replay, prediction-time data boundaries, temporal evaluation, deployment, model/data monitoring | Python, SQL, probability/statistics, feature pipelines, optimization basics, software testing |
| ML platform / MLOps-oriented engineer | Can other people train, deploy, diagnose, and recover a system reproducibly? | Reliability release, artifact versioning, CI, containers, observability, rollback | Stronger Linux/networking/cloud/automation and distributed-system fundamentals |
| Research engineer / research scientist | Can you reproduce and extend a technical result rigorously? | A later replication with ablations and uncertainty, plus mathematical/experimental depth | Often a substantially higher research/degree bar in this sample; not the default first target from zero |

Titles overlap. Read responsibilities and requirements rather than treating this table as a universal job taxonomy. For your starting point, I would build a common software/data base, then orient the first case study toward **eligible applied-AI or junior software roles**, while the forecasting project supplies genuine ML evidence. Keep the ML-engineering path open rather than claiming research readiness prematurely.

### A repeatable project-selection rule

Use this process again when your target or resources change:

1. **Define the opportunity:** collect a small recent set of roles you could actually accept. Separate location, authorization, degree/enrollment and experience constraints from preferred tools. Record unknowns instead of assuming eligibility.
2. **Extract observable work:** turn responsibilities into things a reviewer could inspect—for example, a defensible train/test boundary, a failing-input regression test, a measured retrieval comparison, or a recovery procedure.
3. **Reject infeasible ideas:** require lawful usable data, a baseline, a measurable outcome, and a build you can run within your available hardware and money. An exciting idea without these is a research question, not yet a portfolio commitment.
4. **Choose complementary evidence:** pick one project with the strongest match to repeated responsibilities, then a second that proves an important missing capability. Prefer depth on an existing system over a third project that repeats the same API wrapper.
5. **Release the smallest useful version:** run the baseline and one real evaluation before expanding the interface or model stack. Stop adding features when you cannot explain or validate the current ones.
6. **Update from observations:** after a release, use actual errors, user feedback, technical reviews and application-stage feedback to choose the next change. Recheck role requirements periodically because job pages and eligibility rules change.

This is a decision procedure, not a mathematically proven optimum. I chose forecasting because it makes data timing and ML evaluation visible, and a documentation assistant because it makes retrieval, generative-model integration and evidence handling visible. Their reliability work shares software skills while exposing different model failures. A third chatbot would add relatively little evidence at this stage.

## 4. Foundation project: a CSV quality-checking CLI

**Purpose:** prove that you can save, run, test, document, and repair a useful Python program before composing larger AI systems. A small data team wants to know whether a daily file is safe to ingest.

**Build:** a command-line tool that reads a small CSV, validates an explicit schema, reports missing/duplicate/invalid values, and writes a machine-readable summary. Use a tiny synthetic fixture first, then the bike dataset described below. Keep the original file unchanged.

**MVP contract:** required columns are declared; dates parse; counts are nonnegative integers; duplicate dates are reported; malformed rows produce an actionable message and a nonzero exit code; a valid input produces deterministic JSON. Add one test for each failure, plus a clean-input test. Document exactly which checks are and are not implemented.

**Learn through it:** functions, loops, dictionaries, exceptions, files, paths, command-line arguments, tests, virtual environments, Git, and a readable README. Add SQLite only after the file tool is understandable; a database is not needed to prove the first contract.

**Publish when:** another person can run the documented command in a fresh environment and you can explain the parsing, validation, and error paths from the code. A reasonable initial work allowance is 30–60 focused hours after basic Python exercises; extend it if the independent explanation gate is not met.

**Independent gate:** close the assistant/tutorial, add one new validation rule and a regression test, and explain why it belongs at that boundary. Do not replace this with collecting a course certificate.

## 5. Flagship 1: Demand Replay

### Problem, audience, and honest scope

A hypothetical bike-service planner wants a next-day usage estimate to prepare staffing or capacity. You will build a **historical demand-planning replay**, not claim a live city deployment or current demand prediction. The dataset is the UCI Bike Sharing collection from 2011–2012. Its official page identifies CC BY 4.0; preserve attribution and the source/version record. [S13](#source-s13)

During this guide’s AI-assisted preparation, the actual official ZIP was inspected to check feasibility: `day.csv` has **731 rows**, `hour.csv` has **17,379 rows**, and the daily dates span 1 January 2011 through 31 December 2012. No duplicate dates or empty daily cells were found in that specific file. In every daily row, `cnt = casual + registered`. This was a schema/feasibility inspection, not a trained-model experiment or a performance result. The archive hash is included in the evidence files.

The dataset is familiar; your differentiator is the forecast contract, leakage control, reproducibility, and delivery. Its age, small size, and single-system context are material limitations. A later extension can use a richer openly licensed dataset after you can defend the small system.

### Fix the prediction contract before modeling

**At the end of day t, predict total rentals for day t+1 using only information available by the end of t.** The actual previous day's count may enter the next day's forecast in the historical replay. Model parameters remain frozen during the final test unless a separately specified retraining protocol is being evaluated.

Assume each daily count becomes available at that day's close for this experiment. UCI does not supply arrival timestamps, so this availability is an explicit replay assumption, not a verified operational service guarantee. A real deployment would need its actual reporting delay built into the feature contract.

Allowed MVP inputs: calendar information known in advance, counts lagged from the forecast origin, and trailing summaries computed only from past observations. Exclude the target day's actual weather, temperature, humidity, and wind unless you have genuine historical weather forecasts available at prediction time. A model using observed future weather must be labeled as a different, oracle-information experiment.

Never use same-day `casual` or `registered` to predict `cnt`: those fields contain components of the answer. Avoid arbitrary row IDs as predictive features. A pipeline can run perfectly while answering the wrong prediction-time question. Scikit-learn's guidance on leakage and preprocessing is directly relevant here. [S06](#source-s06)

### Build and evaluate in this order

1. **Data contract:** validate schema, units, dates, duplicates, missingness, and target composition. Save the source URL, license, download date, and checksum.
2. **Exploratory analysis on the training period:** inspect seasonality, growth, holidays, zeros, and unusual days. Record hypotheses before trying models.
3. **Simple baselines:** last observed day; same weekday one week earlier; a trailing average. Choose formulas that use only available history.
4. **One simple trained model:** regularized linear regression with calendar/lag features; then at most one tree-based candidate such as histogram gradient boosting. Establish why the added complexity might help.
5. **Time-aware validation:** use chronological splits and, when useful, several expanding-window checks inside the training/development period. Fit preprocessors on training data only. A time split alone does not repair an incorrectly shifted feature. [S07](#source-s07)
6. **Locked final test:** freeze the chosen feature/model configuration and evaluate once on the untouched period. Repeatedly changing the model after seeing test errors turns that period into development data.
7. **Service and replay:** a small FastAPI service with a health endpoint, validated request/response schema, model/data version metadata, and a local historical-replay command. Reuse one feature-building implementation across training, replay and serving to avoid inconsistent inputs. A simple interface is enough.

**Concrete initial split, assigned by target date:** train through 30 June 2012 (547 daily rows), validate July–September 2012 (92), and test October–December 2012 (92), before any lag warm-up exclusions. Record exclusions explicitly. Check that no training example's target crosses the cutoff even when its feature date precedes it. A rolling one-day-ahead replay can use previously observed test-period history at each origin; it is not a 92-day-ahead forecast from 30 September. Show a timeline in the evaluation report.

### Metrics that answer a decision

| Metric | Definition/use | Pitfall to avoid |
| --- | --- | --- |
| MAE | Mean of `abs(actual − prediction)` over the declared forecast rows | An overall average can hide holiday or peak-period failures. |
| WAPE | `sum(abs(actual − prediction)) / sum(actual)` on a stated set | Undefined when the denominator is zero; aggregation can hide small-group errors. |
| Slice error | The same metric by weekday/holiday/season or a predeclared demand band | Tiny slices are uncertain; never present one good slice as the overall result. |
| Prediction-interval coverage and width | Optional: fraction of actuals inside the interval, and interval size | Check time/slice calibration; intervals that always contain everything are unhelpful. |
| Decision-cost replay | Optional: a clearly labeled cost function for under/over-preparation | Assumed staffing/inventory costs do not establish real business savings. |

Report baseline and candidate results on the same rows. If you estimate uncertainty, respect temporal dependence—for example, a justified block-based comparison rather than pretending daily errors are independent. Keep the first release understandable; point estimates, row-level predictions, and honest limitations are better than a misapplied significance test.

**There is no pre-earned target score.** To claim that ML adds value, demonstrate a meaningful improvement against the baseline under the declared protocol and constraints. If it does not, ship or recommend the baseline and explain what you learned. Do not set a public “20% improvement” claim before measuring it.

### What to publish

- A real replay demo showing a forecast origin, available inputs, prediction, later observed outcome, and model version.
- `reports/predictions.csv`, an actual metrics JSON, a baseline comparison, and an error-slice report tied to a commit/configuration.
- A data card, split diagram, leakage checklist, and a short explanation of why target-day weather is excluded.
- Unit/data-contract tests, one API integration test, a clean-clone run command, a small sample mode, and CI that actually executes them.
- An architecture page and three observed failure cases. Add a one-page “why I kept/rejected the more complex model” decision note.

**A useful work allowance:** 100–160 focused hours after prerequisites, with further time for revisions or unfamiliar concepts. CPU-only scikit-learn, pandas or Polars, SQLite if useful, pytest, FastAPI, and one container are sufficient. Start locally; paid cloud infrastructure is optional.

**Interview checks:** Why was a random split inappropriate? Which feature could accidentally contain the answer? What exactly was known at the forecast origin? Why might a more accurate aggregate model still be a worse operational choice? What would you monitor if labels arrived late? You should be able to answer with your code and recorded examples.

## 6. Flagship 2: Evidence Desk

### A useful bounded assistant

Build an assistant for a narrow set of beginner Python questions about files, CSV/JSON, exceptions, and command-line arguments. Use a versioned subset of official Python documentation. An answer must cite the supporting page/section, or state that the supplied corpus does not support an answer.

The original application code can use MIT; the Python documentation prose is under the PSF license, while specified code examples also have a 0BSD option. Do not relabel all documentation as MIT or public domain. Pin a snapshot/hash, preserve required notices, record transformations, and keep versioned citation URLs. The moving `/3/` URL is not by itself a reproducibility pin. [S14](#source-s14) [S15](#source-s15)

**User promise:** “Find and explain an answer supported by this pinned documentation subset.” Do not promise a universally correct Python tutor. Treat unfamiliar versions, absent pages, ambiguous questions, and unsupported claims as first-class cases. A foundation model may already know public Python documentation; evaluation must check use of the supplied evidence, not just fluent recall.

### Architecture and baselines

Start with `documents → normalized sections → lexical retrieval → cited passages`. This is a useful no-paid-model baseline. Then compare dense retrieval, hybrid retrieval, and optional reranking only when an error category motivates them. Add a constrained generation adapter after you can evaluate retrieval.

The first interface can be a small web page and FastAPI backend. Keep the model adapter interchangeable. CI should use deterministic fixtures/fakes for behavior; clearly separate those from live-model quality evaluations. No API key belongs in browser code. Provide a keyless passage-search/sample mode so a reviewer can inspect the project without spending money.

A useful comparison ladder is:

1. Keyword/BM25 retrieval with direct evidence display.
2. Dense retrieval with the same corpus and evaluation set.
3. Hybrid retrieval or a reranker, if justified by measured retrieval failures.
4. A grounded answer generator, evaluated for answer quality and citation support.
5. Optional model/latency/cost comparison under the same frozen protocol.

Do not start with an autonomous multi-agent framework. This task has a known workflow and bounded data. Anthropic's engineering guidance distinguishes workflows from agents and recommends simpler, composable approaches before unnecessary complexity. [S09](#source-s09)

### Design the evaluation before tuning

Create a small, manually reviewed question set with answerable, unanswerable, ambiguous, version-sensitive, and malicious-instruction cases. Record expected supporting sections and an answerability label. A proposed first target is about **120 questions**: 40 development, 20 threshold/calibration, and 60 held-out test questions. Those numbers are a practical workload choice, not a statistically sufficient universal benchmark.

Keep paraphrases and close topic families in the same split. Do not use test questions to choose chunk sizes, prompts, retrieval settings, or abstention thresholds. Add independently authored questions where possible; if volunteers contribute, remove personal information and obtain permission to publish their examples. Synthetic questions are allowed if labeled and checked; they are not evidence of real-user demand.

Include near-miss passages, contradictions between versions, questions with no supporting page, and attempts to make the assistant follow instructions embedded in retrieved text. Treat retrieved content as data. Avoid giving the assistant tools that can execute code, send messages, or make external changes in the first version. OWASP's prompt-injection guidance is useful for designing these boundaries, but a short attack set does not prove security. [S10](#source-s10)

| Measure | Define it this way | Report it with |
| --- | --- | --- |
| Retrieval hit@k | Answerable queries for which at least one gold supporting section appears in the top k, divided by answerable queries | k, query count, gold-label method, and whether full evidence requires more than one section |
| Citation support | Number of assessed factual claims supported by the cited passage divided by assessed factual claims | The claim-segmentation/rating rubric; missing citations counted as unsupported; inter-reviewer disagreements if reviewed twice |
| Answer correctness | Human-rubric score or pass rate against the expected answer under the pinned docs | Separate answerable/unanswerable slices; do not collapse every behavior into “accuracy” |
| Unsupported answer rate | Unanswerable queries on which the system nevertheless asserts an answer divided by unanswerable queries | Test set size and cases; zero observed failures in a small set is not zero real-world risk |
| Answer coverage | Queries for which the system gives an answer divided by all queries; also report answered answerable queries divided by all answerable queries | Correctness/support among answered queries, plus the answerability mixture, so abstaining on everything cannot look successful |
| Latency and cost | p50/p95 request time and measured tokens/API usage under stated conditions | Hardware, model/provider/date, prompt/output size, concurrency, repetitions, warm/cold state, and price date |

An LLM judge can assist triage, but validate its rubric on a human-reviewed subset and publish disagreements. It is not an independent ground truth simply because another model produced the score. OpenAI's evaluation guidance is useful for the process; it does not remove the need to define task-specific evidence. [S08](#source-s08)

### Ship only what you can demonstrate

Publish an actual evaluation runner, question/label schema, frozen split manifest, row-level outputs, an error taxonomy, and a baseline table. Give three examples: a supported answer, a deliberate abstention, and a remaining failure. Log the configuration/corpus/model versions so another person can reproduce the comparison as closely as the dependencies allow.

Abstention should be calibrated using held-out development/calibration evidence, not a fabricated “confidence” percentage from the generator. A retrieval score is not automatically a probability of correctness. For small test sets, show numerators/denominators and uncertainty rather than theatrical precision.

**A useful work allowance:** 120–180 focused hours after software/retrieval prerequisites. Start with local lexical search and CPU-friendly embeddings. No GPU is required for that path. If you use a hosted LLM, set a personal hard spending cap, log actual usage, and evaluate a narrow corpus. A suggested optional experiment envelope is US$10–30 total, not a verified provider price quote or a requirement. A local/extractive version can remain free.

**Interview checks:** How did you choose the split unit? Could the model answer from memorization without retrieving the right version? What does your retrieval score mean? What happens when retrieval finds a plausible but irrelevant paragraph? How did you measure citation support? Why did you choose a fixed workflow? What would convince you to remove the generator?

## 7. The reliability release: make one system inspectably operable

After one flagship is useful, spend a bounded release improving how it behaves when conditions are bad. Keep this work inside that repository so reviewers can trace the same system from baseline to delivery. Do not manufacture another application merely to obtain a third pin.

Google's ML Test Score work treats production readiness as broader than model quality; its Rules of ML emphasize straightforward engineering and useful baselines. Monitoring guidance also distinguishes changes in input distributions from actual prediction-quality degradation. [S05](#source-s05) [S11](#source-s11) [S12](#source-s12)

### Implement a small operational contract

- **Input boundaries:** schema validation, payload-size limits, explicit versions, missing-value behavior, and useful error messages.
- **Dependency boundaries:** request timeouts, bounded retries where appropriate, rate/spending limits for paid inference, and a documented fallback. A fallback must be distinguishable from a normal model answer.
- **Observability:** structured logs, request IDs, latency/error counters, and model/corpus/configuration IDs. Keep prompts, keys, and personal data out of routine logs unless a justified, consented, redacted design requires otherwise.
- **Release behavior:** a versioned artifact/configuration, a small evaluation gate, and a tested way to restore the last known working version. CI should run affordable deterministic checks; costly quality evaluations can be a separate explicit job.
- **Documentation:** an operator runbook, a system diagram, and an honest incident report from a controlled drill.

### Run four controlled drills

| Drill | What to demonstrate | What the report should say |
| --- | --- | --- |
| Malformed input or missing data | The service rejects or handles it according to its contract | Exact request/fixture, response, logged event, and regression test |
| Slow/unavailable dependency | Bounded wait, visible fallback, no endless retry loop | The injected fault, timeout/retry policy, and observed recovery |
| Bad model/corpus/config release | The evaluation gate or operator detects a problem and restores the prior version | Actual rollback steps, elapsed recovery time in this drill, and remaining manual work |
| Shifted inputs or delayed labels | Input checks surface a change; quality conclusions wait for appropriate outcomes | What the monitoring can observe, what it cannot establish, and how later labels are joined |

Measure p50/p95 latency, errors, and resource use under a declared small load, such as one and five concurrent clients with fixed request sizes. Record actual hardware and sample count. The chosen load is a development experiment, not proof of internet-scale operation. Define your latency/error budget before a run, then report whether you met it.

Do not infer that a model is inaccurate just because a drift detector fired, or accurate because it stayed quiet. Do not automatically retrain from every alert in the first version. Explain the investigation and release policy. If you lack real users and production traffic, call the result a **controlled reliability drill** or **historical replay**, not “production-grade at scale.”

**Publishing package:** a tagged release, a one-page incident report, an actual before/after measurement table, the failure-injection commands, and a 60–90-second demonstration. Allow roughly 50–90 focused hours after a working flagship; this is an estimate, not a requirement to add a large infrastructure stack.

## 8. A real contribution and a small feedback loop

Choose an open-source dependency or tool you genuinely used. Reproduce a specific problem or confusing setup step. Read its contribution guide and existing issues. Offer a minimal reproduction, a focused correction, and a test or executed example when appropriate. Respond to the maintainer's review. The official Open Source Guides provide useful process guidance. [S25](#source-s25)

A meaningful contribution can be a verified setup correction, an example that previously failed, a useful regression test, or a small bug fix. It need not be a new model architecture. Record **submitted**, **reviewed**, and **merged** accurately; an unmerged self-authored PR is not a maintainer endorsement. Avoid mass typo changes or unsolicited rewrites.

Separately, invite a small number of consenting testers to try one realistic task in a flagship. For the documentation assistant, ask them to find an answer and identify its supporting section. Record where they got stuck and one improvement you made. For the forecasting replay, a peer reviewer can inspect whether your prediction-time contract is valid. If no actual operator uses the tool, say so.

A useful first target is three to five testers/reviewers if available. That is a formative usability/review exercise, not a representative user study. Do not claim customer adoption, business savings, or a success rate from a handful of friendly tests. These are proposed activities. Their inclusion does not imply that outreach, user testing, contributions or applications have been completed.

## 9. Package every claim with its evidence

An employer's practical questions are: can you solve a relevant problem, make sound choices, handle failures, finish usable work, and explain your contribution? Organize each repository so the answer is easy to inspect.

| Review path | A useful design target | What should be visible |
| --- | --- | --- |
| Quick skim | About 30 seconds | User/problem, one real demo, your contribution, one qualified result or current status, and evaluation/reproduction links |
| Technical overview | About five minutes | Baseline, split/labels, architecture, three failure cases, measured constraints, and the important tradeoff |
| Deep review/interview | As needed | Small readable modules, tests, raw outputs, configuration/version records, and an explanation you can modify under questioning |

These reading times are presentation heuristics, not empirical claims about recruiter behavior. The point is to reduce the work required to verify you.

### A compact evidence bundle

```text
README.md
pyproject.toml + a reproducible dependency specification
src/                       actual application/model code
tests/                     behavior, boundaries, data contracts, integration
evals/                     evaluation runner, labels, split manifest
configs/                   explicit experiment/runtime settings
reports/                   measured outputs and row-level predictions
docs/data-card.md          source, license, version, target, exclusions
docs/evaluation.md         baseline, split, metrics, limitations
docs/architecture.md       components and consequential tradeoffs
docs/failure-cases.md       observed errors and attempted repairs
docs/decisions/             short records of choices worth defending
scripts/                   data acquisition, replay, training, evaluation
.github/workflows/         checks that actually execute
LICENSE + THIRD_PARTY_NOTICES.md where needed
```

Keep the structure proportional. An empty folder hierarchy does not improve a small project. A result should identify its code commit, data/corpus checksum, split, configuration, library/model version, seed where applicable, environment, and actual output. For hosted models, record provider/model/date and changing dependencies rather than promising exact deterministic reproduction.

### What the README should contain

GitHub's own guidance emphasizes what the project does, why it is useful, how to start, where help is available, and who maintains it. [S16](#source-s16) For your projects, add:

1. A one-sentence problem and main scope limit.
2. Links to a real demo/recording, evaluation report, and tested reproduction command.
3. Your exact contribution and any collaborators or AI assistance.
4. A baseline comparison with actual numbers, units, sample size, and split.
5. A small architecture diagram and the main rejected alternative.
6. Three concrete failures, not just “more data would improve it.”
7. Data/model/code rights and dependency requirements.
8. The next experiment that could change your decision.

Give reviewers a small offline/sample mode and saved evaluation output. Label cached, replayed, and precomputed results. Do not make a paid API key, a sleeping cloud endpoint, or a large model download the only way to see evidence.

**Example result sentence, with placeholders:** “On [N] held-out [queries/days] using [split protocol], [candidate] achieved [actual metric] versus [baseline metric]. This was an [offline/replayed/live] evaluation; [main limitation].” Never publish the placeholders as a claim or fill them with a target you have not measured.

## 10. GitHub and LinkedIn: make the work easy to find

### GitHub

A GitHub profile README conventionally lives in a public repository named exactly after the username, with a nonempty root README. GitHub supports up to six pinned repositories/gists combined. You do not need six completed projects to use the feature. [S17](#source-s17) [S18](#source-s18)

Once the evidence exists, use this pin order:

1. Strongest project aligned with your target role: Evidence Desk for applied-AI product roles, or Demand Replay for MLE roles.
2. The complementary flagship.
3. A meaningful collaboration/contribution record or a later distinct project, if genuinely substantial.
4. A substantial documentation or learning application, if you have built one, as evidence of communication, interface design and delivery.

Keep the reliability release inside its flagship. Link the incident/evaluation report prominently. Do not fill pins with scaffolds just to make the profile appear larger. Accurate About descriptions, relevant topics, a working demo link, and genuine release notes improve navigation; none guarantees stars or hiring.

Use a truthful profile sentence. At the beginning: “Learning Python and ML engineering through reproducible projects.” Later, when supported: “Building evaluated AI applications and ML systems with Python; seeking junior/associate engineering opportunities.” A target role should not be presented as current employment.

CI is evidence that the configured checks ran, not that every possible behavior is correct. Publish readable checks and their scope. If a credential is exposed, revoke/rotate it before treating file deletion as a fix; history and copies can retain it. [S19](#source-s19) [S20](#source-s20)

### LinkedIn and other social media

LinkedIn's Featured section supports posts, articles, links, and media. Use it to surface the strongest case study, a short demo, and a concise portfolio overview or contribution. The platform documentation supports those capabilities; it does not establish a ranking formula or an optimal posting time. [S21](#source-s21)

Make a 60–90-second captioned demonstration for each flagship:

- **0–10 seconds:** who has the problem and one realistic input.
- **10–30 seconds:** the actual useful behavior, including evidence/citations or the forecast origin.
- **30–50 seconds:** an unsupported input or injected failure and the bounded response.
- **50–70 seconds:** the baseline/evaluation result, with sample size and context visible.
- **70–90 seconds:** one tradeoff, your contribution, and where to inspect the work.

Use a clean demonstration profile. Label simulations, historical replay, cached answers, and edited timing. Provide a written equivalent. The purpose is to make real evidence understandable, not to hide weaknesses behind a polished video.

### Three posts worth publishing when the work exists

**An experiment:** “I am building [tool] for [specific problem]. The baseline was [method]. On [N, held-out unit], [change] moved [metric] from [actual A] to [actual B], with [cost/latency tradeoff]. The largest remaining error category was [observed issue]. Evaluation and reproduction: [link].”

**A failure and repair:** “This input broke my [system]. I assumed [assumption]; [trace/test] showed [cause]. I changed [implementation] and added [regression]. It still struggles with [limit]. Before/after evidence: [link].”

**A release and feedback:** “I released [version] to test [user need]. [Actual number/type] of testers tried [task]; I observed [finding] and changed [behavior]. This is a small formative test, not a production-adoption claim. Demo, evaluation, and limitations: [link].”

If nobody has tried it yet, say that and invite specific feedback. If a model loses to the baseline, explain why the simpler approach wins. Avoid vague “95% accuracy,” unmeasured time savings, invented clients, and “production scale” claims from a local test.

Allow about **2–3 hours of a 36-hour work week** for documentation and communication once real artifacts exist. One substantive update a week or every two weeks is a reasonable starting cadence; it is not a quota, an algorithm trick, or a proven hiring intervention. Measure useful reviews, qualified conversations, reproducibility feedback, and application-stage outcomes. Stars and views help distribution, but do not certify skill.

## 11. A 24-week first pass, with evidence gates

This is a planning scaffold for **six focused hours on six days per week**, with one recovery/light-review day. That is 36 scheduled hours weekly. Actual useful time varies; carry unfinished work forward and reduce scope before sacrificing understanding. Completing this calendar is not a job guarantee or a substitute for the gates.

| Weeks | Main work | Publishable output | Gate before moving on |
| --- | --- | --- | --- |
| 1–2 | Python basics, terminal, files, functions, simple tests and Git | Tiny exercises and the first CSV checker version | Add a validation rule and explain its test without copying a solution |
| 3–5 | Collections, data cleaning, SQL basics, HTTP/API basics, readable modules | A documented, tested CSV CLI; small SQL/API exercises | Debug malformed input, write a join, and explain a request/response boundary |
| 6–8 | Arrays, core algebra/probability/statistics, regression, leakage, evaluation | A small baseline experiment and a split diagram | Explain target, features, baseline, loss/metric, and why the split is valid |
| 9–13 | Demand Replay | First flagship repository, actual predictions/metrics, data card and demo | Clean-clone run; honest temporal evaluation; code and failures you can defend |
| 14–18 | Evidence Desk | Second flagship, retrieval/answerability evaluation, citation/abstention demo | Held-out queries; reproducible retrieval; documented unsupported answers and costs |
| 19–21 | Reliability release and tester feedback | Incident report, regression checks, tagged release, revised case study | Demonstrate failure handling, monitoring limits, and a real rollback drill |
| 22–24 | Contribution, interview practice, tailored application loop | Accurate contribution record, profile/Featured assets, targeted applications | Match specific role requirements to evidence and solve a small unfamiliar change independently |

The project-hour estimates above are narrower implementation allowances after prerequisites. These calendar blocks also include learning, debugging, documentation, review, and contingency; they are not additional guaranteed durations. Some learners will need longer than 24 weeks. Apply earlier when an eligible role matches work you can already demonstrate, rather than waiting for every row to be complete.

For an AI-product emphasis, swap the two flagship blocks after week 8 if your target roles justify it. For an MLE emphasis, keep forecasting first and deepen probability, optimization, SQL, and data pipelines. For research roles, treat mathematical depth and reproduction work as a later path, often with additional eligibility requirements.

The related [learning roadmap](https://github.com/MJmuhammadjihad/AI-ML-Engineering-Roadmap) can supply the learning sequence: guided foundations and Python/Git/data modules first; evaluation and classical ML for Demand Replay; retrieval/evaluation modules for Evidence Desk; packaging, serving, monitoring, and responsible-system modules for the reliability release. You do not need to finish every optional vision or research module before beginning a relevant project.

### A six-hour active-work pattern

| Block | Minutes | Purpose |
| --- | --- | --- |
| Retrieve and plan | 30 | Reconstruct yesterday's concept and choose one observable outcome |
| Learn the next prerequisite | 90 | Read, work a small example, and answer a question before running code |
| Build or investigate | 150 | Implement one bounded behavior or reproduce one failure |
| Evaluate and test | 60 | Run meaningful checks and inspect actual outputs |
| Explain and record | 30 | Write the decision, result, limitation, and next step |

The total is 360 active minutes; breaks are additional. Early weeks will need more guided learning; later weeks can transfer that time to implementation. On one day, use part of the documentation block for a real portfolio update. Do not turn every study session into a promotional post.

## 12. Readiness: what you should be able to do without a script

Use these as practice gates, not an external certification. Keep assistance and independent attempts distinct.

1. **Build a small change:** add a new validation rule, feature transform, or API behavior from a written requirement, with a meaningful test.
2. **Debug an unfamiliar failure:** trace a malformed record or retrieval miss through the system without guessing at random fixes.
3. **Explain the baseline:** describe why it is fair, where it fails, and whether complexity was justified.
4. **Defend the split:** identify time/entity/topic leakage and tell a reviewer what the final test does and does not establish.
5. **Read the metrics:** show numerator, denominator, sample size, slices, and uncertainty; identify a metric that would reward the wrong behavior.
6. **Trace a request:** explain the components, failure boundaries, logged metadata, model/data versions, and recovery path.
7. **Discuss tradeoffs:** name an alternative you rejected and the evidence that could change your mind.
8. **Explain your contribution:** distinguish original implementation, borrowed material, collaborators, and AI-assisted work.

A useful AI-assistance note is: “I used [tool] for [specific tasks]. I independently reviewed/implemented [components], ran [checks], and can explain [decisions].” Match it to the truth. Generated code is useful assistance; independent ability must be demonstrated separately.

Anthropic explicitly invites candidates to highlight independent research, thoughtful writing, and open-source work, and describes live coding. OpenAI's interview guide emphasizes reasoning, code quality, performance, test coverage, and communication. These are employer-specific examples, not promises of access to those companies. Their tool rules differ by assessment; follow the explicit instructions and ask the recruiter if unclear. [S22](#source-s22) [S23](#source-s23) [S24](#source-s24)

## 13. Turn the portfolio into an application process

Start a role inventory while learning. Once the first flagship is defensible, begin with a manageable set of genuinely relevant opportunities. For each role, record the employer URL/date, actual responsibilities, required versus preferred qualifications, eligible countries, authorization/sponsorship, language, time zone, degree/enrollment, and your strongest matching evidence.

Use three decisions:

- **Eligible and evidence-aligned:** tailor the application to two or three relevant behaviors and link directly to the proof.
- **Eligibility unclear:** investigate the employer's stated policy or ask a concise appropriate question; do not infer worldwide eligibility from “remote.”
- **Hard eligibility mismatch or substantially different seniority:** choose another opportunity or a longer-term preparation path. A portfolio cannot grant a required enrollment status, clearance, or work authorization.

Do not mechanically reject yourself for every preferred tool you lack. Do not ignore explicit hard conditions. A job-description wish list and a legal/student-status condition are different kinds of constraints. Keep the application truthful.

**Resume bullet pattern:** “Built [system] for [problem]; compared [baseline] and [candidate] on [N, split], obtaining [actual metric] under [measured constraint]. Added [specific failure handling/tests], with [main scope limit].” For a contribution: “Contributed [change] to [project]; [submitted/reviewed/merged], addressing [specific behavior and review feedback].”

Use a simple application log. If you get few screens, inspect eligibility, role alignment, and whether the evidence is visible. If you reach technical interviews but struggle, practice the observed gaps. If people cannot run your project, repair reproduction. Small samples are noisy; do not invent a causal explanation for each rejection or a conversion-rate guarantee.

The global goal is a direction, not a location filter called “anywhere.” A reader’s country and work authorization must be checked separately; this report does not establish eligibility for any sampled vacancy. Build capability, then test the opportunity set available to your actual situation.

## 14. What to postpone, and why

| Temptation | Better default at your stage | When to reconsider |
| --- | --- | --- |
| A generic chat UI with no evaluation | A narrow assistant with a baseline, citations, abstention, and an error report | Broader scope after a real use case and evaluation support it |
| Training an LLM from scratch | Understand small models, then use an existing model behind a bounded interface | A research/infra goal with data, compute, math, and a meaningful experiment |
| Fine-tuning before defining success | Establish a baseline, failure taxonomy, clean data, and held-out evaluation first | A measured failure that adaptation could plausibly address |
| Multiple autonomous agents | A fixed, inspectable workflow with bounded tools | A task requiring dynamic decisions and an evaluation that justifies the extra failure surface |
| Kubernetes, feature stores, distributed training everywhere | One small service/container, explicit artifacts, simple CI and logs | A concrete role/project requirement or a demonstrated scaling problem |
| Dozens of cloned notebooks | Two independently understood systems with reproducible evidence | Small exercises remain useful for learning, without overstating their portfolio significance |
| A huge model score without context | Baseline, split, sample size, constraints, and failures | More complexity only when the decision requires it |
| Posting daily to appear active | Publish when a real experiment, fix, review, or release teaches something | Cadence can change with meaningful work and audience feedback |

A later specialization should follow repeated requirements in your actual eligible role list. Computer vision, recommendations, speech, multilingual NLP, and research replication can all be valuable. Choose one when you have a domain question, appropriate data rights, a measurable task, and a reason that it adds evidence your existing work lacks.

## 15. Your next seven days

Begin with ownership of one small program before starting the flagships.

| Day | Concrete work | Evidence to keep |
| --- | --- | --- |
| 1 | Practice running Python, save a small program, and explain each line | Saved file, actual output, and a short explanation in your own words |
| 2 | Practice functions, loops, and dictionaries on a tiny invented dataset | One small change made without copying, plus its expected/actual output |
| 3 | Read a ten-row CSV fixture and summarize its fields/counts | The fixture, parser, output, and one malformed-input example |
| 4 | Add date/count checks and clear errors | Tests for good input, missing columns, invalid counts, and duplicates |
| 5 | Use Git meaningfully; write run/setup instructions and a scope statement | A clean-clone check and a README another person can follow |
| 6 | Add one new requirement independently; inspect three real role descriptions | A new regression test and an eligibility/evidence worksheet |
| 7 | Rest or do light review; identify what is still not independently understood | A short next-week plan based on actual gaps, not a completion streak |

If those prerequisites take longer, use more days. Do not claim that a seven-day exercise makes you ready for an AI-engineering job. Its purpose is to establish the working method that makes the later projects credible.

The immediate objective is precise: **finish one small program you can run, test, repair, and explain.** The longer-term objective is a small body of work where each claim has a visible result, a valid evaluation, and a contribution you genuinely understand.
