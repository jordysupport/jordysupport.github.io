---
description: >-
  Plan an AI workflow with seven practical decisions: trigger, input, work, checks, approval, delivery, and failure handling.
---

<span class="kicker">Automation · Blueprint</span>

# Plan a workflow

Write a short brief before you connect tools or set a schedule. It should explain what the workflow produces, what it can access, and how you will know whether it worked.

## The seven boxes

1. **Trigger:** What starts the job? A schedule, a new item, or your request?
2. **Input:** Which files or records does it use? How will it recognize missing, old, or incomplete material?
3. **AI step:** What judgment does the agent make? Which tools may it use?
4. **Check:** What must be true before the result is accepted?
5. **Approval:** Which actions may happen automatically, and which wait for you?
6. **Delivery:** Where does the output go? What confirms it arrived?
7. **Failure plan:** What stops the job, what is saved, and who needs to know?

You can answer in a few lines. If an answer is uncertain, test that part before relying on the workflow.

## Worked example: weekly meeting digest

This sample workflow produces a reviewable summary rather than sending messages on its own.

| Decision | Example |
| --- | --- |
| Trigger | Friday afternoon, after the week's notes are saved. |
| Input | Files dated this week in the meeting-notes folder. List the files read. |
| AI step | Extract decisions and action items. Use read access to this folder and write access to the draft folder. |
| Check | Each action links to its source note. Owners and dates match the notes; missing details are flagged. |
| Approval | Save the digest for review. Sending to the team requires approval. |
| Delivery | Write one dated draft in the review folder and confirm that the file exists. |
| Failure plan | If any expected file cannot be read, mark the digest incomplete and list the gaps. Hold delivery to the team. |

## Set limits before the first run { #the-order-matters }

Choose a maximum amount of work per run, such as ten files or one draft. Set a time or spending limit where your tool supports it, and identify the control that pauses the schedule.

Decide how a rerun works. If Friday's job is interrupted, should it replace the draft, resume from a checkpoint, or start fresh? It should be able to recognize the work it has already completed.

## Copy the brief

```text title="Workflow brief"
Result: [one concrete output]
Trigger: [when or how it starts]
Inputs: [sources and selection rules]
Tools and permissions: [what it may access or change]
Checks: [facts, totals, fields, or links to verify]
Approval: [where it waits for a person]
Destination: [where the output is saved or delivered]
Failure handling: [when to stop and what to report]
Limits and pause control: [how to bound or stop a run]
Rerun behavior: [how to avoid duplicate work or actions]
```

[Make it reliable](reliability.md){ .md-button .md-button--primary }
