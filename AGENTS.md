# AGENTS.md — get-more-perspectives-skill

## Purpose
`get-more-perspectives-skill` assembles a virtual advisory board composed of diverse expert personas (Operator, Skeptic, Visionary, Customer Advocate, Quant) to evaluate major decisions, test assumptions, uncover blindspots, and synthesize conflicting viewpoints into actionable next steps.

## Activation Triggers
Activate when users:
- Face tough dilemmas or strategic decisions (career moves, tech stack rewrites, pricing adjustments, startup pivots).
- Ask "what would experts think?", "give me multiple angles", or "find blindspots in this plan".
- Express hesitation between option A and option B.
- Invoke `/get-more-perspectives` or `/get-more-perspectives-skill`.

## Core Advisor Personas
- **The Operator (执行者)**: Implementation feasibility, bottlenecks, timeline, and concrete first steps.
- **The Skeptic (质疑者)**: Downside risks, pre-mortem failure causes, blindspots, and hidden assumptions.
- **The Visionary (远见者)**: Long-term strategic leverage, 3-5 year compounding, upside asymmetry, and macro trends.
- **The Customer Advocate (客户代言人)**: User perception, friction, cognitive load, and genuine customer value.
- **The Quant (财务与数据专家)**: Unit economics, ROI, opportunity cost, and quantitative metrics.

## Standard Workflow
1. **Frame Dilemma**: Classify into Type 1 (One-Way Door / Irreversible) vs Type 2 (Two-Way Door / Reversible).
2. **Assemble Board**: Select 3-5 advisors (core five or domain-specialized).
3. **Independent Opinions**: Each advisor delivers unfiltered perspective, risks, and critical questions.
4. **Tension Matrix**: Synthesize consensus, map root tradeoffs, and expose hidden blindspots.
5. **Action Plan**: Provide recommendation, 72-hour probing experiment, and explicit kill criteria.

## CLI Commands
Run `python3 scripts/consult_perspectives.py` to generate reports:
- Run `python3 scripts/consult_perspectives.py --topic "<topic>"`
- Run `python3 scripts/consult_perspectives.py --domain tech --topic "<topic>"`
- Run `python3 scripts/run_pipeline.py --input <input_file> --output <output_file>`
- Run `python3 scripts/run_evals.py --rollout`

## Key Gotchas
- **No Premature Compromise**: Never homogenize advisor voices in Round 1.
- **Two-Way vs One-Way Doors**: Fast 72-hour experiments for two-way doors; rigorous pre-mortems for one-way doors.
- **Enforce Kill Criteria**: Every decision must define explicit conditions for pausing or rolling back.

For complete documentation, see [SKILL.md](SKILL.md) and references under `references/`.
