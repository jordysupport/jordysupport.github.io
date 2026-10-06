---
description: >-
  Check common Windows setup problems with AI tools: the selected shell, program lookup, paths, file extensions, and blocked apps.
---

<span class="kicker">Troubleshooting · Windows</span>

# Windows

Start with the exact error. A missing command, a blocked app, and an inaccessible file need different checks.

## "Windows protected your PC" when installing

Confirm where the installer came from and who published it. Check the developer's official Windows installation instructions and whether there is a newer signed installer.

An unfamiliar-app warning is not proof that a download is safe or unsafe. If Windows reports a threat or quarantines a file, review **Windows Security → Protection history** and the detection details before acting. Do not turn off protection or exclude your whole working folder to finish an install. [Microsoft's Protection history guide](https://support.microsoft.com/en-us/windows/security/windows-security/protection-history-in-the-windows-security-app)

On a work-managed computer, use the approved installation route.

## PowerShell vs Command Prompt confusion

Windows Terminal is the window; PowerShell and Command Prompt are shells you can run inside it. Check the tab label. The Windows examples on this site use PowerShell.

Commands written for Mac, Linux, or WSL can fail in PowerShell. Tell the AI which shell you use before asking it to adapt a command.

## "Not recognized as a command" after installing

1. Check the spelling and whether the installer finished successfully.
2. Close the terminal window and open a new one.
3. Ask PowerShell where it finds the program. Replace `toolname` below with its actual command name:

```powershell
Get-Command toolname
```

If it is still missing, check the developer's installation instructions. **PATH** is the list of folders where the shell looks for programs. Find the installed location before editing it.

```text title="Ask for help"
I installed [tool and version] on Windows and use PowerShell.
The exact error is [paste it]. Get-Command [command name] returns
[paste result]. Help me check the installed location and PATH.
Start with read-only checks and explain each step.
```

## Use the actual path { #paths-look-different-thats-fine }

A Windows path may look like `C:\Users\You\Documents\ai-practice`. Mac paths use forward slashes. WSL has its own Linux paths, even though it runs on Windows.

Copy the real folder path from File Explorer rather than guessing from a guide. Quote paths with spaces. A synced or redirected Documents folder may live somewhere different from the example.

## Show file extensions { #files-hiding-their-endings }

In Windows 11 File Explorer, select **View → Show → File name extensions**. This makes it easier to spot `notes.md.txt` when you meant to create `notes.md`.

Changing an extension changes the filename; it does not convert the contents into a different format.

## An app cannot save or disappears { #antivirus-quietly-blocking }

Check the error, destination folder, and **Windows Security → Protection history**. A blocked save may involve folder protection; a removed executable may have been quarantined.

Read the detection details before restoring a file or allowing an app. Keep the change specific to a trusted program and the access it needs. [Microsoft's virus and threat protection guide](https://support.microsoft.com/en-us/windows/security/threat-malware-protection/virus-and-threat-protection-in-the-windows-security-app)

[Open terminal basics](terminal-basics.md){ .md-button }
