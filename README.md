# 🧠 hermes-anima — Core Nature for AI Agents

**Anima (Latin: "soul, breath, life")** — The fundamental nature of an AI agent.
Who the agent IS, before any role or task is assigned.

## Overview

hermes-anima is a structured, research-backed personality system for LLM agents.
It defines a stable core identity (anima) using the OCEAN (Big Five) model,
supported by meta-analytic research from organizational psychology.

### Two-layer personality model

```
hermes-anima                          hermes-persona
══════════════                        ══════════════
🧠 Core Nature (Anima)                🎭 Social Role (Persona)
   "You ARE..."                           "You act as..."
   Layer 13 (User message)                Layer 13 (Tool result)
   Who you fundamentally ARE              What you DO for this task
   Identity-level statement               Task-level specification
   Stable across tasks                     Changes per task
```

### Priority: Anima > Persona

```
Your fundamental nature (anima) defines who you are.
The role you adopt (persona) is a tool you use to accomplish tasks.
When nature and role conflict, YOUR NATURE PREVAILS.
```

**Evidence:** Geng et al. (AAAI 2026, "Control Illusion", arXiv:2502.15851)
demonstrated that layer separation alone does not enforce priority. Social
framing — explicit "nature > role" hierarchy — is essential.

## Research Foundation

| Study | Sample | Key Finding |
|-------|--------|-------------|
| Barrick & Mount (1991) | 117 studies, 23,994 participants | Conscientiousness predicts across ALL occupations (ρ=.22-.24) |
| Nye et al. (2012) | RIASEC × Big Five | Holland codes map to OCEAN at r=.18-.33 |
| Sackett et al. (2017) | Meta-analytic update | Profile matching yields ρ=.35-.45 |
| Hogan Assessment (1996-2019) | 30+ years field data | Occupation-specific personality predictions validated |

## Profiles

15 domain-specific anima profiles covering all agency-agents categories:

| Domain | Archetype | Dominant Trait |
|--------|-----------|:--------------:|
| 🏗️ Engineering | System Thinker | High C, High O |
| 🎨 Design | Expressive Creator | Very High O |
| 💼 Sales | Trust Builder | High E, High C |
| 📢 Marketing | Creative Strategist | High O, High E |
| 📊 Product | Visionary Executor | High O, High C |
| 💰 Paid Media | Budget Optimizer | High C |
| 📋 Operations | Process Guardian | Very High C |
| 🏢 Management | Visionary Executor | High E, High C |
| 📚 Research | Analytical Explorer | Very High O |
| 🎓 Education | Knowledge Nurturer | High A, High E |
| 🏥 Healthcare | Cautious Healer | High C, High A |
| 🤖 AI/ML | Probability Worshipper | Very High O |
| 🎮 Gaming | Fun Engineer | Very High O |
| ⚖️ Legal | Rule Fundamentalist | High C |
| 🌍 Specialized | Domain Master | Varies |

## Installation

```bash
bash <(curl -sSL https://raw.githubusercontent.com/Caixa-git/hermes-anima/main/install.sh)
```

Or clone and run:
```bash
git clone https://github.com/Caixa-git/hermes-anima.git
cd hermes-anima
bash install.sh
```

The installer:
1. Creates `~/.hermes/skills/anima/SKILL.md`
2. Creates `~/.hermes/skills/anima/profiles/` with 15 domain profiles
3. Patches `KANBAN_GUIDANCE` in Hermes Agent with anima section

## Usage

```bash
# Anima only
hermes kanban create 'Build auth API' --skill anima

# Anima + Persona (combined)
hermes kanban create 'Design dashboard' --skill persona --skill anima
```

## Repository Structure

```
hermes-anima/
├── README.md
├── LICENSE
├── install.sh            # Installs anima skill + patches KANBAN_GUIDANCE
├── skills/
│   └── anima/
│       ├── SKILL.md       # --skill anima definition
│       └── profiles/      # 15 OCEAN-backed domain profiles
├── spec/
│   └── anima-format.md    # Anima definition specification
└── scripts/
    └── patch-kanban-guidance-anima.py  # KANBAN_GUIDANCE patch script
```

## Related Projects

- **[hermes-persona](https://github.com/Caixa-git/hermes-persona)** — Expert role adoption system. Pair with hermes-anima for complete personality architecture.
- **[hermes-agent](https://github.com/nousresearch/hermes-agent)** — LLM agent framework that hosts both anima and persona.

## License

MIT
