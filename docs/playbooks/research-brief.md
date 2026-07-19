<div class="playbook-hero" markdown>

<span class="kicker">Playbook · Research</span>

# Research a topic and get a useful brief

Use this when you need a source-backed answer about a company, tool, person, technology, market, or decision.

</div>

<div class="playbook-meta">
  <div><strong>Input</strong><span>One clear question</span></div>
  <div><strong>Output</strong><span>Brief + sources</span></div>
  <div><strong>Time</strong><span>15–30 minutes</span></div>
</div>

## 1. Fill this in

```text title="Fill in these details"
Topic: [what should be researched?]
Decision or goal: [what will this research help you decide or understand?]
Audience: [who will read the brief?]
Must cover: [3–5 questions]
Current through: [today or another date]
```

### Example

```text title="Example input"
Topic: Obsidian, Notion, and Google Docs
Decision or goal: Choose a knowledge-base tool for a two-person consulting business
Audience: The two owners
Must cover: setup effort, collaboration, AI-agent access, backups, and cost
Current through: July 2026
```

## 2. Copy this prompt

```text title="Copy this prompt"
Create a source-backed research brief using the details below.

Topic: [TOPIC]
Decision or goal: [DECISION OR GOAL]
Audience: [AUDIENCE]
Must cover: [QUESTIONS]
Current through: [DATE]

Rules:
- Start by showing a short research plan.
- Use reliable and current sources when browsing is available.
- Cite important factual claims with direct source links.
- Separate verified facts, source claims, your inferences, and unknowns.
- Do not invent missing facts or pretend a source was checked.
- Call out conflicting evidence and outdated information.

Output:
1. Executive summary
2. Key findings
3. Comparison table when useful
4. Risks, limitations, and unknowns
5. Implications or recommendation for the stated goal
6. Source list

Stop after the plan if you need me to approve sources or scope.
```

Paste it into your AI, replace the bracketed fields, and provide any sources the AI cannot access itself.

## 3. Check the result

Before using the brief, confirm:

- [ ] Important claims have working sources.
- [ ] Dates are visible where recency matters.
- [ ] Facts and recommendations are not mixed together.
- [ ] Uncertainty and missing information are stated.
- [ ] The conclusion answers your actual question.

!!! warning "Do not trust a polished answer by itself"
    Open the most important sources. Verify names, dates, prices, policies, quotations, and other decision-critical details.

## What the example should produce

For the Obsidian-versus-Notion-versus-Google-Docs example, the final brief should quickly show:

- which tool is easiest to start;
- which supports collaboration best;
- which works most naturally with file-based agents;
- important backup and privacy differences;
- the best low-risk pilot to run before committing.

It should **not** declare a universal winner without connecting the recommendation to the two-person business's needs.

??? info "Optional: run it with a folder-based agent"

    Create a small workspace and start your agent inside it:

    ```text
    research-project/
    ├── INPUT.md
    ├── sources/
    └── output/
    ```

    Then copy this:

    ```text title="Copy this agent prompt"
    Read INPUT.md and work only inside this project folder.
    First write a proposed research plan to output/PLAN.md and stop for approval.
    After approval, save source notes in sources/ and the final brief in output/BRIEF.md.
    Never claim a source was checked unless you actually opened it.
    ```

??? info "Optional: ask for subagents"

    ```text title="Copy this subagent request"
    Use a research subagent to gather evidence and a separate verifier subagent to check the most important claims. The main agent should write the final brief only after reviewing both reports. Do not let the researcher approve its own claims.
    ```

## You are done when

You have a brief that answers the question, exposes uncertainty, and lets another person open the sources behind the important claims.

[Download the short research starter](../downloads/research-brief-starter.zip){ .md-button .md-button--primary }
[Choose another playbook](index.md){ .md-button }
