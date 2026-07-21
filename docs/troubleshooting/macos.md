---
description: >-
  Fix common Mac problems when setting up AI tools: plain-English solutions for installs, permissions, and errors that stop beginners on macOS.
---

<span class="kicker">Troubleshooting · macOS</span>

# macOS

The usual suspects on a Mac, and the plain fix for each.

## "App can't be opened" / unidentified developer

macOS blocks apps it doesn't recognize. If it came from the tool's **official site**: System Settings → Privacy & Security → scroll down → *Open Anyway*. Not sure it's official? Stop and check first.

## It wants permission for folders

The first time a terminal or agent touches Documents/Desktop, macOS asks. This is good — it's your least-privilege system working. Allow the specific folder your practice work lives in; don't grant Full Disk Access just to make dialogs go away.

## "command not found" after installing

Same story as every system: the terminal doesn't know where the new program lives.

1. Fully quit Terminal (Cmd+Q) and reopen. Try again.
2. Still failing? Ask AI: *"I installed [tool] on macOS and get 'command not found'. Walk me through fixing my PATH one step at a time."*

## Homebrew, in one paragraph

Guides will tell you to "brew install" things. **Homebrew** is a free installer for terminal tools — one command installs it (get it from [brew.sh](https://brew.sh), the official site), and afterwards `brew install [tool]` handles the fiddly parts. It's safe and standard; just get the install command from brew.sh itself, not a random blog.

## Where your stuff is

Your files live under `/Users/yourname/` — the terminal shortcut for it is `~`. So `cd ~/Documents/ai-practice` means "go to the ai-practice folder in my Documents." When a command fails with "no such file or directory," you're usually one `cd` away from where you meant to be.

[Next step: Terminal basics](terminal-basics.md){ .md-button }
