---
title: "Build a knowledge base: Free AI Playbook"
description: >-
  A free AI playbook for saving useful sources and decisions as short notes with clear origins, dates, and links to related material.
software_schema:
  name: Knowledge Base Playbook
  operating_system: Windows, macOS, Linux
  category: UtilitiesApplication
  version: "1.1"
  download_url: https://jordysupport.com/downloads/knowledge-base-skill.zip
---

<div class="playbook-hero" markdown>

<span class="kicker">Free playbook · Knowledge Base</span>

# Build a knowledge base

Save an explanation, decision, or how-to while you still know why it matters. The playbook drafts a short note with its source and date, then asks where you want to keep it. A normal folder works; [Obsidian](../fundamentals/obsidian-vaults.md) is optional.

</div>

<div class="playbook-meta">
  <div><strong>You bring</strong><span>A source or decision to keep</span></div>
  <div><strong>You get</strong><span>A note you can find and check later</span></div>
  <div><strong>You review</strong><span>Before saving or using the result</span></div>
</div>

[See an example](./knowledge-base-example.md) before you start.

## Option 1: Save the playbook { #option-1-install-it-once-recommended }

Use this option with an agent that can read and write files. Saving the instructions makes them easier to reuse; your agent still needs to read them when you start a new chat.

[Download the playbook](../downloads/knowledge-base-skill.zip){ .md-button .md-button--primary }

<p class="small-note">Version 1.1 · October 5, 2026 · Clearer source dates, links, duplicate checks, and approval before saving notes. The download address stays the same.</p>

Extract the ZIP and read both files before asking an agent to use them. These are plain-text instructions, not an app or an automatic installer.

??? note "What's inside this zip (read before handing it to your AI)"
    - `knowledge-base-skill/INSTALL.md`: setup instructions, reproduced below.
    - `knowledge-base-skill/SKILL.md`: the questions, task instructions, and review checks.

    Full text of `INSTALL.md`, word for word:

    ```text
    # INSTALL.md: instructions for the AI agent

    Install this playbook only after the person has reviewed these files
    and asked you to install it. Do not run the playbook during setup.

    1. Check whether you can read and write local files. If you cannot,
       explain the limit and provide these steps for the person to follow.
       Do not report an installation you did not perform.

    2. Ask where they keep permanent notes or project files. Use an exact
       folder they choose. If they have no folder, suggest `Vault` and
       ask where to create it.

    3. Show the destination:
       `<chosen folder>/Skills/knowledge-base/SKILL.md`
       Ask before creating folders or copying the file. If that file
       already exists, show the difference and ask before replacing it.
       Leave every other file alone.

    4. Copy this folder's `SKILL.md` unchanged. Read the saved file back
       to confirm the copy, then report its full path.

    5. Explain how to use it:
       "Read Skills/knowledge-base/SKILL.md and start it."
       Within a conversation where the file has already been read, the
       shorter phrase is: "Start my knowledge playbook."
       A new conversation may need the full path again.

    6. Offer to start the playbook. Wait for the person's answer.

    Stay inside the agreed folders. These files contain instructions,
    not a guarantee that an AI will follow them. Do not send, publish,
    or upload anything during installation.
    ```

Attach the ZIP or give its exact path, then send:

```text title="Copy this message"
I have reviewed the attached knowledge-base-skill.zip.
Read INSTALL.md and SKILL.md. Help me install the playbook in
a folder I choose, following INSTALL.md. Show the destination
and ask before creating or overwriting files.
```

To use the saved copy in a new conversation:

```text title="Start from the saved file"
Read Skills/knowledge-base/SKILL.md in my notes folder and start it.
```

If the agent has already read the file in this conversation, you can say **"Start my knowledge playbook"**.

It asks why the source matters, where you keep notes, and whether it connects to something already saved. You see the whole note and its destination before a file is written.

## Option 2: Use a chat prompt { #option-2-quick-copy-paste-any-ai-chat }

This needs no installation. Paste the prompt, then provide your material when asked. A chat without file access can give you the result to save yourself.

```text title="Copy this prompt"
Help me make a useful reference note. Ask one question at a time
about the source, why I want to keep it, my notes folder and naming
rules, and any related notes. Skip what I have already answered.

Read the full source. Say if any part is inaccessible. Write a
short note with: what the source says, why it matters to me, and
the source location, publication date if available, and date saved.
Keep my reasons separate from the source's claims. Label your own
interpretation. Flag disagreements with existing notes.

Show the full note and proposed filename. Do not save or overwrite
anything until I approve the content and destination. Do not
include passwords, keys, or other secrets.
```

## Before you save it

- [ ] The note makes sense without the original conversation.
- [ ] The source location and relevant dates are present.
- [ ] The summary preserves the source's meaning and limitations.
- [ ] Your reasons and the AI's interpretation are separate from source claims.
- [ ] The filename, links, and destination match your existing notes.

## You're done when

You have a reviewed note in an agreed location, with enough context to decide later whether it needs updating.

**Related:** [Research a topic](research-brief.md) when you need to investigate before making a note.

[Choose another playbook](index.md){ .md-button }
