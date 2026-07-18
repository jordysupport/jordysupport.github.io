# Start here

You do not need to become a developer before AI can help you. You do need a clear job, trustworthy source material, a safe place to work, and a way to check the result.

This beginner path takes you from “I use chat” to “I can supervise a simple agent.”

## The 30-minute path

### 1. Choose one repeatable task

Good first tasks have an obvious input and an output you can inspect.

Examples:

- turn raw notes into a structured summary;
- compare three documents against a checklist;
- draft a follow-up email from a meeting transcript;
- organize copied research into a brief;
- convert one long article into several draft formats.

Avoid a first task like “run my whole business,” “manage my inbox,” or “publish automatically.” Those combine too many decisions and too much risk.

### 2. Choose the smallest setup that can do the job

| Need | Sensible starting point |
|---|---|
| Advice or a one-off draft | A normal AI chat |
| Work with a few uploaded files | An AI app with file support |
| Read and edit a project folder | A terminal or editor-based agent |
| Move data between apps | An automation platform |
| Custom rules, APIs, and scale | A coded agent or workflow |

[Use the setup decision guide](choose-a-setup.md) before installing extra tools.

### 3. Create a safe workspace

Use a new folder containing copies of non-sensitive files. Do not begin inside your entire Documents folder, cloud drive, email account, or production system.

A simple structure is enough:

```text
ai-practice/
├── input/       # source material; treat as read-only
├── output/      # drafts created by the agent
├── AGENT_BRIEF.md
└── README.md
```

### 4. Write a task contract

A task contract states:

- the goal;
- the source material;
- the required output;
- rules and constraints;
- how quality will be checked;
- when the agent must stop and ask.

Use the [prompt builder](../prompting/prompt-builder.md) or the starter brief in [Build Your First Agent](first-agent.md).

### 5. Run once with supervision

Watch what the agent reads, plans, changes, and claims. Decline unexpected permissions. Ask it to explain anything you do not understand.

### 6. Verify before trusting

Check at least:

- Were all required sources used?
- Did the output invent facts or citations?
- Did it follow the format?
- Did it change anything outside the workspace?
- Can another person understand the result?

### 7. Save what worked

Keep the useful instructions, examples, corrections, and checklist in project files. Do not depend on remembering the perfect chat message.

## Your first success should be boring

A good first result is not “the AI surprised me.” It is:

> The agent completed a small job, stayed inside its boundaries, produced an output I could verify, and left a clear record of what it did.

That boring success is the foundation for larger systems.

## Beginner rules worth keeping

- **Copies before originals.** Let an agent practice on duplicates.
- **Read-only before write access.** Expand permissions only after the read step works.
- **Draft before publish.** Human review stays between creation and external action.
- **One workflow before many agents.** Multiple agents add coordination problems.
- **Exact errors before guesses.** Save the full error message when something breaks.
- **Files before memory claims.** Put important instructions and facts in inspectable files.

## Continue

<div class="grid cards" markdown>

-   **Choose your setup**

    Decide between chat, file tools, terminal agents, automation platforms, and custom builds.

    [Open the decision guide](choose-a-setup.md)

-   **Build your first agent**

    Create a safe folder and complete an end-to-end task.

    [Start the walkthrough](first-agent.md)

-   **Understand the agent loop**

    Learn how observation, action, verification, and stopping fit together.

    [Learn the loop](../fundamentals/agent-loop.md)

</div>
