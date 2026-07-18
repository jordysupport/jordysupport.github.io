# Tools and MCP

A language model proposes text. A tool gives it a way to inspect or change something outside that text response.

Tools may:

- read or write files;
- search the web;
- query a database;
- run code or commands;
- use email, calendar, or project systems;
- call an API;
- control a browser;
- retrieve knowledge.

The moment a model receives a tool, the design question changes from “Can it answer?” to “What can it access and what could go wrong?”

## Tool anatomy

A well-defined tool has:

- a clear name;
- a narrow purpose;
- typed or structured inputs;
- a predictable output;
- useful errors;
- permission boundaries;
- timeout and rate limits;
- logs;
- no hidden side effects.

Compare:

```text
Bad tool: manage_files(path, action, options)
```

```text
Better tools:
- list_project_files(relative_directory)
- read_project_file(relative_path)
- create_draft(relative_path, content)
- request_file_deletion(relative_path, reason)
```

Narrow tools make policy and review easier.

## Risk tiers

| Tier | Capability | Examples | Default control |
|---|---|---|---|
| 0 | Reason only | classify, draft, compare | review output |
| 1 | Read | files, search, database query | approved sources; log access |
| 2 | Reversible write | create draft, add label, create task | limited scope; report changes |
| 3 | External action | send message, publish, update shared record | explicit approval or strict policy |
| 4 | Destructive or financial | delete, overwrite, purchase, change permissions | separate authorization; usually human execution |

Do not hide high-risk behavior inside a tool with a harmless name.

## What MCP is

Model Context Protocol (MCP) is an open standard for connecting AI applications to external tools and data sources. An MCP server can expose things such as tools, resources, and reusable prompts to a compatible AI host.

The practical benefit is a common connection pattern. The practical warning is that an MCP server is still software with permissions.

Use the official [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro) for current technical details.

## MCP vocabulary

**Host**
: The AI application the user interacts with.

**Client**
: The component inside the host that connects to an MCP server.

**Server**
: A program that exposes approved capabilities or information.

**Tool**
: An action the model may request, such as querying or creating something.

**Resource**
: Information the server makes available for reading.

**Prompt**
: A reusable interaction template exposed by the server.

## Before installing a connector or MCP server

Answer these questions:

1. Who maintains it?
2. Can you inspect the source or package provenance?
3. What exact data and systems can it access?
4. Does it need write access?
5. Where do credentials live?
6. Are tool calls logged?
7. Can it run arbitrary commands?
8. Does it send data to another service?
9. How do you revoke access?
10. What happens if its instructions conflict with yours?

!!! danger "Do not install a server only because a directory calls it popular"
    Treat third-party agent integrations like any other software installation. Review permissions, source, updates, and the maintainer—not just the demo.

## Start read-only

A safe rollout sequence:

1. connect a test account or test folder;
2. grant read-only access;
3. inspect the exposed tool list;
4. run known queries;
5. verify logs and error behavior;
6. add one reversible write tool;
7. require approval for external or destructive actions;
8. monitor before expanding scope.

## Tool descriptions affect behavior

The model uses the tool name and description to decide when to call it. Descriptions should state:

- what the tool does;
- what it does **not** do;
- required inputs;
- side effects;
- permission expectations;
- when another tool should be used instead.

Example:

```text
create_email_draft
Creates an unsent email draft in the approved workspace.
Does not send, schedule, forward, or add recipients not supplied by the user.
Returns the draft ID, recipients, subject, and a preview for review.
```

## Validate tool inputs and outputs

Never depend on the model to generate perfect arguments.

Use:

- required fields;
- allowed-value lists;
- maximum lengths;
- path restrictions;
- recipient allowlists;
- amount limits;
- date validation;
- output schemas;
- explicit “not found” states.

A tool should reject unsafe or ambiguous input even when the model confidently requests it.

## Protect credentials

- Put secrets in the platform's secret store or environment, not prompts or project files.
- Give each integration only the scopes it needs.
- Use test credentials for development.
- Rotate exposed credentials immediately.
- Never ask an agent to print a secret to “confirm it works.”
- Redact secrets from logs and error messages.

## Tool-selection prompt

```text
Before using a tool, state:
- the tool you intend to use;
- why it is necessary;
- the exact scope of the action;
- the expected side effect;
- how you will verify the result.

Do not use a broader tool when a narrower one can complete the step. Ask for approval before any external, destructive, permission-changing, or financial action.
```

## Current official references

- [MCP documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture)
- [Claude Code overview](https://code.claude.com/docs/en/overview)

Product behavior changes. Use official documentation for installation and current permission details; use this guide for the decision framework.
