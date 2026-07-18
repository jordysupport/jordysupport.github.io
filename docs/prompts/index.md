# Prompts

!!! info "Official prompts first"
    Jared's builds — the Voice Line, the Visualizer, Windows versions — live at **[jaredrhod.com/prompts](https://jaredrhod.com/prompts)**. Start there.

This section is for community extras: small utility prompts that come out of Discord questions.

## Vault health check

Paste into Claude Code from your vault's working directory:

```text
Read my CLAUDE.md and VAULT-INDEX.md, then audit the vault:
1. List any [FILL IN: ...] placeholders that were never filled in
2. Check the daily notes folder — when was the last entry?
3. Flag any project folders mentioned in the index that don't exist on disk (or vice versa)
Report findings as a short checklist. Don't fix anything yet — just report.
```

## "Explain it like I'm from marketing"

For when a guide assumes tech knowledge you don't have:

```text
I'm a marketer, not a developer. Explain what this error/instruction means
and exactly what to type, step by step, assuming I've never used a terminal:

[paste the confusing thing here]
```

---

*Got a prompt worth adding? Share it in Discord.*
