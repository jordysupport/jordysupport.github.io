# The agent loop

An agent is useful because it can do more than produce one response. It can inspect the current state, choose an action, use a tool, examine the result, and continue until a stopping rule is met.

```text
observe → decide → act → verify → continue or stop
```

## 1. Observe

The agent gathers only the context needed for the next decision.

It might:

- list files in a project;
- read a task brief;
- inspect the relevant section of a document;
- check the current status of a command;
- retrieve one record from a system;
- read the result of its previous action.

A weak agent reads everything. A better agent first asks, “What information would change my next action?”

## 2. Decide

The agent compares the observed state with the goal and rules.

A useful internal decision can be expressed without hidden reasoning:

```text
Current state: The source notes are available; no output exists.
Next action: Read the notes and identify required sections.
Reason: The brief requires a structured summary grounded in the notes.
Expected result: A list of supported facts, assumptions, and missing information.
```

You do not need a long explanation of every thought. You need enough visible rationale to review important actions.

## 3. Act

The agent uses a tool. Examples:

- read a file;
- create a draft;
- run a test;
- query a database;
- search an approved source;
- update a low-risk field;
- request human approval.

Tool calls should be narrow. “Write `output/brief.md`” is safer than “clean up the project.”

## 4. Verify

The agent checks the result against an objective signal.

Weak verification:

> The output looks good.

Better verification:

- the file exists at the required path;
- every required heading is present;
- the JSON matches the schema;
- every factual claim has a source reference;
- the test command exits successfully;
- the number of processed items equals the number of inputs;
- no files outside the allowed directory changed.

Verification should use a different signal from generation whenever possible. An agent rereading its own prose is weaker than a schema check, source comparison, test, or human approval.

## 5. Continue or stop

A good agent stops for more reasons than “task complete.”

### Completion conditions

- all required outputs exist;
- quality checks pass;
- no unresolved blocker remains;
- the result is ready for the next approved step.

### Blocked conditions

- a required source is missing;
- instructions conflict;
- the requested action exceeds permissions;
- a tool returns an unclear or irreversible result;
- the agent cannot meet the quality threshold.

### Budget conditions

- maximum number of steps reached;
- time or cost limit reached;
- retry limit reached;
- too many items failed validation.

### Approval conditions

- external communication;
- publishing;
- deletion or overwrite;
- financial action;
- access expansion;
- high-impact record changes.

## Plan before action

For a multi-step or risky task, require a plan first:

```text
Before making changes:
1. inspect the workspace;
2. list the files or systems you expect to use;
3. describe each planned action;
4. identify risks, assumptions, and approval points;
5. wait for approval.
```

A plan is not valuable if it is vague. “I will review and improve the files” does not reveal scope. A useful plan names paths, expected changes, and checks.

## Make the loop observable

Ask the system to leave a compact run record:

```markdown
# Run record

- Task ID:
- Started:
- Inputs used:
- Actions taken:
- Files or records changed:
- Validation performed:
- Warnings or assumptions:
- Result:
- Human approval required:
```

For automation, store structured logs rather than relying only on natural-language summaries.

## Avoid endless loops

Agents can repeat the same failing action. Add explicit limits:

```text
- Retry a failed tool at most 2 times.
- Do not repeat an action without changing the approach.
- After 2 failed validations, stop and report the evidence.
- Never broaden permissions as a recovery strategy.
- If the next step is uncertain, ask one focused question.
```

## Separate planning, execution, and review

For important tasks, use three phases:

### Phase A: Plan

Identify sources, actions, risks, and checks. No changes.

### Phase B: Execute

Perform only the approved actions. Record changes.

### Phase C: Review

Compare outputs against the specification. Report failures honestly. Do not silently “fix” beyond the approved scope.

This separation makes supervision easier and reduces accidental scope creep.

## Example loop: document comparison

**Goal:** Compare three vendor proposals against five requirements.

1. Observe: confirm three files and the requirement list exist.
2. Decide: extract comparable fields from each file.
3. Act: create a structured comparison table.
4. Verify: confirm every vendor has a value or “not stated” for every requirement.
5. Decide: identify contradictions and missing information.
6. Act: create a question list.
7. Verify: link each question to the exact missing field.
8. Stop: report that the comparison is a draft and requires human judgment.

The loop is useful because each action produces evidence for the next decision.

## Loop design worksheet

```text
Goal:
Starting state:

Observation 1:
Decision rule:
Action/tool:
Expected result:
Validation:

Observation 2:
Decision rule:
Action/tool:
Expected result:
Validation:

Completion condition:
Blocked condition:
Approval condition:
Maximum steps/retries:
Run record location:
```
