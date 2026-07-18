# Windows troubleshooting

Windows AI-tool setup problems usually come from one of four boundaries: the shell, PATH, execution policy, or mixing Windows and WSL paths.

## First identify your environment

### PowerShell

Windows-native shell. Paths usually look like:

```text
C:\Users\Jordy\project
```

### Command Prompt

Older Windows-native shell. Some PowerShell commands will not work here.

### WSL

A Linux environment inside Windows. Paths usually look like:

```text
/home/jordy/project
/mnt/c/Users/Jordy/project
```

### Codespaces

A remote Linux development environment opened through the browser or VS Code. Paths commonly begin with:

```text
/workspaces/
```

Run instructions for the environment you are actually using. Do not combine PowerShell syntax with a WSL shell unless the guide explicitly says to.

## Record the basics

In PowerShell:

```powershell
$PSVersionTable.PSVersion
Get-Location
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsArchitecture
```

For common tools:

```powershell
Get-Command git -ErrorAction SilentlyContinue
git --version
Get-Command node -ErrorAction SilentlyContinue
node --version
Get-Command python -ErrorAction SilentlyContinue
python --version
```

If `Get-Command` finds nothing, the program may not be installed or may not be on PATH for this shell.

## “Command not found” after installation

1. Close and reopen the terminal.
2. Run `Get-Command <program>`.
3. Check the installer completed for the current user.
4. Check whether the application added its folder to the user or system PATH.
5. Avoid adding random directories until you know where the executable actually is.

Find candidates:

```powershell
where.exe git
where.exe node
where.exe python
```

`where.exe` may return several versions. The first one found on PATH often wins.

Inspect PATH without changing it:

```powershell
$env:Path -split ';'
```

Do not paste the full output publicly if it reveals private usernames or internal locations.

## PowerShell execution policy

An error may say scripts are disabled. Check current policies:

```powershell
Get-ExecutionPolicy -List
```

Execution policy is a Windows safety feature and not a complete security boundary. Do not use `Unrestricted` or change machine-wide policy as a reflex.

When a trusted tool's official instructions require a user-level change, a commonly used scoped command is:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Before running it:

- confirm the error is actually caused by execution policy;
- understand your organization's policy;
- use the narrowest scope;
- install scripts only from trusted sources.

You can inspect a file's origin and unblock a specific trusted downloaded file rather than weakening policy broadly:

```powershell
Get-Item .\script.ps1 -Stream Zone.Identifier -ErrorAction SilentlyContinue
Unblock-File .\script.ps1
```

Only unblock a file you have verified.

## Working directory problems

Check:

```powershell
Get-Location
Get-ChildItem -Force
```

Move to the project:

```powershell
Set-Location "$HOME\project-name"
```

Then verify the expected files are present. Starting an agent from `C:\Users\Jordy` may unintentionally expose or search far more than the intended project.

## Windows path mistakes

### Spaces

Use quotes:

```powershell
Set-Location "C:\Users\Jordy\My Projects\site"
```

### Backslashes versus forward slashes

PowerShell commonly accepts both in many tools, but not every program behaves the same. Use the path style shown by the tool's official Windows instructions.

### Case

Windows file lookup is usually case-insensitive, while GitHub deployment and Linux environments can be case-sensitive. A link to `Images/Logo.png` may fail if the actual folder is `images`.

### Cloud-synced folders

OneDrive or another sync tool can introduce placeholder files, locks, or delayed changes. For development projects, a normal local folder or Codespace may be easier to diagnose.

## WSL path mixing

A Windows program may not understand a Linux path, and a Linux program may require `/mnt/c/...` for Windows files.

Inside WSL:

```bash
pwd
which git
git --version
```

In PowerShell:

```powershell
Get-Location
Get-Command git
git --version
```

Those may refer to different installations and credentials.

Do not install the same tool repeatedly in both environments until you decide where the project will run.

## Node and npm issues

Check:

```powershell
node --version
npm --version
Get-Command node
Get-Command npm
```

Common causes:

- new terminal was not opened after installation;
- several Node installations are on PATH;
- the project expects a different version;
- PowerShell is blocking an npm script wrapper;
- dependencies were installed in another environment.

Read the project's version file or official setup instructions before upgrading or downgrading.

## Python and virtual environments

Windows may expose `python`, `py`, or both.

```powershell
python --version
py --version
```

Create and activate a project environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If activation is blocked, diagnose execution policy rather than installing packages globally as a workaround.

## Git line endings

Windows and Linux may use different line endings. Avoid mass conversion during an unrelated edit.

Inspect Git's setting:

```powershell
git config --show-origin --get core.autocrlf
```

Use the repository's `.gitattributes` if present. Review `git diff` before committing a change that appears to touch every line.

## File permission versus execution policy

These are different:

- “running scripts is disabled” points to PowerShell execution policy;
- “access denied” may point to filesystem permissions, antivirus, a locked file, or controlled folder access;
- “command not found” points to installation or PATH;
- “module not found” often points to the wrong runtime environment or missing project dependency.

Match the fix to the evidence.

## Safe Windows support report

```powershell
$PSVersionTable.PSVersion
Get-Location
Get-ChildItem -Force | Select-Object Name
Get-Command git -ErrorAction SilentlyContinue
git --version
Get-ExecutionPolicy -List
```

Add the failing tool's version and exact error. Remove usernames or private paths if posting publicly, and never include secrets.
