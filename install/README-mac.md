# Installation - macOS

[⬅ Back to Main README](../README.md)

## Prerequisites

- **Python 3**: Required for running the hook scripts
  - Verify: `python3 --version`
  - Install: `brew install python3` (requires [Homebrew](https://brew.sh/))
- **Audio Player**: `afplay` (built-in, no installation needed)

All details are mentioned in [HOOKS-README.md](../.claude/hooks/HOOKS-README.md)

---

## Installation

### Step 1: Copy hooks folder

```bash
cd your-project
mkdir -p .claude/hooks
git clone https://github.com/shanraisshan/claude-code-voice-hooks.git temp-hooks
cp -r temp-hooks/.claude/hooks/* .claude/hooks/
rm -rf temp-hooks
```

### Step 2: Copy settings.json keys into your existing Claude settings file

1. If you don't have a `.claude/settings.json` file in your project, create one
2. Open [`install/settings-mac.json`](settings-mac.json) and copy the keys (`disableAllHooks` and `hooks`) into your `.claude/settings.json`

> **Why separate settings files per platform?**
> - Python command: `python3` (macOS/Linux) vs `python` (Windows)
> - Script path: `${CLAUDE_PROJECT_DIR}` env variable (macOS/Linux) vs relative path (Windows)

---

## Optional: Test Agent Hooks

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
