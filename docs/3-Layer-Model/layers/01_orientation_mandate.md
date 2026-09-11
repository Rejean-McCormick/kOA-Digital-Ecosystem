# Layer 01 — Orientation / Mandate

**Layer status:** Conceptual layer  
**Normative for kOA:** NO  
**Primary technical anchor:** `docs/2-Technical-Reference/20-nodes/keter-mandate.md`

---

## 1. Function

The Orientation / Mandate layer defines the purpose, direction, constraints, and governing intent of the system.

It answers the question:

> What is this system allowed, required, and forbidden to do?

This layer does not produce canonical truth. It does not execute work. It does not deliberate or decide specific cases. It defines the mandate under which all downstream layers operate.

In the kOA Digital Ecosystem, this layer is technically anchored by **Keter: Mandate**, which publishes versioned governance artifacts used by Orgo, Kristal gates, Konnaxion distribution policy, and Architect behavior policies.

---

## 2. Core question

What is the governing purpose of the system, and under which constraints must all downstream activity occur?

Sub-questions:

- What mission is being served?
- What scope is included or excluded?
- What ethical, legal, operational, or institutional constraints apply?
- What risks are acceptable or unacceptable?
- Which policies are active?
- What must fail closed?
- What requires review or approval?
- What is explicitly forbidden?

---

## 3. Internal kOA components

Relevant internal components:

- **Keter**
- **Mandate Bundle**
- policy selections
- enforcement levels
- operating principles
- governance constraints
- risk thresholds
- prohibited actions
- review requirements
- mission / scope statements

Related downstream components:

- **Orgo** — consumes mandate constraints for pipeline governance
- **Kristal gates** — apply mandate-bound validation constraints
- **Konnaxion** — applies distribution and activation policies
- **Architect** — respects behavior policies and planning constraints

---

## 4. Inputs

The Orientation / Mandate layer receives:

- organizational objectives;
- community purpose;
- mission statements;
- ethical requirements;
- legal or regulatory constraints;
- risk appetite;
- operational service-level expectations;
- approved policy templates;
- governance decisions;
- institutional boundaries;
- non-goals and exclusions.

These inputs must be made explicit enough to guide deterministic downstream interpretation.

---

## 5. Outputs

The primary output is a **governance mandate**.

In the technical ecosystem, this becomes a **Mandate Bundle**: a versioned, auditable container that can include mandate identity, descriptive fields, constraints, objectives, policy documents, rule sets, and optional signatures.

Conceptually, this layer outputs:

- a mission definition;
- a scope definition;
- explicit constraints;
- active policy selections;
- enforcement levels;
- forbidden actions;
- review requirements;
- decision principles;
- non-goals;
- success criteria;
- reproducibility-relevant policy context.

These outputs constrain later layers. They do not replace them.

---

## 6. External vocabulary

Comparable external terms:

- mandate;
- mission;
- charter;
- governance source;
- policy bundle;
- operating principles;
- intended impact;
- theory of change;
- institutional mandate;
- governance framework;
- constitutional layer;
- policy-as-code;
- organizational constraints;
- decision rights;
- authority boundary.

Useful public-facing translation:

> This is the layer where the system defines its purpose, limits, and rules before knowledge, decisions, or actions are produced.

---

## 7. Failure mode if absent

If this layer is absent, the system can still process inputs, generate outputs, or execute tasks, but it lacks governed direction.

Common failure modes:

- unclear purpose;
- mission drift;
- hidden policy assumptions;
- ad-hoc overrides;
- conflicting downstream behavior;
- ambiguous authority;
- unbounded execution;
- unverifiable policy changes;
- runtime exceptions replacing governance;
- downstream components making implicit decisions they should not own.

In the technical ecosystem, a missing or ambiguous mandate means the governed pipeline cannot start safely. Downstream components cannot know which policies apply, what constraints bind them, or when to fail closed.

---

## 8. Relation to other layers

### Previous layer

**Layer 00 — Separation of Functions**

Layer 00 separates the major institutional and functional roles: movement, school, infrastructure, narrative, safeguards, legitimacy, and memory.

Layer 01 then gives the active mandate under which those functions operate.

### Next layer

**Layer 02 — Semantics / Meaning**

Once the mandate is defined, the system must clarify the meanings, terms, categories, and concepts used under that mandate.

Without semantic clarity, the mandate cannot be interpreted reliably.

### Downstream dependency

All later layers depend on this one:

```text
Orientation / Mandate
→ Semantics
→ Provenance
→ Structured Knowledge
→ Validation
→ Deliberation
→ Decision
→ Execution
→ Memory
```
The mandate constrains the whole chain.

---

## 9. Layer boundary

This layer defines governing intent and constraints.

It does not:

* validate factual truth;
* produce Kristals;
* resolve claims;
* run deliberations;
* count votes;
* execute tasks;
* mutate canon;
* override downstream gates at runtime.

Its role is to define the policy surface that downstream layers must respect.

---

## 10. One-sentence definition

**Orientation / Mandate is the layer where kOA defines the mission, scope, constraints, policies, and governing intent that bind all downstream knowledge, decision, execution, and memory processes.**

