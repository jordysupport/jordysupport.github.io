---
description: >-
  What AI tokens are in plain English: how they're counted, why chats hit limits, and what actually affects cost, speed, and memory in AI tools.
---

<div class="hero" markdown>

<span class="kicker">Tokenomics / Plain English</span>

# Know what the meter is counting.

Tokens are how AI tools measure reading and writing. You do not need to become a billing expert, but you should know what affects cost, speed, memory, and limits before you hand an AI a giant job.

[Start with the basics](getting-started/index.md){ .md-button .md-button--primary }
[Use the prompt builder](prompting/prompt-builder.md){ .md-button }

</div>

<div class="playbook-meta">
  <div><strong>Token</strong><span>A small chunk of text</span></div>
  <div><strong>Input</strong><span>What the AI reads</span></div>
  <div><strong>Output</strong><span>What the AI writes</span></div>
</div>

## What is a token?

A [token](resources/glossary.md#token) is a piece of text an AI model reads or writes. It might be a whole short word, part of a longer word, a number, punctuation, or a bit of formatting.

The simple version:

- Short message, fewer tokens.
- Long paste, more tokens.
- Big file, many more tokens.
- Long answer, more output tokens.

You usually do not need to count them by hand. You just need the habit: every word you send and every word it returns uses part of the model's working space.

## The four costs

<div class="grid cards" markdown>

-   **Money**

    Some tools charge by tokens. Longer prompts and longer answers can cost more.

-   **Attention**

    A model can only pay attention to so much at once. Extra clutter can push out the important parts.

-   **Speed**

    More text takes longer to read, reason over, and answer.

-   **Quality**

    A huge prompt can make the model miss the actual job. Clear, smaller context often wins.

</div>

## Input vs. output

| Type | What it means | Example |
| --- | --- | --- |
| Input tokens | Everything the AI reads | Your prompt, pasted notes, files, system instructions, tool results |
| Output tokens | Everything the AI writes | The answer, draft, summary, code, plan, or checklist |
| Context window | The total working space | How much the model can keep available in one conversation |

If a task starts getting weird, token pressure might be part of it. The AI may be trying to juggle too many instructions, too much background, or too many old messages at once.

## How to spend tokens wisely

- Give the AI the exact files or notes it needs, not the whole attic.
- Put the job first, then the background.
- Ask for the shape of the answer you want.
- Split large jobs into stages: inspect, plan, draft, verify.
- Replace repeated explanations with a reusable playbook.
- Ask the AI to summarize long source material before asking it to transform it.
- Keep final instructions short and specific when the task matters.

## Good prompt economics

Bad token spend sounds like:

> Read everything and do whatever you think is best.

Better token spend sounds like:

> Read these three notes, find the five most useful ideas for a beginner guide, then draft a 700-word page in plain English. Do not change files yet.

The second prompt spends fewer tokens on confusion. It tells the AI what to read, what to produce, how long it should be, and what not to do.

## When bigger context helps

Bigger context is useful when the AI really needs the history:

- Comparing several documents.
- Refactoring code that touches multiple files.
- Finding contradictions across notes.
- Writing from a long source.
- Keeping a project brief in mind while editing.

Bigger context is not automatically better. If the task is small, tight context usually gives a cleaner result.

## A simple rule

Use enough context for the AI to make a good decision, then stop. Tokens are not magic points. They are working space.

[Learn context and memory](fundamentals/context-memory.md){ .md-button }
[See reusable playbooks](playbooks/index.md){ .md-button }

[Next step: Prompting that works](prompting/index.md){ .md-button }
