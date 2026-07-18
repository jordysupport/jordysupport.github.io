# Glossary

## Agent

A system in which a model can use context and tools in a loop to work toward a goal. An agent may still require human approval.

## Agent loop

The repeated pattern of observing the current state, choosing an action, using a tool, checking the result, and continuing or stopping.

## Approval gate

A required human or policy authorization before a high-impact action can continue.

## API

Application Programming Interface. A defined way for one software system to request data or actions from another.

## Authentication

Proving which user or system identity is making a request.

## Authorization

Deciding what an authenticated identity is allowed to access or do.

## Automation

A process that starts or advances without a person manually performing every step.

## Context

The information available to the model during a run, including messages, instructions, selected files, and tool results.

## Context window

The practical limit on how much information a model can actively consider in one request or session.

## Connector

An integration that gives an AI application access to another source or service. A connector is also a permission decision.

## Deterministic

Expected to produce the same defined result from the same input under the same rules. Required-field validation and exact calculations are common deterministic steps.

## Embedding

A numerical representation used to compare semantic similarity. Embeddings can help retrieve related content but do not prove factual authority.

## Evaluation

A repeatable method for measuring whether model or workflow output meets the required quality and safety standard.

## External action

A change outside the agent's private draft space, such as sending a message, publishing, updating a shared record, or creating a purchase.

## Few-shot example

One or more examples included to demonstrate the desired output or behavior.

## Grounding

Providing approved evidence or sources so the model's output is tied to real information.

## Guardrail

An instruction, permission boundary, validation, policy, or other control intended to prevent or contain unwanted behavior.

## Hallucination

Content generated without adequate support, often presented as though it were factual. “Confabulation” is another term sometimes used.

## Human in the loop

A design where a person reviews, corrects, approves, or performs an important part of the process.

## Idempotency

A property that lets the same event be processed more than once without creating duplicate effects.

## Inference

A conclusion drawn from evidence rather than directly stated by a source. Good systems label important inferences.

## Input contract

A definition of the required fields, formats, limits, source, and behavior for incoming data.

## Instruction hierarchy

The order used to resolve competing instructions, such as safety rules, approved task instructions, project policy, and style preferences.

## Least privilege

Giving a user, agent, or integration only the access required for the task, and no more.

## Large language model (LLM)

A model trained to predict and generate language and related structured outputs. A model is one component of an agent system.

## Log

A record of events, actions, statuses, errors, and other operational evidence.

## Long-term memory

Information made available across sessions through saved product features or external storage. It should not be assumed to be complete or always active.

## MCP

Model Context Protocol. An open standard for connecting compatible AI applications to tools and data sources.

## Model

The underlying system that generates or reasons from the supplied input. The product interface, tools, and memory around it are separate components.

## Multi-agent system

A design with more than one agent role or worker coordinating on a task. It adds communication, handoff, and consistency problems and is not automatically better.

## Observability

The ability to understand a system's state and behavior through logs, traces, metrics, run records, and outputs.

## Output contract

The required structure, fields, allowed values, length, and semantics of a result.

## Permission scope

The exact resources and actions allowed by a credential or connector.

## Prompt

Instructions and information supplied to a model for a task. A prompt is not a complete safety boundary.

## Prompt injection

Untrusted content attempting to manipulate an AI system's instructions, permissions, or tool use.

## Provenance

Information showing where content came from, how it was transformed, and which version or source supports it.

## RAG

Retrieval-augmented generation. A pattern that retrieves relevant external content and supplies it to a model for a response.

## Rate limit

A service limit on requests, tokens, or actions over a period.

## Reconciliation

A process that compares expected and actual external state to find missing, duplicated, or partially completed actions.

## Retry

A repeated attempt after a failure. Retries should be limited and used only when the failure may be temporary.

## Reversibility

The ability to undo or correct an action, such as restoring a version or deleting an unsent draft.

## Run

One execution of an agent or workflow from input through final status.

## Run ID

A unique identifier used to trace a run across logs, validations, and external records.

## Schema

A formal description of data structure, types, required fields, and allowed values.

## Secret

A credential such as an API key, token, password, private key, or session value that must be protected.

## Source of truth

The approved authoritative location for a particular type of information.

## State

The current stage or recorded condition of a workflow, such as `AWAITING_APPROVAL` or `COMPLETED`.

## Structured output

Output constrained to a defined shape such as JSON fields, a table, or required Markdown headings.

## System instruction

A high-priority instruction supplied by an AI application. Product terminology and exact priority behavior vary.

## Temperature

A model-generation setting commonly associated with output variability. It is not a correctness control.

## Tool

A capability the model can request, such as reading a file, running a command, searching, or updating a record.

## Tool call

A structured request from the model to invoke a tool with particular arguments.

## Trace

A detailed record of steps, model calls, tool calls, handoffs, and results across a run.

## Trigger

The event or schedule that starts a workflow.

## Untrusted content

Information that may be useful as data but has no authority to change the task or permissions, such as webpages, emails, documents, and external tool results.

## Validation

A check that confirms structure, content, policy, or workflow state before the result is accepted or an action occurs.

## Vector database

A data store designed to retrieve items using numerical vectors such as embeddings. It is a retrieval mechanism, not a guarantee of truth.

## Workflow

A designed sequence of steps, decisions, checks, approvals, actions, and failure handling.

## Working directory

The folder from which a terminal program or file-based agent currently operates. Relative paths begin there.
