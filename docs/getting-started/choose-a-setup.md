# Choose your AI setup

The best setup is the least complicated one that can safely complete the task. Installing more tools does not automatically create more value.

## Five common levels

### Level 1: Chat assistant

**Best for:** brainstorming, explanations, rewriting, small decisions, and one-off drafts.

**Strengths:** fast, simple, no environment setup.

**Limits:** context may be temporary; it cannot reliably manage a project folder or external workflow unless the product provides those tools.

Choose chat when the work can be pasted in, reviewed, and copied out.

### Level 2: Assistant with files or connected sources

**Best for:** summarizing documents, comparing files, answering questions from a collection, and drafting from approved source material.

**Strengths:** more grounded than a blank chat; useful for nontechnical users.

**Limits:** file limits, unclear persistence, and connector permissions vary by product.

Choose this when the task needs documents but not direct file-system changes.

### Level 3: Terminal or editor-based agent

**Best for:** working across many local files, maintaining a knowledge folder, editing a website, running scripts, or assisting with code.

**Strengths:** transparent files, reusable instructions, version control, and command execution.

**Limits:** it can make real changes. Working directory, permissions, Git, and command safety matter.

Choose this when the work lives in a folder and you are willing to supervise changes.

### Level 4: No-code or low-code automation platform

**Best for:** moving structured data between forms, spreadsheets, databases, email, calendars, CRMs, and AI steps.

**Strengths:** visual workflows, triggers, app connectors, schedules, and logs.

**Limits:** costs can grow; error handling is easy to overlook; AI output must be validated before it reaches another app.

Choose this when the value comes from repeatable movement between systems.

### Level 5: Custom coded agent or workflow

**Best for:** product features, high volume, custom interfaces, specialized rules, complex data, or strict testing.

**Strengths:** maximum control, observability, and integration depth.

**Limits:** engineering, security, evaluation, maintenance, and operational costs.

Choose this only when simpler options cannot meet the requirement.

## Decision questions

Work through these in order:

1. **Can a normal chat complete the task?** If yes, stop there.
2. **Does the model need source files?** Use file upload or a connected knowledge source.
3. **Does it need to edit many files or run commands?** Use a terminal/editor agent in a limited folder.
4. **Does the task start from an event or schedule?** Consider an automation platform.
5. **Does it need to serve many users or enforce custom logic?** Consider a coded workflow.

## Data boundary first

Before selecting a product, classify the data.

| Data type | Example | Starting rule |
|---|---|---|
| Public | published articles, public websites | Usually suitable for normal experimentation |
| Internal | draft plans, internal process notes | Use approved tools and limited access |
| Confidential | customer records, private contracts | Confirm policy, retention, and permissions first |
| Regulated or highly sensitive | health, legal, financial, authentication data | Do not experiment casually; involve the responsible owner |

!!! warning "A connector is a permission decision"
    Connecting email, cloud storage, a database, or a project tool gives the AI system a path to real information. Review the exact scopes, not just the product name.

## Local versus cloud

**Local file work** gives you visible folders, Git history, and direct control over copies. It still may send content to a cloud model depending on the tool.

**Cloud app work** is easier to access from anywhere and may simplify collaboration. It also requires you to understand storage, sharing, retention, and connector settings.

The important question is not “local or cloud?” It is:

> Where does the data travel, what is stored, who can access it, and how can I revoke that access?

## Recommended beginner progression

1. Complete the task manually in chat.
2. Turn the successful prompt into a reusable template.
3. Move the work into a dedicated project folder.
4. Let an agent create drafts inside an output folder.
5. Add a checklist or structured output.
6. Add automation only after several supervised runs succeed.

## Setup scorecard

Give each candidate setup 0–2 points for each item:

- I can understand what it can access.
- I can review actions before they happen.
- I can export or inspect the source files.
- I can recover from a bad change.
- I can see errors and logs.
- The cost is predictable enough for the expected volume.
- A nontechnical helper could understand the workflow later.

A setup with more features but a lower clarity score is usually the wrong first choice.
