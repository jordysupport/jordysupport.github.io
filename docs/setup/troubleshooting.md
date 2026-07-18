# Troubleshooting

The fixes for questions that keep coming up in Discord. Platform-specific install problems: [Windows](windows.md) · [Mac](mac.md).

## Claude Code doesn't see my CLAUDE.md

CLAUDE.md loads from the folder you **start Claude Code in**, not wherever the file happens to live. Check where you are:

```bash
pwd        # Mac / WSL
cd         # Windows Command Prompt (no arguments)
```

Then `ls` (Mac) or `dir` (Windows) — you should see `CLAUDE.md` in the listing. If not, `cd` into the right folder and restart Claude Code.

## Claude says it can't find my vault

The vault path in your CLAUDE.md doesn't match reality. Open CLAUDE.md, copy the path, and try to open that exact path in your file explorer. Typos, a renamed folder, or OneDrive/iCloud moving things are the usual culprits.

## "It forgot everything from yesterday"

The memory lives in the vault files, not in Claude itself. If a new session boots "nameless":

1. You started Claude Code in the wrong folder (no CLAUDE.md loaded) — see above
2. The daily note or profile never got written — ask Claude to show you the vault's daily notes folder and check dates

## Login / authentication loops

Log out and back in inside Claude Code (`/logout`, then restart). If the browser window never opens, copy the URL it prints into your browser manually.

## It's slow or hitting limits

Long sessions accumulate context. Start a fresh session for a new task — the vault is the memory, so a fresh session loses nothing that was written down.

---

*Something else broke? Ask in Discord — if it comes up twice, it lands on this page.*
