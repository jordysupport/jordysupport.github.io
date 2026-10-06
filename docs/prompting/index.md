---
description: >-
  Write clear AI requests, provide useful source material, and set boundaries when an agent can use tools or change files.
---

<span class="kicker">Prompting</span>

# Prompting that works

A [prompt](../resources/glossary.md#prompt) is the request you give an AI. It can be one sentence. For a larger job, explain the result you need and give it the information that could change the answer.

We use the same approach for a quick draft and an agent that can work across files and apps. The difference is that an agent also needs clear permission to act.

## The five ingredients

1. **The job.** Name the finished result: a reply, a comparison, an edited file.
2. **The material.** Provide the relevant notes, files, or sources. Say which version to use.
3. **The audience.** Explain who will read or use the result.
4. **The shape.** Set a useful length, format, and tone.
5. **The rules.** Say what must stay unchanged and where approval is needed.

Include the parts that matter for this job. A short spelling fix doesn't need a full brief.

## Before and after

**Vague:** “Write something about our new service.”

**Clear:** “Draft a short announcement of our new lawn-care service for existing customers. Use the details below. Keep it friendly, preserve the booking link, and leave out claims we haven't measured.”

The clearer request gives you something specific to review. If the draft misses the mark, point to the sentence or detail that needs changing.

## Two useful habits { #two-habits-that-beat-any-trick }

- **Give an example.** Share a paragraph you like and explain what to borrow from it: the short sentences, the level of detail, or the way it addresses the reader.
- **Ask for help defining the job.** If you aren't sure what you need, say: “Ask me the questions you need to turn this into a clear brief.”

## When the AI can take actions

Tool access changes what a request can do. “Clean up this folder” could mean suggesting filenames, editing files, or moving them. Say which you want.

```text title="An agent task with clear limits"
Review the files in [folder] and propose a clearer naming scheme.
Show the old name and proposed name for each file.
Do not rename, move, or delete anything yet.
```

For a task you want completed, state what the agent may change and how it should check the result. Keep sending, publishing, purchases, and other consequential actions separate when you want a review first.

## Go deeper

- [Prompt builder](prompt-builder.md): turn a rough request into a usable brief.
- [Project instructions](system-instructions.md): save preferences that apply to recurring work.
- [Prompt library](prompt-library.md): adapt examples for drafts, research, and agent tasks.

[Next step: The prompt builder](prompt-builder.md){ .md-button }
