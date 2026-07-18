# Agentic AI basics

“AI agent” is used for everything from a chatbot with one button to software that can work for hours. Ignore the label and inspect the actual system.

A practical agent has six parts:

1. **A goal** — the job it is trying to complete.
2. **Context** — the information available for this run.
3. **Instructions** — rules, priorities, and boundaries.
4. **Tools** — ways to read, calculate, search, edit, or act.
5. **A loop** — observe, decide, act, and check.
6. **A stop condition** — done, blocked, budget reached, or approval required.

## Model, assistant, agent, workflow

| Term | Useful definition | Example |
|---|---|---|
| Model | The language or reasoning engine | Generates a proposed answer from the available context |
| Assistant | A user-facing product around a model | Chat interface with files, memory, or browsing |
| Agent | A model allowed to choose and use tools within a loop | Reads a folder, edits a draft, runs a check, and reports |
| Workflow | A designed sequence of steps and decisions | Trigger → extract → validate → approve → deliver |
| Automation | A workflow that starts or continues without a person manually performing every step | New form submission launches the workflow |

An agent may be one step inside a workflow. A workflow may use no AI at all. Keeping those ideas separate makes systems easier to design.

## The capability ladder

Do not jump straight to “fully autonomous.” Add one capability at a time.

### 1. Generate

The model creates text from a prompt.

### 2. Ground

The model uses supplied documents, examples, or data.

### 3. Structure

The output follows a schema, checklist, or template.

### 4. Use tools

The model can search, calculate, read files, or call a service.

### 5. Change state

The agent can edit files, update a record, create a task, or send a draft.

### 6. Continue over multiple steps

The system can inspect results, recover, and decide the next action.

### 7. Run from a trigger

The process begins on a schedule or event.

Every step adds value **and** failure modes. Add the next level only when the previous level is reliable.

## Autonomy is a dial

You can design different approval levels:

| Level | Agent behavior | Good use |
|---|---|---|
| Suggest | Recommends an action; human performs it | New or high-risk tasks |
| Draft | Creates a reversible draft | Emails, documents, plans, code changes |
| Act with approval | Prepares an action and waits | Publishing, payments, external updates |
| Act within policy | Performs low-risk actions inside strict rules | Sorting, tagging, internal summaries |
| Act and monitor | Runs independently with logs, limits, and alerts | Mature, tested workflows |

A system is not less “agentic” because it asks for approval. Approval is part of good control design.

## What agents are good at

- transforming messy information into a defined structure;
- searching a bounded source set;
- drafting and revising against a checklist;
- applying consistent rules across many similar items;
- coordinating file and command operations inside a project;
- suggesting decisions when uncertainty is visible;
- handling routine exceptions that were anticipated in advance.

## What agents are bad at

- knowing unstated business rules;
- recognizing every high-impact edge case;
- proving a claim merely because it sounds confident;
- safely operating with unlimited permissions;
- deciding what “good” means without examples or tests;
- recovering from every external-service failure;
- replacing accountable human judgment in sensitive decisions.

## The minimum useful agent specification

Before giving an agent tools, write these seven lines:

```text
Goal:
Inputs:
Allowed tools:
Allowed changes:
Forbidden actions:
Definition of done:
Stop and ask when:
```

Example:

```text
Goal: Turn approved meeting notes into a draft follow-up email and task list.
Inputs: One transcript and our project-owner list.
Allowed tools: Read the project folder; create files in drafts/.
Allowed changes: New Markdown drafts only.
Forbidden actions: No sending email, changing calendars, or inventing deadlines.
Definition of done: Email draft, action table, open questions, and source references.
Stop and ask when: An owner or deadline is unclear, or the transcript contains conflicting decisions.
```

## A healthy design test

Ask three questions:

1. **Can I explain what the agent can access?**
2. **Can I verify what it did?**
3. **Can I recover from a bad result?**

If any answer is no, reduce scope before increasing capability.

## Continue

- [Understand the agent loop](agent-loop.md)
- [Organize context and memory](context-memory.md)
- [Connect tools and understand MCP](tools-mcp.md)
- [Design permissions and safety controls](safety-permissions.md)
