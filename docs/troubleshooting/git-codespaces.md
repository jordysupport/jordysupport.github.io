# Git and Codespaces

Git records changes to files. Codespaces gives you a cloud development environment connected to a repository. Together they let you preview, compare, commit, push, and recover website changes without editing the live site directly.

## The normal safe flow

```text
inspect → create branch → edit → preview → review diff → commit → push → merge
```

## Confirm the repository

```bash
pwd
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git status
```

These commands answer:

- Where am I?
- Which Git repository am I in?
- Which GitHub repository is connected?
- Which branch am I changing?
- What files differ?

## Start a branch for a large rework

```bash
git switch -c redesign/general-ai-support
```

A branch lets you push and review the rebuild without immediately replacing `main`.

If the branch already exists locally:

```bash
git switch redesign/general-ai-support
```

## Preview a MkDocs site

From the repository root:

```bash
python -m pip install -r requirements.txt
mkdocs serve -a 0.0.0.0:8000
```

In Codespaces, open the forwarded port `8000`. The server keeps running; press `Ctrl+C` in the terminal to stop it.

Run a strict build before committing:

```bash
mkdocs build --strict
```

A successful preview does not replace a build check. The strict build catches warnings that may be easy to miss.

## Review changes

```bash
git status
git diff --stat
git diff
```

For a large change, inspect individual files:

```bash
git diff -- mkdocs.yml
git diff -- docs/index.md
```

After staging:

```bash
git diff --cached --stat
git diff --cached
```

## Commit and push

```bash
git add -A
git status
git commit -m "Rebuild site as a practical AI agent support hub"
git push -u origin redesign/general-ai-support
```

`git add -A` stages new, modified, and deleted files. Always read `git status` before committing.

## Merge after review

A GitHub pull request is the easiest review path. You can also merge in the terminal:

```bash
git switch main
git pull --ff-only
git merge --no-ff redesign/general-ai-support
git push origin main
```

The push to `main` triggers the deployment workflow.

## Verify deployment

On GitHub:

1. open the repository;
2. open **Actions**;
3. select the latest “Deploy docs” run;
4. confirm the build and deploy steps succeeded;
5. open the live site in a private window or hard refresh.

A GitHub Pages update may not appear in the same browser tab immediately because of caching. Check the Action before changing files again.

## Understanding `git status`

### Modified

A tracked file changed.

### Untracked

A new file exists but Git is not tracking it.

### Deleted

A tracked file was removed.

### Staged

The change is included in the next commit.

### Working tree clean

Your current files match the current commit.

## Undo a file before staging

```bash
git restore path/to/file
```

This discards the uncommitted changes in that file. Review first; recovery may be difficult.

## Unstage without discarding the edit

```bash
git restore --staged path/to/file
```

The file remains changed in your working tree.

## Recover a deleted file before commit

```bash
git restore path/to/file
```

## Correct the last commit message

Before pushing:

```bash
git commit --amend -m "Better commit message"
```

Avoid rewriting a shared pushed commit unless you understand the impact.

## Revert a pushed commit safely

Create a new commit that undoes it:

```bash
git log --oneline -5
git revert <commit-id>
git push
```

This is safer for shared history than `git reset --hard` and force push.

## Your branch is behind the remote

Save or commit your work first, then:

```bash
git fetch origin
git status
git pull --rebase
```

Resolve conflicts carefully. Do not run a hard reset because a message looks intimidating.

## Push says the repository moved

Update the remote URL:

```bash
git remote set-url origin https://github.com/jordysupport/jordysupport.github.io.git
git remote -v
```

## Push rejected because remote has new work

```bash
git fetch origin
git log --oneline --decorate --graph --all -12
git pull --rebase
```

If a conflict appears:

1. open each conflicted file;
2. choose the correct combined content;
3. remove conflict markers;
4. run the build;
5. stage the resolved files;
6. continue:

```bash
git add path/to/resolved-file
git rebase --continue
```

Abort the rebase without losing the original branch state:

```bash
git rebase --abort
```

## Do not commit generated or secret files

Check for:

- `.env`;
- API keys or tokens;
- private certificates;
- virtual environments;
- `site/` build output;
- editor caches;
- large private source files.

Search filenames, not secret values:

```bash
find . -maxdepth 3 -type f | sort
```

Review staged content:

```bash
git diff --cached
```

If a secret was committed, removing it in a later commit does not erase it from history. Revoke the secret immediately and use GitHub's secret-removal guidance.

## Useful Codespaces commands

```bash
# Repository state
git status --short --branch

# Recent commits
git log -5 --oneline --decorate

# Changed-file summary
git diff --stat

# Current disk space
df -h

# Running processes that contain mkdocs
ps aux | grep '[m]kdocs'

# Find site files
find docs -maxdepth 3 -type f | sort
```

## A complete website edit session

```bash
cd /workspaces/setup
git status
git switch -c content/add-agent-guide

# Edit files, then preview
python -m pip install -r requirements.txt
mkdocs serve -a 0.0.0.0:8000
# Press Ctrl+C after reviewing

mkdocs build --strict
git diff --stat
git diff
git add -A
git status
git commit -m "Add agent guide"
git push -u origin content/add-agent-guide
```

The habit to keep is simple: know the repository, know the branch, inspect the diff, run the check, and make recovery possible.
