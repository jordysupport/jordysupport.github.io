---
description: >-
  Learn how scheduled automation differs from an AI agent, choose a useful first workflow, and decide which actions need review.
---

<span class="kicker">Automation</span>

# Automation basics

[Automation](../resources/glossary.md#automation) runs work from a trigger, such as a schedule, a new file, or a button. An AI agent can make decisions and use tools within that work. A scheduled job may use an agent, a fixed set of steps, or both.

A weekly digest is a useful example: the schedule starts the job, the agent reads new notes and drafts a summary, and a check catches missing files before you review it.

## From a task to a recurring workflow { #the-honest-promotion-path }

<div class="path-strip">
  <div><span class="step-no">01</span>Choose a recurring job</div>
  <div><span class="step-no">02</span>Run it with real inputs</div>
  <div><span class="step-no">03</span>Save the instructions</div>
  <div><span class="step-no">04</span>Add checks and limits</div>
  <div><span class="step-no">05</span>Schedule it and review</div>
</div>

We suggest starting with one output you can inspect. Compare several runs with the original material, including a run with a missing or awkward input. That will show which parts need a rule, a better source, or your judgment.

A [playbook](../playbooks/index.md) can hold the recurring instructions. The scheduler, tool permissions, and checks still need to be set up in the app that runs it.

## What's actually worth automating

Look for work that repeats and has a clear result:

- Turn new meeting notes into an action list with links to the originals.
- Gather figures from a known set of reports into a draft summary.
- Label incoming files according to a naming rule.
- Prepare replies from approved customer information.

Ask whether you can tell a good result from a bad one without repeating the whole job yourself. If you can't, keep the work assisted until you have a workable check.

For exact tasks such as adding totals or copying fields, use a fixed rule or ordinary software where possible. Let the AI handle the parts that need interpretation.

## Plan for a failed run { #the-one-design-rule }

Decide what happens if a file is missing, a tool loses access, or a result cannot be verified. The job might stop, save an incomplete draft, or put the item in a review queue.

Make that state visible. A missing output should not look like a successful run.

## Go deeper

- [Plan a workflow](workflow-blueprint.md): define the inputs, permissions, and result.
- [Make it reliable](reliability.md): handle duplicates, partial work, and failures.
- [Ideas to try](ideas.md): choose a first job with a clear review point.

[Next step: Plan a workflow](workflow-blueprint.md){ .md-button }
