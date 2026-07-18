# Windows gotchas

Follow the official install first: **[jaredrhod.com/start](https://jaredrhod.com/start)**. Come back here if something breaks.

## Before you start

- [ ] You know whether you're in **PowerShell**, **Command Prompt**, or **WSL** (they behave differently — check the window title)
- [ ] Node.js is installed: run `node -v`. If it errors, install the LTS from [nodejs.org](https://nodejs.org)

## Common breaks

### "claude is not recognized as a command"

npm installed it somewhere that's not on your PATH. Close the terminal completely and open a new one first — that fixes it most of the time.

Still broken:

```powershell
npm config get prefix
```

Add that folder to your PATH (Start → "environment variables" → edit Path → add the folder), then open a new terminal.

### Script execution is disabled (PowerShell red text)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Answer `Y`, open a new terminal.

### WSL vs native — which one?

If Jared's guide worked for you natively, stay native. Don't add WSL to the mix unless something requires it — two environments means two PATHs, two Nodes, and files living in two places.

### Vault path looks wrong

Windows paths use backslashes: `C:\Users\you\Documents\Brain`. If a config file complains, try forward slashes instead: `C:/Users/you/Documents/Brain` — most tools accept them and they avoid escaping issues.

---

*Something else broke? Ask in Discord — if it comes up twice, it lands on this page.*
