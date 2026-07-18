# Content repurposing playbook

Use this playbook to turn one approved source into several channel-specific drafts while preserving the original meaning and claims.

The system should **transform**, not manufacture evidence, testimonials, urgency, or promises.

## Best for

- article to newsletter and social drafts;
- webinar transcript to recap and clips list;
- podcast notes to post ideas;
- approved announcement to channel variations;
- long guide to short educational pieces.

## Folder structure

```text
content-run/
├── SOURCE.md
├── CONTENT_SPEC.md
├── examples/
├── drafts/
├── review/
└── RUN_RECORD.md
```

Keep a single approved source package for the run. Do not mix unreviewed research into the transformation step.

## Step 1: Prepare the source

`SOURCE.md` should include:

```markdown
# Source identity
- Title:
- Owner:
- Approved date:
- Canonical URL if published:
- Intended audience:

# Source content
[paste or reference the approved source]

# Approved claims
-

# Claims requiring exact wording
-

# Prohibited or unsupported claims
-

# Required links or disclosures
-
```

If the source itself is not approved, pause. Repurposing multiplies mistakes.

## Step 2: Define each format

Write `CONTENT_SPEC.md`:

```markdown
## Format: Newsletter
- Audience:
- Objective:
- Length:
- Required structure:
- Call to action:
- Tone:
- Required links:
- Prohibited content:

## Format: Short professional post
- Audience:
- Objective:
- Length:
- Required structure:
- Call to action:
- Tone:
- Required links:
- Prohibited content:
```

Do not use “make it engaging” as the whole specification. Define what the reader should understand or do.

## Step 3: Extract a claim ledger

Before drafting, create:

| Claim ID | Approved claim | Source location | May paraphrase? | Required qualification | Allowed formats |
|---|---|---|---|---|---|
| C01 |  |  | Yes/No |  |  |

Also extract:

- key examples;
- definitions;
- required warnings;
- links;
- phrases that should not be reused;
- points that are interpretation rather than fact.

## Step 4: Draft by format

```text
Use SOURCE.md, CONTENT_SPEC.md, and the approved claim ledger.

Create drafts only inside drafts/.

Rules:
- Preserve the meaning of the source.
- Use only approved claims and examples.
- Do not add statistics, quotes, testimonials, urgency, scarcity, guarantees, or product capabilities.
- Keep required qualifications attached to the relevant claim.
- Adapt structure and wording to each format rather than merely shortening the same text.
- Use the required link and disclosure rules.
- Label any creative suggestion that goes beyond the source as "Needs approval" and keep it out of the publishable draft.

Before writing, summarize the core message and list the claim IDs you plan to use in each format.
```

Approve the claim plan before drafting if the content is public-facing or sensitive.

## Step 5: Run three reviews

### Claim review

Does every factual statement map to the claim ledger?

### Format review

Does each draft fit its audience, structure, length, and call to action?

### Cross-format review

Do the drafts remain consistent with each other and the source?

Use this audit prompt:

```text
Audit all files in drafts/ against SOURCE.md, CONTENT_SPEC.md, and the claim ledger.

Return:
1. unsupported or overstated claims;
2. missing qualifications or required links;
3. contradictions between formats;
4. wording that accidentally changes the source meaning;
5. content that is too similar across formats;
6. length or structural violations;
7. invented quotes, testimonials, urgency, promises, or product behavior;
8. a claim-usage table showing which claim IDs appear in each draft.

Do not rewrite until the findings are reviewed.
```

## Step 6: Human approval

A reviewer should confirm:

- [ ] The source is approved.
- [ ] Every claim is supported.
- [ ] Qualifications remain attached.
- [ ] Each channel draft has a clear purpose.
- [ ] Links and calls to action are correct.
- [ ] Private or internal details were not leaked.
- [ ] Tone matches the owner, not a generic “AI voice.”
- [ ] The publication date or schedule is still correct.
- [ ] The exact final version is visible before publishing.

## Voice without vague adjectives

Instead of:

> Friendly, authentic, punchy, and professional.

Use observable rules:

```text
- Open with the reader problem, not a greeting.
- Use first person only for experiences stated in the source.
- Keep paragraphs under 3 sentences.
- Avoid hype words: revolutionary, game-changing, effortless, guaranteed.
- Explain one idea per post.
- End with one specific next action, not “thoughts?” by default.
```

Store approved examples and explain the qualities to copy.

## Safe automation upgrade

```text
approved source enters Ready state
→ validate source metadata and required fields
→ generate claim ledger
→ human approves claim ledger
→ create channel drafts
→ validate links, lengths, and prohibited phrases
→ claim audit
→ place exact drafts in approval queue
→ human approves each final version
→ publishing system schedules approved content
→ record publication IDs and URLs
```

Do not let the same model generate, approve, and publish its own output without independent controls.

## Useful metrics

- percentage of drafts approved without factual correction;
- average human editing time;
- unsupported-claim rate;
- format-compliance rate;
- percentage of scheduled items changed after approval;
- performance by source and channel, interpreted carefully;
- cost per approved asset, including review time.

The goal is not maximum output volume. It is more approved, useful content from the same source effort.
