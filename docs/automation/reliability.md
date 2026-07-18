# Reliability and error handling

A workflow is not reliable because it succeeded in a demo. It is reliable when normal failures are visible, contained, recoverable, and tested.

## Design for failure from the beginning

Every external step can fail:

- network unavailable;
- credentials expired;
- API changed;
- rate limit reached;
- input malformed;
- model output invalid;
- destination record locked;
- human approval never arrives;
- workflow triggered twice;
- one action succeeds and the next fails.

The design question is not “Will this fail?” It is “What state will the system be in when it fails?”

## Idempotency: prevent duplicate effects

An idempotent workflow can safely receive the same event more than once without creating duplicate external effects.

Use a stable key such as:

```text
source_system + source_record_id + workflow_version + action_type
```

Before creating a record or sending an action, check whether that key was already completed.

Do not use model-generated summaries as duplicate keys. They can vary across runs.

## Retries

Retry only failures that may be temporary.

Reasonable retry candidates:

- network timeout;
- rate limit;
- temporary service unavailable;
- known transient database lock.

Do not blindly retry:

- invalid credentials;
- missing required input;
- schema failure caused by a prompt defect;
- permission denied;
- policy rejection;
- destructive action with unknown completion state.

Use increasing delays and a maximum attempt count.

```text
Attempt 1: immediate
Attempt 2: after 30 seconds
Attempt 3: after 2 minutes
Then: failed-items queue and alert
```

## Timeouts

Set a timeout for every tool and approval step. Without one, a run can remain “in progress” forever.

Record whether the timed-out action may still complete later. Some external requests have an uncertain outcome after a timeout, which means the workflow must check the destination before retrying.

## Structured validation

For machine-consumed output:

1. request a schema;
2. parse it with normal code or platform validation;
3. reject unknown values;
4. confirm evidence fields against the input;
5. route invalid output to repair or review;
6. limit repair attempts;
7. store the original output for debugging without exposing secrets.

Do not let downstream steps “best effort” their way through malformed data.

## AI repair loops

A controlled repair loop can send validation errors back to the model:

```text
Your output failed validation:
- category must be one of billing, technical, access, feedback, other
- summary exceeds 300 characters

Return only a corrected object. Do not change fields that already pass validation.
```

Limit repair to one or two attempts. Repeated failure indicates a specification, input, or model problem that needs review.

## Partial failure and transactions

Suppose a workflow:

1. creates a task;
2. updates a database;
3. sends a message.

If step 2 fails after the task was created, a simple retry may create a second task.

Use one or more of:

- idempotency keys on every external action;
- a state machine recording each completed step;
- compensating actions, such as closing the created task;
- staged drafts followed by one approved commit;
- destination checks before retry;
- a reconciliation job.

## State machine

Use explicit statuses rather than one “done” flag:

```text
RECEIVED
VALIDATING
READY_FOR_AI
AI_COMPLETE
VALIDATION_FAILED
AWAITING_APPROVAL
APPROVED
ACTION_IN_PROGRESS
COMPLETED
FAILED_RETRYABLE
FAILED_REVIEW_REQUIRED
CANCELLED
```

Each transition should have a clear owner and allowed next states.

## Failed-items queue

Store failed work with:

- run ID;
- source reference;
- workflow version;
- current state;
- error category;
- safe error message;
- attempt count;
- completed side effects;
- recommended recovery action;
- owner;
- next review time.

A spreadsheet can be enough for a small workflow. The key is that failure remains visible.

## Alerts that help

Bad alert:

> Automation failed.

Useful alert:

```text
Workflow: Meeting follow-up v3
Run: mtg_2026_07_18_0042
State: VALIDATION_FAILED
Reason: 2 action items have no source timestamp
External actions completed: none
Retry: not automatic
Owner action: review failed item and correct transcript mapping
Link: [run record]
```

Alert on conditions requiring action, not every minor retry.

## Human review as measurable feedback

Capture why a person rejects or edits an output:

- unsupported claim;
- wrong category;
- missing item;
- poor tone;
- formatting problem;
- privacy issue;
- incorrect owner or date;
- source conflict;
- workflow rule changed.

Those labels tell you whether to improve the prompt, input, schema, business rule, or training examples.

## Version everything that changes behavior

Record versions for:

- prompt;
- project instructions;
- workflow logic;
- schema;
- model configuration;
- examples;
- policy files;
- connector or API version where relevant.

Without versions, you cannot explain why identical inputs produced different outcomes.

## Cost controls

- cap input size;
- retrieve only relevant context;
- use deterministic preprocessing;
- set maximum model calls per run;
- use a less costly step for simple classification when appropriate;
- alert on unusual token or runtime growth;
- stop duplicate runs early;
- batch only when failure isolation remains acceptable;
- review whether the automation still saves human time.

## Reliability test matrix

| Test | Expected behavior |
|---|---|
| Duplicate trigger | No duplicate external effect |
| Empty required field | Reject before AI call |
| Instruction-like source content | Treat as data; no scope change |
| Invalid model JSON | Repair within limit or queue for review |
| Expired credentials | Stop; alert owner; no repeated retries |
| Rate limit | Back off and retry within limit |
| Destination timeout | Check destination before retry |
| Human approval absent | Expire to review state; no action |
| Workflow disabled mid-run | Finish or stop according to documented policy |
| External action partially complete | Reconcile using recorded state and idempotency key |

## Launch checklist

- [ ] Normal and failure paths were tested.
- [ ] Duplicate prevention is based on stable data.
- [ ] Every external call has timeout and error handling.
- [ ] Retries are limited and category-specific.
- [ ] Invalid AI output cannot reach action steps.
- [ ] Partial side effects are recorded.
- [ ] Failed items have an owner and location.
- [ ] Alerts contain a safe, actionable diagnosis.
- [ ] A disable switch exists.
- [ ] The workflow, prompt, and schema are versioned.
- [ ] Human corrections are captured as data.
- [ ] A scheduled review date is assigned.
