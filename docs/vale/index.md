---
description: >-
  Download VALE for Windows: a free voice assistant with four visual worlds, local speech, and music-reactive fields. One prompt installs it via your AI.
---

<div class="vale-hero" markdown>

<span class="kicker">VALE / Windows Desktop Preview</span>

# A voice assistant you can see.

VALE turns listening, thinking, speaking, and music into a living full-screen environment. Four visual fields, local speech, a cinematic interface, and music reactions that belong to each world.

[Download VALE for Windows](https://github.com/jordysupport/jordysupport.github.io/releases/latest/download/VALE-Windows-x64.zip){ .md-button .md-button--primary }
[Watch the real-time demo](demo.md){ .md-button }
[Release details](https://github.com/jordysupport/jordysupport.github.io/releases/latest){ .md-button }

</div>

<div class="vale-preview">
  <img src="/assets/vale-demo/vale-cosmos-hero.webp" alt="Fresh VALE COSMOS render showing its music-active stellar field and playback interface">
</div>

<p class="vale-preview-note">Captured from the current Windows build. <a href="demo/">See the full silent demo and download the new render assets →</a></p>

<div class="vale-facts">
  <div><strong>Current release</strong><span>0.2.1 Preview</span></div>
  <div><strong>Platform</strong><span>Windows 10 / 11</span></div>
  <div><strong>Visual fields</strong><span>Four distinct worlds</span></div>
  <div><strong>Speech</strong><span>Local Whisper + Kokoro</span></div>
  <div><strong>AI connection</strong><span>Your Codex or Claude subscription</span></div>
</div>

!!! success "Updated July 20, 2026"
    Version 0.2.1 improves Windows service ownership detection so **Start VALE** and **Stop VALE** reliably recognize and manage the local Kokoro voice process.

## Give your agent one prompt

<div class="vale-install">
  <div><strong>Copy the prompt</strong>Use the copy button on the setup prompt below.</div>
  <div><strong>Paste it into your agent</strong>Use Codex or Claude Code on the Windows PC where VALE will run.</div>
  <div><strong>Let the agent verify everything</strong>It downloads, checks, installs, connects, tests, and starts VALE.</div>
</div>

```text
Install the latest public VALE for Windows release from:
https://github.com/jordysupport/jordysupport.github.io/releases/latest

Complete and verify the setup for me. Do not ask me to run terminal commands that you can safely run yourself.

1. Confirm this is 64-bit Windows 10 or Windows 11.
2. Download VALE-Windows-x64.zip and VALE-Windows-x64.zip.sha256 from the latest release into a new temporary folder.
3. Verify the ZIP against the SHA-256 checksum. Stop if verification fails.
4. Extract it and read README.md, RELEASE_NOTES.md, and INSTALL WITH YOUR AI AGENT.md.
5. Confirm your own CLI is authenticated with my existing subscription: use `codex login status` if you are Codex or `claude auth status` if you are Claude Code. Never request, reveal, copy, or manufacture an API key or authentication token. If the official CLI is unavailable, install it from the provider's official documentation and ask me only to complete an official browser sign-in if required.
6. Run scripts\Install-VALEForAgent.ps1 with `-AgentRuntime Codex` or `-AgentRuntime Claude`, matching the agent you are. Use the default per-user install location. Do not skip integrity checks, dependencies, the response probe, or diagnostics.
7. Run the installed scripts\Test-VALEInstallation.ps1, resolve every required failure, start VALE, and report the version, selected agent runtime, diagnostic result, and remaining warnings. Never include credentials or authentication-file contents.

VALE must use my authenticated agent CLI as its language-model backend. Whisper transcription and Kokoro speech generation must remain local. Do not configure a metered API key unless I explicitly reject subscription-agent mode and request an API endpoint instead.
```

This reuses the agent CLI's existing subscription session. VALE does not read, copy, or store the login. Codex runs ephemerally in a read-only sandbox; Claude runs with tools disabled and session persistence off. Agent usage is still subject to the limits of the person's plan.

The first setup downloads the local Kokoro voice runtime, so the agent may need several minutes and at least **4 GB of free disk space**.

[Download the Windows preview](https://github.com/jordysupport/jordysupport.github.io/releases/latest/download/VALE-Windows-x64.zip){ .md-button .md-button--primary }
[SHA-256 checksum](https://github.com/jordysupport/jordysupport.github.io/releases/latest/download/VALE-Windows-x64.zip.sha256){ .md-button }

## What it does

<div class="grid cards" markdown>

-   **Four native visual worlds**

    ECLIPSE, AXIOM, COSMOS, and PELAGOS have their own geometry, transitions, voice states, and music behavior.

-   **A real voice line**

    Hold **Right Ctrl** to speak. Whisper transcribes locally; Kokoro replies with the Bella voice by default.

-   **Music that moves the field**

    Play music in Spotify Desktop. VALE reads the Windows media session and system audio so each field reacts in its own visual language.

-   **Cinema without the clutter**

    Full-screen display controls, screen selection, captions, and a cinema mode designed for a dedicated monitor.

</div>

## No separate API billing required

The recommended setup connects VALE to an already-authenticated Codex or Claude Code CLI. It does not turn a subscription login into an API key, and it never copies agent credentials. Instead, a loopback-only bridge asks the signed-in CLI for each response using the person's existing plan access.

People who prefer Ollama or another OpenAI-compatible endpoint can still use the manual **Install VALE.cmd** path and provide their own endpoint. An API key is needed only when that chosen endpoint requires one.

## Privacy in plain English

- Your microphone recording is transcribed on your PC.
- Kokoro generates VALE's speech on your PC.
- In agent mode, only the conversation text is handed to the authenticated local agent CLI.
- VALE does not read or store the agent CLI's credentials.
- In manual endpoint mode, any optional API key stays in the local VALE installation.
- The public download contains no personal token, machine path, or private network address.

## Controls

| Control | Action |
| --- | --- |
| Hold **Right Ctrl** | Speak to VALE |
| **1-4** | Switch visual fields |
| **M** | Toggle cinema mode |
| **C** | Toggle captions |
| Spotify Desktop | Drive music visuals and playback controls |

If setup or audio ever behaves unexpectedly, run **Check VALE** from the Start Menu. It verifies the download, local runtimes, agent authentication, microphone visibility, browser, and port conflicts without showing credentials.

!!! note "Windows preview"
    This release is built and tested for 64-bit Windows. It requires Chrome or Microsoft Edge and an internet connection during the first installation.
