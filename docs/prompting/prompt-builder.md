---
description: >-
  Build an AI request with a clear goal, source material, output format, and permissions. Includes a template and a worked example.
---

<span class="kicker">Prompting · Builder</span>

# Prompt builder

Use this template when a request needs more than a sentence. Fill in the parts that matter and remove the rest. You can write the same information in ordinary paragraphs if you prefer.

## The template

```text title="Copy and fill in"
Job: [the result you want]

Work from: [attach the material or name the files and sources]

Audience: [who will read or use the result]

Output: [format, length, and tone]

Keep unchanged: [facts, wording, files, or links to preserve]

Permissions:
- You may [read files, research, draft, or make named changes].
- Ask before [actions you want to review first].

Missing information: Ask if it would change the result.
Otherwise, state any small assumption you make.

Before finishing: [how to check the result]
```

If you only want a plan, add: “Explain the proposed changes and wait for my approval.” For a draft you can review on screen, you can usually let the AI start drafting.

## Worked example

```text title="Example, filled in"
Job: Draft a reply declining a vendor's renewal offer.

Work from: [paste the vendor's email]

Audience: The vendor's account manager.

Output: A short, polite email in our usual direct style.

Keep unchanged: We are declining this year's renewal but may
reconsider next year. Do not mention our budget.

Permissions: Draft the reply. Do not send it.

Before finishing: Check that you haven't invented a reason
for declining or promised a future purchase.
```

## When you can't fill in the blanks

Start with the situation. The AI can help you decide what the deliverable should be.

```text title="Copy this instead"
I need help with [situation]. Ask me one question at a time
until you can suggest a clear next step. Then explain what
you would produce and what information you would use.
```

## For work in files or apps

Name the destination as well as the task. “Create the report in [folder] using [template]” is more useful than “make me a report.” Tell the agent whether it may edit the original, should save a new copy, or should show proposed changes first.

[Save your rules as project instructions](system-instructions.md){ .md-button .md-button--primary }
