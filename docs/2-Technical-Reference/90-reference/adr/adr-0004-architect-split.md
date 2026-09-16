# ADR-0004: Architect Strategy / Render split

- **Status:** Accepted, amended for Kristal v5 by ADR-0008

## Decision

Keep planning/strategy and rendering as separable responsibilities. Both consume material according to an explicit Reader Policy/Profile and preserve epistemic labels.

Neither role may assign Kristal validation or authority recognition, mutate a Reference Exchange by side effect, or manufacture factual claims through presentation.

## v5 amendment

The earlier assumption that Architect consumes only “canonical truth after validation + compilation” is superseded. Kristal v5 permits Reader Policies that expose Working, disputed or lower-certainty material with labels. Strict production surfaces can still choose reference-only policies.
