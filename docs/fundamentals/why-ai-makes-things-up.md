---
description: >-
  Learn how to catch unsupported AI claims, invented sources, incorrect numbers, and reports of actions that never happened.
---

<span class="kicker">How agents work · Accuracy</span>

# Why AI makes things up (and how to catch it)

An AI can give a fluent answer with a false detail: an invented citation, an incorrect date, or a feature the software does not have. This is often called [**hallucination**](../resources/glossary.md#hallucination). With agents, the same problem can appear as “I saved the file” when no file was saved.

## Why it happens, in plain words

Language models generate responses from learned patterns and the information available in their context. That ability helps them draft and explain, but it does not guarantee each claim matches a real source.

Search and file tools give an agent evidence to work with. It can still read the wrong source, miss a condition, or draw a conclusion the source does not support. [OpenAI's accuracy guidance](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy) covers problems with both retrieved context and model output.

## Where to check carefully { #where-it-bites-hardest }

| Claim | What to compare it with |
| --- | --- |
| A quote, title, or citation | The actual source, including the passage cited. |
| A date, price, version, or rule | A current authoritative page. |
| A calculation | The inputs and a calculator or spreadsheet formula. |
| A fact from an uploaded document | The relevant page, row, or section in that document. |
| A completed action | The saved file, app record, or tool result showing what happened. |

If the claim affects a decision, make the check before acting on it. You can check a low-stakes draft yourself; specialist decisions may need a qualified reviewer.

## How to catch it

- [ ] Ask for sources alongside factual claims. Use the guide to [answers you can check](../prompting/ai-answers-with-sources.md).
- [ ] Open the cited source and find the supporting passage. A working link alone proves little.
- [ ] Check names, numbers, dates, and conditions against the original.
- [ ] Ask the agent to separate direct evidence, its interpretation, and what remains unknown.
- [ ] For actions, inspect the result in the file or app. Distinguish drafted, saved, sent, and confirmed received.
- [ ] Use the research playbook's [Before you trust it](../playbooks/research-brief.md#before-you-trust-it) checklist for a larger brief.

```text title="Ask for an evidence check"
Review the claims in this answer. For each important claim,
identify the source and the passage or record that supports it.
Mark inferences as inferences. Remove or flag anything you cannot
verify. Do not create a citation to fill a gap.
```

## What doesn't establish accuracy { #what-doesnt-work }

**“Are you sure?”** may produce a revision, but supplies no new evidence.

**A second answer** can expose disagreement. Matching answers can still repeat the same error, so check the source either way.

**A confident tone** tells you how the response is written. It does not show how well the claim is supported.

## Make verification part of the task { #youre-done-when }

Tell the agent what evidence you expect before it starts. A request for a brief with source passages, unknowns, and a saved file is easier to check than an unrestricted request to “research this.”

[Next: Answers with sources you can check](../prompting/ai-answers-with-sources.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
