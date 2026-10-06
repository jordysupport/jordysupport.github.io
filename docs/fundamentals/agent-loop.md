---
description: >-
  Follow an AI agent through a task: read the input, choose a step, use a tool, inspect the result, and decide whether to continue.
---

<span class="kicker">How agents work · The loop</span>

# The agent loop

An agent often works in a cycle: **look → plan → act → check**. The result of one step becomes part of the input for the next. It continues until it reaches the goal, hits a limit, or needs a decision from you.

## The loop in plain words

Suppose you ask for a task list from meeting notes:

1. **Look:** Read the request and find the notes.
2. **Plan:** Decide which files to read and how to organize the tasks.
3. **Act:** Read the files and create the draft.
4. **Check:** Compare the draft with the notes and confirm where it was saved.

The tool may combine steps or repeat them. If a file is missing, the next action might be a search or a question. If the draft has an unsupported deadline, the agent should remove it or flag it for you.

## Where loops go wrong

| What you see | What to change |
| --- | --- |
| It keeps searching without producing anything | Give a finish line, such as “use these three sources and return a one-page brief.” |
| It says a task is done when the output is missing | Ask it to open the saved file and report its location. Check it yourself. |
| It expands into unrelated work | Name the output and the work that needs a separate approval. |
| It repeats the same failed step | Set a retry limit and require it to report the error when the limit is reached. |

## Choose an approval point { #the-one-sentence-that-improves-any-agent }

For unfamiliar work, a short plan helps you catch misunderstandings before files change:

```text title="Review the plan"
Before making changes, list the files you expect to change and
the result you intend to produce. Wait for my approval.
```

For a task you have already tested, you can allow routine steps and keep approval for sending, publishing, spending, or deleting. State those boundaries clearly and use the tool's permission controls where available. A prompt is guidance; enforced permissions provide a separate limit on access.

Checking must have a reference. “Review your answer” is vague. “Compare every task owner and deadline with the meeting notes; mark anything absent as unknown” gives the agent a check you can inspect.

[Next: Context & memory](context-memory.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
