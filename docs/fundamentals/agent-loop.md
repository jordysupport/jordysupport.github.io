---
description: >-
  How AI agents actually work: the look, plan, act, check loop explained in plain words, so agent behavior stops looking like magic and gets predictable.
---

<span class="kicker">How agents work · The loop</span>

# The agent loop

Every agent runs the same cycle: **look → plan → act → check → repeat or stop.** Once you see the loop, agent behavior stops being magic.

## The loop in plain words

1. **Look** — it reads what it can see: your request, the files, earlier steps.
2. **Plan** — it decides the next small step.
3. **Act** — it does one thing: reads a file, writes a draft, runs a step.
4. **Check** — it looks at what happened and decides: keep going, or done?

A good agent goes around this loop in small hops, and pauses to ask you at the important moments.

## Where loops go wrong

- **It never stops.** No clear finish line in the instructions. Fix: say exactly what "done" looks like.
- **It's confidently wrong.** It acted without checking. Fix: ask it to state its plan first and verify results against the source.
- **It wanders.** The job was vague, so it invented one. Fix: one job per request.

## The one sentence that improves any agent

> "Tell me your plan first and wait for my OK."

That single line turns the loop from *act → oops* into *plan → approve → act*. It's on almost every prompt on this site for a reason.

[Next: context & memory](context-memory.md){ .md-button .md-button--primary }

!!! tip "If this helped"
    If the loop finally clicked, a small tip on Ko-fi keeps every guide here free.
    [Tip on Ko-fi](https://ko-fi.com/support_jordy)

[Next step: Context & memory](context-memory.md){ .md-button }
