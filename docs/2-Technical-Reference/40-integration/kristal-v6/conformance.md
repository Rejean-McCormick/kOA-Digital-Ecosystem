# Kristal v6 conformance for kOA

A kOA integration claiming Kristal v6 alignment must demonstrate at least:

1. exact Standard 6.0.0 manifest/core-schema digest verification;
2. `kristal_state` support at the Kristal boundary;
3. typed `valuations[]` without coercing unknown/NA into numeric values;
4. `coordinates` and `applicability` preserved distinctly;
5. provenance/evidence, validation and recognition kept separate;
6. `record_role` preserved where supplied;
7. `actionability` preserved independently of valuation magnitude;
8. no assumption that `automatic` transfers execution authority;
9. owner mutation still gated by the target system's explicit contract/admission policy;
10. derived projections remain rebuildable and non-authoritative;
11. content-addressed identities are recomputed after canonical mutation;
12. Reader Policy filters are coherent with the valuation dimensions they consume.
