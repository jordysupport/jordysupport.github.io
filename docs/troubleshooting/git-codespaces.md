---
description: >-
  Git and GitHub Codespaces for beginners: what commits and pushes are in plain English, plus fixes for the errors that most often trip people up.
---

<span class="kicker">Troubleshooting · Git & Codespaces</span>

# Git & Codespaces

You only need Git if you keep a project on GitHub — like this site. Here's the minimum that keeps you safe, in plain words.

## Git in one paragraph

**Git** tracks versions of a folder. A **commit** is a snapshot with a note. **Push** sends your snapshots to GitHub. A **Codespace** is a computer in your browser already connected to your project — the easiest way to work on a GitHub project without installing anything.

## The daily loop

```text
git status                      ← what changed?
git add -A                      ← include everything changed
git commit -m "what I did"      ← snapshot with a note
git push                        ← send it to GitHub
```

Run `git status` before and after. It's Git's "where am I?" command.

## The messages that scare people

- **"nothing to commit"** — you haven't changed anything (or already committed it). Not an error.
- **"rejected … fetch first"** — GitHub has changes you don't. Run `git pull`, then push again.
- **"merge conflict"** — the same lines changed in two places, and Git wants a human to pick. Open the file, look for `<<<<<<<` markers, keep the version you want, delete the markers, then add/commit/push. Or paste the conflicted file into AI and say "help me resolve this conflict — I want to keep X."

## The safety rule

**Commit before you experiment.** A commit is a save point; anything can be undone after one. If you're about to let an agent loose on the project, commit first, always.

## Undo, the safe way

Made a mess since your last commit?

```text
git restore .        ← put every file back to the last commit
```

That's the beginner-safe undo. For anything scarier (undoing pushed commits), ask AI to walk you through it one step at a time rather than pasting internet commands.

[Next step: Your first agent](../getting-started/first-agent.md){ .md-button }
