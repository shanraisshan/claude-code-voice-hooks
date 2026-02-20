# HOOKS-README
contains all the details, scripts, and instructions for the hooks

## Hook Events Overview - [Official 16 Hooks](https://code.claude.com/docs/en/hooks)
Claude Code provides several hook events that run at different points in the workflow:

| # | Hook | Description | Options |
|:-:|------|-------------|---------|
| 1 | `PreToolUse` | Runs before tool calls (can block them) | `async`, `timeout: 5000` |
| 2 | `PermissionRequest` | Runs when Claude Code requests permission from the user | `async`, `timeout: 5000`, `permission_suggestions` |
| 3 | `PostToolUse` | Runs after tool calls complete successfully | `async`, `timeout: 5000` |
| 4 | `PostToolUseFailure` | Runs after tool calls fail | `async`, `timeout: 5000` |
| 5 | `UserPromptSubmit` | Runs when the user submits a prompt, before Claude processes it | `async`, `timeout: 5000` |
| 6 | `Notification` | Runs when Claude Code sends notifications | `async`, `timeout: 5000` |
| 7 | `Stop` | Runs when Claude Code finishes responding | `async`, `timeout: 5000`, `last_assistant_message` |
| 8 | `SubagentStart` | Runs when subagent tasks start | `async`, `timeout: 5000` |
| 9 | `SubagentStop` | Runs when subagent tasks complete | `async`, `timeout: 5000`, `last_assistant_message`, `agent_transcript_path` |
| 10 | `PreCompact` | Runs before Claude Code is about to run a compact operation | `async`, `timeout: 5000`, `once` |
| 11 | `SessionStart` | Runs when Claude Code starts a new session or resumes an existing session | `async`, `timeout: 5000`, `once`, `agent_type`, `model` |
| 12 | `SessionEnd` | Runs when Claude Code session ends | `async`, `timeout: 5000`, `once` |
| 13 | `Setup` | Runs when Claude Code runs the /setup command for project initialization | `async`, `timeout: 30000` |
| 14 | `TeammateIdle` | Runs when a teammate agent becomes idle (experimental agent teams) | `async`, `timeout: 5000`, `teammate_name`, `team_name` |
| 15 | `TaskCompleted` | Runs when a background task completes (experimental agent teams) | `async`, `timeout: 5000`, `task_id`, `task_subject`, `task_description` |
| 16 | `ConfigChange` | Runs when a configuration file changes during a session | `async`, `timeout: 5000`, `file_path` |

> **Note:** Hooks 14-15 (`TeammateIdle` and `TaskCompleted`) require the experimental agent teams feature. Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` when launching Claude Code to enable them.

### Not in Official Docs

The following items exist in the [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) but are **not listed** in the [Official Hooks Reference](https://code.claude.com/docs/en/hooks):

| Item | Added In | Changelog Reference | Notes |
|------|----------|-------------------|-------|
| `Setup` hook | [v2.1.10](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2110) | "Added new Setup hook event that can be triggered via `--init`, `--init-only`, or `--maintenance` CLI flags for repository setup and maintenance operations" | Not listed in official hooks reference page (15 hooks listed, Setup excluded) |
| Agent frontmatter hooks limited to 3 | [v2.1.0](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#210) | "Added hooks support to agent frontmatter, allowing agents to define PreToolUse, PostToolUse, and Stop hooks scoped to the agent's lifecycle" | Official docs now say "All hook events are supported" in frontmatter, but the changelog only mentions 3 hooks |

## Prerequisites

Before using hooks, ensure you have **Python 3** installed on your system.

### Required Software

#### All Platforms (Windows, macOS, Linux)
- **Python 3**: Required for running the hook scripts
- Verify installation: `python3 --version`

**Installation Instructions:**
- **Windows**: Download from [python.org](https://www.python.org/downloads/) or install via `winget install Python.Python.3`
- **macOS**: Install via `brew install python3` (requires [Homebrew](https://brew.sh/))
- **Linux**: Install via `sudo apt install python3` (Ubuntu/Debian) or `sudo yum install python3` (RHEL/CentOS)

### Audio Players (Optional - Automatically Detected)

The hook scripts automatically detect and use the appropriate audio player for your platform:

- **macOS**: Uses `afplay` (built-in, no installation needed)
- **Linux**: Uses `paplay` from `pulseaudio-utils` - install via `sudo apt install pulseaudio-utils`
- **Windows**: Uses built-in `winsound` module (included with Python)

### How Hooks Are Executed

The hooks are configured in `.claude/settings.json` to run directly with Python 3:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py"
}
```

## Configuring Hooks (Enable/Disable)

Hooks can be easily enabled or disabled at both the global and individual levels.

### Disable All Hooks at Once

Edit `.claude/settings.local.json` and set:
```json
{
  "disableAllHooks": true
}
```

**Note:** The `.claude/settings.local.json` file is git-ignored, so each user can configure their own hook preferences without affecting the team's shared settings in `.claude/settings.json`.

> **Managed Settings:** If an administrator has configured hooks through managed policy settings, `disableAllHooks` set in user, project, or local settings cannot disable those managed hooks (fixed in v2.1.49).

### Disable Individual Hooks

For granular control, you can disable specific hooks by editing the hooks configuration files.

#### Configuration Files

There are two configuration files for managing individual hooks:

1. **`.claude/hooks/config/hooks-config.json`** - The shared/default configuration that is committed to git
2. **`.claude/hooks/config/hooks-config.local.json`** - Your personal overrides (git-ignored)

The local config file (`.local.json`) takes precedence over the shared config, allowing each developer to customize their hook behavior without affecting the team.

#### Shared Configuration

Edit `.claude/hooks/config/hooks-config.json` for team-wide defaults:

```json
{
  "disableLogging": false,
  "disablePreToolUseHook": false,
  "disablePermissionRequestHook": false,
  "disablePostToolUseHook": false,
  "disablePostToolUseFailureHook": false,
  "disableUserPromptSubmitHook": false,
  "disableNotificationHook": false,
  "disableStopHook": false,
  "disableSubagentStartHook": false,
  "disableSubagentStopHook": false,
  "disablePreCompactHook": false,
  "disableSessionStartHook": false,
  "disableSessionEndHook": false,
  "disableSetupHook": false,
  "disableTeammateIdleHook": false,
  "disableTaskCompletedHook": false,
  "disableConfigChangeHook": false
}
```

**Configuration Options:**
- `disableLogging`: Set to `true` to disable logging hook events to `.claude/hooks/logs/hooks-log.jsonl` (useful to prevent log file growth)

#### Local Configuration (Personal Overrides)

Create or edit `.claude/hooks/config/hooks-config.local.json` for personal preferences:

```json
{
  "disableLogging": true,
  "disablePostToolUseHook": true,
  "disableSessionStartHook": true
}
```

In this example, logging is disabled, and the PostToolUse and SessionStart hooks are overridden locally. All other hooks will use the shared configuration values.

**Note:** Individual hook toggles are checked by the hook script (`.claude/hooks/scripts/hooks.py`). Local settings override shared settings, and if a hook is disabled, the script exits silently without playing any sounds or executing hook logic.

### Text to Speech (TTS)
website used to generate sounds: https://elevenlabs.io/
voice used: Samara X

## Agent Frontmatter Hooks

Claude Code 2.1.0 introduced support for agent-specific hooks defined in agent frontmatter files. These hooks only run within the agent's lifecycle and support a subset of hook events.

### Supported Agent Hooks

Agent frontmatter hooks only support **3 hooks**:
- `PreToolUse`: Runs before the agent uses a tool
- `PostToolUse`: Runs after the agent completes a tool use
- `Stop`: Runs when the agent finishes

> **Note:** The [official hooks reference](https://code.claude.com/docs/en/hooks) now states "All hook events are supported" in frontmatter. However, the [v2.1.0 changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#210) only mentions these 3 hooks: *"Added hooks support to agent frontmatter, allowing agents to define PreToolUse, PostToolUse, and Stop hooks scoped to the agent's lifecycle"*. This project follows the changelog specification. See [Not in Official Docs](#not-in-official-docs) for details.

### Agent Sound Folders

Agent-specific sounds are stored in separate folders:
- `.claude/hooks/sounds/agent_pretooluse/`
- `.claude/hooks/sounds/agent_posttooluse/`
- `.claude/hooks/sounds/agent_stop/`

### Creating an Agent with Hooks

1. Create an agent definition file in `.claude/agents/`:

```markdown
---
name: my-agent
description: Description of what this agent does
hooks:
  PreToolUse:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: PreToolUse
  PostToolUse:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: PostToolUse
  Stop:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: Stop
---

Your agent instructions here...
```

2. Add sound files to the agent sound folders:
   - `agent_pretooluse/agent_pretooluse.wav`
   - `agent_posttooluse/agent_posttooluse.wav`
   - `agent_stop/agent_stop.wav`

### Example: Weather Fetcher Agent

See `.claude/agents/claude-code-voice-hook-agent.md` for a complete example of an agent with hooks configured.

### Hook Option: `once: true`

The `once: true` option ensures a hook only runs once per session:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "once": true
}
```

This is useful for hooks like `SessionStart`, `SessionEnd`, and `PreCompact` that should only trigger once.

> **Note:** The `once` option is for **skills only, not agents**. It works in settings-based hooks and skill frontmatter, but is not supported in agent frontmatter hooks.

### Hook Option: `async: true`

Hooks can run in the background without blocking Claude Code's execution by adding `"async": true`:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "async": true
}
```

**When to use async hooks:**
- Logging and analytics
- Notifications and sound effects
- Any side-effect that shouldn't slow down Claude Code

This project uses `async: true` for all hooks since voice notifications are side-effects that don't need to block execution. The `timeout` specifies how long the async hook can run before being terminated.

### Hook Option: `statusMessage`

The `statusMessage` field sets a custom spinner message displayed to the user while the hook is running:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "async": true,
  "statusMessage": "PreToolUse"
}
```

This project sets `statusMessage` to the hook event name on all hooks, so the spinner briefly shows which hook is firing (e.g., "PreToolUse", "SessionStart", "Stop"). This is most visible for synchronous hooks; for async hooks the message flashes briefly before the hook runs in the background.

## Hook Types

Claude Code supports three hook handler types. This project uses `command` hooks for all sound playback.

### `type: "command"` (used by this project)

Runs a shell command. Receives JSON input via stdin, communicates results through exit codes and stdout.

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "async": true
}
```

### `type: "prompt"`

Sends a prompt to a Claude model for single-turn evaluation. The model returns a yes/no decision as JSON (`{"ok": true/false, "reason": "..."}`). Useful for decisions that require judgment rather than deterministic rules.

```json
{
  "type": "prompt",
  "prompt": "Check if all tasks are complete. $ARGUMENTS",
  "timeout": 30
}
```

**Supported events:** PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, UserPromptSubmit, Stop, SubagentStop, TaskCompleted. **Not supported:** TeammateIdle.

### `type: "agent"`

Spawns a subagent with multi-turn tool access (Read, Grep, Glob) to verify conditions before returning a decision. Same response format as prompt hooks. Useful when verification requires inspecting actual files or test output.

```json
{
  "type": "agent",
  "prompt": "Verify that all unit tests pass. $ARGUMENTS",
  "timeout": 120
}
```

## Environment Variables

Claude Code provides these environment variables to hook scripts:

| Variable | Availability | Description |
|----------|-------------|-------------|
| `$CLAUDE_PROJECT_DIR` | All hooks | Project root directory. Wrap in quotes for paths with spaces |
| `$CLAUDE_ENV_FILE` | SessionStart only | File path for persisting environment variables for subsequent Bash commands. Use append (`>>`) to preserve variables from other hooks |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | Plugin's root directory, for scripts bundled with a plugin |
| `$CLAUDE_CODE_REMOTE` | All hooks | Set to `"true"` in remote web environments, not set in local CLI |
| `$CLAUDE_SESSION_ID` | Skill hooks | Current session ID, available in skills with hooks |

## Hooks Management Commands

Claude Code provides built-in commands for managing hooks:

- **`/hooks`** — Interactive hook management UI. View, add, and delete hooks without editing JSON files. Hooks are labeled by source: `[User]`, `[Project]`, `[Local]`, `[Plugin]`. You can also toggle `disableAllHooks` from this menu.
- **`claude hooks reload`** — Reload hooks configuration without restarting the session. Useful after editing settings files (since v2.0.47).

## MCP Tool Matchers

For `PreToolUse`, `PostToolUse`, and `PermissionRequest` hooks, you can match MCP (Model Context Protocol) tools using the pattern `mcp__<server>__<tool>`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "mcp__memory__.*",
      "hooks": [{ "type": "command", "command": "echo 'MCP memory tool used'" }]
    }]
  }
}
```

Full regex is supported: `mcp__memory__.*` (all tools from memory server), `mcp__.*__write.*` (any write tool from any server).

## Known Issues & Workarounds

### Agent Stop Hook Bug (SubagentStop vs Stop)

**Bug Report:** [GitHub Issue #19220](https://github.com/anthropics/claude-code/issues/19220)

**Issue:** When defining a `Stop` hook in an agent's frontmatter, the `hook_event_name` passed to the hook script is `"SubagentStop"` instead of `"Stop"`. This contradicts the official documentation and breaks consistency with other agent hooks (`PreToolUse` and `PostToolUse`), which correctly pass their configured names.

| Hook | Defined As | Received As | Status |
|------|------------|-------------|--------|
| PreToolUse | `PreToolUse:` | `"PreToolUse"` | ✅ Correct |
| PostToolUse | `PostToolUse:` | `"PostToolUse"` | ✅ Correct |
| Stop | `Stop:` | `"SubagentStop"` | ❌ Inconsistent |

**Workaround in `hooks.py`:**

```python
# WORKAROUND: Claude Code bug - agent's Stop hook receives "SubagentStop"
# instead of "Stop" as hook_event_name. Map it back to "Stop".
# See: https://github.com/anthropics/claude-code/issues/19220
if event_name == "SubagentStop":
    event_name = "Stop"
```

**Status:** The [official hooks reference](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents) now documents this as expected behavior: *"For subagents, Stop hooks are automatically converted to SubagentStop since that is the event that fires when a subagent completes."* The workaround in `hooks.py` remains in place to correctly map the event name back for agent-specific sound playback.

### PreToolUse Decision Control Deprecation

The `PreToolUse` hook previously used top-level `decision` and `reason` fields for blocking tool calls. These are now **deprecated**. Use `hookSpecificOutput.permissionDecision` and `hookSpecificOutput.permissionDecisionReason` instead:

| Deprecated | Current |
|-----------|---------|
| `"decision": "approve"` | `"hookSpecificOutput": { "permissionDecision": "allow" }` |
| `"decision": "block"` | `"hookSpecificOutput": { "permissionDecision": "deny" }` |

This does not affect this project since `hooks.py` uses async sound playback and does not use decision control.