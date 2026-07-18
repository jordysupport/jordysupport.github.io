# Context and memory

When an AI gives an inconsistent answer, people often blame “memory.” Usually the real problem is that the system did not receive the right information, received too much irrelevant information, or relied on an unclear source of truth.

## Four different things people call memory

### 1. Current context

The information available during this run: messages, selected files, tool results, and instructions. It is limited and can become crowded.

### 2. Conversation history

Previous messages that the product may include in the current context. Long history does not guarantee that every detail is actively considered.

### 3. Saved preferences or product memory

Facts or preferences a product stores between conversations. Behavior, controls, and retention vary by tool.

### 4. External project memory

Files, databases, notes, or records that you control and deliberately retrieve. This is usually the most inspectable and dependable form for serious work.

## Context is not a warehouse

Giving the model every file can reduce quality. Good context is:

- relevant to the current decision;
- trustworthy enough for the claim being made;
- clearly labeled by purpose;
- small enough to inspect;
- organized so conflicts are visible.

A useful pattern is **retrieve, use, cite, discard** rather than permanently stuffing everything into one prompt.

## Establish a source-of-truth hierarchy

Write down what wins when information conflicts.

Example:

```text
1. Approved policy files in context/policies/
2. Current project plan in PROJECT_STATUS.md
3. Confirmed decisions in decisions/
4. Working notes in inbox/
5. Conversation statements
6. Model assumptions
```

The agent should stop when two high-priority sources conflict. It should not choose whichever one is easier.

## A practical project structure

```text
project/
├── AGENT.md                 # durable instructions and boundaries
├── PROJECT_STATUS.md        # current goal, phase, blockers, next actions
├── context/
│   ├── policies/            # stable rules
│   ├── examples/            # approved examples
│   └── references/          # source material
├── inbox/                   # new, unprocessed items
├── work/                    # temporary working files
├── output/                  # deliverables and drafts
├── decisions/               # dated confirmed decisions
└── logs/                    # run records
```

Use only the folders your project needs. The value comes from clear meaning, not a complicated tree.

## What belongs in durable instructions

Keep items that should apply across many runs:

- purpose and audience;
- allowed and forbidden actions;
- source-of-truth order;
- output locations and formats;
- naming conventions;
- quality checks;
- approval requirements;
- known commands or workflows;
- rules learned from repeated corrections.

Do not put temporary task details into permanent instructions. Old goals become invisible traps.

## What belongs in project status

A status file should be short and current:

```markdown
# Project status

Updated: YYYY-MM-DD

## Current goal

## Current phase

## Completed

## In progress

## Blockers

## Confirmed decisions

## Next actions
```

Update it at a clear point, such as the end of an approved work session.

## Use examples as specifications

A strong example often communicates quality better than many adjectives.

Store:

- one approved output;
- one rejected output with an explanation;
- edge cases;
- formatting examples;
- examples of when the agent must ask.

Tell the agent what to learn from the example. Otherwise it may copy surface details that do not matter.

## Summaries lose information

Every summary is a transformation. Important nuance can disappear.

For high-value source material:

- keep the original;
- record where the summary came from;
- separate direct facts from interpretation;
- link claims back to a section or file;
- avoid summarizing a summary repeatedly;
- re-check the original before a high-impact decision.

## Prevent stale memory

Add dates and review rules:

```markdown
Status: approved
Effective: 2026-07-01
Review by: 2026-10-01
Owner: Operations
Supersedes: policy-2026-02.md
```

Ask the agent to flag expired or competing sources rather than silently using them.

## Context-loading strategy

For a large project, use layers:

1. **Always load:** compact instructions and current status.
2. **Load by task:** relevant policy, examples, and current source files.
3. **Retrieve on demand:** archive, past runs, or large references.
4. **Never auto-load:** secrets, unrelated private data, and untrusted external content.

## A memory-maintenance prompt

```text
Review the project memory files without changing them.

Report:
1. duplicated instructions;
2. conflicting rules;
3. statements that appear stale or undated;
4. temporary task details that should be removed from durable instructions;
5. important repeated corrections that are not yet documented;
6. files that should be the source of truth but are not clearly labeled.

For every recommendation, cite the file and heading. Do not rewrite anything until I approve the plan.
```

## The test that matters

A memory system is working when a new supervised session can:

- understand the current goal quickly;
- locate the right source;
- distinguish facts from assumptions;
- follow established rules;
- explain conflicts;
- continue work without relying on a hidden conversation.

If it cannot, improve the project structure before adding more memory technology.
