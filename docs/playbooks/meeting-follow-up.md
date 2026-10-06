---
title: "Process a meeting: Free AI Playbook"
description: >-
  A free AI playbook for turning meeting notes into decisions, assigned tasks, open questions, and a follow-up draft you can check before sending.
software_schema:
  name: Meeting Follow-Up Playbook
  operating_system: Windows, macOS, Linux
  category: UtilitiesApplication
  version: "1.1"
  download_url: https://jordysupport.com/downloads/meeting-follow-up-skill.zip
---

<div class="playbook-hero" markdown>

<span class="kicker">Free playbook · Meeting Follow-Up</span>

# Process a meeting

Use your notes or a transcript to work out what was decided, who needs to do what, and which questions are still open. The follow-up stays a draft for you to check and send.

</div>

<div class="playbook-meta">
  <div><strong>You bring</strong><span>Notes or an approved transcript</span></div>
  <div><strong>You get</strong><span>Decisions, tasks, and a draft message</span></div>
  <div><strong>You review</strong><span>Before saving or using the result</span></div>
</div>

[See an example](./meeting-follow-up-example.md) before you start.

## Option 1: Save the playbook { #option-1-install-it-once-recommended }

Use this option with an agent that can read and write files. Saving the instructions makes them easier to reuse; your agent still needs to read them when you start a new chat.

[Download the playbook](../downloads/meeting-follow-up-skill.zip){ .md-button .md-button--primary }

<p class="small-note">Version 1.1 · October 5, 2026 · Clearer decision checks, date handling, and privacy rules for follow-up drafts. The download address stays the same.</p>

Extract the ZIP and read both files before asking an agent to use them. These are plain-text instructions, not an app or an automatic installer.

??? note "What's inside this zip (read before handing it to your AI)"
    - `meeting-follow-up-skill/INSTALL.md`: setup instructions, reproduced below.
    - `meeting-follow-up-skill/SKILL.md`: the questions, task instructions, and review checks.

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
       `<chosen folder>/Skills/meeting-follow-up/SKILL.md`
       Ask before creating folders or copying the file. If that file
       already exists, show the difference and ask before replacing it.
       Leave every other file alone.

    4. Copy this folder's `SKILL.md` unchanged. Read the saved file back
       to confirm the copy, then report its full path.

    5. Explain how to use it:
       "Read Skills/meeting-follow-up/SKILL.md and start it."
       Within a conversation where the file has already been read, the
       shorter phrase is: "Start my meeting playbook."
       A new conversation may need the full path again.

    6. Offer to start the playbook. Wait for the person's answer.

    Stay inside the agreed folders. These files contain instructions,
    not a guarantee that an AI will follow them. Do not send, publish,
    or upload anything during installation.
    ```

Attach the ZIP or give its exact path, then send:

```text title="Copy this message"
I have reviewed the attached meeting-follow-up-skill.zip.
Read INSTALL.md and SKILL.md. Help me install the playbook in
a folder I choose, following INSTALL.md. Show the destination
and ask before creating or overwriting files.
```

To use the saved copy in a new conversation:

```text title="Start from the saved file"
Read Skills/meeting-follow-up/SKILL.md in my notes folder and start it.
```

If the agent has already read the file in this conversation, you can say **"Start my meeting playbook"**.

It asks for the notes, the meeting context, the recipients, and anything to leave out. Missing owners and dates remain visible instead of being filled in by guesswork.

## Option 2: Use a chat prompt { #option-2-quick-copy-paste-any-ai-chat }

This needs no installation. Paste the prompt, then provide your material when asked. A chat without file access can give you the result to save yourself.

```text title="Copy this prompt"
Help me turn meeting notes into a follow-up. Ask one question at
a time about the notes, the meeting context and date, the intended
recipients and tone, and sensitive details to leave out. Skip
questions I have already answered.

Use only the notes. Separate decisions from proposals. For each
action item, show owner, task, and due date. Write "unassigned"
or "no date" where the notes do not say. Keep a relative date
as written unless the meeting date makes it clear. Flag ambiguity.

Deliver: decisions, action items, open questions, and a draft
follow-up. Leave excluded details out of the output. Do not ask
anyone to email passwords or credentials. Keep the message a
draft. I will review and send it.
```

## Before you send it

- [ ] Decisions were agreed, rather than suggested or discussed.
- [ ] Tasks, names, and dates match the notes.
- [ ] Unassigned work and unclear deadlines are easy to spot.
- [ ] The draft goes only to the intended audience and omits sensitive details.
- [ ] The message does not ask anyone to send a password or other secret.

## You're done when

The agreed work is clear, the missing details are visible, and the draft reflects the meeting accurately.

**Related:** [Build a knowledge base](knowledge-base.md) to keep decisions you will need later.

[Choose another playbook](index.md){ .md-button }
