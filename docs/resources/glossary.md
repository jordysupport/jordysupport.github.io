---
description: >-
  Plain-English definitions of AI agents, context, tokens, tools, MCP, memory, and other terms used in the Jordy Support guides.
---

# Glossary

These are the meanings used in our guides. Tool names and settings can differ between products.

**Agent**{ #agent }: An AI system that takes steps toward a goal using tools, such as web search or file editing. Its access depends on the tools and permissions available.

**Automation**{ #automation }: A task configured to run when an event happens or on a schedule. It may include an AI step, but it doesn't have to.

**Commit**{ #commit }: A saved snapshot of tracked project files in Git, with a message explaining the change. Files you haven't added are not part of that snapshot.

**Context / context window**{ #context }: The information supplied to a model for its current response. This can include messages, instructions, selected files, and tool results. A context window has a size limit; a tool may shorten or retrieve information to fit.

**Folder agent**{ #folder-agent }: Our shorthand for an agent working with files in a project folder. Starting it in a folder does not, by itself, prevent access elsewhere.

**Git**{ #git }: Software for tracking changes to project files. It helps compare versions and recover committed work. It isn't a backup of everything on your computer.

**Hallucination**{ #hallucination }: An incorrect or invented detail in an AI response, sometimes presented confidently. Check important claims against evidence.

**LLM (large language model)**{ #llm }: A model trained to work with language. It generates responses from the information it receives and patterns learned during training.

**MCP**{ #mcp }: Model Context Protocol, a standard for connecting AI applications to tools and information. A connection still needs appropriate access controls; the standard doesn't make its contents trustworthy.

**Memory**{ #memory }: Information a tool saves for use later. Some products retrieve it automatically; others require you to ask for a file to be read. Saved information may be incomplete or outdated.

**Model**{ #model }: The trained system that generates an AI response. Different models vary in cost, speed, supported inputs, and how well they handle a task.

**Playbook**{ #playbook }: A set of instructions for a repeatable job. Our [playbooks](../playbooks/index.md) include prompts, examples, and downloadable files.

**Prompt**{ #prompt }: The request or instructions you give an AI tool.

**Project instructions**{ #project-instructions }: Written guidance an AI tool loads for a project. Which files it reads and how often depends on the tool. Instructions don't replace permission controls.

**Skill**{ #skill }: A reusable set of instructions, sometimes with supporting files. Our downloadable skills are text files that an agent can read from your notes.

**Subagent**{ #subagent }: A separate agent assigned part of a larger task. It may receive only selected context, and its work still needs review.

**Terminal**{ #terminal }: An interface for running text commands. Commands can read, change, or delete files, install software, and contact services.

**Token**{ #token }: A unit a model uses to process input and output. Depending on the model and input, it can represent part of a word or other data. Usage limits and API charges often count tokens.

**Tool**{ #tool }: A capability an agent can call, such as searching the web, reading a file, or updating an app.

**Vault**{ #vault }: A folder of notes, often managed in Obsidian. An agent can use it as a reference if it has access and reads the relevant files.

**Workflow**{ #workflow }: The steps a task follows from its starting input to its finished result, including any checks and approvals.

[Find documentation for your tool](learning-links.md){ .md-button }
