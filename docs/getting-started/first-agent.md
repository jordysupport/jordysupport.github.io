---
description: >-
  Set up your first AI agent step by step: give it one folder, one small job, and clear rules — a safe walkthrough with nothing important at risk.
---

<span class="kicker">Start here · First agent</span>

# Your first agent

This walkthrough gives an AI a folder of its own, one small job, and clear rules — the whole loop, start to finish, with nothing at risk.

## 1. Make the folder

Create a new folder anywhere easy to find. Inside it, make two more:

```text
ai-practice/
├── input/     ← copies of a few non-private files
└── output/    ← where the AI puts its drafts
```

Put 2–3 **copies** of harmless files in `input/` — some notes, an article you saved, anything you'd like summarized or reorganized.

## 2. Open your agent in that folder

In a folder agent (like Claude Code), open or start it *inside* `ai-practice/`. If it asks for permissions, that's normal — but it should only need this folder.

## 3. Give it the job

```text title="Copy this — your first agent job"
Work only inside this folder. Read the files in input/ and write
a clear one-page summary of them to output/summary.md. Before
writing anything, tell me your plan in two sentences and wait
for my OK. Don't change anything in input/.
```

## 4. Watch and approve

It should tell you its plan, wait, then write one file. If it tries to do more, say stop. You're the supervisor.

## 5. Check the work

Open `output/summary.md` and ask yourself:

- [ ] Did it only use what's in `input/`?
- [ ] Did it invent anything?
- [ ] Did it touch anything it shouldn't have?
- [ ] Is the summary actually useful?

## That's it — you supervised an agent

Everything bigger on this site is this same loop with more steps: clear job, limited access, plan first, human check.

**Next:** install a [playbook](../playbooks/index.md) — a job your agent saves and remembers, so you never have to explain it twice.

[How playbooks work](../playbooks/index.md){ .md-button .md-button--primary }

[Next step: How agents work](../fundamentals/index.md){ .md-button }
