---
description: >-
  Create a small folder of project notes and reusable instructions that you and your AI agent can read, update, and carry between tools.
---

<span class="kicker">How agents work · Vaults</span>

# A vault for your agent

A [**vault**](../resources/glossary.md#vault) is a folder of notes. [Obsidian](https://obsidian.md) is one way to manage them; a text editor works too. For an agent, the useful part is a set of readable files containing the project facts and instructions it needs.

## Why keep notes in files? { #why-files-beat-ai-memory-features }

You can read and correct a note, keep a backup, and give it to another tool. You can also see what has become outdated. Built-in AI memory may help with preferences, while files give you a more explicit project record.

Keep the notes selective. An agent does not need your entire personal history to summarize a meeting or draft a page.

## A starter vault { #a-starter-vault-five-minutes }

Create a folder with a few places for the work:

```text
MyVault/
├── About-Me.md      ← preferences relevant to the work
├── Projects/        ← one note per active project
├── Skills/          ← reusable task instructions
└── Output/          ← drafts for you to review
```

In `About-Me.md`, write a few practical preferences: the language you use, the kind of work you do, and how you want drafts presented. Leave out sensitive details.

A project note can begin with four headings: **Goal**, **Decisions**, **Current state**, and **Next action**. Date information such as account status or software versions. Add the source or location for facts the next session needs to check.

## Using it with an agent

Give the agent access to the notes it needs, then point to them explicitly:

```text title="Load the relevant notes"
Read About-Me.md and Projects/[project-name].md before working
on this task. Use those notes as background. Verify any current
status needed for today's work. Do not load unrelated notes.

Afterward, propose an update to the project note with confirmed
decisions, changes, unresolved questions, and the next action.
Show me the update before saving it. Keep secrets out of notes.
```

Check the access settings before opening a vault in an agent. Notes stored on your computer may still be sent to a cloud model when the tool reads them. Local storage alone does not determine how the AI processes them.

## Two rules for a healthy vault

1. **Update the existing note.** Replace outdated status instead of leaving several conflicting versions. Keep a backup before large changes.
2. **Save evidence and decisions.** A concise handoff is easier to use than a copy of the whole conversation. Label an untested suggestion as a suggestion.

The site's [playbooks](../playbooks/index.md) can live in `Skills/`. Read each playbook's installation instructions and tell your agent which file to load. Saving a file does not automatically make every AI app discover it.

[Next: Subagents](subagents.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
