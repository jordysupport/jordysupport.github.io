---
description: >-
  Learn the Git steps that make an agent's file changes reviewable: inspect, stage specific files, commit, and push, plus common sync errors.
---

<span class="kicker">Troubleshooting · Git & Codespaces</span>

# Git & Codespaces

Git gives a project a history of saved changes. When an agent edits files, that history helps you compare the result and recover earlier work.

## What the names mean { #git-in-one-paragraph }

A **repository** is a folder tracked by Git. A **commit** records the staged version of its files. **Push** sends local commits to a remote repository, such as one on GitHub.

A **Codespace** is a cloud development environment connected to a repository. You can open it in a browser; it runs in a Linux environment, even if your computer uses Windows. Check GitHub's included usage and billing rules before starting one. [GitHub Codespaces documentation](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)

## Review, save, then share { #the-daily-loop }

Run these commands from the repository folder, one at a time. This example assumes you changed `notes.md`; replace it with the file you intend to save.

```sh
git status
git diff -- notes.md
git add -- notes.md
git diff --staged
git commit -m "Clarify the project notes"
git status
```

`git diff` shows changes to tracked files that have not been staged. Open new, untracked files yourself. `git add` stages the chosen file, and `git diff --staged` shows what the next commit will include.

Keep passwords, API keys, and private files out of commits. Broad commands such as `git add -A` can include changes you did not mean to share. [Git's staging documentation](https://git-scm.com/docs/git-add)

When you intend to share the reviewed commit:

```sh
git push
```

A push can trigger a site's deployment or other automation. Check the repository's publishing setup before pushing.

## Common messages { #the-messages-that-scare-people }

**"Nothing to commit."** Git sees no staged changes to record. Check `git status` to see whether the file is untracked, unchanged, or already committed.

**"Rejected" or "fetch first."** The remote may contain commits you do not have. First check `git status` and save or otherwise preserve your local work. If your branch is clean and tracks the intended remote branch, try:

```sh
git pull --ff-only
```

This updates the branch only when Git can move it forward without combining divergent histories. If it refuses, inspect the local and remote commits before deciding how to combine them. Do not force-push to clear the error. [Git's pull documentation](https://git-scm.com/docs/git-pull)

**"Merge conflict."** Git needs a decision about overlapping changes. Read both versions, choose the intended content, and remove the `<<<<<<<`, `=======`, and `>>>>>>>` markers. Test the result before staging it. Ask for help with the exact conflict if you are unsure which changes belong.

## Before an agent edits the project { #the-safety-rule }

Check `git status` and inspect the current changes. Make a reviewed commit or another backup of work you need to keep, then give the agent a specific task and file scope.

A commit preserves what it contains. Untracked, ignored, and uncommitted work still needs attention. A local commit also stays on that computer until you push or back up the repository.

## Undo one change carefully { #undo-the-safe-way }

To unstage `notes.md` while keeping its edits in the working file:

```sh
git restore --staged -- notes.md
```

To discard edits made since that file's staged version:

```sh
git restore -- notes.md
```

The second command replaces the working file. Copy or inspect anything you may want to keep before using it. By default, `git restore` uses the staging area; it does not always restore the last commit. [Git's restore documentation](https://git-scm.com/docs/git-restore)

Avoid broad reset, clean, or restore commands until you know which files they affect. To undo a published commit, inspect the history and choose an approach that preserves other people's work.

[Try your first agent task](../getting-started/first-agent.md){ .md-button }
