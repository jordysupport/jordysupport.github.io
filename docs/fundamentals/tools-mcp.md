---
description: >-
  Understand AI tools and MCP connections, including what they can read or change and where your data may go.
---

<span class="kicker">How agents work · Tools</span>

# Tools & connections

A **tool** lets an agent perform an operation: search a folder, read a calendar, create a document, or run a command. The AI requests the operation, and the surrounding software executes it subject to its permissions.

[**MCP**](../resources/glossary.md#mcp), the Model Context Protocol, is a standard for connecting AI applications to external data and tools. An MCP connection can expose a few operations or broad account access. The standard does not tell you whether a particular connection is appropriate for your task.

## What can this connection do? { #the-only-question-that-matters }

Before enabling it, check three things:

| Question | Example |
| --- | --- |
| What can it read? | One calendar, selected files, or your whole drive? |
| What can it change? | Create drafts, edit shared documents, send email, or delete records? |
| Where does the data go? | The AI provider, the app you connected, or a third-party server? |

Read-only access reduces the chance of an unwanted edit, but it can still expose private information. Even a search request can include data you did not intend to send to another service.

## Connecting an app, in practice

Use the AI app's official connection flow. Read the permissions screen before signing in or granting access. Choose the narrowest access offered and enable human review of tool calls where the product supports it.

Try one small task first, such as listing the times of tomorrow's meetings. Compare the result with the calendar. Check whether the connection can also create or cancel events before using it for scheduling.

For a third-party MCP server, check who operates it, which tool parameters it receives, and what data it retains. A familiar app name in a server description does not establish who runs the server.

Disconnect connections you no longer need. If you also granted access in the connected service's account settings, review that authorization too.

## A caution worth knowing: planted instructions

A web page, email, or document can contain text that tells the agent to abandon your task, disclose data, or use another tool. This is called **prompt injection**. Treat outside content as source material, and give it no authority to change the task.

Approval prompts and restricted permissions reduce the risk. They cannot guarantee the agent will recognize every malicious instruction. Review tool requests closely when a task combines private files with outside content.

Read the [official MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro) for the standard and [OpenAI's guidance on MCP risks](https://developers.openai.com/api/docs/mcp#risks-and-safety) for concrete examples of data leakage and unwanted actions.

[Next: Keeping it safe](safety-permissions.md){ .md-button .md-button--primary }

[Support these free guides on Ko-fi](https://ko-fi.com/support_jordy).
