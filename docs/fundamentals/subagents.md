# Subagents: automatic and explicit delegation

A subagent is a specialized worker that handles a bounded part of a larger task and returns its findings to the main agent. It usually has its own instructions, context, tools, and permissions.

Use subagents to divide work by **responsibility**, not merely to make the system look more advanced.

!!! warning "Product behavior varies"
    “Subagent” is not implemented identically across AI products. The general design guidance on this page applies broadly. Commands, file locations, and invocation examples labeled **Claude Code** are specific to Claude Code and may change with versions.

## Main agent versus subagent

| Main agent | Subagent |
|---|---|
| Owns the overall task and conversation | Owns one delegated responsibility |
| Combines findings and makes the final report | Returns a focused result |
| Often has broader project context | Usually starts with a smaller, isolated context |
| Decides what happens next | Stops when its assigned task is complete or blocked |
| Should manage approvals and conflicts | Should stay within its own tool and permission limits |

Example:

```text
Main agent: Maintain this Obsidian vault safely.

Subagent 1: Audit note structure without editing.
Subagent 2: Check source support for factual claims.
Subagent 3: Suggest useful internal links.
Main agent: Combine the reports, remove duplicates, present one approved change plan.
```

## Why use a subagent

A subagent is useful when the work is:

- self-contained;
- specialized;
- noisy or likely to produce large search results;
- safe to summarize back to the main agent;
- easier to control with narrower tools;
- independent enough to run beside another task;
- repeated often enough to deserve reusable instructions.

Good examples:

- inspect a folder and return a map;
- review notes for unsupported claims;
- run tests and report only failures;
- compare naming conventions;
- search for duplicate notes;
- audit links without changing them;
- check a draft against a style guide.

Keep the task in the main conversation when it needs frequent clarification, shares a lot of context with the rest of the work, or is only one small change.

## How automatic delegation works

In systems that support it, the main agent can decide that part of your request matches a known subagent.

A simplified loop is:

```text
Your request
    ↓
Main agent identifies a bounded specialist task
    ↓
It compares the task with available subagent descriptions
    ↓
It sends a focused task to the selected subagent
    ↓
The subagent works in its own context and returns a result
    ↓
The main agent evaluates and combines that result
```

Automatic delegation depends heavily on the subagent's **description**. A vague description makes selection unpredictable.

Weak:

```yaml
description: Helps with notes.
```

Better:

```yaml
description: Read-only auditor for Obsidian vaults. Use proactively when the user asks about duplicates, stale notes, inconsistent properties, unresolved links, or vault organization. Return evidence and a change plan; never edit files.
```

The better description tells the main agent:

- the domain;
- the trigger conditions;
- whether to use it proactively;
- the expected output;
- the safety boundary.

### Automatic does not mean invisible permission

A delegated worker should not gain broader access merely because the main agent selected it. Design the subagent with the narrowest tools it needs and keep high-impact actions behind human approval.

## Ask for a subagent in plain language

The most portable method is to request the role and result directly.

```text
Use a read-only vault-auditor subagent to inspect `00 Inbox/` for duplicates and stale notes. Return evidence and proposed actions. Do not edit anything.
```

```text
Have separate subagents review the research sources, note structure, and internal links. They must not edit files. Combine their findings into one prioritized report and show disagreements.
```

```text
Delegate the source-verification step to a specialist subagent. It should cite the exact note and heading for every unsupported claim.
```

Naming a subagent in natural language strongly signals what you want, but some products still let the main agent decide whether delegation is appropriate.

## Claude Code: three ways to request a subagent

Claude Code currently supports three escalating patterns.

### 1. Natural-language request

```text
Use the vault-auditor subagent to review this vault before proposing changes.
```

Claude normally delegates when the task and subagent description match, but the main agent still makes the choice.

### 2. `@`-mention for one task

In Claude Code, type `@` and choose the agent from the suggestion list.

```text
@"vault-auditor (agent)" inspect `10 Projects/` for stale status notes. Do not edit files.
```

An agent `@`-mention selects that specific subagent for the task. Your complete message still defines the work it receives.

### 3. Run the entire session as one agent

```bash
claude --agent vault-auditor
```

This starts the session using that agent's prompt, tool limits, and model configuration. Use this when the whole session should stay in one specialized role, not merely for a single delegated check.

!!! tip
    Look at the Claude Code startup header and current official documentation to confirm which agent is active. Product behavior changes; do not rely on an old screenshot or tutorial.

## Create a project-specific Claude Code subagent

Project subagents live in:

```text
.claude/agents/
```

Personal subagents available across projects live in:

```text
~/.claude/agents/
```

A subagent is a Markdown file with YAML frontmatter followed by its instructions.

### Read-only vault auditor

Create `.claude/agents/vault-auditor.md`:

```markdown
---
name: vault-auditor
description: Read-only auditor for Obsidian vaults. Use proactively for duplicate notes, stale project status, inconsistent properties, unresolved links, unclear folder placement, and instruction conflicts. Never edit files.
tools: Read, Grep, Glob
model: sonnet
---

You audit Obsidian vaults without making changes.

Before working:
1. read `VAULT-GUIDE.md` if it exists;
2. identify the exact folder scope;
3. stop if the request requires writing, moving, renaming, deleting, or changing `.obsidian/`.

For every finding, report:
- severity: high, medium, or low;
- evidence: file and heading;
- why it matters;
- smallest recommended action;
- files that would be affected;
- uncertainty or possible false positives.

Prioritize findings that improve retrieval, source trust, or recovery.
Return no more than 20 findings unless the user asks for a complete inventory.
Never invent note content, ownership, dates, or destinations.
```

Why this is safe:

- it has read/search tools only;
- its description clearly states when it should be selected;
- its output is evidence plus a proposed action;
- it cannot silently reorganize the vault.

### Source verifier

Create `.claude/agents/source-verifier.md`:

```markdown
---
name: source-verifier
description: Verifies factual claims in vault notes against named source files. Use when a draft needs evidence checking, attribution review, or separation of fact from interpretation. Read-only; never rewrites notes.
tools: Read, Grep, Glob
model: sonnet
---

You verify claims using only the files and source locations supplied in the task.

For each material claim, classify it as:
- supported;
- partially supported;
- unsupported;
- contradicted;
- not verifiable from the supplied sources.

Cite the claim location and supporting or conflicting source location.
Do not use general knowledge to fill gaps.
Do not treat a summary as stronger evidence than its original source.
Do not edit files.
Return the highest-risk problems first.
```

### Link curator

Create `.claude/agents/link-curator.md`:

```markdown
---
name: link-curator
description: Suggests high-value Obsidian internal links when notes have a meaningful evidence, decision, dependency, or context relationship. Use for link audits. Read-only and never inserts links automatically.
tools: Read, Grep, Glob
model: sonnet
---

Suggest links only when they help a reader understand evidence, context, a decision, a dependency, or a sequence.

For every suggestion, provide:
- source file and heading;
- target note;
- relationship type;
- why the link is useful;
- exact suggested placement.

Do not suggest links based only on a shared word or tag.
Do not modify files.
Flag ambiguous filenames and likely duplicates separately.
```

## Ask Claude Code to create the files for you

You can also request them in Claude Code:

```text
Create three project-level subagents in `.claude/agents/`:

1. `vault-auditor`: read-only audit for duplicates, stale notes, properties, links, and instruction conflicts.
2. `source-verifier`: read-only evidence checker using only named source files.
3. `link-curator`: read-only high-value internal-link suggestions.

Use clear descriptions that encourage automatic delegation when relevant. Limit tools to Read, Grep, and Glob. Show me every proposed file before writing it.
```

Review generated frontmatter and instructions. A subagent definition is a permission and behavior policy, not just a clever prompt.

## Make automatic selection more reliable

Use this description formula:

```text
[Role and domain]. Use [automatically/proactively] when [specific trigger conditions]. Produce [specific result]. [Important permission or safety boundary].
```

Example:

```text
Read-only source verifier for research notes. Use proactively when a draft contains factual claims or citations that need checking. Return a claim-evidence table with exact file references. Never edit files or use unlisted sources.
```

Avoid descriptions that:

- overlap several other agents;
- claim universal expertise;
- omit the read/write boundary;
- say only “use when helpful”;
- combine research, editing, publishing, and deletion;
- provide no clear finish condition.

## Give every delegated task a contract

A good subagent name does not replace a good task prompt.

Use:

```text
Subagent:
Goal:
Scope:
Inputs:
Allowed tools:
Forbidden actions:
Required output:
Stop and ask when:
```

Example:

```text
Subagent: vault-auditor
Goal: Identify maintenance issues that block reliable retrieval.
Scope: `10 Projects/Current Project/` only.
Inputs: `VAULT-GUIDE.md`, project notes, and current status files.
Allowed tools: Read and search only.
Forbidden actions: No edits, moves, renames, deletion, or `.obsidian/` access.
Required output: Prioritized table with file evidence and smallest safe fix.
Stop and ask when: Folder rules conflict or the source of truth is unclear.
```

## Use parallel subagents only for independent work

Parallel work is helpful when one result does not depend on another.

Good:

```text
Run three read-only reviews in parallel:
1. structure and naming;
2. source support;
3. links and navigation.

Give each subagent the same folder scope and vault rules. Then combine the reports, remove duplicate findings, and show any disagreement.
```

Poor:

```text
Have one subagent decide the new folder structure while another simultaneously moves the files.
```

The second task depends on the first decision. Run them in sequence with approval between stages.

## Chain subagents safely

For dependent work, use stages:

```text
1. Auditor identifies an issue.
2. Source verifier checks the evidence.
3. Main agent prepares a change plan.
4. Human approves specific files.
5. Main agent or a tightly scoped editor applies the change.
6. Auditor verifies the result.
```

Do not let one subagent's confident report automatically authorize another to make high-impact changes. Agent output is input, not human approval.

## A useful Obsidian maintenance team

| Subagent | Access | Responsibility | Output |
|---|---|---|---|
| `vault-auditor` | Read-only | Structure, duplicates, staleness, rules | Prioritized findings |
| `source-verifier` | Read-only | Claims and attribution | Claim-evidence table |
| `link-curator` | Read-only | Meaningful internal links | Link proposals |
| Main agent | Initially read-only; approved writes only | Combine findings and apply approved edits | Change plan and final report |

Start with read-only specialists. Add a write-capable subagent only after you have stable instructions, backups, change limits, and a review habit.

## When a write-capable subagent is justified

A write-capable specialist can help with highly repetitive, reversible edits such as:

- adding an approved property to a small named set of files;
- creating new drafts in one dedicated folder;
- applying a confirmed template;
- fixing a list of approved typos;
- updating links after an approved rename map.

It should still have:

- an exact folder scope;
- a maximum number of files per run;
- no delete permission;
- no `.obsidian/` changes;
- a required pre-change plan;
- a checkpoint or backup;
- a final changed-file report.

## Common mistakes

### Too many overlapping subagents

If three agents all “help organize notes,” automatic selection becomes unreliable. Split by measurable responsibility.

### Treating delegation as guaranteed quality

A specialist can still misunderstand the task, miss a source, or return a confident error. The main agent must evaluate the result.

### Passing too little context

A subagent that does not receive the vault rules, folder scope, and source files will invent a local interpretation of “organized.”

### Passing the entire vault unnecessarily

Context isolation loses its benefit when every subagent scans everything. Give the smallest useful scope.

### Letting subagents approve each other

Another agent's message is not human authorization. Keep destructive or external actions behind your approval.

### Parallelizing dependent work

Parallel workers can make incompatible assumptions. Use sequential stages when one result changes another task's inputs.

### Ignoring cost and latency

More agents mean more model calls, repeated context loading, and more results for the main agent to evaluate. Use a subagent because it improves control or context—not because the feature exists.

## Prompt library

### Let the main agent choose specialists

```text
Inspect this request and delegate only the self-contained parts that benefit from specialist context.

Before delegating, tell me:
- which subagent you plan to use;
- its exact responsibility;
- its file scope;
- whether it can write;
- what result it must return.

Do not delegate approval decisions or destructive actions.
```

### Require one named subagent

```text
Use the `vault-auditor` subagent for this task.
Scope it to `20 Areas/`.
It must remain read-only and return no more than 15 prioritized findings with file-and-heading evidence.
Do not substitute another agent and do not make edits after it returns.
```

### Parallel read-only audit

```text
Use separate read-only subagents to audit:
1. folder and filename consistency;
2. source support and attribution;
3. internal links and navigation.

All three must read `VAULT-GUIDE.md`, stay within `10 Projects/Active/`, and cite exact files.
After they return, merge duplicate findings and show disagreements. Do not edit files.
```

### Verify an applied change

```text
Use the `vault-auditor` subagent to verify only the files changed in the most recent approved maintenance batch.

Check:
- requested changes were applied;
- unrelated content was not altered;
- links still resolve;
- properties follow the vault standard;
- no file was deleted or moved outside the approved list.

Return pass, fail, or needs-review for each file. Do not fix problems.
```

## How to tell whether delegation helped

After a run, ask:

1. Did the subagent receive a clear, bounded job?
2. Did it stay within the allowed scope?
3. Did its output include evidence rather than conclusions alone?
4. Did it keep noisy exploration out of the main context?
5. Did the main agent evaluate rather than blindly repeat the result?
6. Did delegation reduce risk, confusion, or repetition?
7. Was the extra time and cost justified?

If not, improve the description and task contract—or keep the task in the main conversation.

## Official reference

- [Claude Code: create custom subagents](https://code.claude.com/docs/en/sub-agents)

## Continue

- [Set up an Obsidian vault for agents](obsidian-vaults.md)
- [Organize context and memory](context-memory.md)
- [Design permissions and safety controls](safety-permissions.md)
