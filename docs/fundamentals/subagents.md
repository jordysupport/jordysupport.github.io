---
description: >-
  Learn when helper agents are useful, what to give each one, and how to check their work before combining the results.
---

<span class="kicker">How agents work · Subagents</span>

# Subagents

A **subagent** handles a task delegated by another agent. The main agent assigns work, receives the result, and decides how to use it. In a tool such as [Claude Code](https://code.claude.com/docs/en/sub-agents), a helper can work in its own context and return a summary.

That separation helps with large reading or research jobs. It also creates a handoff: each helper needs the task, the relevant source material, and the rules it must follow.

## When they actually help

- **Separate inputs:** Three helpers can each read a different report and return findings with page references.
- **A focused review:** A helper can check a draft against its sources while the main agent continues organizing the material.
- **A large side task:** A helper can inspect logs or search files and return the relevant findings without filling the main conversation with everything it read.

A useful division has outputs the main agent can combine or inspect. “Be a researcher” is less clear than “find the official setup requirements and return the source for each one.”

## When to skip them

Use one agent when the task is short or each step depends on the previous one. Helpers add their own model requests, handoffs, and opportunities for misunderstanding. Parallel work helps only when the tasks can actually proceed separately.

Two agents agreeing does not establish that an answer is correct. They may share a model, a source, or the same mistaken assumption. Review needs independent evidence.

## How to ask { #how-to-ask-no-setup-required }

If your tool supports subagents, describe the division explicitly:

```text title="Research and review"
Use one helper to gather official sources for this question and
return findings with links and the passage supporting each claim.

Use a separate helper to check the three most important claims
against those sources. Have it report unsupported claims,
contradictions, and missing information. Agreement alone does
not count as verification.

Both helpers must use only the tools and data allowed for this
task. They must not edit files or contact anyone. Review both
reports before writing the final answer, and preserve any
unresolved uncertainty.
```

The exact controls depend on the tool. Check whether helpers inherit access and instructions; do not assume they saw the main conversation.

## Keep ownership clear { #the-rule-that-keeps-it-sane }

For editing work, assign each helper different files or use isolated copies. Two helpers changing the same file can overwrite each other's work. Have the main agent review the combined changes and report what remains incomplete.

[Next: Tools & connections](tools-mcp.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
