# Plan: Add TeammateIdle and TaskCompleted Hooks

## Background

Claude Code v2.1.33 introduced two new hook events for multi-agent workflows:
- **TeammateIdle** - Fires when a teammate agent becomes idle in agent teams
- **TaskCompleted** - Fires when a background task completes

These are tied to the experimental agent teams feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Our repo currently supports all 13 established hooks but is missing these two new ones.

## Scope

Add full support for both hooks across all configuration files, scripts, sounds, and documentation — matching the existing pattern used by the other 13 hooks.

---

## Step 1: Add Sound Files

Create sound directories and generate TTS audio files (ElevenLabs, Samara X voice):

```
.claude/hooks/sounds/teammateidle/
  teammateidle.wav
  teammateidle.mp3

.claude/hooks/sounds/taskcompleted/
  taskcompleted.wav
  taskcompleted.mp3
```

**TTS phrases to generate:**
- TeammateIdle: "Teammate idle" or "Teammate is idle"
- TaskCompleted: "Task completed"

---

## Step 2: Update `.claude/settings.json` (macOS/Linux)

Add two new hook entries after the existing `Setup` hook:

```json
"TeammateIdle": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TeammateIdle"
      }
    ]
  }
],
"TaskCompleted": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TaskCompleted"
      }
    ]
  }
]
```

---

## Step 3: Update `.claude/settings-windows.json`

Same as Step 2 but using `python` and relative path:

```json
"TeammateIdle": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python .claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TeammateIdle"
      }
    ]
  }
],
"TaskCompleted": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python .claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TaskCompleted"
      }
    ]
  }
]
```

---

## Step 4: Update `.claude/hooks/config/hooks-config.json`

Add two new toggle flags:

```json
"disableTeammateIdleHook": false,
"disableTaskCompletedHook": false
```

---

## Step 5: Update `.claude/hooks/scripts/hooks.py`

### 5a: Add new event-to-disable mapping

In the config mapping section, add:

```python
"TeammateIdle": "disableTeammateIdleHook",
"TaskCompleted": "disableTaskCompletedHook",
```

### 5b: Add sound file resolution

Ensure the script maps the new event names to their sound directories:
- `"TeammateIdle"` -> `sounds/teammateidle/teammateidle.wav`
- `"TaskCompleted"` -> `sounds/taskcompleted/taskcompleted.wav`

The existing `event_name.lower()` logic should handle this automatically if the directory and file names follow the lowercase convention.

---

## Step 6: Update Documentation

### 6a: `.claude/hooks/HOOKS-README.md`

- Update the hook count from **13** to **15** in the heading and overview
- Add entries 14 and 15 to the numbered list:
  ```
  14. TeammateIdle: Runs when a teammate agent becomes idle (agent teams)
  15. TaskCompleted: Runs when a background task completes
  ```
- Update the shared configuration example to include the two new disable flags
- Add a note that these hooks require the experimental agent teams feature

### 6b: `README.md`

- Update "all 13 hooks" references to "all 15 hooks" throughout
- Add the two new hooks to both macOS/Linux and Windows inline JSON examples
- Update the Features section count

---

## Step 7: Verify

- [ ] Sound files exist in correct directories with both `.wav` and `.mp3` formats
- [ ] `settings.json` has 15 hook entries with `statusMessage`
- [ ] `settings-windows.json` has 15 hook entries with `statusMessage`
- [ ] `hooks-config.json` has 15 disable flags
- [ ] `hooks.py` handles both new event names
- [ ] `HOOKS-README.md` documents 15 hooks
- [ ] `README.md` references 15 hooks
- [ ] Test with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` if possible

---

## How to Enable Agent Teams (Required for These Hooks)

The `TeammateIdle` and `TaskCompleted` hooks only fire when the experimental agent teams feature is active. You must set the environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` when launching Claude Code.

### Option A: Set inline when launching Claude Code

**macOS/Linux:**
```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

**Windows (PowerShell):**
```powershell
$env:CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS="1"; claude
```

**Windows (Command Prompt):**
```cmd
set CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 && claude
```

### Option B: Export in your shell profile (persistent across sessions)

**macOS/Linux** - add to `~/.bashrc`, `~/.zshrc`, or equivalent:
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```
Then restart your terminal or run `source ~/.zshrc` (or `~/.bashrc`).

**Windows** - set as a system/user environment variable:
```powershell
[System.Environment]::SetEnvironmentVariable("CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS", "1", "User")
```
Then restart your terminal.

### Option C: Add to `.claude/settings.local.json` env block

If your Claude Code version supports environment variables in settings, you can add:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Verifying It Works

Once agent teams are enabled, you can trigger the hooks by:
1. Starting a session that spawns teammate agents
2. `TeammateIdle` will fire when a teammate agent finishes its work and becomes idle
3. `TaskCompleted` will fire when a background task finishes

Without the environment variable set, these two hooks will simply never fire (but they won't cause errors either — they just remain dormant).

---

## Notes

- These hooks are part of an **experimental** feature (agent teams). They may change in future releases.
- The `TeammateIdle` and `TaskCompleted` hooks were introduced in v2.1.33 release notes with matcher support for multi-agent workflows.
- Until the feature is stable, consider adding a note in documentation that these two hooks require the experimental flag.
