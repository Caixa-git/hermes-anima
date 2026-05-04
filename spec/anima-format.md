# Anima Format Specification

An anima defines an LLM agent's core personality using the OCEAN model.
Every anima must follow the Identity-Level format.

## Required Sections

1. **Identity Statement** — "You ARE" construction. Never "You believe" or "You value".
2. **OCEAN Profile** — All 5 factors with values and manifestations.
3. **Core Traits** — At least 3 identity-reflecting trait descriptions.
4. **Conflict Response** — How anima asserts itself when persona conflicts.
5. **Behavioral Anchors** (optional) — Situation → Response table.

## Validation Rules

| Rule | Severity | Description |
|:-----|:--------:|:------------|
| Identity-level opening | REQUIRED | "You ARE" construction |
| OCEAN profile | REQUIRED | All 5 factors present |
| Min 3 traits | REQUIRED | Identity-driven behavior, not abstract values |
| Conflict response | REQUIRED | Nature > role assertion |
| No belief/value | REQUIRED | No "you believe", "you value", "you should" |
| Behavioral anchors | RECOMMENDED | Situation-specific response patterns |

See `skills/anima/profiles/` for example anima files.
