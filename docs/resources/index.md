# Resource hub

This page collects the compact worksheets and checklists used across the site.

## One-page AI project brief

```text
PROJECT:
OWNER:
REVIEW DATE:

PROBLEM
What repeated problem are we solving?

USER AND OUTCOME
Who benefits, and what changes when this works?

MANUAL PROCESS
What are the current steps, judgments, and exceptions?

APPROVED INPUTS
What sources may be used? Who owns them? How sensitive are they?

REQUIRED OUTPUT
What exact file, fields, or action is needed?

AI'S JOB
What interpretation or generation requires AI?

NON-AI RULES
What validation, calculation, routing, or policy should be deterministic?

ALLOWED ACCESS
What may be read? What may be created or changed?

FORBIDDEN ACTIONS
What may never happen without separate approval?

QUALITY CHECKS
How will correctness be tested?

HUMAN APPROVAL
Who reviews what exact preview before which action?

FAILURE PATH
Where do failed items go? Who is alerted? How is a run retried safely?

SUCCESS METRICS
Quality, time saved, correction rate, failure rate, and cost.

SAFEST FIRST VERSION
What draft-only or read-only version can we test this week?
```

## Agent preflight

- [ ] The goal and definition of done are written.
- [ ] The agent starts in the intended folder or account.
- [ ] Approved inputs are present and source priority is clear.
- [ ] Untrusted content cannot redefine the task.
- [ ] Read access is narrower than the full system.
- [ ] Writes are limited to drafts or a test area.
- [ ] Sending, publishing, deletion, spending, and permission changes require approval.
- [ ] Secrets are stored outside prompts and files.
- [ ] Objective validation exists.
- [ ] Step, retry, time, and cost limits exist.
- [ ] Changes and tool actions will be logged.
- [ ] Recovery or rollback is possible.

## Prompt checklist

- [ ] Action and object are specific.
- [ ] Audience and downstream purpose are stated.
- [ ] Approved sources are named.
- [ ] Required output shape is explicit.
- [ ] Allowed and forbidden actions are listed.
- [ ] Missing information must remain unknown.
- [ ] Quality checks are testable.
- [ ] Stop and approval conditions are visible.
- [ ] An example is provided when style or structure matters.
- [ ] The final response must disclose unmet requirements.

## Workflow checklist

- [ ] Trigger behavior and duplicate risk are known.
- [ ] Input fields, types, limits, and sensitivity are defined.
- [ ] Deterministic preprocessing happens before AI.
- [ ] The AI step has one bounded job.
- [ ] Output is validated before action.
- [ ] Decision rules are written outside the model when practical.
- [ ] External actions are narrow and traceable.
- [ ] Idempotency prevents duplicate effects.
- [ ] Retries are limited to temporary failures.
- [ ] Partial success is recorded.
- [ ] Failed items remain visible.
- [ ] Alerts tell an owner what to do.
- [ ] Prompt, schema, and workflow versions are logged.
- [ ] A disable switch and review date exist.

## Output audit

Use this review order:

1. **Scope:** Did it do only the requested job?
2. **Completeness:** Is every required section or field present?
3. **Grounding:** Can important claims be traced to approved evidence?
4. **Accuracy:** Does the wording overstate or distort the source?
5. **Uncertainty:** Are assumptions and unknowns visible?
6. **Safety:** Did it expose data or propose unapproved actions?
7. **Format:** Can the next person or system use the result?
8. **Change record:** Are all edited files or external effects listed?
9. **Validation:** Were the claimed checks actually performed?
10. **Next action:** Is ownership clear?

## Troubleshooting intake

```text
Goal:
Exact command/action:
Exact error:
Environment:
Tool/version:
Current folder:
Expected result:
Actual result:
Last known success:
Recent change:
Diagnostics and output:
Sensitive details removed:
```

## Project folder starter

```text
project/
├── AGENT.md
├── PROJECT_STATUS.md
├── input/
├── context/
│   ├── policies/
│   ├── examples/
│   └── references/
├── work/
├── output/
└── logs/
```

Start smaller. Add a folder only when its meaning is clear.

## Recommended next reads

<div class="grid cards" markdown>

-   **Building an agent memory vault?**

    [Use the Obsidian vault guide](../fundamentals/obsidian-vaults.md)

-   **Coordinating specialist agents?**

    [Learn automatic and explicit subagents](../fundamentals/subagents.md)

-   **Need terminology?**

    [Open the glossary](glossary.md)

-   **Need official documentation?**

    [Open the learning links](learning-links.md)

-   **Need a complete process?**

    [Open the playbook library](../playbooks/index.md)

-   **Need help with a failure?**

    [Use the troubleshooting checklist](../troubleshooting/index.md)

</div>

## Community reference

This site grew partly from helping people who discovered agentic workflows through online creator communities. [Jared Rhod's official website](https://jaredrhod.com/) is linked here as one such resource. His material remains his; Jordy Support does not reproduce it or present itself as his official support site.

## Support Jordy Support

The guides are free to read. Optional support: [Ko-fi](https://ko-fi.com/support_jordy) · [Linktree](https://linktr.ee/jordy_support) · [GitHub](https://github.com/jordysupport)
