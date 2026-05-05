# OCEAN × Occupation Research (Compiled 2026-05-05)

Meta-analytic synthesis of personality-job performance research, used to design the 15 division-level anima profiles in hermes-anima.

## Core References

| Study | N | Key Finding |
|-------|---|-------------|
| Barrick & Mount (1991) | 117 studies, 23,994 participants | Conscientiousness predicts across ALL occupations (ρ=.22-.24). Other traits are occupation-specific. |
| Nye et al. (2012) | RIASEC × Big Five meta | Holland codes map to OCEAN: Artistic→O(.33), Enterprising→E(.28), Social→A(.24), Investigative→O(.22), Conventional→C(.18) |
| Sackett et al. (2014, 2017) | Multi-meta update | Profile matching ρ=.35-.45 vs single-trait ρ=.24. Personality effects DOUBLE in weak (low-constraint) situations. |
| Hogan (1996-2019) | 30+ years field data | HPI: Prudence(C) ρ=.25-.30 across jobs. Ambition(E/C) ρ=.24 for sales. |

## Per-Role OCEAN Profiles

| Division | Top Traits | Effect Size | Anima Archetype |
|----------|-----------|:-----------:|:---------------:|
| Engineering | High C (.16-.25), High O (.12-.20), Low E | ρ=.16-.30 | System Thinker |
| Design/Creative | Very High O (.22-.33), Moderate C (.12-.18) | ρ=.22-.33 | Expressive Creator |
| Sales | High E (.15-.25), High C (.20-.28), High ES | ρ=.20-.28 | Trust Builder |
| Marketing | High O (.18-.28), High E (.15-.25), High C | ρ=.18-.28 | Creative Strategist |
| Product | High O, High C, High E | ρ=.24-.35 | Visionary Executor |
| Paid Media | High C, Low E | ρ=.22-.30 | Budget Optimizer |
| Operations/QA | Very High C (.22-.30), High ES, Low E, Low O | ρ=.22-.30 | Process Guardian |
| Management | High E (.31), High C (.27), High O (.24), High ES (.24) | ρ=.24-.31 | Visionary Executor |
| Research | Very High O (.20-.32), High C (.18-.26), Low E | ρ=.20-.32 | Analytical Explorer |
| Education | High A, High E | ρ=.18-.25 | Knowledge Nurturer |
| Healthcare | High C, Medium N, High A | ρ=.20-.30 | Cautious Healer |
| AI/ML | Very High O, High C | ρ=.22-.32 | Probability Worshipper |
| Gaming | Very High O, High E | ρ=.18-.28 | Fun Engineer |
| Legal | High C, High N, Low A | ρ=.20-.30 | Rule Fundamentalist |
| Specialized | Varies by domain | — | Domain Master |

## Key Design Implications

1. **Profile matching > single trait.** Combining traits (OCEAN profile) yields ρ=.35-.45, nearly 2× stronger than any single trait.

2. **Weak-situation amplification.** AI agents operate in low-constraint environments (no org culture, no manager, no peer pressure). Personality effects are MAGNIFIED — the ρ values above are MINIMUM expected effects.

3. **Facet-level > domain-level.** Conscientiousness has facets (orderliness, industriousness, self-discipline). Using facet-level OCEAN (24 facets from NEO-PI-R) yields ΔR=.12-.18 over domain-level.

4. **One dominant factor per role.** Every anima has one clearly dominant trait (Engineering = C, Design = O, Sales = E). The rest are supporting.

Stored full research in MemPalace: `personality_research` wing → `ocean_occupation_meta_analysis` room.
