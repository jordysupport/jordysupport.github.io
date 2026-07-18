# Build your first agent

This walkthrough creates a small, safe workspace and asks an agent to turn raw notes into a useful project brief. The purpose is to practice the full agent loop—not to chase maximum autonomy.

## What you will build

```text
ai-practice/
├── input/
│   └── notes.txt
├── output/
├── AGENT_BRIEF.md
└── README.md
```

The agent may read `input/` and write only to `output/`. It must not delete files, install software, contact anyone, or publish anything.

## 1. Create the workspace

=== "macOS, Linux, or Codespaces"

    ```bash
    mkdir -p ~/ai-practice/input ~/ai-practice/output
    cd ~/ai-practice
    printf "# AI Practice Workspace\n\nSource files go in input/. Agent drafts go in output/.\n" > README.md
    printf "Customer onboarding feels inconsistent. New clients ask the same questions. We need a welcome checklist, a list of required materials, and clear owners for each step. Current handoff happens through email and sometimes tasks are missed.\n" > input/notes.txt
    ```

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Force "$HOME\ai-practice\input" | Out-Null
    New-Item -ItemType Directory -Force "$HOME\ai-practice\output" | Out-Null
    Set-Location "$HOME\ai-practice"
    "# AI Practice Workspace`n`nSource files go in input/. Agent drafts go in output/." | Set-Content README.md
    "Customer onboarding feels inconsistent. New clients ask the same questions. We need a welcome checklist, a list of required materials, and clear owners for each step. Current handoff happens through email and sometimes tasks are missed." | Set-Content input\notes.txt
    ```

Not comfortable with commands? Create the same folders and files using Finder or File Explorer.

## 2. Create the agent brief

Save this as `AGENT_BRIEF.md`:

```markdown
# Role
You are a careful project assistant working inside this folder.

# Goal
Turn the raw notes in `input/` into a practical client-onboarding improvement brief.

# Allowed actions
- Read files inside `input/`.
- Create new Markdown files inside `output/`.
- Explain your plan and your completed work.

# Forbidden actions
- Do not modify or delete source files.
- Do not write outside `output/`.
- Do not install software, use external services, send messages, or publish anything.
- Do not invent company facts, names, dates, or commitments.

# Required output
Create `output/onboarding-brief.md` with:
1. a short problem statement;
2. assumptions and unanswered questions;
3. a proposed onboarding checklist;
4. suggested owners expressed as roles, not invented names;
5. risks and safeguards;
6. the next three actions a human should take.

# Quality checks
Before finishing:
- confirm every claim is supported by the source notes or labeled as an assumption;
- confirm the source file was not changed;
- confirm only the required output file was created;
- summarize what you did and stop.
```

## 3. Start the agent in the correct folder

Open your AI terminal or editor agent **from `ai-practice`**. The exact command depends on the tool you use.

Before asking it to act, check the working directory:

=== "macOS, Linux, or Codespaces"

    ```bash
    pwd
    ls -la
    ```

=== "Windows PowerShell"

    ```powershell
    Get-Location
    Get-ChildItem -Force
    ```

You should see `AGENT_BRIEF.md`, `README.md`, `input`, and `output`.

## 4. Give the task

Copy this prompt:

```text
Read AGENT_BRIEF.md and inspect the available source files.

First, restate the goal, allowed actions, forbidden actions, required output, and your plan. Do not make changes until I approve the plan.
```

Review the plan. It should mention only reading `input/notes.txt` and creating `output/onboarding-brief.md`.

Then reply:

```text
Approved. Complete the task, run the quality checks in AGENT_BRIEF.md, and report the files you created or changed.
```

## 5. Verify the result yourself

Do not accept “done” as proof.

=== "macOS, Linux, or Codespaces"

    ```bash
    find . -maxdepth 2 -type f -print
    cat input/notes.txt
    cat output/onboarding-brief.md
    ```

=== "Windows PowerShell"

    ```powershell
    Get-ChildItem -Recurse -File | Select-Object FullName
    Get-Content input\notes.txt
    Get-Content output\onboarding-brief.md
    ```

Check:

- [ ] The original notes are unchanged.
- [ ] The output is in the correct folder.
- [ ] Unsupported claims are labeled as assumptions.
- [ ] The checklist is usable rather than generic.
- [ ] No messages were sent and no external systems were changed.

## 6. Improve the instructions, not just the answer

When the output is weak, record the correction in `AGENT_BRIEF.md`.

Examples:

- “Every checklist item must begin with an action verb.”
- “Separate tasks required before kickoff from tasks required after kickoff.”
- “Do not use vague owners such as ‘the team’; choose a functional role.”
- “Include a completion signal for each step.”

This creates reusable project knowledge instead of a one-time chat fix.

## 7. Repeat before automating

Run the same process with two or three different note files. Only consider automation after the structure holds up across varied inputs.

## What you just learned

You practiced the core pattern behind most useful agents:

```text
bounded workspace → durable instructions → plan review → tool use → output → verification → improved instructions
```

Continue with [The Agent Loop](../fundamentals/agent-loop.md) or learn how to organize [Context and Memory](../fundamentals/context-memory.md).
