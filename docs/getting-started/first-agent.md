---
description: >-
  Give a folder agent a small summary task, review its plan, and check the saved draft against the source files.
---

<span class="kicker">Start here · First agent</span>

# Your first agent

This exercise uses a few notes and produces one summary file. You will see the agent read the input, save a draft, and report what it did. No app connections are needed.

## 1. Make the folder

Create this folder structure somewhere easy to find:

```text
ai-practice/
├── input/     ← copies of a few non-sensitive notes
└── output/    ← the agent's draft goes here
```

Put two or three short text or Markdown files in `input/`. Use notes you wrote or sample material you are comfortable sharing with the AI provider. Keep your originals elsewhere.

## 2. Open your agent in that folder

Open `ai-practice/` in a folder agent such as Codex or Claude Code. Follow the product's setup instructions and inspect its permission settings. Choose restricted access and human approvals where available. Leave unrelated apps disconnected.

A folder choice and a written instruction help define the job. The tool's permissions determine what access is actually enforced. See [Keeping it safe](../fundamentals/safety-permissions.md) if the settings are unfamiliar.

## 3. Give it the job

```text title="First agent task"
Read the files in input/ and prepare a summary for someone who
has not read them. Use only those files. Include the main points,
any decisions, and any unanswered questions. Name the source file
for each decision. If the notes conflict, say so.

Save no more than one page to output/summary.md. Do not edit,
move, or delete the input files. Do not use the web or other apps.
If summary.md already exists, ask before replacing it.

First list the input files and describe your plan in two sentences.
Wait for my approval before writing. Afterward, report the file
you created and anything you could not read or verify.
```

## 4. Watch and approve

Check that the plan names the right files and the right destination. Then approve the draft. If the tool asks to run a command, read the request before allowing it. A simple summary should not need new software or access to another account.

The agent may finish in several tool calls or combine steps. Watch the files and actions rather than expecting a particular sequence of chat messages.

## 5. Check the work

Open `output/summary.md` and compare it with the inputs:

- [ ] The main points are present.
- [ ] Names, dates, and decisions match the notes.
- [ ] Missing or conflicting details are identified.
- [ ] The input files remain unchanged.
- [ ] The agent reports any skipped or unreadable material.

If it invented a detail, point to the exact sentence and ask for a correction using the source file. If it worked outside the task, stop and review the permissions before another run.

## Reuse the task { #thats-it-you-supervised-an-agent }

Save the request with any corrections that helped. Next time, change the input and destination while keeping the checks. A [playbook](../playbooks/index.md) packages instructions like these for a recurring task. Your agent still needs to load those instructions and have the right tools.

[How playbooks work](../playbooks/index.md){ .md-button }
[Next: How agents work](../fundamentals/index.md){ .md-button .md-button--primary }
