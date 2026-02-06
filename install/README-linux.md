# Installation - Linux

[⬅ Back to Main README](../README.md)

## Prerequisites

- **Python 3**: Required for running the hook scripts
  - Verify: `python3 --version`
  - Install: `sudo apt install python3` (Ubuntu/Debian) or `sudo yum install python3` (RHEL/CentOS)
- **Audio Player**: `paplay` from `pulseaudio-utils`
  - Install: `sudo apt install pulseaudio-utils`

All details are mentioned in [HOOKS-README.md](../.claude/hooks/HOOKS-README.md)

---

## 1 ■ METHOD: Fresh Installation (No existing `.claude/settings.json`)

Use this method if you **don't have** a `.claude/settings.json` file in your project.

```bash
cd your-project
mkdir -p .claude
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
cp -r temp-hooks/.claude/. .claude/
rm -f .claude/settings-windows.json
rm -rf temp-hooks
```

---

## 2 ■ METHOD: Merge with Existing `.claude/settings.json`

Use this method if you **already have** a `.claude/settings.json` file with your own hooks or settings.

### A ■ Step: Copy only the hook scripts and resources

```bash
cd your-project
mkdir -p .claude/hooks
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
cp -r temp-hooks/.claude/hooks/* .claude/hooks/
rm -rf temp-hooks
```

### B ■ Step: Manually merge hooks into your existing `.claude/settings.json`

Open your existing `.claude/settings.json` and add the 2 keys (disableAllHooks and hooks) below (use `python3`)

```
  "disableAllHooks": false,
  "hooks": {
    "PreToolUse": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "PreToolUse"}]}],
    "PermissionRequest": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "PermissionRequest"}]}],
    "PostToolUse": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "PostToolUse"}]}],
    "PostToolUseFailure": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "PostToolUseFailure"}]}],
    "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "UserPromptSubmit"}]}],
    "Notification": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "Notification"}]}],
    "Stop": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "Stop"}]}],
    "SubagentStart": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "SubagentStart"}]}],
    "SubagentStop": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "SubagentStop"}]}],
    "PreCompact": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "once": true, "statusMessage": "PreCompact"}]}],
    "SessionStart": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "once": true, "statusMessage": "SessionStart"}]}],
    "SessionEnd": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "once": true, "statusMessage": "SessionEnd"}]}],
    "Setup": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 30000, "async": true, "statusMessage": "Setup"}]}],
    "TeammateIdle": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "TeammateIdle"}]}],
    "TaskCompleted": [{"hooks": [{"type": "command", "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py", "timeout": 5000, "async": true, "statusMessage": "TaskCompleted"}]}]
  }
```

**Hook Configuration Options:**
- `timeout`: Maximum time in milliseconds for the hook to complete (5000ms default, 30000ms for Setup)
- `async`: When `true`, hooks run in the background without blocking Claude Code
- `once`: When `true`, the hook runs only once per session (used for SessionStart, SessionEnd, PreCompact)
- `statusMessage`: Custom spinner message shown while the hook runs (set to the hook event name)

---

## 3 ■ Optional: Test Agent Hooks

To test the agent-specific hooks (PreToolUse, PostToolUse, Stop), copy the demo agent file:

```bash
cd your-project
mkdir -p .claude/agents
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
cp temp-hooks/.claude/agents/claude-code-voice-hook-agent.md .claude/agents/
rm -rf temp-hooks
```

After copying, run the agent in Claude Code with:
```
/agents claude-code-voice-hook-agent
```

This agent fetches the weather for Dubai and demonstrates the PreToolUse, PostToolUse, and Stop hooks in action.
