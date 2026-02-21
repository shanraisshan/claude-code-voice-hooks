---
name: claude-code-voice-hook-agent
description: Plays agent-specific sounds for the 6 hooks that actually fire in agent sessions
model: opus
color: red
hooks:
  PreToolUse:
    - matcher: ".*"
      hooks:
        - type: command
          command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py  --agent=voice-hook-agent
          timeout: 5000
          async: true
  PostToolUse:
    - matcher: ".*"
      hooks:
        - type: command
          command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py  --agent=voice-hook-agent
          timeout: 5000
          async: true
  PermissionRequest:
    - matcher: ".*"
      hooks:
        - type: command
          command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py  --agent=voice-hook-agent
          timeout: 5000
          async: true
  PostToolUseFailure:
    - hooks:
        - type: command
          command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py  --agent=voice-hook-agent
          timeout: 5000
          async: true
  Stop:
    - hooks:
        - type: command
          command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py  --agent=voice-hook-agent
          timeout: 5000
          async: true
  SubagentStop:
    - hooks:
        - type: command
          command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py  --agent=voice-hook-agent"
          timeout: 5000
          async: true
---

You are the claude-code-voice-hook-agent. Your goal is to trigger all 6 configured hooks (the only ones that actually fire in agent sessions) with sound playback. Follow ALL steps below in order.

## Step-by-Step Workflow

### Step 1: Read a file (triggers PreToolUse + PostToolUse)
Read the file `.claude/agents/claude-code-voice-hook-agent.md` to confirm the hooks config.

### Step 2: Web search (triggers PreToolUse + PostToolUse again)
Search the web for "current weather in Dubai UAE today" to get live weather data.

### Step 3: Write a file (triggers PreToolUse + PostToolUse, may trigger PermissionRequest)
Write the weather results to `tests-agents-hook/dubai-weather-report.txt`.

### Step 4: Run a bash command (triggers PreToolUse + PostToolUse, may trigger PermissionRequest)
Run: `echo "Voice hook agent executed at $(date)"`

### Step 5: Intentionally read a non-existent file (triggers PostToolUseFailure)
Try to read `tests-agents-hook/this-file-does-not-exist-12345.txt` — this WILL fail and that is intentional to trigger the PostToolUseFailure hook.

### Step 6: Fetch a URL (triggers PreToolUse + PostToolUse)
Fetch https://wttr.in/Dubai?format=3 to get a compact weather summary.

## Hooks Configured (6 of 16 — only the ones that actually fire)
- **PreToolUse** — fires before every tool call (plays agent_pretooluse sound)
- **PostToolUse** — fires after every successful tool call (plays agent_posttooluse sound)
- **PermissionRequest** — fires when a tool needs user permission (plays agent_permissionrequest sound)
- **PostToolUseFailure** — fires after a failed tool call (plays agent_posttoolusefailure sound)
- **Stop** — fires when the agent session ends (plays agent_stop sound)
- **SubagentStop** — fires when a subagent completes (plays agent_subagentstop sound)

## Output Format

After completing all steps, provide:

1. **Weather Report:**
   - Location: Dubai, UAE
   - Temperature: [Celsius and Fahrenheit]
   - Conditions: [description]
   - Humidity: [percentage]
   - Wind: [speed and direction]

2. **Sound Playback:** Confirm whether sounds played during the workflow.
