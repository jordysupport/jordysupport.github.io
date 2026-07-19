<div class="playbook-hero" markdown>

<span class="kicker">Playbook · Knowledge</span>

# Add one trustworthy note to a knowledge base

Use this for an Obsidian vault or another Markdown knowledge base. Start with **one approved source and one note**—not a full-vault reorganization.

</div>

<div class="playbook-meta">
  <div><strong>Input</strong><span>One trusted source</span></div>
  <div><strong>Output</strong><span>One reviewed note</span></div>
  <div><strong>Time</strong><span>10–20 minutes</span></div>
</div>

## 1. Fill this in

```text title="Fill in these details"
Knowledge base or vault: [name or folder]
Source: [file, page, notes, or approved text]
Note purpose: [what should this note help someone do?]
Suggested location: [Inbox, Guides, Reference, etc.]
Required properties: [source, status, reviewed, owner, etc.]
Do not change: [folders, .obsidian, existing notes, attachments, etc.]
```

### Example

```text title="Example input"
Knowledge base or vault: Jordy Support Vault
Source: Approved Windows setup guide
Note purpose: Help a beginner fix a PowerShell execution-policy error
Suggested location: Inbox
Required properties: source, status, reviewed
Do not change: existing notes, folder structure, attachments, or .obsidian
```

## 2. Copy this prompt

```text title="Copy this prompt"
Create one draft knowledge note from the approved source.

Knowledge base: [NAME OR FOLDER]
Source: [SOURCE]
Note purpose: [PURPOSE]
Suggested location: [LOCATION]
Required properties: [PROPERTIES]
Do not change: [PROTECTED ITEMS]

Rules:
- Read the source before writing.
- Keep source facts separate from your explanation or inference.
- Do not invent missing steps, links, owners, dates, or policies.
- Add provenance: source, status, and review date.
- Suggest links only when the relationship is useful and real.
- Write the new note as a draft in the suggested location.
- Do not rename, move, merge, delete, or reorganize anything without approval.

Before writing, show:
1. Proposed note title
2. Proposed location
3. Short outline
4. Existing notes you plan to link

Stop for approval. After approval, create the draft and list any unresolved questions.
```

## 3. Check the result

- [ ] The note helps with one clear job.
- [ ] The source and review status are visible.
- [ ] Facts match the source.
- [ ] Links are useful rather than decorative.
- [ ] No unrelated files or vault settings changed.
- [ ] Unknowns remain visible.

## What the example should produce

The Windows example should become one focused troubleshooting note with:

- the error symptom;
- the safest first checks;
- the approved commands from the source;
- a warning about scope or permissions;
- a source link and review date;
- links to related Windows or terminal notes only when they already exist.

It should **not** reorganize the entire vault or edit `.obsidian/`.

## Simple weekly maintenance

Run this only after you have reviewed recent notes:

```text title="Copy this weekly maintenance prompt"
Review notes added or changed during the last seven days.

Report only—do not edit files.

List:
1. Notes missing source, status, owner, or review date
2. Likely duplicates
3. Broken or weak links
4. Notes that contain unresolved [VERIFY] or [NEEDS CONFIRMATION] markers
5. Stale notes that should be reviewed
6. The five highest-value maintenance actions

For every finding, include the file path and a short reason. Do not reorganize the vault.
```

??? info "Optional: run it with a folder-based agent"

    Start the agent in the vault or, more safely, in a test copy. Require it to read your vault instruction file first.

    ```text title="Copy this agent prompt"
    Read VAULT-GUIDE.md before doing anything.
    Work only inside this vault. Begin in read-only mode and report the relevant files.
    For this task, create drafts only in Inbox/. Do not edit .obsidian/, rename folders, move attachments, or delete files.
    Show a plan and wait for approval before writing.
    ```

??? info "Optional: ask for subagents"

    ```text title="Copy this subagent request"
    Use a read-only source-review subagent to extract supported facts and a separate link-auditor subagent to suggest relevant existing notes. The main agent should propose the draft plan. No subagent may write or reorganize the vault.
    ```

## You are done when

One useful note is approved, traceable to its source, easy to find, and safe to maintain later.

[Read the full Obsidian vault guide](../fundamentals/obsidian-vaults.md){ .md-button }
[Download the short knowledge-base starter](../downloads/knowledge-base-starter.zip){ .md-button .md-button--primary }
[Choose another playbook](index.md){ .md-button }
