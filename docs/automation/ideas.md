# Automation ideas

Choose an idea because it removes a real bottleneck, not because the demo looks futuristic. Each idea below includes a safe first version.

## Beginner: draft and review

### Meeting follow-up draft

**Input:** transcript or notes.

**Output:** summary, decisions, action candidates, questions, and email draft.

**Safe first version:** create files only; a person confirms owners and dates. [Use the playbook](../playbooks/meeting-follow-up.md).

### Support-request triage

**Input:** copied request text.

**Output:** category, short summary, missing diagnostic information, and suggested next question.

**Safe first version:** no customer response and no account access.

### Research-note formatter

**Input:** one approved article or report.

**Output:** source metadata, key claims, evidence, limitations, and reusable note.

**Safe first version:** process one source at a time and require exact source references.

### Content repurposing drafts

**Input:** one approved source piece.

**Output:** several platform-specific drafts with a claim-consistency table.

**Safe first version:** no publishing. [Use the playbook](../playbooks/content-repurpose.md).

### SOP generator

**Input:** messy process notes plus screenshots or examples.

**Output:** beginner-friendly procedure, warnings, expected results, and open questions.

**Safe first version:** label anything not supported rather than filling gaps.

### File intake report

**Input:** copies of files in a review folder.

**Output:** inventory, likely duplicates, missing metadata, and proposed organization.

**Safe first version:** do not move, rename, or delete originals.

### Form-response summary

**Input:** exported responses.

**Output:** themes, counts from deterministic calculations, representative examples, and unresolved needs.

**Safe first version:** remove unnecessary personal details before the model step.

### Weekly project digest

**Input:** approved status files or task export.

**Output:** progress, blockers, decisions needed, overdue items, and next week’s focus.

**Safe first version:** drafts only; source links on every item.

## Intermediate: connected workflows

### Knowledge inbox

**Trigger:** new item in a designated folder.

**Workflow:** validate file → extract metadata → draft note → human review → move to approved library.

**Controls:** file-type allowlist, duplicate key, source preservation. [Use the playbook](../playbooks/knowledge-base.md).

### Lead-research packet

**Trigger:** approved company name and domain.

**Workflow:** gather approved public sources → extract facts → identify uncertainty → create a meeting brief.

**Controls:** no personal-data enrichment, no outreach, current-date checks, source citations.

### Proposal requirement checker

**Trigger:** proposal moved to “review.”

**Workflow:** compare draft against requirement checklist → flag missing items → create review report.

**Controls:** no automatic submission; deterministic requirement list; versioned draft.

### Content approval queue

**Trigger:** approved source added.

**Workflow:** create multiple drafts → validate links and prohibited claims → place in approval board.

**Controls:** publication tools unavailable until approval state is recorded.

### Invoice or receipt extraction

**Trigger:** document added to intake folder.

**Workflow:** extract fields → deterministic format checks → compare totals → queue exceptions.

**Controls:** no payment, no ledger posting until validated; sensitive retention policy.

### Internal policy Q&A

**Trigger:** employee question.

**Workflow:** retrieve approved policy sections → draft answer with citations → route unclear cases to owner.

**Controls:** answer only from approved current documents; expose review dates and conflicts.

### Product-feedback router

**Trigger:** new feedback record.

**Workflow:** redact unnecessary personal data → classify theme → link possible duplicates → create internal summary.

**Controls:** model does not decide roadmap priority; human owns merge and priority.

### Job-candidate scheduling assistant

**Trigger:** recruiter-approved candidate state.

**Workflow:** identify allowed windows → create a proposed scheduling message → wait for approval.

**Controls:** no candidate evaluation, no autonomous sending, no calendar changes without approval.

## Advanced: multi-step systems

### Research monitoring workflow

**Trigger:** schedule.

**Workflow:** check approved sources → identify new items → deduplicate → extract claims → compare with prior brief → notify reviewer.

**Controls:** source allowlist, event date versus publication date, no automatic strategic decision.

### Incident-summary assistant

**Trigger:** incident channel or ticket enters review state.

**Workflow:** collect approved logs and notes → create timeline → separate facts from hypotheses → draft follow-up questions.

**Controls:** read-only source access, secret redaction, no public communication, human incident owner.

### Contract-obligation tracker

**Trigger:** approved contract copy added.

**Workflow:** extract candidate obligations and dates → cite clauses → legal/owner review → create tracked items.

**Controls:** never present extraction as legal advice; no automatic acceptance or calendar commitments.

### Catalog enrichment

**Trigger:** new product record with approved source data.

**Workflow:** normalize deterministic fields → draft descriptions and tags → validate prohibited claims → approval queue.

**Controls:** factual claims limited to approved data; batch and cost limits; rollback by record version.

### Data-quality investigator

**Trigger:** anomaly rule fires.

**Workflow:** gather relevant rows and metadata → propose likely causes → run approved read-only queries → create investigation report.

**Controls:** no database writes; query limits; sensitive data minimization.

### Multi-stage publishing pipeline

**Trigger:** source reaches approved state.

**Workflow:** research check → draft → fact audit → style review → legal/policy check → human approval → scheduled publish.

**Controls:** separate stages and identities; no model self-approval; immutable source package.

## Idea scoring card

For any idea, answer:

```text
Pain removed:
Current time per run:
Runs per month:
Error cost:
Approved inputs:
Required output:
Objective checks:
Human judgment that remains:
Safest first version:
External actions:
Rollback:
Owner:
Estimated monthly cost:
Review date:
```

Prioritize the idea with clear inputs, measurable output, frequent repetition, reversible actions, and a responsible owner—not the idea with the most agents.
