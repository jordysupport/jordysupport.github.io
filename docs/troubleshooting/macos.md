# macOS troubleshooting

Most macOS setup problems come from PATH differences, developer tools, permissions, processor architecture, or running a command from the wrong folder.

## Record the basics

```bash
sw_vers
uname -m
echo "$SHELL"
pwd
```

Common architecture results:

- `arm64`: Apple silicon;
- `x86_64`: Intel, or sometimes a process running through translation.

A package built for the wrong architecture can behave strangely even when it appears installed.

## Command Line Tools

Git and build tools may require Apple's Command Line Tools.

Check:

```bash
xcode-select -p
git --version
```

If macOS reports that developer tools are required, use the official installer prompt or:

```bash
xcode-select --install
```

If tools are already installed, do not reinstall them as the first response to every error.

## “Command not found” after installation

Check what the current shell can see:

```bash
command -v git
command -v node
command -v python3
printf '%s\n' "$PATH" | tr ':' '\n'
```

Open a new terminal after installation. Shell startup files may differ:

- `~/.zshrc` for interactive Zsh settings;
- `~/.zprofile` for login-shell environment;
- older setups may use Bash files.

Do not add the same PATH line to every startup file. Identify which shell and installation location are in use.

## Homebrew locations

Common locations are:

```text
/opt/homebrew/bin   # Apple silicon default
/usr/local/bin      # Intel default or other installations
```

Check:

```bash
command -v brew
brew --prefix 2>/dev/null
```

Use Homebrew only when it is the chosen installation method. Do not mix several package managers without tracking which executable is active.

## Wrong working directory

```bash
pwd
ls -la
```

Move to the project before starting an agent:

```bash
cd ~/Projects/project-name
```

Paths with spaces need quotes:

```bash
cd "$HOME/My Projects/site"
```

## File and folder permissions

Inspect a file:

```bash
ls -l path/to/file
```

Inspect a directory path:

```bash
ls -ld path/to/folder
```

Avoid recursive `chmod` or `chown` commands until you understand ownership and the intended permission. A project should rarely require broad write or execute access across your home folder.

## Privacy permissions

macOS may block a terminal or editor from Desktop, Documents, Downloads, external drives, microphone, camera, or other protected data.

When a trusted application truly needs access:

1. identify the exact folder or service;
2. review the macOS privacy prompt or System Settings entry;
3. grant only the needed access;
4. restart the application if required;
5. revoke access when no longer needed.

Do not grant Full Disk Access merely to silence an unexplained error.

## Quarantine and downloaded apps

macOS may warn that downloaded software cannot be opened or cannot be verified. Use the product's official installation and signing guidance.

Do not bypass Gatekeeper with broad commands copied from a forum. Verify the publisher, download source, and package signature first.

## Node and npm

```bash
node --version
npm --version
command -v node
command -v npm
```

If versions differ between Terminal, an editor, and an agent:

- compare `echo "$PATH"`;
- check whether a version manager is initialized;
- reopen the application after changing shell configuration;
- read the project's expected version;
- avoid using `sudo npm install -g` as a general permission fix.

## Python

Use `python3` on many macOS systems:

```bash
python3 --version
python3 -m pip --version
```

Create a project virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

A virtual environment keeps project packages separate from system-managed Python.

## Case-sensitive deployment surprises

A macOS disk may treat filenames as case-insensitive while a Linux deployment is case-sensitive.

Check exact names:

```bash
find . -maxdepth 3 -type f | sort
```

Make sure links and imports match capitalization exactly.

## Intel versus Apple silicon

Check both shell and executable:

```bash
uname -m
file "$(command -v node)" 2>/dev/null
```

If one tool is running under a different architecture, use its official architecture-specific installation guidance. Avoid combining translated and native package directories casually.

## Safe macOS support report

```bash
sw_vers
uname -m
echo "$SHELL"
pwd
command -v git && git --version
command -v python3 && python3 --version
command -v node && node --version
```

Add the exact failing command and error. Redact private path segments and never include credentials.
