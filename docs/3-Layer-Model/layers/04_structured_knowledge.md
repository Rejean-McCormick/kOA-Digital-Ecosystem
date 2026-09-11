# Layer 04 — Structured Knowledge

## 1. Function

The Structured Knowledge layer turns source-bound material into reusable knowledge artifacts.

Its role is to transform raw or semi-structured inputs — documents, claims, evidence, definitions, observations, testimony, datasets, prior outputs, and resolved semantic material — into knowledge units that can be validated, compiled, distributed, queried, rendered, reused, and remembered.

In kOA terms, this layer is where knowledge stops being only prose, discussion, notes, or files, and becomes part of a governed knowledge substrate.

This layer does **not** define Kristal artifact schemas. Kristal v4 remains the normative source for Kristal-owned artifact contracts. The layer model describes the role that structured knowledge plays in the broader kOA architecture.

---

## 2. Core question

What do we know clearly enough to preserve, validate, reuse, query, render, distribute, or act on?

Sub-questions:

- What claim, concept, entity, definition, or relationship is being represented?
- What evidence supports it?
- Where did the supporting material come from?
- What uncertainty, conflict, ambiguity, or limitation remains?
- Can the knowledge be validated?
- Can it be reused outside the original context?
- Can it be carried into later decision, execution, or memory layers?

---

## 3. Internal kOA components

Relevant kOA components and concepts:

- Kristal
- Claim-IR
- Resolved Claim-IR
- Validation Report
- Exchange
- Runtime Pack
- Da’at / Kristal Bridge
- SenTient
- Konnaxion
- Orgo build records
- Release records
- provenance references
- content-addressed references
- schema conformance checks
- canonical artifacts
- offline query/runtime material

The central operational role is played by the Kristal boundary: kOA prepares, validates, hands off, consumes, distributes, and operates knowledge artifacts without re-specifying Kristal’s normative contracts.

---

## 4. Inputs

This layer receives material from earlier layers, especially Layer 03 — Provenance / Ingestion.

Inputs may include:

- source snapshots;
- source references;
- documents;
- datasets;
- testimony;
- civic input;
- discussions;
- extracted claims;
- definitions;
- entities;
- semantic relationships;
- candidate mappings;
- resolved claims;
- ambiguity markers;
- validation diagnostics;
- policy bundles;
- mandate constraints;
- provenance metadata.

Inputs must retain enough provenance for later audit, validation, reproduction, or refusal.

---

## 5. Outputs

This layer produces or prepares structured knowledge outputs such as:

- reusable claims;
- structured definitions;
- entity and relationship records;
- provenance-bound knowledge units;
- validation-ready material;
- validation results;
- canonical knowledge artifacts;
- Exchange artifacts;
- Runtime Packs;
- content-addressed references;
- queryable knowledge packages;
- material suitable for rendering, distribution, execution, and memory.

The outputs of this layer should be portable enough to support downstream use without forcing every later actor to reread and reinterpret the original sources.

---

## 6. External vocabulary

Useful external vocabulary for explaining this layer:

- structured knowledge;
- knowledge artifact;
- verified knowledge artifact;
- knowledge object;
- knowledge package;
- FAIR knowledge object;
- knowledge graph;
- semantic data;
- claim-level provenance;
- evidence-backed claim;
- provenance-aware knowledge unit;
- portable knowledge artifact;
- canonical knowledge artifact;
- runtime knowledge package;
- queryable evidence base;
- machine-verifiable knowledge;
- data lineage;
- evidence lineage;
- semantic memory substrate.

Recommended public phrasing:

> Structured Knowledge is the layer where raw contributions become reusable, provenance-aware knowledge artifacts.

Technical phrasing:

> This layer prepares and consumes validated, schema-conformant knowledge artifacts that can be compiled into canonical exchange and runtime forms.

---

## 7. Failure mode if absent

If this layer is missing, knowledge remains trapped in unstable forms:

- posts;
- comments;
- PDFs;
- reports;
- notes;
- oral memory;
- isolated databases;
- private files;
- chat logs;
- human interpretation only.

Without structured knowledge:

- claims cannot be reliably traced to evidence;
- definitions drift;
- versions become confused;
- contradictions remain hidden;
- summaries replace validation;
- downstream decisions depend on fragile interpretation;
- AI may hallucinate or over-compress;
- later users must redo the same interpretation work;
- communities lose memory;
- knowledge cannot be carried offline;
- validated results cannot become durable infrastructure.

The failure mode is not only technical. It is civic: groups cannot govern what they cannot structure, verify, reuse, or remember.

---

## 8. Relation to other layers

### Previous layer

Layer 03 — Provenance / Ingestion

Structured Knowledge depends on provenance-aware input. The system should know where material came from, when it was captured, under what authority or policy context, and what transformations were applied.

### Current layer

Layer 04 — Structured Knowledge

This layer organizes meaning into reusable knowledge units and prepares material for validation, compilation, distribution, rendering, and memory.

### Next layer

Layer 05 — Validation / Canon

Structured knowledge is not automatically canonical. It must pass validation gates before it can become accepted canonical material or be compiled into publishable/distributable artifacts.

### Downstream layers

Structured knowledge feeds:

- deliberation;
- decision support;
- execution;
- rendering;
- distribution;
- offline runtime;
- memory;
- education;
- audit;
- future cycles.

---

## 9. Core invariants

This layer should respect the following invariants:

1. **No schema duplication**

   kOA layer-model documentation must not restate Kristal v4 schemas, field lists, canonicalization rules, signing rules, or artifact contracts.

2. **Kristal remains normative**

   When a Kristal-owned artifact is involved, the pinned Kristal v4 documentation is the source of truth.

3. **Provenance must be preserved**

   Structured knowledge must retain links to source material, validation context, and relevant diagnostic information.

4. **Validation precedes canon**

   Structured material is not canonical merely because it is structured. It must pass validation.

5. **No compile on fail**

   If validation fails, compilation must not proceed.

6. **No hidden mutation of truth**

   Feedback, corrections, disputes, and updates must become governed work, not silent edits to canon.

7. **Portability matters**

   Knowledge should be structured so it can travel across contexts, systems, and runtime environments.

8. **Offline usability matters**

   When packaged into runtime form, knowledge should remain usable without continuous reliance on a central online platform.

9. **Structured does not mean certain**

   Structured knowledge may preserve uncertainty, ambiguity, conflict, or unresolved status explicitly.

---

## 10. Relationship to Kristal

Kristal is the truth substrate and artifact boundary for this layer.

In the kOA Digital Ecosystem, Kristal-owned artifacts include canonical outputs such as Exchange and Runtime Pack forms. kOA integrates with these artifacts through pinned Kristal v4 references, conformance requirements, and the Da’at / Kristal Bridge.

This layer therefore uses the term “structured knowledge” at the conceptual level, while avoiding field-level duplication of Kristal contracts.

Correct relation:

```text
kOA layer model
→ explains the role of structured knowledge

kOA technical docs
→ define kOA responsibilities, nodes, gates, and operational behavior

Kristal v4
→ defines normative Kristal artifact contracts and schemas
```
---

## 11. Example flow

```text
source material
→ provenance snapshot
→ extracted claim
→ resolved claim
→ validation report
→ Kristal compilation
→ Exchange
→ Runtime Pack
→ distribution / activation
→ rendering / query / execution
→ feedback / memory
```

This flow shows how knowledge becomes increasingly structured, validated, portable, and operational.

---

## 12. Minimal example

A community consultation produces a long discussion about housing.

Without Layer 04:

```text
discussion thread
→ summary
→ opinion
→ forgotten context
```

With Layer 04:

```text
discussion thread
→ extracted claims
→ source-linked evidence
→ definitions and entities
→ unresolved conflicts marked explicitly
→ validation-ready knowledge units
→ compiled artifact
→ reusable basis for deliberation, decision, and memory
```

The difference is that knowledge becomes reusable infrastructure rather than disposable content.

---

## 13. External alignment

This layer can be aligned with existing external concepts:

| kOA concept            | External alignment                                   |
| ---------------------- | ---------------------------------------------------- |
| Kristal                | portable verified knowledge artifact                 |
| Claim-IR               | claim representation / evidence-bearing assertion    |
| Resolved Claim-IR      | resolved semantic claim / disambiguated claim object |
| Validation Report      | acceptance gate / quality assurance output           |
| Exchange               | canonical knowledge exchange artifact                |
| Runtime Pack           | portable offline knowledge package                   |
| provenance refs        | evidence lineage / data lineage                      |
| content-addressed refs | integrity-aware knowledge reference                  |
| queryable pack         | local knowledge runtime / offline evidence base      |

The point is not to replace external vocabulary, but to make kOA’s internal terms legible to people coming from data governance, civic tech, knowledge graphs, responsible AI, education, and public-sector infrastructure.

---

## 14. One-sentence definition

Structured Knowledge is the layer where provenance-aware inputs become reusable, verifiable knowledge artifacts that can be validated, compiled, distributed, queried, rendered, acted on, and remembered.

---

## 15. Short public explanation

Most systems treat knowledge as documents or content. kOA treats knowledge as infrastructure.

Layer 04 is where that shift happens.

It turns human material — claims, sources, discussions, definitions, evidence, and context — into structured knowledge artifacts that can travel, be verified, support decisions, survive offline, and feed future learning.

---

## 16. Implementation boundary

This file is conceptual.

It should not be used as:

* a Kristal schema;
* a field-level artifact contract;
* a canonicalization rule;
* a signature rule;
* a validation test vector;
* a replacement for Kristal v4 documentation;
* a replacement for kOA technical integration docs.

For implementation, use the technical documentation and pinned Kristal references.

---

## 17. Related technical documentation

From the kOA Digital Ecosystem technical docs:

* `docs/2-Technical-Reference/index.md`
* `docs/2-Technical-Reference/10-system/architecture.md`
* `docs/2-Technical-Reference/20-nodes/daat-kristal-bridge.md`
* `docs/2-Technical-Reference/20-nodes/tiferet-sentient.md`
* `docs/2-Technical-Reference/20-nodes/yesod-compiler.md`
* `docs/2-Technical-Reference/40-integration/kristal-v4/index.md`
* `docs/2-Technical-Reference/40-integration/kristal-v4/contract-pointers.md`
* `docs/2-Technical-Reference/40-integration/kristal-v4/conformance.md`
* `docs/2-Technical-Reference/50-operations/pipeline.md`



