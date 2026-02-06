# Installation - Windows

[⬅ Back to Main README](../README.md)

## Prerequisites

- **Python 3**: Required for running the hook scripts
  - Verify: `python --version`
  - Install: Download from [python.org](https://www.python.org/downloads/) or install via `winget install Python.Python.3`
- **Audio Player**: Built-in `winsound` module (included with Python)

All details are mentioned in [HOOKS-README.md](../.claude/hooks/HOOKS-README.md)

---

## Installation

### Step 1: Copy hooks folder

**PowerShell:**
```powershell
cd your-project
New-Item -ItemType Directory -Force -Path .claude\hooks
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
Copy-Item -Recurse -Force temp-hooks\.claude\hooks\* .claude\hooks\
Remove-Item -Recurse -Force temp-hooks
```

**Command Prompt:**
```cmd
cd your-project
if not exist .claude\hooks mkdir .claude\hooks
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
xcopy /E /I /Y temp-hooks\.claude\hooks\* .claude\hooks\
rmdir /S /Q temp-hooks
```

### Step 2: Copy settings.json keys into your existing Claude settings file

1. If you don't have a `.claude/settings.json` file in your project, create one
2. Open [`install/settings-windows.json`](settings-windows.json) and copy the keys (`disableAllHooks` and `hooks`) into your `.claude/settings.json`

> **Why separate settings files per platform?**
> - Python command: `python3` (macOS/Linux) vs `python` (Windows)
> - Script path: `${CLAUDE_PROJECT_DIR}` env variable (macOS/Linux) vs relative path (Windows)

---

## Optional: Test Agent Hooks

To test the agent-specific hooks (PreToolUse, PostToolUse, Stop), copy the demo agent file:

**PowerShell:**
```powershell
cd your-project
New-Item -ItemType Directory -Force -Path .claude\agents
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
Copy-Item temp-hooks\.claude\agents\claude-code-voice-hook-agent.md .claude\agents\
Remove-Item -Recurse -Force temp-hooks
```

**Command Prompt:**
```cmd
cd your-project
if not exist .claude\agents mkdir .claude\agents
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
copy temp-hooks\.claude\agents\claude-code-voice-hook-agent.md .claude\agents\
rmdir /S /Q temp-hooks
```

After copying, run the agent in Claude Code with:
```
/agents claude-code-voice-hook-agent
```

This agent fetches the weather for Dubai and demonstrates the PreToolUse, PostToolUse, and Stop hooks in action.
