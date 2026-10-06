---
description: >-
  See an official privacy article turned into a short reference note, with the source's claims separated from the reader's reasons for saving it.
---

<div class="playbook-hero" markdown>

<span class="kicker">Knowledge base · Worked example</span>

# Keep a source you can revisit { #example-output-a-real-article-becomes-a-vault-note }

This example uses a real Anthropic privacy article. The note keeps the policy summary separate from the reader's reason for saving it.

</div>

!!! example "Sample inputs, real source"
    **Source:** Anthropic's [Is my data used for model training?](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training), checked October 5, 2026. **Reader's reason:** "We use Claude and want to remember which data settings to check before work." **Notes folder:** `Reference/`, with lowercase tags.

## Draft note { #the-note-as-delivered-for-approval }

```markdown
---
tags:
  - ai
  - privacy
  - reference
---

# Claude: data used for model training

## What the source says

This article covers personal Claude plans, including their use of
Claude Code. Commercial products have separate policies.

Anthropic describes model improvement through user permission,
explicit testing opt-ins, and safety review. Incognito chats are
excluded from model improvement. Feedback can allow use of the
related conversation for training.

## Why we are keeping this

We need to check our actual plan and settings before using Claude
for work. This note is a reminder to review the policy, not approval
to put client or employer information into the tool.

## Source

Anthropic Privacy Center, "Is my data used for model training?"
https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training
Article dated March 16, 2026. Checked and saved October 5, 2026.
```

The proposed destination is `Reference/claude-model-training.md`. The playbook shows the draft and asks before saving or replacing a file.

## What to check { #why-this-output-is-trustworthy }

The "What the source says" section summarizes the article. The reason for keeping it comes from the sample reader. Those are different kinds of information, so they have separate sections.

The note records both the article date and the date checked. When you revisit it, open the source again before relying on the policy.

Use the [Before you save it](knowledge-base.md#before-you-save-it) checklist to check your own note.

<span id="want-notes-like-this"></span>

[Try the knowledge playbook](knowledge-base.md){ .md-button .md-button--primary }
