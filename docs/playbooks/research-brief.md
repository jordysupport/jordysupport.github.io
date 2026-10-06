---
title: "Research a topic: Free AI Playbook"
description: >-
  A free AI playbook for a short research brief with linked evidence, clear unknowns, and a recommendation tied to your question.
software_schema:
  name: Research Brief Playbook
  operating_system: Windows, macOS, Linux
  category: UtilitiesApplication
  version: "1.1"
  download_url: https://jordysupport.com/downloads/research-brief-skill.zip
---

<div class="playbook-hero" markdown>

<span class="kicker">Free playbook · Research Brief</span>

# Research a topic

Use this when you need to understand a question before making a decision. The playbook asks what matters to you, checks sources, and turns the findings into a brief you can review.

</div>

<div class="playbook-meta">
  <div><strong>You bring</strong><span>A question and a decision</span></div>
  <div><strong>You get</strong><span>Findings, sources, and open questions</span></div>
  <div><strong>You review</strong><span>Before saving or using the result</span></div>
</div>

[See an example](./research-brief-example.md) before you start.

## Option 1: Save the playbook { #option-1-install-it-once-recommended }

Use this option with an agent that can read and write files. Saving the instructions makes them easier to reuse; your agent still needs to read them when you start a new chat.

[Download the playbook](../downloads/research-brief-skill.zip){ .md-button .md-button--primary }

<p class="small-note">Version 1.1 · October 5, 2026 · Clearer source checks, browsing limits, and instructions for saving a reviewed brief. The download address stays the same.</p>

Extract the ZIP and read both files before asking an agent to use them. These are plain-text instructions, not an app or an automatic installer.

??? note "What's inside this zip (read before handing it to your AI)"
    - `research-brief-skill/INSTALL.md`: setup instructions, reproduced below.
    - `research-brief-skill/SKILL.md`: the questions, task instructions, and review checks.

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
       `<chosen folder>/Skills/research-brief/SKILL.md`
       Ask before creating folders or copying the file. If that file
       already exists, show the difference and ask before replacing it.
       Leave every other file alone.

    4. Copy this folder's `SKILL.md` unchanged. Read the saved file back
       to confirm the copy, then report its full path.

    5. Explain how to use it:
       "Read Skills/research-brief/SKILL.md and start it."
       Within a conversation where the file has already been read, the
       shorter phrase is: "Start my research playbook."
       A new conversation may need the full path again.

    6. Offer to start the playbook. Wait for the person's answer.

    Stay inside the agreed folders. These files contain instructions,
    not a guarantee that an AI will follow them. Do not send, publish,
    or upload anything during installation.
    ```

Attach the ZIP or give its exact path, then send:

```text title="Copy this message"
I have reviewed the attached research-brief-skill.zip.
Read INSTALL.md and SKILL.md. Help me install the playbook in
a folder I choose, following INSTALL.md. Show the destination
and ask before creating or overwriting files.
```

To use the saved copy in a new conversation:

```text title="Start from the saved file"
Read Skills/research-brief/SKILL.md in my notes folder and start it.
```

If the agent has already read the file in this conversation, you can say **"Start my research playbook"**.

It asks what you need to find out, what the answer will help you decide, who will read it, what to cover, and how recent the evidence must be. It then researches and shows where each important finding came from.

## Option 2: Use a chat prompt { #option-2-quick-copy-paste-any-ai-chat }

This needs no installation. Paste the prompt, then provide your material when asked. A chat without file access can give you the result to save yourself.

```text title="Copy this prompt"
Help me build a research brief. Ask one question at a time about
my question, the decision it supports, the audience, what it must
cover, and how recent the information needs to be. Skip questions
I have already answered.

If you can browse, open current primary sources and link the pages
that support important claims. If you cannot browse, say so and
ask me for source material. Do not claim you checked a page you
could not read. Separate source claims, your interpretation, and
unknowns. Flag conflicting evidence and dates that matter.

Deliver: a short answer, key findings, risks and unknowns,
what the evidence means for my decision, and sources.
Keep it a draft. Do not save or send anything without my approval.
```

## Before you trust it

- [ ] Open the sources behind the claims you will act on.
- [ ] Check whether the source actually supports the claim, including any limits.
- [ ] Look for dates on prices, policies, schedules, or other changing information.
- [ ] Make sure the conclusion answers your question and names what is still unknown.

## You're done when

You have an answer you can explain, evidence you can inspect, and a clear view of what needs another check.

**Related:** [Build a knowledge base](knowledge-base.md) to keep a useful brief with its sources.

[Choose another playbook](index.md){ .md-button }
