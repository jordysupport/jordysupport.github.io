---
description: >-
  Decide which files to share with an AI by checking their contents, the tool's data handling, and the access it has to your computer or accounts.
---

<span class="kicker">How agents work · File safety</span>

# Is it safe to let an AI read my files?

It depends on the files, the tool, and the access you grant. A public article and a customer export need different treatment. Before sharing either, know what is in it and where the tool sends it.

## Start with a small set of files { #the-one-habit-that-does-most-of-the-work }

Create a task folder containing copies of only the material you need. Check the tool's settings for what it can read, edit, and send over the network. Opening that folder does not, by itself, block access to the rest of your computer.

This follows the [limited-access approach](safety-permissions.md) used throughout these guides. Copies protect your originals from accidental edits. They do not remove private information from the copy.

## What "reading a file" actually means

The tool extracts some or all of a file's contents and supplies them to the AI as [context](context-memory.md). A cloud-backed tool may send that content to its provider even when the file stays on your computer. A fully local setup may process it locally; check the actual configuration.

Review the provider's data controls and retention terms for the account you use. Personal accounts, business accounts, and API tools can have different rules. Storage location, processing location, and permission to use the data are separate questions.

## Before you share a file, check it

- [ ] Read the full file, including attachments, comments, and extra sheets that may be included.
- [ ] Remove passwords, API keys, card details, and unnecessary personal information. See [Keeping it safe](safety-permissions.md).
- [ ] Confirm you are allowed to share work or customer material with this service.
- [ ] Use a copy and keep the original somewhere the agent cannot edit.
- [ ] Confirm which other files and accounts the tool can access.
- [ ] Decide whether the task really needs the sensitive parts. A redacted example may be enough.

## Files that need extra care

**Spreadsheets:** Check hidden sheets, columns, comments, and linked data. Remove what the task does not need rather than relying on what is visible when the file opens.

**Email and chat exports:** Read the export before sharing it. It may contain older messages, contact details, and attachments beyond the exchange you meant to use.

**Unfamiliar downloads:** Read task instructions before letting an agent follow them. A document can contain instructions aimed at the AI. The [playbook pages](../playbooks/index.md) show their installation text so you can review it before use.

## What about agents, not just chat?

An agent may be able to edit or send the material it reads. Inspect both file access and connected tools. Require approval for actions involving other people, live systems, or information leaving the workspace.

The [first agent walkthrough](../getting-started/first-agent.md) starts with non-sensitive copies and a saved draft, so you can inspect the work before expanding access.

## A check before you begin { #youre-done-when }

You should be able to name the files the task needs, explain who can receive their contents, and identify which actions the tool can take. If a setting is unclear, use sample material until you resolve it.

[Next: Keeping it safe](safety-permissions.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
