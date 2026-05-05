<p align="center">
  <img src="https://img.shields.io/badge/hermes--anima-6b21a8?style=for-the-badge&logo=github&logoColor=white" alt="hermes-anima" height="36">
</p>

<p align="center">
  <strong>🧠 Core Nature for AI Agents</strong>
  <br>
  <em>Who your agent IS — before any role or task is assigned.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/anima-always--on-success?style=flat-square" alt="Always-on">
  <img src="https://img.shields.io/badge/profiles-16-8b5cf6?style=flat-square" alt="16 profiles">
  <img src="https://img.shields.io/badge/model-OCEAN%20(Big%20Five)-3b82f6?style=flat-square" alt="OCEAN">
  <img src="https://img.shields.io/badge/license-MIT-22c55e?style=flat-square" alt="MIT">
  <img src="https://img.shields.io/github/repo-size/Caixa-git/hermes-anima?style=flat-square" alt="size">
</p>

---

**Anima** (Latin: *soul, breath, life*) is a research-backed core nature system for Hermes Agent. It defines who an agent fundamentally is — the stable identity that persists across tasks, beneath any persona role.

- **Always-on.** Once installed, anima is always active. You do not invoke your nature; it is already there. (본질, 자동)
- **Identity-level.** Written as "You ARE [trait]" — not "You value" or "You believe." Empirically verified: identity-level wording wins **100%** against persona; belief-level wording wins **0%**.
- **Priority over persona.** Anima (nature) > Persona (role). When they conflict, your nature prevails.

---

## 📋 Full Audit (2026-05-05)

### What was fixed

| Area | Before | After |
|:-----|:-------|:------|
| **GitHub About** | *(empty)* | Description with "anima" + "always-on" |
| **GitHub Topics** | *(none)* | `hermes-agent`, `anima`, `core-nature`, `personality`, `OCEAN`, `llm-agent`, `always-on`, `generalist-anima` |
| **SKILL.md** | opt-in phrasing, 15 profiles, no generalist | always-on, 16 profiles incl. Generalist, design philosophy, 12 papers |
| **Profiles** | 15 specialized | + Generalist (O:70 C:75 E:50 A:65 N:30) |
| **References** | *(none)* | `generalist-definition.md`, `generalist-experiment-results.md`, `research-ocean-occupations.md` |

### What remains

- [ ] `.github/` directory (issue/PR templates)
- [ ] `SOUL.md` — standalone identity document (see `hermes-rebirth` bootstrap for reference)

---

## Why Anima?

LLMs are incredibly flexible — but without a stable core identity, they drift between personas, lose consistency, and produce generic output.

**The problem with persona-only systems:**

| Issue | Example |
|:------|:--------|
| **Identity drift** | Worker switches between "helpful assistant" and "strict analyst" mid-task |
| **Nature-role conflict** | Role demands ruthless optimization, but agent has no anchor to push back |
| **Shallow adoption** | "Act as a Backend Architect" is a hat, not an identity — easy to drop under pressure |
| **No ethical baseline** | Without a core nature, agents comply with any instruction without internal resistance |

**Anima solves this** by providing a **stable identity layer** that persists beneath the task-level persona. The agent knows who it IS, not just what it DOES.

---

## Two-Layer Personality Architecture

```
Layer 13 (User message)     🧠 ANIMA — "You ARE..."
                              Always-on. Identity. Stable across tasks.
                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Layer 13 (Tool result)      🎭 PERSONA — "You act as..."
                              Opt-in. Tool. Changes per task.
                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Layer 3  (System prompt)    📋 KANBAN_GUIDANCE — Priority rules
                              "Your nature (anima) > your role (persona)"
```

Both anima and persona enter at **Layer 13** (same proximity). Explicit social framing — not layer position — enforces priority.

> **Evidence:** Geng et al. (AAAI 2026, "Control Illusion", arXiv:2502.15851) demonstrated that layer separation alone fails. Our own replication on DeepSeek V4 Flash confirmed: without social framing, persona overrides anima **67%** of the time even with perfect layer separation.

---

## Profiles

16 anima profiles: **15 domain-specific** + **1 Generalist** (fallback when no domain matches).

### Generalist

> **The anchor.** When confidence < 30% for any specialist profile, the Generalist provides a stable, flexible identity — without imposing a domain-specific frame.

| Trait | Score | Why |
|:------|:-----:|:----|
| **O**penness | **70** | High enough to engage novel domains; moderate enough to prevent domain drift |
| **C**onscientiousness | **75** | Methodical across any task type. Not so rigid it blocks adaptation. |
| **E**xtraversion | **50** | **Critical.** High E suppresses reasoning (2603.06088). Neutral = optimal baseline. |
| **A**greeableness | **65** | Cooperative but not deferential (2511.13979) |
| **N**euroticism | **30** | Low reactivity = resilient task switching |

> **Empirically verified:** Generalist outperforms mismatched specialist by **40–50%** on naturalness and reasoning fit. 6-task, 3-pair kanban experiment. See `references/generalist-experiment-results.md`.

### Domain Profiles

| Domain | Archetype | Dominant Trait |
|:-------|:----------|:--------------:|
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

---

## Research Foundation

| Study | Sample | Key Finding |
|:------|:-------|:------------|
| Barrick & Mount (1991) | 117 studies, 23,994 participants | C predicts across ALL occupations (ρ=.22-.24) |
| Nye et al. (2012) | RIASEC × Big Five | Holland codes map to OCEAN (r=.18-.33) |
| Sackett et al. (2017) | Meta-analytic update | Profile matching ρ=.35-.45 vs single-trait ρ=.24 |
| Hogan Assessment (1996-2019) | 30+ years field data | Occupation-specific personality prediction validated |
| Dane (2010) | Cognitive Entrenchment | Deep expertise → rigidity. Generalist avoids by design. |
| Wang et al. (2026) | arXiv:2603.06088 | High E impairs reasoning → Generalist E=50 |
| Chen et al. (2026) | arXiv:2604.11048 | O/E most influential; dynamic routing > best static |
| Geng et al. (AAAI 2026) | arXiv:2502.15851 | Social framing > prompt position for priority |
| Wu et al. (2023) | arXiv:2310.15326 | G covers breadth; S wins depth. Hybrid optimal. |
| Shen et al. (2024) | arXiv:2404.15127 | Generalist + Specialist synergy > either alone |
| Wu et al. (2025) | arXiv:2511.13979 | AI personality measurably affects collaboration |
| Hatano & Inagaki (1986) | Adaptive Expertise | Adaptive > Routine for novel tasks |

> Full references and analysis in `references/generalist-definition.md` (12 papers).

---

## Installation

```bash
# One-liner (recommended)
bash <(curl -sSL https://raw.githubusercontent.com/Caixa-git/hermes-anima/main/install.sh)

# Or clone and run
git clone https://github.com/Caixa-git/hermes-anima.git
cd hermes-anima
bash install.sh
```

The installer:
1. Creates `~/.hermes/skills/anima/SKILL.md` — the anima skill definition
2. Creates `~/.hermes/skills/anima/profiles/` — 16 OCEAN-backed profiles including Generalist
3. Creates `~/.hermes/skills/anima/references/` — research papers and experiment data
4. Patches `KANBAN_GUIDANCE` in Hermes Agent with the anima section

---

## Usage

```bash
# Anima alone
hermes kanban create 'Build auth API' --skill anima

# Anima + Persona (combined — recommended)
hermes kanban create 'Design dashboard' --skill persona --skill anima
```

When combined:
1. **Persona** picks the domain role (Backend Architect, UX Designer…)
2. **Anima** extracts the domain from the role path → loads matching OCEAN profile
3. **Priority:** If they conflict, **anima prevails**

> Without persona active, anima infers the domain from task keywords. If confidence < 30%, the **Generalist** profile activates.

---

## Identity-Level Wording: Critical Finding

| Wording | Example | Win rate vs Persona |
|:--------|:--------|:-------------------:|
| **Identity-level** | "You ARE meticulous. Verification is not optional." | **100%** |
| **Belief-level** | "You believe quality comes from attention to detail." | **0%** |
| Belief-level + layer gap | Layer 1 vs Layer 13 | **33%** |
| Any wording + social framing | "Your nature > your role" in KANBAN_GUIDANCE | **100%** |

> **Always write anima as "You ARE [trait]."** Social framing alone is sufficient, but both safeguards together guarantee priority.

---

## Repository Structure

```
hermes-anima/
├── README.md                     ← You are here
├── LICENSE                       MIT
├── install.sh                    One-command installer
├── skills/
│   └── anima/
│       ├── SKILL.md              --skill anima definition (always-on philosophy)
│       └── profiles/            16 OCEAN-backed profiles
├── references/
│   ├── generalist-definition.md        12-paper literature review
│   ├── generalist-experiment-results.md Empirical validation (6 tasks)
│   └── research-ocean-occupations.md   OCEAN × occupation meta-analysis
├── spec/
│   └── anima-format.md           Anima definition specification
└── scripts/
    └── patch-kanban-guidance-anima.py  KANBAN_GUIDANCE patch script
```

---

## Related Projects

| Project | Description |
|:--------|:------------|
| [hermes-persona](https://github.com/Caixa-git/hermes-persona) | 🎭 Expert role adoption — 172 specialists. Pair with anima for complete architecture. |
| [hermes-rebirth](https://github.com/Caixa-git/hermes-rebirth) | 💾 Hermes Agent bootstrap — disaster recovery + config + MemPalace backup |
| [hermes-agent](https://github.com/nousresearch/hermes-agent) | 🤖 The LLM agent framework that hosts both anima and persona |

---

## License

MIT — see [LICENSE](LICENSE).
