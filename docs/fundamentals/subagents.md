<span class="kicker">How agents work · Subagents</span>

# Subagents

A **subagent** is a helper AI that your main AI hands a task to — like a lead contractor bringing in a specialist. Useful sometimes. Not needed nearly as often as the internet suggests.

## When they actually help

- **Big reading jobs.** "Have helpers each read one report; you combine the findings."
- **Checking work.** One helper writes, a separate one verifies. The writer never grades its own homework.
- **Different hats.** A "researcher" and a "skeptic" reviewing the same claim.

## When to skip them

If one AI can do the job in one pass — which covers most everyday work — subagents just add cost, time, and coordination confusion. **One agent doing one clear job beats three agents doing a vague one.**

## How to ask (no setup required)

In tools that support it (like Claude Code), you can simply say:

```text title="Copy this"
Use one subagent to gather the evidence and a separate subagent
to double-check the three most important claims. You write the
final answer only after reviewing both. The researcher may not
approve its own claims.
```

## The rule that keeps it sane

Subagents follow the same rules as the main agent: stay in the folder, plan first, you review the result. More agents never means less supervision.

[Next: tools & connections](tools-mcp.md){ .md-button .md-button--primary }
