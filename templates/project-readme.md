# [Project name] — [specific problem]

**Status:** [learning exercise / prototype / evaluated release; date and version].

[Audience] needs to [decision/task]. This project [bounded behavior]. Its main limit is [limit].

[Demo or labeled replay] · [Evaluation] · [Reproduce] · [Failure cases]

## What I built

[Your implementation and consequential decisions. State whether this is a historical replay, offline benchmark, local service, or genuinely used deployment. Credit collaborators, borrowed work, and AI assistance.]

## Main finding

**Until evaluation is complete:** Results are not yet measured. The current release implements [actual behavior].

**Replace that sentence only after measurement:** On [N held-out units, split definition], [candidate] obtained [metric, numerator/denominator where relevant] compared with [baseline result], under [protocol/version]. The tradeoff was [measured cost/latency/quality difference]. [Uncertainty and scope limit].

If the baseline wins, explain why you retained it. Do not invent a target improvement, business saving, or production-adoption claim.

## Reproduce

- Supported OS/runtime: [actually tested versions].
- Hardware and observed runtime/memory: [measured, or explicitly not measured].
- Dependencies and installation: [tested clean-clone commands].
- Small offline/sample run: [command, inputs, expected output location, success check].
- Full evaluation: [command, prerequisites, artifact locations].
- Network/API requirements and spending cap: [none or exact requirements; never include a key].
- Precomputed/cached outputs: [explicit labels and how to reproduce them].

```text
[Replace this block with commands you actually ran in a fresh environment.]
```

## Data and evaluation

- Source, version/checksum, retrieval date, attribution, license: [records].
- Task, target, prediction/request boundary: [definition].
- Baseline and reason it is fair: [definition].
- Split unit, boundaries, exclusions and final-test lock: [protocol].
- Leakage risks and prevention: [specific checks].
- Metrics, denominators, sample sizes, labels and reviewer rubric: [evaluation link].
- Results: [machine-readable outputs, commit/config IDs, error-slice table].

## System and tradeoffs

[Small architecture diagram: input → validation → inference/retrieval → response → measured output. Name versioned artifacts and failure boundaries. Explain one rejected alternative and what evidence could change that decision.]

## Failure cases

| Observed case | What happened | Cause/evidence | Fix or remaining limit |
| --- | --- | --- | --- |
| [Case 1] | [Actual behavior] | [Trace/test] | [Status] |
| [Case 2] | [Actual behavior] | [Trace/test] | [Status] |
| [Case 3] | [Actual behavior] | [Trace/test] | [Status] |

## Tests and delivery

[What CI actually executes; data/contract, behavior, integration and quality checks; versioned release/replay procedure; bounded timeouts/retries where applicable; rollback instructions. State untested conditions.]

## Limitations and next experiment

[Population, data age, sample size, unsupported cases and deployment limits. One next question justified by current evidence.]

## Ownership, assistance and licenses

[Your role, collaborator credits, cited materials, AI-assisted tasks, independent validation. State code, data, documentation and model-weight licenses separately; grant only rights you hold. Add maintainer/help/contribution information when applicable.]
