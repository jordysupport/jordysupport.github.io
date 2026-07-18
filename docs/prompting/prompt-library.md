# Copy-paste prompt library

These templates are starting points. Replace bracketed text, remove irrelevant sections, and never paste secrets or unapproved private data.

## Explain an error to a beginner

```text
Explain the error below to someone who is not technical.

ERROR
[paste the complete error and the command that produced it]

ENVIRONMENT
- Operating system:
- Tool and version:
- Current folder:
- What I expected:
- What changed recently:

Return:
1. a plain-language explanation;
2. the most likely cause and the evidence for it;
3. the safest single diagnostic command;
4. what result I should expect;
5. the next step for each likely result;
6. how to undo any proposed change.

Do not recommend reinstalling everything unless the evidence supports it. Do not hide risk behind “just run this.”
```

## Turn a goal into an agent plan

```text
Convert this goal into a bounded agent task:
[goal]

Return:
- objective;
- approved inputs;
- required outputs;
- allowed tools;
- allowed changes;
- forbidden actions;
- assumptions to confirm;
- step-by-step plan;
- validation checks;
- approval gates;
- stop conditions;
- run-log fields.

Prefer the smallest useful scope. Do not propose full autonomy when a supervised draft workflow is enough.
```

## Audit a project folder

```text
Inspect this project in read-only mode.

Goal: explain what the project contains, how it appears to work, and what requires attention.

Report:
1. a concise directory map;
2. the likely purpose of important files;
3. documented build, test, or run commands;
4. missing or conflicting instructions;
5. sensitive-looking files that should not be committed—name paths only, never print secret values;
6. broken internal references or obvious stale files;
7. the five highest-value cleanup actions.

Cite paths for every finding. Do not modify, install, run, or delete anything.
```

## Summarize without losing accountability

```text
Summarize the supplied material for [audience and decision].

Separate the output into:
- confirmed facts;
- decisions already made;
- action items with owner and due date exactly as stated;
- risks or disagreements;
- unresolved questions;
- information that was not stated.

After each important item, cite the source filename and section or timestamp. Do not assign an owner or deadline that the source does not provide.
```

## Compare options

```text
Compare [options] for [decision and audience].

Use only [approved sources]. Evaluate each option against these criteria:
[criteria]

Return:
1. a comparison table with one row per criterion;
2. evidence and source for each rating;
3. missing information;
4. tradeoffs that could reverse the decision;
5. a conditional recommendation in the form “Choose A when..., choose B when...”;
6. questions to resolve before committing.

Do not create a winner from unsupported assumptions. Use “not stated” where evidence is missing.
```

## Extract action items

```text
Extract action items from the supplied notes or transcript.

For each item return:
- action;
- owner exactly as stated;
- due date exactly as stated;
- status if stated;
- source quote or timestamp;
- confidence: Confirmed / Inferred / Unclear.

Do not convert suggestions, hypotheticals, or discussion topics into commitments. Put ambiguous candidates in a separate “Needs confirmation” table.
```

## Create a standard operating procedure

```text
Turn the supplied process notes into a beginner-friendly SOP.

Required sections:
1. purpose;
2. when to use this process;
3. prerequisites and access needed;
4. numbered steps, one primary action per step;
5. expected result after each major step;
6. common failure signs and recovery;
7. safety or approval points;
8. completion checklist;
9. source gaps that must be confirmed.

Preserve required warnings. Do not invent product behavior. Define technical terms at first use.
```

## Research brief

```text
Create a research brief on [question] for [audience and decision].

Scope:
- Time period:
- Geography:
- Approved source types:
- Excluded source types:
- Maximum age for time-sensitive claims:

Method:
1. write the subquestions before researching;
2. gather evidence from primary sources first;
3. record source, publication date, event date, and access date;
4. distinguish fact, source claim, and inference;
5. surface disagreement and missing data.

Output:
- executive summary;
- key findings with citations;
- evidence table;
- conflicting views or uncertainty;
- implications;
- next questions;
- complete source list.

Do not cite a source you did not inspect. Do not use a search-result snippet as evidence when the underlying source is available.
```

## Quality-control an output

```text
Audit the draft against the specification and source material. Do not rewrite it yet.

Check:
- every required section;
- factual support;
- invented names, dates, links, prices, or commitments;
- internal contradictions;
- unclear assumptions;
- audience and tone;
- formatting and length limits;
- safety, privacy, or permission issues;
- whether the claimed completion checks were actually performed.

Return a table:
Severity | Location | Issue | Evidence | Required fix

Then provide:
- requirements fully met;
- requirements partially met;
- requirements not met;
- recommendation: approve / revise / block.
```

## Transform one source into multiple formats

```text
Use [source] as the only factual source. Create drafts for:
[list formats]

For each format specify:
- audience;
- objective;
- length;
- structure;
- call to action;
- prohibited claims;
- required source references.

Preserve the source meaning. Do not add statistics, quotes, testimonials, urgency, or promises that are not supported. End with a cross-format consistency check listing the core claims used in every draft.
```

## Design an automation before building it

```text
Design a reliable workflow for:
[process]

Return:
1. trigger;
2. input schema and source;
3. deterministic preprocessing;
4. exact AI task;
5. required structured output;
6. validation rules;
7. human approval points;
8. allowed external actions;
9. duplicate prevention;
10. retries, timeout, and failure queue;
11. logs, alerts, and metrics;
12. data retention and secret handling;
13. test cases including missing, conflicting, malicious, and duplicate inputs;
14. a manual version to run before automation.

Flag any step where AI is unnecessary or a deterministic rule would be safer.
```

## Ask for a minimal change

```text
Make the smallest change that satisfies this request:
[request]

Before editing:
- identify the exact files and sections involved;
- explain why each file must change;
- identify tests or checks;
- wait for approval.

During editing:
- preserve unrelated content and formatting;
- do not rename, reorganize, upgrade, or “clean up” outside the request;
- do not add dependencies unless approved.

After editing:
- show a concise diff summary;
- run the documented checks;
- report anything not verified.
```
