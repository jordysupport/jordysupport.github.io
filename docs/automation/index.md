# Automation basics

Automation is not “let the AI handle it.” It is a designed process that receives an event or input, performs defined steps, checks the result, and records what happened.

A reliable AI workflow usually looks like:

```text
trigger → collect → normalize → AI task → validate → approve → act → log
                                      ↘ fail safely ↗
```

## Task, workflow, and automation

**Task**
: One piece of work, such as summarizing a transcript.

**Workflow**
: A repeatable sequence, such as receive transcript → extract decisions → review → create tasks.

**Automation**
: A workflow that starts or advances without someone manually performing every step.

Design the task first, then the workflow, then the automation.

## What should be automated

Good candidates are:

- repeated often enough to matter;
- based on recognizable inputs;
- governed by stable rules;
- easy to inspect;
- low-risk or protected by approval;
- valuable even when only part is automated;
- supported by an owner who will maintain it.

Poor candidates are:

- rare tasks with unclear value;
- processes nobody understands;
- decisions that depend on hidden judgment;
- workflows with constantly changing rules;
- actions where one error creates serious harm;
- tasks with no clean source data;
- problems whose real cause is organizational rather than manual effort.

## Automation readiness score

Score each item 0, 1, or 2.

| Question | 0 | 1 | 2 |
|---|---|---|---|
| Is the current process documented? | No | Partly | Yes |
| Are inputs predictable? | Rarely | Usually | Consistently |
| Is the output clearly defined? | No | Somewhat | Yes |
| Can quality be checked? | Subjective only | Mixed | Objective checks exist |
| Are exceptions known? | No | Some | Most common ones are known |
| Is the action reversible? | No | Partly | Yes |
| Is there an owner? | No | Informal | Named owner |
| Can the workflow fail without major harm? | No | With controls | Yes |

- **0–6:** clarify the process before automating.
- **7–11:** automate a supervised draft or one step.
- **12–16:** a broader automation may be reasonable with testing and monitoring.

## Use AI only where it adds value

Deterministic rules are better for:

- exact calculations;
- required-field checks;
- date and number validation;
- routing based on known codes;
- deduplication keys;
- permission checks;
- file naming;
- schema validation;
- hard business rules.

AI is useful for:

- interpreting messy text;
- extracting meaning from varied language;
- classifying ambiguous content;
- drafting from evidence;
- summarizing;
- suggesting options;
- handling known language variation.

A strong workflow combines both.

## Build the manual version first

Before connecting apps, perform the workflow manually five times.

Record:

- real input examples;
- the exact output;
- every judgment call;
- exceptions;
- time spent per step;
- errors you caught;
- what required approval;
- what information was missing.

This becomes the automation specification and test set.

## The first useful automation

A safe first automation often stops at a draft:

```text
new input → extract fields → validate → create draft → notify human
```

Examples:

- new meeting transcript → draft summary and action table;
- new form response → classify request and draft response;
- new article → draft social variations;
- new support message → suggest category and next diagnostic question;
- new research item → extract metadata and draft a note.

The human remains responsible for sending, publishing, accepting, or rejecting.

## Cost and volume

Estimate cost before scheduling:

```text
monthly runs × average model calls per run × average input/output size
```

Also include:

- retries;
- duplicate triggers;
- large or malformed inputs;
- premium connectors;
- storage;
- monitoring;
- human review time;
- maintenance when an API changes.

A workflow that saves two minutes but creates ten minutes of review is not automated value.

## Ownership

Every automation needs:

- a business owner who defines correct behavior;
- a technical or operational owner who can inspect failures;
- a documented disable switch;
- a review schedule;
- a place for logs and failed items;
- a policy for stale credentials and departed users.

“AI built it” is not ownership.

## Start with the blueprint

Use the [Workflow Blueprint](workflow-blueprint.md), then add [Reliability and Error Handling](reliability.md). Browse [Automation Ideas](ideas.md) for projects sized by difficulty.
