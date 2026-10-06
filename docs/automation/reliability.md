---
description: >-
  Make AI workflows easier to trust with input checks, bounded retries, duplicate protection, clear run records, and a tested pause control.
---

<span class="kicker">Automation · Reliability</span>

# Make it reliable

A workflow needs to handle the cases you expect and the ones that interrupt it. We start by deciding what counts as a complete result and what should happen when that result cannot be produced.

## The checklist

- **Check the input.** Confirm the required files or fields exist and cover the right period. Stop or flag incomplete material before producing an apparently complete report.
- **Check the output.** Check format separately from accuracy. A well-formed table can still contain invented figures or incorrect totals.
- **Bound retries.** Retry a temporary read failure a limited number of times. A bad source file needs a correction, not endless attempts.
- **Track completed items.** Give each input or run an identifier. Check it before repeating work, especially before sending or changing anything.
- **Save intermediate work.** Record which steps finished so an interrupted run can resume without repeating completed actions.
- **Make failure visible.** Show the affected item, the failed step, and what needs attention. Track the last successful run as well as individual errors.

## Be careful with an uncertain result

A tool can time out after an action succeeds. For example, an email may have been sent even though the workflow didn't receive a confirmation.

Before retrying an action that sends, pays, deletes, or changes a record, check the destination or activity history. If the result is still uncertain, hold the item for review. A retry can create a second action.

## Logs, minus the jargon

A log records what happened: when the run started, which inputs it used, which checks passed, and where it saved the output. It should distinguish a prepared draft from a delivered message.

A useful record might read:

```text title="Sample run record"
Run: weekly-digest-2026-10-02
Inputs: 6 meeting notes
Result: Draft saved to the review folder
Checks: All 8 action items link to source notes
Gaps: 2 action items have no owner in the original notes
Delivery: Waiting for approval
```

Keep the record useful without copying passwords, access tokens, or unnecessary private content into it.

## Decide what can run unattended { #the-maturity-rule }

Start with reviewable outputs. Try empty inputs, duplicate files, lost tool access, and a stopped run. Confirm the checks catch the problems and the pause control works.

Use the results of those tests to decide which steps can run unattended. A clean run history helps, but it does not by itself justify broader permissions. Keep a person at the point where an error would have a serious cost.

[Ideas to try](ideas.md){ .md-button .md-button--primary }
