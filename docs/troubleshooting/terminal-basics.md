<span class="kicker">Troubleshooting · Terminal</span>

# Terminal basics

The **terminal** is a text box where you type commands to your computer. Agents like Claude Code live there. You need about five commands and one habit — that's it.

## Open it

- **Windows:** Start menu → type "Terminal" → open **Windows Terminal** (or PowerShell).
- **Mac:** Cmd+Space → type "Terminal" → Enter.

## The five commands

| Type this | It means |
| --- | --- |
| `pwd` | "Where am I?" — shows your current folder |
| `ls` (Mac) / `dir` (Windows) | "What's in here?" — lists the folder's contents |
| `cd Documents` | "Go into the Documents folder" |
| `cd ..` | "Go up one folder" |
| `mkdir ai-practice` | "Make a new folder called ai-practice" |

That's genuinely most of what you'll use. Everything else, you can ask AI for as you need it.

## The one habit

**Know where you are before you run anything.** Type `pwd` first. Agents act in the folder you're standing in — being in the wrong folder is the #1 beginner mistake.

## When a command fails

Read the message. The classics:

- *"command not found"* — a typo, or the program isn't installed.
- *"no such file or directory"* — you're in the wrong folder, or the name's misspelled. `pwd` and `ls` will show you.
- *"permission denied"* — the computer is protecting something. Stop and ask AI about the specific message rather than forcing it.

[Windows help](windows.md){ .md-button }
[macOS help](macos.md){ .md-button }
