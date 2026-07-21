---
description: >-
  Fix computer and AI problems in the right order: read the error, retry once, ask what changed, shrink the problem, search the message, then reinstall.
---

<span class="kicker">Troubleshooting</span>

# Fix it in order

When something breaks, people reinstall everything, try random fixes, and make it worse. This order works for almost any computer problem — AI-related or not.

## The universal order

1. **Read the actual error.** Copy the exact message. Don't summarize it as "it's broken" — the message usually names the problem.
2. **Change nothing; try again once.** Lots of failures are one-time hiccups.
3. **Ask: what changed?** It worked before. What's different — an update, a new file, a rename, a different folder?
4. **Shrink the problem.** Does it fail with a tiny test file? In a fresh folder? Finding where it *works* tells you where it breaks.
5. **Search the exact message.** Paste the error, in quotes, into a search engine or an AI.
6. **Then, and only then, reinstall.**

## Ask AI the right way

```text title="Copy this"
Something failed. Here's the exact error message: [paste it].
Here's what I was doing: [one sentence]. Here's what changed
recently: [anything you know]. Walk me through fixing it one
step at a time — one step per message, and tell me what each
step does before I run it.
```

The "one step per message" part matters — it stops the AI from dumping ten commands you can't judge.

## By system

- [Terminal basics](terminal-basics.md) — the five commands that cover 90% of it.
- [Windows](windows.md) · [macOS](macos.md) — the usual suspects on each.
- [Git & Codespaces](git-codespaces.md) — for site and code projects.

[Next step: Terminal basics](terminal-basics.md){ .md-button }
