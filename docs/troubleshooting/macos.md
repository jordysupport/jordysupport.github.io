---
description: >-
  Check common Mac setup problems with AI tools: app warnings, file access, missing commands, and the difference between local and cloud folders.
---

<span class="kicker">Troubleshooting · macOS</span>

# macOS

Use the exact message to choose your next check. An app warning and a terminal permissions error are different problems.

## "App can't be opened" / unidentified developer

Confirm the download source and check for an updated, signed version from the developer. A warning that macOS cannot verify a developer differs from a warning that the app will damage your computer.

For an unverified app you have checked and trust, macOS may offer **System Settings → Privacy & Security → Open Anyway** after the first attempt. Read [Apple's instructions](https://support.apple.com/en-us/102445) before making the exception. Do not override a malware or damaged-app warning.

On a managed Mac, some security settings are controlled by your organization.

## It wants permission for folders

An app may need permission to read Documents or Desktop. Check which app is asking and which files your task requires. Use a practice folder and copied files for an exercise.

Mac permissions may cover a wider location than one file. Review that scope before approving. Full Disk Access is a broad grant; a routine practice task should not require it just to remove a dialog.

## "Command not found" after installing

Check the command's spelling and whether the installation completed. Quit Terminal and reopen it, then use this read-only check with the actual program name:

```sh
command -v toolname
```

If no path is returned, check the developer's installation instructions. The command name may differ from the app name, or its location may be missing from **PATH**, the folders your shell searches.

```text title="Ask for help"
I installed [tool and version] on macOS. The command [name] gives
"command not found", and command -v [name] returns nothing.
Help me check the installation and PATH one step at a time.
Start with read-only checks.
```

## Homebrew { #homebrew-in-one-paragraph }

Homebrew installs many command-line tools on a Mac. Some guides require it; others provide a standalone installer.

If you need Homebrew, read the installation instructions at [brew.sh](https://brew.sh) and review the command before running it. An install command can download and execute software. Check that it came from the official project and applies to your Mac.

## Find your files { #where-your-stuff-is }

The shortcut `~` means your home folder. For example:

```sh
cd ~/Documents/ai-practice
pwd
ls
```

This works only if that folder exists at that path. iCloud or another sync service may place your files elsewhere. Use Finder to confirm the location, and quote any path containing spaces.

[Open terminal basics](terminal-basics.md){ .md-button }
