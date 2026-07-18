# Universal troubleshooting checklist

When an AI tool, terminal command, automation, or project stops working, do not change five things at once. Preserve the exact evidence and narrow the problem.

## The 10-minute diagnostic order

### 1. Save the exact error

Capture:

- the complete command or action;
- the complete error text;
- the time it happened;
- the current folder;
- the tool and version;
- what you expected;
- the last known time it worked;
- what changed since then.

Do not summarize the error as “it failed.” One word in the original message can change the diagnosis.

### 2. Confirm the current location

Many agent and project errors come from starting in the wrong directory.

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

Confirm the expected instruction, configuration, source, and project files are visible.

### 3. Check whether the command exists

=== "macOS, Linux, or Codespaces"

    ```bash
    command -v git
    git --version
    command -v python
    python --version
    ```

=== "Windows PowerShell"

    ```powershell
    Get-Command git
    git --version
    Get-Command python
    python --version
    ```

Replace the example program with the one failing.

### 4. Check authentication separately

Authentication problems often look like tool failures.

Ask:

- Is the login or token expired?
- Am I using the intended account?
- Does this environment have access to the credential?
- Did the repository, organization, or resource move?
- Did permission scopes change?
- Is the failure “not found” because access is denied?

Do not print tokens or passwords into the terminal transcript.

### 5. Check permissions

Identify whether the operation is read, create, edit, delete, execute, or network access.

Confirm:

- the file or folder exists;
- your account owns or can access it;
- the agent started inside the allowed workspace;
- the connector scope includes the requested action;
- an operating-system security prompt was not denied;
- a read-only mode is not active.

Do not solve a narrow permission problem by granting administrator access to everything.

### 6. Check version and environment

Record:

- operating system;
- shell;
- runtime version;
- package version;
- project dependency file;
- virtual environment or container status.

A command working in one terminal does not prove another terminal loaded the same PATH, environment variables, or virtual environment.

### 7. Reproduce the smallest failure

Remove unrelated steps.

Instead of rerunning an entire automation, test:

1. Can it read one known input?
2. Can it produce valid structured output?
3. Can validation parse it?
4. Can the destination be reached?
5. Can a test record be created?

The first failing boundary identifies the responsible layer.

### 8. Read the first meaningful error

Long logs often contain later failures caused by the first one. Start near the earliest `error`, `failed`, `denied`, `not found`, or nonzero exit.

Warnings matter, but do not treat every warning as the root cause.

### 9. Change one thing

Write down the hypothesis:

> I think the build fails because the dependency is missing from this environment. I will verify the package list before installing anything.

Run one diagnostic or reversible change. Record the result. Avoid a chain of guessed fixes copied from unrelated cases.

### 10. Verify recovery

After a fix:

- rerun the smallest failing step;
- rerun the normal workflow;
- confirm outputs and side effects;
- remove temporary debug access;
- document the cause and stable fix;
- add a check that catches the problem sooner next time.

## Symptom map

| Symptom | First checks |
|---|---|
| “Command not found” | spelling, installation, PATH, new terminal session |
| “File not found” | current folder, relative path, filename case, mounted volume |
| “Permission denied” | requested operation, ownership, connector scope, execution bit |
| Login loop or unauthorized | account, token expiry, environment secret, scopes, clock |
| Agent ignores project rules | working directory, instruction filename, conflicting rules, context load |
| Agent changed wrong files | start folder, path scope, tool permissions, plan review, Git diff |
| Structured output fails | schema, required fields, escaping, output length, repair limit |
| Workflow runs twice | duplicate trigger, idempotency key, retry behavior |
| Works locally but not in deployment | environment variables, dependency lock, filesystem case, network access |
| Session becomes confused | too much context, stale task details, conflicting sources, restart with compact status |

## Ask for help with this template

```text
Goal:

What I did:

Exact command or action:

Exact error:

Operating system and shell:

Tool and version:

Current folder:

Relevant files present:

Expected result:

Actual result:

Last time it worked:

What changed:

Diagnostics already run and their output:

Sensitive details removed:
```

A good support request lets another person reproduce your reasoning without guessing.

## Do not paste these publicly

Remove or redact:

- API keys and tokens;
- passwords;
- private repository URLs containing credentials;
- customer or employee information;
- full environment-variable dumps;
- private keys;
- cookies and session headers;
- internal file contents unrelated to the error.

Leave useful structure visible. For example, replace a token with `<REDACTED_TOKEN>` rather than deleting the whole line.

## Next guides

- [Terminal basics](terminal-basics.md)
- [Windows troubleshooting](windows.md)
- [macOS troubleshooting](macos.md)
- [Git and Codespaces](git-codespaces.md)
