---
description: >-
  Work through a failed AI task or computer setup by checking the error, isolating the cause, and making one change at a time.
---

<span class="kicker">Troubleshooting</span>

# Work out what failed { #fix-it-in-order }

When a task stops working, save the error and check what happened before changing anything. We use this order to keep the next step small and useful.

## Start with the evidence { #the-universal-order }

1. **Capture the error.** Copy the exact text and the command or action that produced it. Remove passwords, tokens, and private details before sharing.
2. **Check whether it is safe to retry.** A file read can usually be repeated. A payment, message, upload, or other submission may already have succeeded; check its status first.
3. **Look for the last change.** An update, renamed file, expired sign-in, moved folder, or different account can explain a new failure.
4. **Try a small example.** Use a copy of a simple file in a practice folder. Does the same step fail there?
5. **Check the tool's official help.** Search the exact error and confirm that any fix applies to your operating system and version.
6. **Change one thing and test again.** Reinstall only if the evidence points to an installation problem. Save files and settings you need before removing anything.

## Ask for a diagnosis { #ask-ai-the-right-way }

Give the AI enough evidence to distinguish a missing program from a wrong path or a permissions problem.

```text title="Copy this"
Help me diagnose this failure.

What I was trying to do: [one sentence]
Exact command or action: [paste it]
Exact error, with secrets removed: [paste it]
Operating system and tool version: [what I know]
Last successful attempt: [when, if known]
Recent changes: [what changed, or "unknown"]

Start with a read-only check. Give me one step at a time and explain
what it will tell us. Wait for the result before choosing the next
step. Tell me before a step changes files, settings, or accounts.
Do not repeat a submission until we know whether it succeeded.
```

If the AI keeps proposing the same failed fix, bring it back to the observed result: "That returned this error. What does it rule out?"

## Find the relevant guide { #by-system }

- [Terminal basics](terminal-basics.md): folders, commands, and common error messages.
- [Windows](windows.md): shell differences, file paths, and security blocks.
- [macOS](macos.md): permissions, app warnings, and command lookup.
- [Git & Codespaces](git-codespaces.md): reviewing changes, commits, and sync problems.

[Open terminal basics](terminal-basics.md){ .md-button }
