---
description: >-
  How to give your AI long-term memory with a vault: a plain folder of notes (often in free Obsidian) that any AI can read — and you can always check.
---

<span class="kicker">How agents work · Vaults</span>

# A vault for your agent

A [**vault**](../resources/glossary.md#vault) is just a folder of plain-text notes — often managed with a free app called [Obsidian](https://obsidian.md). It becomes your AI's long-term memory: everything important lives in files you can open, read, and fix.

## Why files beat "AI memory" features

- **You can see them.** No mystery about what the AI "knows" about you.
- **You can fix them.** Wrong note? Edit it. Done.
- **They work everywhere.** Any AI that can read files can use your vault. You're not locked in.

## A starter vault (five minutes)

Create a folder like this — with Obsidian or just your file manager:

```text
MyVault/
├── About-Me.md      ← who you are, how you like things done
├── Projects/        ← one note per project
├── Skills/          ← installed playbooks live here
└── Output/          ← things your AI drafts for you
```

In `About-Me.md`, write a few honest lines: what you do, what you're working on, how you like answers (short? step-by-step?).

## Using it with an agent

Start your agent inside the vault folder and say:

```text title="Copy this"
Read About-Me.md and the relevant note in Projects/ before
helping me. Save anything worth keeping to the right note, and
show me before saving.
```

## Two rules for a healthy vault

1. **The AI proposes, you approve.** It shows the note before saving.
2. **Short notes beat long ones.** A note you'd actually reread wins.

This is also where [playbooks](../playbooks/index.md) install themselves — into `Skills/` — which is why your AI can run them in any future chat.

[Next: subagents](subagents.md){ .md-button .md-button--primary }

!!! tip "If this helped"
    If this helped you set up a vault, a small tip on Ko-fi keeps every guide here free.
    [Tip on Ko-fi](https://ko-fi.com/support_jordy)

[Next step: Subagents](subagents.md){ .md-button }
