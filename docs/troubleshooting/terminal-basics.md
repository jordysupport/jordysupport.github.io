# Terminal basics

The terminal is a text interface for starting programs and working with files. An AI coding or file agent often runs there because the terminal provides a clear current folder, visible commands, and direct feedback.

## The prompt

You may see something like:

```text
@jordysupport ➜ /workspaces/setup (main) $
```

It tells you:

- user: `jordysupport`;
- current folder: `/workspaces/setup`;
- Git branch: `main`;
- `$`: ready for a command.

Do not copy the prompt itself. Type only the command after `$`.

## Current folder

The current folder is where relative paths begin.

=== "macOS, Linux, or Codespaces"

    ```bash
    pwd
    ```

=== "Windows PowerShell"

    ```powershell
    Get-Location
    ```

If an agent cannot find project instructions, check this first.

## List files

=== "macOS, Linux, or Codespaces"

    ```bash
    ls
    ls -la
    ```

=== "Windows PowerShell"

    ```powershell
    Get-ChildItem
    Get-ChildItem -Force
    ```

The expanded command includes hidden files such as `.git` or `.env`. Do not paste secret-file contents.

## Change folders

```bash
cd folder-name
cd ..
cd ~
```

PowerShell uses `cd` too.

- `cd folder-name`: enter a child folder;
- `cd ..`: move to the parent;
- `cd ~`: move to your home folder.

Paths containing spaces need quotes:

```bash
cd "My Projects/site"
```

## Create folders

=== "macOS, Linux, or Codespaces"

    ```bash
    mkdir project
    mkdir -p project/input project/output
    ```

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Force project
    New-Item -ItemType Directory -Force project\input, project\output
    ```

## Read a text file

=== "macOS, Linux, or Codespaces"

    ```bash
    cat README.md
    less README.md
    ```

=== "Windows PowerShell"

    ```powershell
    Get-Content README.md
    ```

Use an editor for large files. `less` exits with `q`.

## Open the current folder in VS Code

```bash
code .
```

The dot means “this folder.”

## Check a program and version

=== "macOS, Linux, or Codespaces"

    ```bash
    command -v git
    git --version
    ```

=== "Windows PowerShell"

    ```powershell
    Get-Command git
    git --version
    ```

A version command proves the current terminal can locate and start the program.

## Understand command pieces

```bash
git commit -m "Update guide"
```

- `git`: program;
- `commit`: subcommand;
- `-m`: option;
- `"Update guide"`: value for the option.

Do not split a command into separate lines unless the instructions show a continuation character or separate commands.

## Exit status

Programs normally return a status code:

- `0`: success;
- nonzero: failure or special condition.

=== "macOS, Linux, or Codespaces"

    ```bash
    echo $?
    ```

=== "Windows PowerShell"

    ```powershell
    $LASTEXITCODE
    ```

Read the error text as well. A status code alone does not explain the cause.

## Stop a running command

Press:

```text
Ctrl+C
```

This commonly stops a local server or command that is waiting. It does not close the terminal.

## Command history

Use the Up Arrow to recall previous commands. Check the command before pressing Enter, especially after moving to a different project.

=== "macOS, Linux, or Codespaces"

    ```bash
    history | tail -20
    ```

=== "Windows PowerShell"

    ```powershell
    Get-History
    ```

History may contain sensitive arguments. Do not share it blindly.

## Paths: absolute and relative

Absolute path:

```text
/workspaces/setup/docs/index.md
C:\Users\Jordy\project\docs\index.md
```

Relative path from the project root:

```text
docs/index.md
```

Relative paths depend on the current folder. Absolute paths identify one location but vary between computers.

## Environment variables

Environment variables provide configuration to programs.

=== "macOS, Linux, or Codespaces"

    ```bash
    echo "$HOME"
    printenv PATH
    ```

=== "Windows PowerShell"

    ```powershell
    $HOME
    $env:Path
    ```

Do not run commands that print all environment variables in a shared transcript; secrets may be included.

## Pipes and redirection

These symbols deserve care:

- `>` writes output to a file and **overwrites** it;
- `>>` appends output;
- `|` sends one command's output into another;
- `&&` runs the next command only after success in many shells;
- `;` separates commands.

Read the full line before running it.

## Commands to pause before approving

```text
rm -rf
sudo
chmod -R
chown -R
curl ... | sh
wget ... | bash
git reset --hard
git clean -fd
```

Do not run an unfamiliar destructive, administrative, or download-and-execute command just because it is presented in a code block.

## Safe learning routine

1. Create a practice folder.
2. Use `pwd` or `Get-Location` before file commands.
3. List files before editing.
4. Use copies.
5. Read the output after every command.
6. Stop when the output differs from the expected result.
7. Save the exact error.

The terminal becomes much less intimidating when location, command, expected result, and recovery are explicit.
