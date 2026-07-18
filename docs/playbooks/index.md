# Playbook library

A playbook is more useful than a loose prompt because it includes the sources, steps, output, checks, boundaries, and failure path.

Start manually. Keep the human review step. Automate only after several successful runs.

<div class="grid cards" markdown>

-   **Research brief**

    Turn a question into a source-backed brief that separates facts, source claims, inferences, and unknowns.

    [Open the research playbook](research-brief.md)

-   **Content repurposing**

    Transform one approved source into several drafts without adding unsupported claims.

    [Open the content playbook](content-repurpose.md)

-   **Meeting follow-up**

    Create a reliable summary, decision log, action candidates, and follow-up draft from notes or a transcript.

    [Open the meeting playbook](meeting-follow-up.md)

-   **Knowledge base**

    Turn scattered sources into inspectable notes with metadata, provenance, review status, and retrieval rules.

    [Open the knowledge playbook](knowledge-base.md)

</div>

## How to use a playbook

1. Copy the folder structure or worksheet.
2. Replace the example source with an approved real source.
3. Run the task manually with supervision.
4. Use the quality checklist yourself.
5. Record every correction that applies to future runs.
6. Repeat with varied inputs.
7. Add structured validation.
8. Connect a trigger only after the manual version is dependable.

## Playbook maturity levels

### Level 1: Personal checklist

You follow the steps manually in chat or with files.

### Level 2: Supervised agent

The agent reads a bounded workspace and creates drafts. You approve its plan and review the output.

### Level 3: Structured workflow

Input and output contracts, validations, logs, and failure states are defined.

### Level 4: Connected automation

A trigger starts the workflow, low-risk steps run automatically, and approval protects external or high-impact actions.

### Level 5: Monitored operation

Metrics, feedback labels, versioning, failure queues, cost limits, and scheduled review are in place.

Do not skip levels because a product makes the connection easy.

## Universal run record

Use this with any playbook:

```markdown
# Run record

- Playbook:
- Playbook version:
- Run ID:
- Date:
- Operator:
- Source files or record IDs:
- Prompt/instruction version:
- Actions performed:
- Outputs created:
- Validation results:
- Human corrections:
- External actions:
- Warnings or unresolved questions:
- Final status:
```

## Universal approval rule

The examples stop at drafts by default. Add sending, publishing, updating shared systems, or deleting only when the playbook explicitly defines:

- who can approve;
- what exact preview is shown;
- how approval is recorded;
- what action is permitted;
- how duplicate action is prevented;
- how the action can be reversed or corrected.
