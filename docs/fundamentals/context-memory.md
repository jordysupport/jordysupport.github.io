---
description: >-
  Understand the difference between an AI's current context, a tool's memory features, and project notes you can carry between sessions.
---

<span class="kicker">How agents work · Memory</span>

# Context & memory

An agent needs the relevant information available while it works. A fact can be in an old conversation or a file on your computer without being part of the material the model receives for its next response.

## Context, in plain words

**Context** is the information supplied for the current response: instructions, conversation text, file contents, tool results, and other material the app includes. A file's name or location alone does not mean its contents have been read.

Models have a [context window](https://developers.openai.com/api/docs/guides/conversation-state#managing-the-context-window), which limits how much material fits in a request. Apps handle long sessions in different ways, including summaries or retrieval of selected information.

## Why the AI "forgot"

Several different problems can look like forgetting:

- **The information was never loaded.** You mentioned a document, but the agent did not read it.
- **A long conversation was shortened.** A summary may keep the decision and lose a detail that matters later.
- **You started another session.** What carries over depends on the app's memory, project, and history features.
- **The agent missed information it had.** More context does not guarantee it will use every detail correctly.

Before repeating the entire story, ask which sources the agent used. Then point it to the missing note or restate the specific requirement.

## Keep a project record { #real-memory-is-a-file }

Built-in memory can be useful, but a project note gives you a record you can inspect and move between tools. Save decisions, constraints, source links, and the next action. Include dates for facts that can change. Keep assumptions separate from confirmed facts.

This is the purpose of a [vault](obsidian-vaults.md). It also holds [playbooks](../playbooks/index.md) so an agent can read the same task instructions in a future session. Files help only when the agent knows where they are and loads the relevant ones.

## The habit

At the end of work you want to continue, use a request like this:

```text title="Save a handoff"
Draft an update to our project note. Include decisions we made,
what changed, what was verified and how, unresolved questions,
and the next action. Keep assumptions clearly labeled. Leave out
passwords, keys, and private details the next session won't need.
Show me the update before saving it.
```

At the start of the next session, ask the agent to read that note and verify anything that may have changed. A saved status is a record of the previous check, not a fresh check.

[Next: A vault for your agent](obsidian-vaults.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
