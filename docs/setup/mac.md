# Mac gotchas

Follow the official install first: **[jaredrhod.com/start](https://jaredrhod.com/start)**. Come back here if something breaks.

## Common breaks

### "command not found: claude"

Close Terminal completely (⌘Q) and reopen. If still broken:

```bash
npm config get prefix
```

If that prints something like `/usr/local` or `~/.npm-global`, add its `bin` folder to your PATH:

```bash
echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### "command not found: npm"

Node isn't installed. Easiest route:

```bash
xcode-select --install
```

Then install Node LTS from [nodejs.org](https://nodejs.org), or via Homebrew if you have it: `brew install node`.

### Permission errors during npm install (EACCES)

Don't use `sudo`. Instead point npm at a folder you own:

```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
```

Then rerun the install command from Jared's guide.

### Finding your vault path

Drag your Obsidian vault folder from Finder into the Terminal window — it pastes the full path for you.

---

*Something else broke? Ask in Discord — if it comes up twice, it lands on this page.*
