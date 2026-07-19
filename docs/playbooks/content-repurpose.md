<div class="playbook-hero" markdown>

<span class="kicker">Playbook · Content</span>

# Turn one approved source into several drafts

Use this to repurpose an article, transcript, guide, announcement, or video outline without inventing new claims.

</div>

<div class="playbook-meta">
  <div><strong>Input</strong><span>One approved source</span></div>
  <div><strong>Output</strong><span>Channel-specific drafts</span></div>
  <div><strong>Time</strong><span>10–20 minutes</span></div>
</div>

## 1. Fill this in

```text title="Fill in these details"
Source: [paste text or provide the file]
Audience: [who is this for?]
Formats: [newsletter, LinkedIn post, short video script, summary, etc.]
Voice: [3–5 useful style words]
Call to action: [what should the reader do, if anything?]
Do not include: [claims, topics, or phrases to avoid]
```

### Example

```text title="Example input"
Source: My approved guide to organizing an Obsidian vault
Audience: Beginners using AI agents with Obsidian
Formats: one newsletter intro, one LinkedIn post, and one 45-second video script
Voice: practical, friendly, calm, direct
Call to action: Read the full vault guide
Do not include: promises that the vault maintains itself
```

## 2. Copy this prompt

```text title="Copy this prompt"
Repurpose the approved source below into the requested formats.

Audience: [AUDIENCE]
Formats: [FORMATS]
Voice: [VOICE]
Call to action: [CALL TO ACTION]
Do not include: [EXCLUSIONS]

Rules:
- Treat the source as the boundary for factual claims.
- Do not invent statistics, quotes, results, testimonials, or features.
- Preserve the original meaning while adapting structure and length.
- Make each format feel native to its channel instead of copying the same draft repeatedly.
- Mark anything that needs confirmation as [VERIFY].

For each format, provide:
1. Draft
2. One-sentence purpose
3. Claims or details that should be checked before publishing

Approved source:
[PASTE OR ATTACH SOURCE]
```

## 3. Check the result

- [ ] Every factual claim came from the approved source.
- [ ] Each format fits its audience and channel.
- [ ] The voice sounds like the original creator.
- [ ] The call to action is accurate and not overpromising.
- [ ] Names, links, dates, and quotations were checked.

## What the example should produce

The Obsidian example should create three genuinely different drafts:

- a newsletter opening that explains the problem and benefit;
- a concise professional post with one practical takeaway;
- a spoken script that sounds natural aloud.

All three can point to the full guide, but none should claim that an AI can safely reorganize a vault without review.

??? info "Optional: run it with a folder-based agent"

    ```text title="Copy this agent prompt"
    Read the approved source in source/ and the requirements in INPUT.md.
    Draft each requested format as a separate file in output/.
    Create output/REVIEW.md listing every factual claim, its source location, and anything marked [VERIFY].
    Do not edit the original source.
    ```

??? info "Optional: ask for subagents"

    ```text title="Copy this subagent request"
    Use one drafting subagent per independent format. Then use a separate source-auditor subagent to compare every draft against the approved source. Return the drafts and audit; do not publish anything.
    ```

## You are done when

The drafts are useful on their own, faithful to the source, and ready for a human to approve—not automatically publish.

[Download the short content starter](../downloads/content-repurpose-starter.zip){ .md-button .md-button--primary }
[Choose another playbook](index.md){ .md-button }
