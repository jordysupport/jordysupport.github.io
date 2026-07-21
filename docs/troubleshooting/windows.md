---
description: >-
  Fix common Windows problems when setting up AI tools: plain-English solutions for installs, paths, permissions, and errors that block beginners.
---

<span class="kicker">Troubleshooting · Windows</span>

# Windows

The usual suspects when AI tools misbehave on Windows, and the plain fix for each.

## "Windows protected your PC" when installing

SmartScreen warns about unfamiliar downloads. If you downloaded from the tool's **official site**, click *More info → Run anyway*. If you're not sure it's the official site, stop and check first.

## PowerShell vs Command Prompt confusion

They're two different text boxes with slightly different commands. When a guide's commands fail, you may be in the wrong one. Use **Windows Terminal** and check the tab label; guides on this site work in PowerShell.

## "Not recognized as a command" after installing

The program installed, but Windows doesn't know where it lives yet. Two fixes, in order:

1. Close the terminal completely and open a new one. (Fixes it half the time.)
2. Still failing? Ask AI: *"I installed [tool] on Windows and get 'not recognized'. Walk me through checking my PATH one step at a time."* PATH is just the list of places Windows looks for programs.

## Paths look different — that's fine

Windows writes folders as `C:\Users\You\Documents`. Guides written for Mac use `/home/you/documents`. Same idea, different punctuation. When copying a command, swap the path for your real one.

## Files hiding their endings

Windows hides `.txt`/`.md` by default, so `notes.md` shows as "notes." In File Explorer: **View → Show → File name extensions.** Turn it on and leave it on — you can't work with agents while extensions are hidden.

## Antivirus quietly blocking

If a tool worked yesterday and silently fails today, check your antivirus's quarantine or "protected folders" screen. Add your practice folder as an allowed location if it got flagged.

[Next step: Terminal basics](terminal-basics.md){ .md-button }
