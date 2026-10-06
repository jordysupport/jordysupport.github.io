---
title: "Repurpose content: Free AI Playbook"
description: >-
  A free AI playbook for turning a source you own into useful drafts for email, social posts, or a video script without adding unsupported claims.
software_schema:
  name: Content Repurpose Playbook
  operating_system: Windows, macOS, Linux
  category: UtilitiesApplication
  version: "1.1"
  download_url: https://jordysupport.com/downloads/content-repurpose-skill.zip
---

<div class="playbook-hero" markdown>

<span class="kicker">Free playbook · Content Repurpose</span>

# Repurpose content

Have an article, transcript, or useful set of notes? Turn it into a few drafts for the places you actually publish. Keep the meaning, adapt the length and shape, and review each version before using it.

</div>

<div class="playbook-meta">
  <div><strong>You bring</strong><span>Content you can reuse</span></div>
  <div><strong>You get</strong><span>Drafts for your chosen formats</span></div>
  <div><strong>You review</strong><span>Before saving or using the result</span></div>
</div>

[See an example](./content-repurpose-example.md) before you start.

## Option 1: Save the playbook { #option-1-install-it-once-recommended }

Use this option with an agent that can read and write files. Saving the instructions makes them easier to reuse; your agent still needs to read them when you start a new chat.

[Download the playbook](../downloads/content-repurpose-skill.zip){ .md-button .md-button--primary }

<p class="small-note">Version 1.1 · October 5, 2026 · Clearer source access, reuse checks, and rules for preserving meaning across formats. The download address stays the same.</p>

Extract the ZIP and read both files before asking an agent to use them. These are plain-text instructions, not an app or an automatic installer.

??? note "What's inside this zip (read before handing it to your AI)"
    - `content-repurpose-skill/INSTALL.md`: setup instructions, reproduced below.
    - `content-repurpose-skill/SKILL.md`: the questions, task instructions, and review checks.

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
       `<chosen folder>/Skills/content-repurpose/SKILL.md`
       Ask before creating folders or copying the file. If that file
       already exists, show the difference and ask before replacing it.
       Leave every other file alone.

    4. Copy this folder's `SKILL.md` unchanged. Read the saved file back
       to confirm the copy, then report its full path.

    5. Explain how to use it:
       "Read Skills/content-repurpose/SKILL.md and start it."
       Within a conversation where the file has already been read, the
       shorter phrase is: "Start my repurpose playbook."
       A new conversation may need the full path again.

    6. Offer to start the playbook. Wait for the person's answer.

    Stay inside the agreed folders. These files contain instructions,
    not a guarantee that an AI will follow them. Do not send, publish,
    or upload anything during installation.
    ```

Attach the ZIP or give its exact path, then send:

```text title="Copy this message"
I have reviewed the attached content-repurpose-skill.zip.
Read INSTALL.md and SKILL.md. Help me install the playbook in
a folder I choose, following INSTALL.md. Show the destination
and ask before creating or overwriting files.
```

To use the saved copy in a new conversation:

```text title="Start from the saved file"
Read Skills/content-repurpose/SKILL.md in my notes folder and start it.
```

If the agent has already read the file in this conversation, you can say **"Start my repurpose playbook"**.

It asks for the source, the formats you need, the audience, and any limits on voice or length. You review one draft at a time, so corrections carry into the next version.

## Option 2: Use a chat prompt { #option-2-quick-copy-paste-any-ai-chat }

This needs no installation. Paste the prompt, then provide your material when asked. A chat without file access can give you the result to save yourself.

```text title="Copy this prompt"
Help me adapt one piece of content for other formats. Ask one
question at a time about the source, the formats I need, my
audience, and my rules for tone, length, and links. Skip anything
I have already answered.

Read the full source. If you cannot access it, ask me for the text
or transcript. Use only claims the source supports. Keep its
qualifications and uncertainty. Do not add statistics, quotes,
testimonials, or personal experience. Flag anything that needs
checking or permission to reuse.

Draft one format at a time for my review. Make it sound natural
for that format, with no em dashes or stock sales language.
Everything stays a draft. Do not save, schedule, or publish it.
```

## Before you post anything

- [ ] Each factual claim is supported by the source.
- [ ] The draft keeps qualifications that matter to the meaning.
- [ ] Quotes are accurate, and you have permission to reuse the material.
- [ ] The length, links, and voice fit the destination.
- [ ] Names and private details are suitable for the intended audience.

## You're done when

You have the drafts you asked for, with changes to meaning and missing evidence resolved before publication.

**Related:** [Research a topic](research-brief.md) if the source needs fact-checking before you reuse it.

[Choose another playbook](index.md){ .md-button }
