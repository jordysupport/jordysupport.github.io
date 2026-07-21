---
description: >-
  Why AI forgets what you told it: context windows and memory explained in plain English, plus simple habits that make an AI remember what matters.
---

<span class="kicker">How agents work · Memory</span>

# Context & memory

The AI doesn't remember your life. It sees a **window**: your current conversation plus whatever files it just read. When the window's gone, the memory is gone — unless it's written down somewhere.

## Context, in plain words

**Context** = everything the AI can see *right now*. Your message, the chat so far, attached files, open project files. That's it. If it's not in the window, the AI doesn't know it — no matter how many times you've said it in other chats.

## Why the AI "forgot"

- New chat = empty window. Yesterday's conversation isn't in it.
- Long chat = the oldest parts fall out of the window.
- "I told the other AI" = different tool, different window.

None of this is the AI being dumb. It's just what a window is.

## Real memory is a file

The fix is simple: **anything worth remembering goes in a file the AI can read next time.** Your preferences, your project facts, your good prompts. That's the whole trick behind [vaults](obsidian-vaults.md) — and it's why the [playbooks](../playbooks/index.md) install themselves as files instead of asking you to re-explain the job every time.

## The habit

End sessions worth keeping with:

```text title="Copy this"
Save what we decided and anything worth remembering to a notes
file in this folder, so a future session can pick up where we
left off.
```

[Next: a vault for your agent](obsidian-vaults.md){ .md-button .md-button--primary }

!!! tip "If this helped"
    If this explained why your AI "forgot," a small tip on Ko-fi keeps every guide here free.
    [Tip on Ko-fi](https://ko-fi.com/support_jordy)

[Next step: A vault for your agent](obsidian-vaults.md){ .md-button }
