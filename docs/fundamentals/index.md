---
description: >-
  Understand how AI agents use instructions, context, and tools to complete a task, and how to review what they do.
---

<span class="kicker">How agents work</span>

# The basics

An [**agent**](../resources/glossary.md#agent) uses AI to choose steps and tools while working toward a goal. Give one a folder of meeting notes, and it might find the relevant files, read them, draft a task list, and save it for review.

How much it can do depends on the software and permissions around it. An agent with file access works differently from one connected to your inbox, browser, or payment account.

## Six things to understand { #the-six-pieces-of-every-agent }

| Part | What it means | In the meeting-notes example |
| --- | --- | --- |
| Instructions | The requested job and its boundaries | List the decisions and tasks; leave unknown owners blank. |
| Context | The material available for the current response | Your request, the notes it read, and tool results. |
| Tools | The operations available to the agent | Search files, read notes, and create a draft. |
| Actions | The operations it actually takes | Read two files and write `tasks.md`. |
| Checks | Evidence that the result meets the request | Compare tasks, owners, and dates with the notes. |
| Stop points | The moments that require your decision | Ask before replacing an existing file or sending the list. |

Use these questions when something goes wrong. Did the agent have the source? Did it use the correct tool? Was the requested output clear? Did anyone check the saved result? The answers give you a starting point for a fix.

## Read these in order

<div class="grid cards" markdown>

-   **The agent loop**

    Follow a task from reading the input to checking the output. [Read the guide](agent-loop.md)

-   **Context & memory**

    Understand what an agent sees and how to carry decisions into another session. [Read the guide](context-memory.md)

-   **A vault for your agent**

    Keep project notes and reusable instructions in files you control. [Read the guide](obsidian-vaults.md)

-   **Subagents**

    Split a larger job into separate tasks without losing track of the evidence. [Read the guide](subagents.md)

-   **Tools & connections**

    Check what an app connection can access and change. [Read the guide](tools-mcp.md)

-   **Keeping it safe**

    Set permissions, practice on copies, and review consequential actions. [Read the guide](safety-permissions.md)

</div>

The guides are free to read. You can [support Jordy on Ko-fi](https://ko-fi.com/support_jordy) if you would like to help fund the site.

[Next: The agent loop](agent-loop.md){ .md-button .md-button--primary }
