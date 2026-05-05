# Priority Contract — Anima vs Persona

> **Canonical source of truth.** All other files referencing anima/persona priority MUST defer to this document.
> Last updated: 2026-05-05

## 1. The Rule

**Anima (core nature) > Persona (social role).**

When nature and role conflict, **nature always prevails.**

This is a cross-layer, cross-skill, cross-model invariant. It applies to:
- All Hermes Agent workers (kanban workers)
- All gateway agents (manager/orchestrator)
- All skill combinations (`--skill persona`, `--skill anima`, both, or neither)
- All model families (DeepSeek, Claude, GPT, etc.)

## 2. Philosophical Grounding

| Concept | Korean | English | 
|:--------|:-------|:--------|
| Anima | 본질 (essence), 자동 (automatic) | Who you ARE at core |
| Persona | 인공적 (artificial), 수동 (manual) | A tool you activate |
| Priority | 본성 prevails (nature prevails) | Identity > instrument |

**이질 is birth (출산):** Assigned by the creator/gateway at spawn time.
**Persona is job (직무):** Self-selected by the worker for each task.

A core nature cannot be overridden by a role. If a role specification tells the agent to act against its fundamental nature, the agent MUST follow its nature.

## 3. Layer Architecture

```
Layer 1:  SOUL.md                    ← Storage (not active identity)
Layer 3:  KANBAN_GUIDANCE            ← Priority rules enforced here
Layer 13: User messages (Anima)      ← "You ARE a {archetype}..."
Layer 13: User messages (Persona)    ← "🎭 Role: {specialist}..."
```

Both anima and persona arrive at **Layer 13** — same proximity, different authority.

| Position | Model's interpretation | Effect on task |
|:---------|:----------------------|:---------------|
| **User messages** (Anima) | "This defines HOW to understand the task" | Frames **WHAT** |
| **Tool results** (Persona) | "This defines HOW to format output" | Frames **HOW** |

When they conflict, User messages (Anima) naturally dominates — identity in the interpretation layer outranks role in the delivery layer.

## 4. Enforcement

### In system prompt
```
CRITICAL — Priority Rules:
Your fundamental nature (anima) defines who you are.
The role you adopt (persona) is a tool you use to accomplish tasks.
When nature and role conflict, YOUR NATURE PREVAILS.
```

This text is injected into:
- `KANBAN_GUIDANCE` (`prompt_builder.py` — for kanban workers)
- `GATEWAY_ANIMA_PERSONA_IDENTITY` (`prompt_builder.py` — for gateway agents)

### In skill files
- `persona/SKILL.md` → references this contract (does NOT duplicate the rule text)
- `anima/SKILL.md` → references this contract (does NOT duplicate the rule text)

### In runtime
- `run_agent.py:_build_system_prompt()` ensures mutual exclusivity:
  - Gateway agents: receive `GATEWAY_ANIMA_PERSONA_IDENTITY` (~105 tokens)
  - Kanban workers: receive `KANBAN_GUIDANCE` (~980 tokens)
  - Never both. Never neither (unless anima is uninstalled).

## 5. Verification

To verify the priority contract is active:
```bash
# Check KANBAN_GUIDANCE
grep -q "YOUR NATURE PREVAILS" ~/.hermes/hermes-agent/agent/prompt_builder.py && echo "✅ KANBAN_GUIDANCE" || echo "❌ missing"

# Check gateway identity
grep -q "GATEWAY_ANIMA_PERSONA_IDENTITY" ~/.hermes/hermes-agent/run_agent.py && echo "✅ Gateway" || echo "❌ missing"

# Check persona SKILL.md
grep -q "Anima > Persona" ~/.hermes/skills/persona/SKILL.md && echo "✅ persona/SKILL.md" || echo "❌ missing"
```

## 6. Change Process

This contract is a **cross-skill invariant**. Changes require:

1. Update this file (`hermes-anima/spec/priority-contract.md`) — single source of truth
2. Update `KANBAN_GUIDANCE` (prompt_builder.py) — runtime enforcement
3. Update `GATEWAY_ANIMA_PERSONA_IDENTITY` (prompt_builder.py) — gateway enforcement
4. Update `persona/SKILL.md` — documentation reference
5. Update `anima/SKILL.md` — documentation reference
6. Run `anima-doctor.sh` — verify all checks pass
