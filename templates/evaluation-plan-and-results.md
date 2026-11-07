# Evaluation plan and results — [project/version]

**Protocol status:** [draft / frozen on date / amended with reason].
**Results status:** Not measured until actual run artifacts are linked.

## 1. Decision and scope — fill before tuning

- User/task: [specific decision].
- Question: [what comparison could change a design choice].
- Baseline: [exact formula/system/configuration].
- Candidate: [single bounded change initially].
- Success/release rule: [predeclared quality and resource conditions, with rationale; not a claimed result].
- Non-goals and unsupported inputs: [scope].
- What a negative result would mean: [including keeping the baseline].

## 2. Data and split contract

- Source URL, access date, license/attribution, artifact SHA-256: [record].
- Version, units, target, labels, sample provenance: [record].
- Split unit and assignment: [time/entity/topic family; boundaries and manifest hash].
- Development / calibration / held-out counts: [actual before/after exclusions].
- Exclusions and missing-data behavior: [predeclared reason and affected counts].
- Preprocessing fits and selection: [training/development only].
- Final-test lock: [date/config; who can inspect it; changes after inspection require a new evaluation boundary].
- Labeling rubric, human review and disagreement handling: [method, where applicable].

### Demand Replay contract, if used

At the end of day t, predict rentals for t+1 from information available through t. Completed-day count availability is a replay assumption; UCI does not provide arrival timestamps. Exclude target-day observed weather and same-day target components. Use known calendar information and correctly shifted lag/trailing features. Document each feature's availability and reuse one feature builder across training, replay and serving.

Suggested initial daily split, assigned by target date: train through 2012-06-30; validation July–September 2012; final test October–December 2012. The source has 547 / 92 / 92 rows before lag warm-up exclusions; record your actual evaluated counts. Check no training label crosses the cutoff. Freeze model weights on the final test. Previously observed test-period counts can enter subsequent one-day forecasts; this is not a 92-day forecast from one origin.

Compare previous-day, previous-weekday and trailing-average baselines on the **same eligible forecast rows**. Record lag warm-up and any common-row restriction. Fit all preprocessing within the appropriate training boundary.

### Evidence Desk contract, if used

Pin the documentation version and corpus hash. Group paraphrases/close topic families within one split. The proposed 40 development / 20 calibration / 60 held-out questions are a workload plan, not a universal statistical guarantee. Report actual counts, answerability categories, gold sections, and question authorship (including labeled synthetic questions).

Tune retrieval, prompts and abstention only on development/calibration data. Include unsupported, ambiguous, version-sensitive and instruction-injection cases. Do not treat an LLM judge as ground truth; compare its judgments with a human-reviewed rubric/subset. State whether answers could come from memorized public documentation without correct retrieval.

## 3. Metric definitions

Delete irrelevant rows and add task-specific measures before running.

| Metric | Numerator / denominator or formula | Required context |
| --- | --- | --- |
| MAE | Sum absolute error / evaluated forecast rows | Units, exclusions, same rows for baseline/candidate |
| WAPE | Sum absolute error / sum actual demand | Undefined if denominator is zero; show slice sizes |
| Retrieval hit@k | Answerable queries with ≥1 gold section in top k / answerable queries | k, gold-label method; a complete answer may require several sections |
| Citation support | Assessed factual claims supported by cited passages / assessed factual claims | Missing citations count as unsupported; publish segmentation/rating rubric |
| Unsupported answer rate | Unanswerable queries receiving an asserted answer / unanswerable queries | Answerability rubric and observed cases |
| Answer coverage | Queries receiving an answer / all queries | Report correctness/support among answered queries alongside this |
| Answerable coverage | Answerable queries receiving an answer / all answerable queries | Report the test-set answerability mixture; total coverage alone depends on that mixture |
| Answer correctness | Human-rubric passes or score / explicitly defined assessed units | Answerable/unanswerable slices and disagreements |
| Latency | p50/p95 of measured elapsed request times | Request count, size, concurrency, warm/cold state, hardware |
| API cost | Measured usage × recorded unit prices | Provider/model/date, price date/currency; estimates distinguished from bills |

Predeclare slices: [weekday/holiday; answerability/version/injection; other justified categories]. Record every slice's sample count. Small slices are uncertain. If adding uncertainty estimates, justify the method and dependencies; daily forecast errors are not automatically independent.

## 4. Reproduction manifest

| Field | Value |
| --- | --- |
| Code commit and dirty working-tree status | [ ] |
| Dataset/corpus and split hashes | [ ] |
| Configuration and prompt IDs | [ ] |
| Runtime/library/embedding/model versions | [ ] |
| API provider/model identifier and date | [If used] |
| Seeds, repetitions and nondeterminism limits | [ ] |
| OS/CPU/GPU/RAM | [ ] |
| Request sizes, concurrency and warm-up | [ ] |
| Exact execution command | [ ] |
| Started/finished timestamps and time zone | [ ] |
| Raw predictions/answers, metrics and logs | [Paths/hashes] |

## 5. Results — fill only after execution

| System/version | Split/slice | N and denominator | Metric | Actual value | Resource context | Artifact |
| --- | --- | --- | --- | --- | --- | --- |
| [Baseline] | [ ] | [ ] | [ ] | Not measured | [ ] | [ ] |
| [Candidate] | [ ] | [ ] | [ ] | Not measured | [ ] | [ ] |

Use `results.csv` for long-form measured rows. Preserve raw outputs needed to verify the metrics, subject to data rights/privacy. Do not substitute an intended target for a value.

## 6. Interpretation and decision

- Observed difference, uncertainty and resource tradeoff: [actual evidence].
- Three specific failures: [examples and links].
- Does the candidate satisfy the predeclared rule? [yes/no/inconclusive, why].
- Keep/reject/modify decision: [reason].
- What this evaluation cannot establish: [production behavior, generalization, security, business impact as appropriate].
- Next bounded experiment: [question].

## 7. Reliability drill addendum, when applicable

For each injected fault, record the fixture, expected behavior, actual response/logs, elapsed recovery time, regression test and remaining manual steps. Cover malformed input, slow/unavailable dependencies, bad release/rollback, and changed inputs/delayed labels as applicable. State the measured local load, hardware and sample count. Input drift alone neither proves nor rules out quality degradation. Label drills as simulations, not real production incidents.
