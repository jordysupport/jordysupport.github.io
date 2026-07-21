---
description: >-
  Why AI makes things up: hallucination explained in plain English, plus simple habits that catch invented facts, fake sources, and confident guesses.
---

<span class="kicker">How agents work · Hallucination</span>

# Why AI makes things up (and how to catch it)

!!! warning "Draft"
    This page is a draft awaiting review. Remove this banner when it's approved.

Sometimes an AI states something false with total confidence — a fact, a quote, a source that doesn't exist. People call this [**hallucination**](../resources/glossary.md#hallucination). It's not lying, and it's not a glitch you can turn off. It's how the tool works, so the fix is a checking habit, not a setting.

## Why it happens, in plain words

An AI writes by predicting what text should come next, based on patterns it learned. It's very good at producing text that *looks right*. It has no built-in step that asks "is this actually true?"

So when it doesn't know something, it doesn't feel a gap the way you would. The pattern-machine keeps going — and fills the gap with something plausible. Plausible is the problem: wrong answers arrive in the same confident tone as right ones.

## Where it bites hardest

- **Sources and citations.** Invented links, invented titles, real authors attached to papers they never wrote.
- **Numbers and dates.** Close-but-wrong figures that survive a skim.
- **Quotes.** Things a real person plausibly *could* have said, but didn't.
- **Niche details.** The less material exists about a topic, the more the AI fills in.
- **Long jobs.** Late in a big task, with a full [context window](context-memory.md), small inventions creep in.

## How to catch it

- [ ] Click the sources behind anything you'll act on. A source you can't open isn't a source. (More in [answers you can check](../prompting/ai-answers-with-sources.md).)
- [ ] Check names, numbers, and dates against the original material.
- [ ] Ask the same important question a second time, fresh. Two different confident answers means at least one is made up.
- [ ] Tell it up front: "say what you don't know — never invent a source." Banning the guess out loud helps.
- [ ] Keep the [Before you trust it](../playbooks/research-brief.md#before-you-trust-it) checklist from the research playbook for anything that matters.

## What doesn't work

- **Asking "are you sure?"** It will apologize and produce a new confident answer — which may also be wrong.
- **Trusting tone.** Confidence and correctness are unrelated. That's the whole trap.
- **One giant prompt saying "be accurate."** Helpful, not sufficient. Checking is still your job.

## You're done when

You treat every AI answer as a draft until the parts you'll act on are checked — and checking takes you minutes, because you asked for sources up front.

!!! tip "If this helped"
    If this saves you from acting on one made-up fact, it earned its keep. A small tip on Ko-fi keeps every guide here free.
    [Tip on Ko-fi](https://ko-fi.com/support_jordy)

[Next step: get answers with sources you can check](../prompting/ai-answers-with-sources.md){ .md-button }
