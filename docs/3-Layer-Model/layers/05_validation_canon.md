# Layer 05 — Validation / Canon

## 1. Function

The Validation / Canon layer determines what may become stable enough to be compiled, published, distributed, referenced, rendered, or acted on.

Its role is not to create truth by assertion. Its role is to enforce the boundary where proposed knowledge becomes validated, canonical, versioned, traceable, and safe to reuse.

In the kOA Digital Ecosystem, validation sits between resolved knowledge and canonical compilation:

```text
Ingest → Extract → Resolve → Validate → Compile → Publish/Distribute
```
Nothing should enter the canon merely because it was submitted, generated, summarized, popular, or useful. It must pass explicit validation gates.

## 2. Core question

What is stable, validated, and traceable enough to become canonical or canon-adjacent?

Sub-questions:

* Has the claim, artifact, or resolution been validated?
* Are its sources and provenance traceable?
* Are ambiguities preserved rather than hidden?
* Are failures explicit and structured?
* Are inputs, policies, configurations, and references pinned?
* Can the result be rebuilt, audited, compared, or contested?
* Is this allowed to become canonical truth, or only proposed work?

## 3. Internal kOA components

Relevant kOA components:

* Orgo
* Kristal
* SenTient
* Validation Report
* Kristal Exchange
* Runtime Pack
* Build Record
* Release Record
* Orgo Case
* Orgo Task
* artifact references
* gate outcomes
* pinned policies
* canonical refs
* governed feedback

Role split:

* **SenTient** resolves ambiguity and produces explicit resolved structures.
* **Validation** checks whether resolved inputs pass deterministic acceptance criteria.
* **Orgo** enforces stage ordering, gates, audit records, and publication rules.
* **Kristal** compiles validated knowledge into canonical Exchange and derived Runtime Packs.
* **Konnaxion** verifies, activates, and rolls back distributed Runtime Packs fail-closed.
* **Feedback** creates new governed work; it does not mutate canon directly.

## 4. Inputs

This layer receives material from previous layers, especially:

* resolved claims;
* structured knowledge candidates;
* provenance-aware inputs;
* ambiguity reports;
* policy context;
* mandate references;
* validation rules;
* schema references;
* pinned toolchain information;
* prior canonical references;
* proposed changes to existing canon;
* feedback that has been turned into governed work.

Typical input artifacts:

```text
Input Snapshot Set
Claim-IR
Resolved Claim-IR
policy / mandate refs
blueprint refs
candidate artifact refs
```

## 5. Outputs

This layer produces or enables:

* Validation Reports;
* PASS / FAIL gate outcomes;
* structured error codes and categories;
* Build Records;
* Release Records;
* canonical artifact references;
* Kristal Exchange compilation eligibility;
* Runtime Pack compilation eligibility;
* rejection records;
* new governed work for failed, partial, or contested inputs.

Typical output path:

```text
Resolved Claim-IR
→ Validation Report
→ if PASS: Compile via Kristal
→ Kristal Exchange + Runtime Pack
→ Release / Distribution
```

If validation fails:

```text
Resolved Claim-IR
→ Validation Report FAIL
→ no compile
→ Orgo Case / Task for correction, review, or rejection
```

## 6. External vocabulary

Useful external vocabulary for this layer:

* validation gate;
* quality assurance;
* conformance testing;
* evidence governance;
* canon governance;
* truth boundary;
* canonical release;
* schema conformance;
* deterministic validation;
* content-addressed artifact;
* immutable release;
* audit trail;
* change control;
* versioned knowledge base;
* governed feedback loop.

## 7. Core invariants

### 7.1 No compile on fail

If validation fails, Orgo must not compile Exchange or Runtime Pack.

Validation failure blocks compilation, publication, activation, and downstream canonical use.

### 7.2 Fail-closed by default

When validation or verification cannot prove correctness, the system must refuse progression.

A failed or uncertain validation state is not treated as partial truth.

### 7.3 Canon is immutable after publication

Canonical truth artifacts are immutable once published.

Changes produce new versions. They do not mutate the existing canonical artifact in place.

### 7.4 Feedback does not mutate canon directly

Feedback creates new governed work.

It may trigger new Cases, Tasks, validations, builds, or releases, but it does not directly rewrite canon.

### 7.5 Determinism is required at the gate

Given the same pinned inputs, policies, configurations, and toolchain versions, validation must produce the same gate outcome and stable error categories.

### 7.6 Canonical truth depends on typed artifacts

Canon is not implicit state.

kOA boundaries exchange typed artifacts and references, not hidden memory or informal assumptions.

### 7.7 kOA does not redefine Kristal contracts

Kristal-owned artifact formats and schemas remain defined by the pinned Kristal dependency.

This layer describes kOA’s use of validation and canon boundaries; it does not restate Kristal schemas, canonicalization rules, hashing rules, or signature rules.

## 8. Failure mode if absent

Without this layer:

* proposals become “truth” too easily;
* summaries replace validated knowledge;
* feedback silently rewrites canon;
* generated outputs can introduce unsupported facts;
* failed validation may still leak downstream;
* conflicting versions become indistinguishable;
* decisions cannot be audited;
* downstream action may execute on untrusted knowledge;
* rollback and investigation become unreliable;
* communities lose the ability to contest what became official.

The result is epistemic drift: the system appears to know, but cannot prove how it knows.

## 9. Relation to other layers

### Previous layer: Layer 04 — Structured Knowledge

Layer 04 turns sources, claims, evidence, and context into structured knowledge candidates.

Layer 05 decides whether those candidates may become validated, canonical, or eligible for compilation.

### Next layer: Layer 06 — Deliberation

Layer 06 can use validated knowledge as a shared substrate for structured discussion.

Deliberation should know whether it is discussing:

* proposed knowledge;
* validated knowledge;
* canonical knowledge;
* contested knowledge;
* failed or rejected knowledge.

### Later layers

Layer 07 — Decision / Legitimacy depends on this layer so that decisions can distinguish evidence from unsupported opinion.

Layer 08 — Execution depends on this layer so that tasks do not operate on unvalidated canon.

Layer 09 — Memory / Learning depends on this layer so that lessons learned become governed updates rather than uncontrolled mutation.

## 10. Layer boundary

This layer is the boundary between:

```text
structured but not yet canonical
```

and:

```text
validated, versioned, traceable, canon-eligible
```

It is also the boundary between:

```text
feedback as social input
```

and:

```text
feedback as governed work
```

## 11. Minimal example

A community submits a set of claims about a civic issue.

1. Sources are ingested with provenance.
2. Claims are extracted.
3. SenTient resolves ambiguity where possible.
4. Validation checks consistency, provenance, schema conformance, policy requirements, and deterministic criteria.
5. If validation passes, Kristal may compile the validated material into canonical artifacts.
6. If validation fails, Orgo records the failure and creates governed work for correction, review, or rejection.

At no point does a comment, vote, AI summary, or feedback event directly mutate canon.

## 12. One-sentence definition

Validation / Canon is the layer where structured knowledge is tested, gated, versioned, and made eligible for canonical use without allowing hidden mutation, unverifiable truth, or downstream drift.


