<div class="playbook-hero" markdown>

<span class="kicker">Playbook 2 · Content</span>

# Turn one approved source into useful content

Use this when you already have something trustworthy—a guide, transcript, announcement, lesson, podcast outline, or article—and want several channel-specific drafts **without inventing facts, quotes, promises, or experiences**.

</div>

<div class="playbook-meta">
  <div><strong>Time</strong><span>15–30 minutes</span></div>
  <div><strong>Difficulty</strong><span>Beginner</span></div>
  <div><strong>Start with</strong><span>One approved source</span></div>
  <div><strong>Finish with</strong><span>Reviewed channel drafts</span></div>
</div>

[Download the content starter ZIP](../downloads/content-repurpose-starter.zip){ .md-button .md-button--primary }
[Choose another playbook](index.md){ .md-button }

## What you will make

You will create several drafts from one source while preserving its meaning. A folder-based run can look like:

```text
content-run/
├── SOURCE.md
├── CONTENT_SPEC.md
├── examples/
├── drafts/
├── review/
└── RUN_RECORD.md
```

Common outputs include:

- a newsletter draft;
- a professional social post;
- a short educational thread or carousel outline;
- a 60–90 second video script;
- several headlines or hooks;
- a short recap;
- an FAQ based only on the source.

## How someone uses this page

1. Choose **one approved source**.
2. Decide which formats you need and who each one is for.
3. Copy the quick-start prompt and paste or attach the source.
4. Review the claim list before the AI creates drafts.
5. Review each draft for accuracy, voice, links, and channel fit.
6. Save or publish only the exact version a person approved.

<div class="playbook-flow">
  <span>Approved source</span><b>→</b><span>Claim list</span><b>→</b><span>Format plan</span><b>→</b><span>Drafts</span><b>→</b><span>Review</span>
</div>

## Try it now: the quick chat version

Paste or attach one source, then copy this prompt:

```text
Repurpose the approved source I provide into the formats below.

Source owner:
[person or organization responsible for the source]

Intended audience:
[who should receive the new content]

Formats:
1. [format, length, audience, and desired reader action]
2. [format, length, audience, and desired reader action]
3. [optional format]

Voice rules:
- [observable rule, such as “open with the reader problem”]
- [observable rule, such as “keep paragraphs under three sentences”]
- [words, styles, or claims to avoid]

Required links or disclosures:
[list them]

Rules:
- Use only information and experiences contained in the approved source.
- Preserve qualifications, uncertainty, and warnings.
- Do not invent statistics, quotations, testimonials, urgency, scarcity, guarantees, personal stories, product behavior, or results.
- Do not describe an idea as the author's experience unless the source says it is.
- Adapt the structure for each format; do not merely shorten the same draft.
- Label suggestions that go beyond the source as “Needs approval” and keep them outside the publishable drafts.

First return only:
A. the core message in one sentence;
B. an approved-claim list with source locations;
C. the proposed angle and claim IDs for each format;
D. questions or source problems.

Wait for my approval before drafting.
```

After reviewing the claim and format plan, say:

```text
Approved with these changes: [list changes, or say none].
Create the drafts. Keep each format in its own clearly labeled section. Do not add any claim that is not in the approved claim list.
```

## Worked example: an Obsidian organization guide

Imagine you wrote a guide called **“How to Keep an Obsidian Vault Organized Without Overengineering It.”** You want to create:

1. a short email newsletter;
2. a professional social post;
3. a 75-second video script.

A useful source package might say:

```markdown
# Source identity
- Title: How to Keep an Obsidian Vault Organized Without Overengineering It
- Owner: Jordy Support
- Approved date: [date]
- Intended audience: beginners using AI agents with Obsidian

# Approved claims
- Start with a small number of broad folders.
- Use an inbox for unprocessed notes.
- Add status and review dates when maintenance matters.
- Agents should not rename unrelated notes or modify .obsidian/ without approval.
- A weekly review can catch duplicate, stale, and unlinked notes.

# Claims requiring qualification
- There is no universal folder structure that works for every vault.
- More automation is not always better.

# Prohibited or unsupported claims
- This system guarantees perfect organization.
- This is the only correct way to use Obsidian.
- An AI agent can maintain the vault safely without human review.

# Required link
- Link to the full Obsidian vault guide.
```

Then define each format:

| Format | Audience | Objective | Length | Reader action |
|---|---|---|---|---|
| Newsletter | Existing community | Teach the four-part system | 300–450 words | Open the full guide |
| Professional post | People exploring AI workflows | Share one practical framework | 120–180 words | Save the post or read the guide |
| Video script | Beginners | Explain the system quickly | 75 seconds | Try the weekly review |

The AI should first return a claim plan such as:

| Claim ID | Approved claim | Newsletter | Post | Video |
|---|---|---:|---:|---:|
| C01 | Start with broad folders | Yes | Yes | Yes |
| C02 | Use an inbox | Yes | Yes | Yes |
| C03 | Add review dates | Yes | No | Yes |
| C04 | Protect `.obsidian/` | Yes | No | No |
| C05 | Run a weekly review | Yes | Yes | Yes |

You can now catch problems before drafting. For example, you might decide the post should focus only on the weekly review rather than squeeze the entire guide into 150 words.

A good output is not three versions of the same paragraph. Each format should serve its channel:

- the newsletter can explain and connect ideas;
- the post can teach one memorable framework;
- the video script can use spoken language, pacing, and a clear ending.

## Choose your setup

=== "Normal AI chat"

    Paste or attach the source. Use the quick prompt. Approve the claim plan, then request the drafts and audit in separate turns.

    Best for one-time repurposing or a small source.

=== "Folder-based agent"

    Create a bounded workspace:

    ```bash
    mkdir -p content-run/{examples,drafts,review}
    cd content-run
    touch SOURCE.md CONTENT_SPEC.md RUN_RECORD.md
    ```

    Put the source and approved claims in `SOURCE.md`. Put channel requirements in `CONTENT_SPEC.md`. Start the agent inside `content-run/` and say:

    ```text
    Work only inside this content-run folder.
    Read SOURCE.md and CONTENT_SPEC.md first.
    Create the claim plan in review/claim-plan.md and wait for approval.
    After approval, create one file per format inside drafts/.
    Put audit findings in review/audit.md.
    Do not publish, schedule, send, or modify the original source.
    ```

=== "Obsidian vault"

    Save the source and run inside a dedicated project folder:

    ```text
    Projects/
    └── Content Runs/
        └── obsidian-organization-guide/
            ├── Source.md
            ├── Content Spec.md
            ├── Claim Plan.md
            ├── Drafts/
            └── Review.md
    ```

    Tell the agent not to treat other vault notes as approved source material unless you explicitly add them to the run.

    Use properties such as:

    ```yaml
    ---
    type: content-run
    status: draft
    source-title: How to Keep an Obsidian Vault Organized Without Overengineering It
    owner: Jordy Support
    review-by:
    ---
    ```

## Full workflow

### Step 1: Approve the source

Use one source package per run. `SOURCE.md` can contain:

```markdown
# Source identity
- Title:
- Owner:
- Approved date:
- Canonical URL if published:
- Intended audience:

# Source content
[paste the source or reference the approved file]

# Approved claims
-

# Claims requiring exact wording or qualification
-

# Prohibited or unsupported claims
-

# Required links or disclosures
-
```

If the source itself is unfinished or unapproved, pause. Repurposing multiplies both the value and the mistakes in the source.

### Step 2: Define the formats

Write observable requirements in `CONTENT_SPEC.md`:

```markdown
## Format: Newsletter
- Audience:
- Objective:
- Length:
- Required structure:
- Reader action:
- Voice rules:
- Required links:
- Prohibited content:

## Format: Professional post
- Audience:
- Objective:
- Length:
- Required structure:
- Reader action:
- Voice rules:
- Required links:
- Prohibited content:
```

“Make it engaging” is not enough. Describe what the reader should understand or do and how the writing should behave.

### Step 3: Build the claim list

Before drafting, create:

| Claim ID | Approved claim | Source location | May paraphrase? | Required qualification | Allowed formats |
|---|---|---|---|---|---|
| C01 |  |  | Yes / No |  |  |

Also record:

- approved examples;
- definitions;
- warnings and qualifications;
- required links;
- phrases that must remain exact;
- points that are interpretation rather than fact;
- details that are private or not approved for public use.

### Step 4: Approve the format plan

For each format, ask the AI to list:

- the central message;
- the intended reader action;
- the claim IDs it will use;
- the structure;
- anything it plans to omit;
- any creative idea requiring approval.

This keeps the AI from improvising facts while trying to make the content more interesting.

### Step 5: Draft each format separately

Use this instruction:

```text
Use SOURCE.md, CONTENT_SPEC.md, and the approved claim plan.

Create drafts only inside drafts/.

Rules:
- Preserve the source meaning.
- Use only approved claims and examples.
- Keep required qualifications attached to the relevant claim.
- Do not add statistics, quotes, testimonials, urgency, scarcity, guarantees, results, or product capabilities.
- Adapt structure and wording for each format.
- Use required links and disclosures.
- Keep “Needs approval” ideas outside the publishable draft.
- Do not publish, schedule, send, or update external systems.
```

### Step 6: Run three reviews

**Claim review:** Does every factual statement map to the approved claim list?

**Format review:** Does each draft fit its audience, length, structure, and reader action?

**Cross-format review:** Do all drafts remain consistent with the source and each other?

Use this audit prompt:

```text
Audit all drafts against the approved source, content specification, and claim list.

Return:
1. unsupported or overstated claims;
2. missing qualifications, links, or disclosures;
3. contradictions between formats;
4. wording that changes the source meaning;
5. content that is too similar across formats;
6. length or structure violations;
7. invented quotes, experiences, statistics, urgency, promises, or product behavior;
8. private or internal details that should not be public;
9. a claim-usage table showing which claim IDs appear in each draft.

Do not rewrite until I review the audit.
```

### Step 7: Human approval

A person should inspect the exact final versions and confirm:

- the source was approved;
- claims are supported;
- qualifications remain attached;
- each format has a clear purpose;
- links and calls to action are correct;
- no private details leaked;
- the voice matches the owner;
- the current date, offer, and schedule are still correct;
- the approved version is the same version that will be published.

## Optional: use subagents

Separate roles can reduce context mixing:

| Subagent | Job |
|---|---|
| `claim-extractor` | Creates the claim list and flags unsupported material |
| `channel-writer` | Drafts one assigned format from approved claims |
| `content-auditor` | Compares every draft against the source and specification |

Example requests:

```text
Use the claim-extractor subagent to build review/claim-plan.md. Do not draft content.
```

```text
Use one channel-writer subagent per approved format. Each subagent may use only the claim IDs assigned to that format.
```

```text
Use the content-auditor subagent to return findings only. Do not rewrite or approve its own drafts.
```

When several drafts are independent, channel-writing subagents can run in parallel. The claim plan must be approved first, and one final cross-format review should happen afterward. See [Subagents](../fundamentals/subagents.md).

## Voice rules that an AI can follow

Instead of:

> Friendly, authentic, punchy, and professional.

Use rules that can be observed:

```text
- Open with the reader's problem, not a greeting.
- Use first person only for experiences stated in the source.
- Keep paragraphs under three sentences.
- Avoid hype words such as revolutionary, game-changing, effortless, and guaranteed.
- Explain one main idea per short post.
- Prefer concrete examples over vague enthusiasm.
- End with one specific next action.
```

Approved examples help more than a list of adjectives. Explain what should be copied from each example: sentence length, structure, level of detail, or use of evidence.

## Human quality checklist

- [ ] The source is approved and clearly identified.
- [ ] Every factual statement comes from the approved source package.
- [ ] Qualifications, uncertainty, and warnings remain attached.
- [ ] No personal story or experience was invented.
- [ ] No statistics, quotations, testimonials, urgency, scarcity, guarantee, or capability was added.
- [ ] Each format fits its audience and channel.
- [ ] Required links and disclosures are correct.
- [ ] Private or internal details are excluded.
- [ ] The voice rules are observable and satisfied.
- [ ] A person reviewed the exact final versions.
- [ ] Publishing or scheduling remains a separate approved action.

## You are done when

You have:

1. one approved source package;
2. an approved claim plan;
3. distinct channel-specific drafts;
4. an audit with no unresolved high-severity findings;
5. a human-approved final version for each channel.

## Automate later—not first

After the manual workflow succeeds repeatedly:

```text
approved source enters Ready state
→ validate source metadata
→ generate claim plan
→ human approves claims and format assignments
→ create channel drafts
→ validate links, lengths, and prohibited language
→ run claim and cross-format audits
→ place exact drafts in an approval queue
→ human approves each final version
→ publishing system schedules approved content
→ record publication IDs and URLs
```

Do not allow the same model to generate, approve, and publish its own output without independent controls.
