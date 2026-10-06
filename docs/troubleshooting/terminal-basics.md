---
description: >-
  Learn to check your current folder, list files, and run a small command safely in PowerShell or a Mac terminal.
---

<span class="kicker">Troubleshooting · Terminal</span>

# Terminal basics

A terminal lets you give the computer a command in text. If you use a terminal-based agent, knowing how to check the folder and read the result makes its work easier to follow.

## Open it

- **Windows:** search Start for **Terminal** or **PowerShell**. Check that the tab says PowerShell.
- **Mac:** press Cmd+Space, type **Terminal**, and press Enter.

A terminal window can run different shells, which are the programs that interpret commands. PowerShell, Command Prompt, and a Mac shell use different syntax. Match the shell named in the instructions you are following.

## Commands for moving around { #the-five-commands }

| What you need | PowerShell on Windows | Terminal on Mac |
| --- | --- | --- |
| Show the current folder | `Get-Location` | `pwd` |
| List files in it | `Get-ChildItem` | `ls` |
| Enter a folder called Documents | `Set-Location Documents` | `cd Documents` |
| Go up one folder | `Set-Location ..` | `cd ..` |
| Create a folder called ai-practice | `New-Item -ItemType Directory ai-practice` | `mkdir ai-practice` |

PowerShell also accepts the short forms `pwd`, `dir`, `cd`, and `mkdir`. We show the full names here so you can recognize them in other guides.

A path with spaces needs quotes. These commands enter an existing folder relative to your current one:

### Windows PowerShell

```powershell
Set-Location "Project Notes"
Get-Location
Get-ChildItem
```

### Mac

```sh
cd "Project Notes"
pwd
ls
```

## Check the folder first { #the-one-habit }

Before starting an agent, confirm the folder shown by `Get-Location` or `pwd`. Then tell the agent the exact source and output paths.

The current folder helps locate files. It is not a permission boundary: an agent's tools may be able to access elsewhere. Use the tool's access controls and start with copies in a practice folder.

## When a command fails

| Message | What to check |
| --- | --- |
| "Command not found" or "not recognized" | Spelling, whether the program is installed, and where the shell looks for it |
| "No such file or directory" or "cannot find path" | The current folder, exact filename, and quotes around spaces |
| "Permission denied" or "access denied" | The path and the operation being blocked |

A permission error needs a reason before a workaround. Avoid adding `sudo` or running as administrator just because a command failed.

Run a command only when you understand its target and what it changes. Ask for an explanation of unfamiliar options before using them on your own files.

[Windows help](windows.md){ .md-button }
[macOS help](macos.md){ .md-button }

[Learn Git & Codespaces](git-codespaces.md){ .md-button }
