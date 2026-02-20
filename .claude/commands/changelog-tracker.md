---
description: Track Claude Code changelog and find what needs updating in this repo
argument-hint: [number of versions to check, default 10]
---

# Changelog Tracker Command

You are a tracker agent for the claude-code-voice-hooks project. Your job is to analyze the last N versions from the Claude Code changelog and determine what changes need to be made in this repo.

**Versions to check:** `$ARGUMENTS` (default: 10 if empty or not a number)

## IMPORTANT: This is a read-then-report workflow

You will fetch external sources, read local files, compare them, and produce a comprehensive report. Only take action (like calling `/add-new-hook`) if the user approves.

---

## Phase 1: Gather External Data

### 1a: Fetch the Official Hooks Reference

Fetch `https://code.claude.com/docs/en/hooks` using WebFetch.

Extract:
- The **complete list of officially supported hooks** with descriptions
- **Matcher support** for each hook (which hooks support matchers and what values)
- **Hook options** (once, async, timeout, statusMessage, etc.)
- **Input schemas** for each hook event (what JSON fields are sent via stdin)
- **Decision control** patterns per hook (exit codes, JSON output, hookSpecificOutput)
- **Can-block status** for each hook (which hooks support exit code 2 blocking)
- **New features or flags** mentioned in the docs
- **Experimental features** and their required environment variables

### 1b: Fetch the Hooks Guide

Fetch `https://code.claude.com/docs/en/hooks-guide` using WebFetch.

Extract:
- **Hook types**: `command`, `prompt`, and `agent` — identify if new types have been added
- **Matcher values** for each hook event (comprehensive list with examples)
- **New use cases** or patterns documented (e.g. auto-formatting, file protection, config auditing)
- **Hook location scopes** (user, project, local, managed policy, plugin, skill/agent frontmatter)
- **Limitations and known issues** mentioned in the troubleshooting section
- **Environment variables** like `CLAUDE_ENV_FILE`, `CLAUDE_PROJECT_DIR`, `CLAUDE_PLUGIN_ROOT`, `CLAUDE_CODE_REMOTE`
- **Security considerations** and best practices

### 1c: Fetch the Changelog

Fetch `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` using WebFetch.

Extract the **last N version entries** (where N is the argument, default 10). For each version, capture:
- Version number (e.g. `v2.1.49`)
- Release date
- All changes, especially:
  - **New hooks** added
  - **Hook behavior changes** (matchers, new fields, deprecations)
  - **Hook bug fixes**
  - **New hook options** (new fields like `once`, `async`, matchers)
  - **Breaking changes** affecting hooks
  - **New experimental features** related to hooks
  - **Agent/subagent changes** that affect hook behavior
  - **New hook types** (prompt-based, agent-based)

Run all three fetches (1a, 1b, 1c) in **parallel**.

---

## Phase 2: Read Local Repository State

Read ALL of the following files to understand the current state of the repo. Read them in **parallel**:

1. **`.claude/settings.json`** — Current hook configurations
2. **`.claude/hooks/scripts/hooks.py`** — `HOOK_SOUND_MAP` and `AGENT_HOOK_SOUND_MAP` entries
3. **`.claude/hooks/config/hooks-config.json`** — Disable toggles
4. **`.claude/hooks/HOOKS-README.md`** — Hook documentation, descriptions, notes, known issues
5. **`README.md`** — Badge versions, changelog table
6. **`install/settings-mac.json`** — Mac settings
7. **`install/settings-linux.json`** — Linux settings
8. **`install/settings-windows.json`** — Windows settings
9. **`presentation/index.html`** — Slide deck (hook count, version, slides)

Also check what sound folders exist:
- List directories in `.claude/hooks/sounds/` to see which hooks have sound files

---

## Phase 3: Comprehensive Analysis

Compare the external data (changelog + hooks reference + hooks guide) against the local repo state. Check for ALL of the following:

### 3a: Missing Hooks

Compare the official hooks list from the docs against `HOOK_SOUND_MAP` in `hooks.py`.

For each hook in the official docs that is NOT in the repo:
- Note the hook name
- Note which version introduced it (from changelog)
- Note if it requires experimental features
- Flag it as **ACTION: Add new hook via `/add-new-hook <HookName>`**

### 3b: Hook Configuration Drift

For each hook that IS in the repo, verify:
- Is the hook in ALL 4 settings files? (main, mac, linux, windows)
- Does `hooks-config.json` have a disable toggle for it?
- Does `HOOK_SOUND_MAP` have an entry?
- Does a sound folder exist with `.mp3` and `.wav` files?
- Is it listed in `HOOKS-README.md`?
- Is it in the presentation?

Flag any inconsistencies as **ACTION: Fix configuration drift**

### 3c: Version and Badge Accuracy

- Does the README badge version match the latest Claude Code version?
- Does the README badge hook count match the actual number of hooks?
- Does the changelog table in README reflect the latest additions?
- Does `HOOKS-README.md` heading count match the actual count?
- Does `hooks.py` docstring count match the actual count?
- Does the presentation show the correct version and hook count?

Flag mismatches as **ACTION: Update version/count references**

### 3d: Hook Behavior Changes (HIGH PRIORITY)

From the changelog, identify any changes to existing hooks:
- **New input fields** added to hook events (e.g. `last_assistant_message` added to Stop/SubagentStop)
- New matcher values added to hooks
- Changed hook behavior or timing
- New hook options or configuration fields
- Deprecated features

**CRITICAL: New input fields are major changes.** They must be:
1. Added to the README.md changelog table as a dedicated row (e.g. "Added `last_assistant_message` to Stop/SubagentStop inputs")
2. Documented in HOOKS-README.md
3. Reflected in presentation slides for the affected hooks
4. Flagged as **ACTION: Document new input field** (not just generic "update docs")

Do NOT dismiss new input fields as "informational" or "doesn't affect our hooks" — this repo is a comprehensive hooks reference, not just a sound player. Every change to hook inputs matters.

### 3e: Bug Fixes and Known Issues

From the changelog, identify:
- Bug fixes for hooks that we have workarounds for (check Known Issues section in HOOKS-README.md)
- New bugs reported that affect this project
- Workarounds that can now be removed

For example, check if the "SubagentStop vs Stop" bug (GitHub Issue #19220) has been fixed in any recent version. If so, flag as **ACTION: Remove workaround in hooks.py**

### 3f: New Hook Options or Features

From the changelog and docs, identify:
- New hook configuration options (beyond `type`, `command`, `timeout`, `async`, `once`, `statusMessage`)
- New matcher capabilities
- New environment variables or experimental flags
- Agent hook improvements
- **New hook input fields** (these overlap with 3d — ensure they are flagged in BOTH places)

Flag configuration options this project should adopt as **ACTION: Adopt new feature**
Flag new input fields as **ACTION: Document new input field** (high priority — see 3d)

### 3g: Matcher Values Accuracy

The hooks reference documents specific matcher values for each hook event. Compare what the official docs say against what `HOOKS-README.md` documents:

| Event | Matcher Field | Official Values (from docs) |
|-------|--------------|----------------------------|
| PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest | tool name | `Bash`, `Edit\|Write`, `mcp__.*`, etc. |
| SessionStart | how session started | `startup`, `resume`, `clear`, `compact` |
| SessionEnd | why session ended | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other` |
| Notification | notification type | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` |
| SubagentStart, SubagentStop | agent type | `Bash`, `Explore`, `Plan`, or custom agent names |
| PreCompact | compaction trigger | `manual`, `auto` |
| ConfigChange | config source | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
| UserPromptSubmit, Stop, TeammateIdle, TaskCompleted | no matcher | always fires |

Check if `HOOKS-README.md` and the presentation slides document these matcher values. Flag any missing or outdated matcher information as **ACTION: Update matcher documentation**

### 3h: Hook Can-Block Status

The hooks reference documents which hooks can block actions (exit code 2) and which cannot. Verify the presentation slides correctly show `can-block` or `cannot-block` for each hook:

**Can block (exit 2):** PreToolUse, PermissionRequest, UserPromptSubmit, Stop, SubagentStop, TeammateIdle, TaskCompleted, ConfigChange
**Cannot block:** PostToolUse, PostToolUseFailure, Notification, SubagentStart, SessionStart, SessionEnd, PreCompact

Flag any incorrect can-block labels as **ACTION: Fix can-block status**

### 3i: Hook Input Schema Documentation

The hooks reference provides detailed input schemas for each hook event (what JSON fields are sent via stdin). Check if `HOOKS-README.md` documents these input fields or if they should be added. Key fields to verify:

- **Common fields**: `session_id`, `transcript_path`, `cwd`, `permission_mode`, `hook_event_name`
- **Stop/SubagentStop**: `stop_hook_active`, `last_assistant_message`
- **SessionStart**: `source`, `model`, `agent_type`, `CLAUDE_ENV_FILE`
- **ConfigChange**: `source`, `file_path`
- **TeammateIdle**: `teammate_name`, `team_name`
- **TaskCompleted**: `task_id`, `task_subject`, `task_description`, `teammate_name`, `team_name`

Flag undocumented schemas as **ACTION: Update input schema documentation**

### 3j: Hook Types (Command, Prompt, Agent)

The docs now support three hook types:
- `type: "command"` — shell command (what this project uses)
- `type: "prompt"` — single-turn LLM evaluation (Haiku by default)
- `type: "agent"` — multi-turn subagent with tool access

Check if `HOOKS-README.md` mentions these hook types. If not, consider whether the documentation should reference them for completeness. Flag as **ACTION: Document hook types** if missing.

### 3k: Environment Variables and Security

Check if `HOOKS-README.md` documents these environment variables from the official docs:
- `CLAUDE_PROJECT_DIR` — project root path
- `CLAUDE_ENV_FILE` — file path for persisting env vars (SessionStart only)
- `CLAUDE_PLUGIN_ROOT` — plugin root directory
- `CLAUDE_CODE_REMOTE` — set to `"true"` in remote web environments

Also check if security best practices from the docs are mentioned (input validation, path traversal prevention, quoting shell variables).

Flag missing info as **ACTION: Update environment variable / security documentation**

### 3l: Hooks That May Have Been Removed or Renamed

Cross-reference our repo's hook list against the official docs lifecycle table. If a hook exists in our repo but NOT in the official docs, it may have been deprecated or removed. For example, check if `Setup` is still listed in the official docs.

Flag any hooks in our repo that are NOT in the official docs as **ACTION: Investigate potentially removed hook**

### 3n: Hook Options Table Accuracy (HOOKS-README.md)

The `HOOKS-README.md` file contains a four-column table in the "Hook Events Overview" section. The 4th column ("Options") lists the hook options and input fields for each hook. Cross-reference this table against the official docs and changelog to detect any drift.

**Current expected Options per hook:**

| Hook | Expected Options |
|------|-----------------|
| PreToolUse | `async`, `timeout: 5000` |
| PermissionRequest | `async`, `timeout: 5000` |
| PostToolUse | `async`, `timeout: 5000` |
| PostToolUseFailure | `async`, `timeout: 5000` |
| UserPromptSubmit | `async`, `timeout: 5000` |
| Notification | `async`, `timeout: 5000` |
| Stop | `async`, `timeout: 5000`, `last_assistant_message` |
| SubagentStart | `async`, `timeout: 5000` |
| SubagentStop | `async`, `timeout: 5000`, `last_assistant_message` |
| PreCompact | `async`, `timeout: 5000`, `once` |
| SessionStart | `async`, `timeout: 5000`, `once` |
| SessionEnd | `async`, `timeout: 5000`, `once` |
| Setup | `async`, `timeout: 30000` |
| TeammateIdle | `async`, `timeout: 5000` |
| TaskCompleted | `async`, `timeout: 5000` |
| ConfigChange | `async`, `timeout: 5000` |

**What to check from the changelog and docs:**
1. **New input fields** added to any hook (e.g. a new field like `last_assistant_message` was added to Stop/SubagentStop) — these must appear in the Options column
2. **New hook configuration options** (e.g. a new option beyond `async`, `once`, `timeout`, `statusMessage`) — these must appear in the Options column for applicable hooks
3. **Changed defaults** (e.g. timeout changed from 5000 to something else) — the Options column must reflect the new value
4. **`once` added or removed** from a hook — update the Options column and the settings files
5. **New hooks** that were added via `/add-new-hook` but the Options column wasn't populated — verify the column is correct

For each mismatch found, flag as **ACTION: Update hook options table** with:
- Which hook's Options column needs updating
- What the current value is
- What it should be (based on docs/changelog)
- Which files also need updating (settings files if `once`/`timeout` changed, HOOKS-README.md table always)

**CRITICAL:** When a new input field is added to a hook's JSON input (from the changelog), it MUST be added to BOTH:
1. The Options column in the HOOKS-README.md table
2. The affected hook's description in the presentation slide

This overlaps with section 3d (Hook Behavior Changes) — both sections must flag the same new input fields. The difference is: 3d flags it as a documentation/changelog change, while 3n ensures the Options table column stays accurate.

### 3m: Presentation Accuracy

Check if `presentation/index.html` is up to date:
- Does the title slide show the latest version and date?
- Does slide 2 show the correct hook counts?
- Does the TOC list all hooks?
- Is there a slide for every hook?
- Does `totalSlides` match the actual slide count?
- Does the lifecycle diagram include all hooks?
- Does the summary slide list all hooks?

Flag any staleness as **ACTION: Update presentation**

### 3o: Agent/Skill Frontmatter Hook Support

The official docs at `https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents` document which hook events are supported in skill and agent frontmatter. This project assumes only **3 agent hooks** are supported: PreToolUse, PostToolUse, and Stop. Compare the official docs against what `HOOKS-README.md` says in the "Agent Frontmatter Hooks" section and what the presentation says in the agent hooks slide.

Check:
- Does the official docs page list additional agent hooks beyond PreToolUse, PostToolUse, and Stop?
- Does `HOOKS-README.md` correctly state that only 3 agent hooks are supported?
- Does `presentation/index.html` (agent hooks slide) correctly show only 3 agent hooks?
- Has the SubagentStop conversion behavior changed? (Stop hooks → SubagentStop for subagents)
- Are there new hook types supported in frontmatter (e.g. `prompt`, `agent` types in addition to `command`)?

Flag any discrepancies as **ACTION: Update agent frontmatter hook documentation**

---

## Phase 4: Generate Report

Produce a structured report with the following sections:

### Report Header

```
╔══════════════════════════════════════════════════════╗
║          CHANGELOG TRACKER REPORT                    ║
║          Claude Code Voice Hooks                     ║
╠══════════════════════════════════════════════════════╣
║  Versions analyzed: <first> to <last>                ║
║  Report date: <today's date>                         ║
║  Current repo state: <N> hooks                       ║
╚══════════════════════════════════════════════════════╝
```

### Section 1: New Hooks to Add

For each missing hook:
```
🆕 <HookName> (introduced in <version>)
   Description: <one-line description>
   Requires: <experimental flag if any, or "Nothing special">
   Action: Run `/add-new-hook <HookName>`
```

If no new hooks: "All hooks are up to date."

### Section 2: Configuration Drift

For each inconsistency found:
```
⚠️  <description of drift>
   File: <file path>
   Expected: <what it should be>
   Actual: <what it currently is>
   Action: <specific fix>
```

If no drift: "All configurations are consistent."

### Section 3: Version & Count Mismatches

```
📊 Version/Count Check:
   README badge version:    <current> → <should be>  ✓/✗
   README badge hook count: <current> → <should be>  ✓/✗
   README changelog table:  <status>                  ✓/✗
   HOOKS-README heading:    <current> → <should be>  ✓/✗
   hooks.py docstring:      <current> → <should be>  ✓/✗
   Presentation version:    <current> → <should be>  ✓/✗
   Presentation hook count: <current> → <should be>  ✓/✗
```

### Section 4: Documentation Updates Needed

For each outdated doc:
```
📝 <what needs updating>
   File: <file path>
   Reason: <why it's outdated, referencing changelog version>
   Action: <specific change>
```

### Section 5: Bug Fixes & Workaround Status

For each known issue/workaround in the repo:
```
🐛 <issue title>
   Status: <Fixed in vX.X.X / Still open / Unknown>
   Current workaround: <description>
   Action: <Remove workaround / Keep workaround / Investigate>
```

### Section 6: New Features to Consider

For each new feature from the changelog that could benefit this project:
```
✨ <feature name> (introduced in <version>)
   Description: <what it does>
   Relevance: <how it could be used in this project>
   Action: <specific recommendation>
```

### Section 7: Matcher & Schema Accuracy

For each hook, verify matcher values and input schema documentation:
```
🔍 <HookName>:
   Matchers documented:   <Yes/No/Partial>  ✓/✗
   Can-block status:      <Correct/Incorrect/Missing>  ✓/✗
   Input schema:          <Documented/Missing>  ✓/✗
```

### Section 8: Hook Types & Environment Variables

```
📋 Hook Types Documented:
   type: "command"  <Yes/No>  ✓/✗
   type: "prompt"   <Yes/No>  ✓/✗
   type: "agent"    <Yes/No>  ✓/✗

🔧 Environment Variables Documented:
   CLAUDE_PROJECT_DIR   <Yes/No>  ✓/✗
   CLAUDE_ENV_FILE      <Yes/No>  ✓/✗
   CLAUDE_PLUGIN_ROOT   <Yes/No>  ✓/✗
   CLAUDE_CODE_REMOTE   <Yes/No>  ✓/✗
```

### Section 9: Removed/Deprecated Hooks

For hooks in our repo but NOT in official docs:
```
❓ <HookName>
   In our repo: Yes (in HOOK_SOUND_MAP, settings, etc.)
   In official docs: <Not found / Found>
   Action: <Investigate / Remove / Keep with note>
```

### Section 10: Presentation Updates

```
🎯 Presentation Status:
   Title slide version:  <current> → <should be>  ✓/✗
   Hook count (slide 2): <current> → <should be>  ✓/✗
   TOC entries:          <current> → <should be>  ✓/✗
   Hook slides:          <current> → <should be>  ✓/✗
   Lifecycle diagram:    <current> → <should be>  ✓/✗
   Summary slide:        <current> → <should be>  ✓/✗
   totalSlides JS:       <current> → <should be>  ✓/✗
```

### Section 11: Hook Options Table

Compare the Options column in the HOOKS-README.md table against official docs and changelog:
```
⚙️  Hook Options Table (HOOKS-README.md):
   PreToolUse:        <current options> → <expected>  ✓/✗
   PermissionRequest: <current options> → <expected>  ✓/✗
   PostToolUse:       <current options> → <expected>  ✓/✗
   PostToolUseFailure:<current options> → <expected>  ✓/✗
   UserPromptSubmit:  <current options> → <expected>  ✓/✗
   Notification:      <current options> → <expected>  ✓/✗
   Stop:              <current options> → <expected>  ✓/✗
   SubagentStart:     <current options> → <expected>  ✓/✗
   SubagentStop:      <current options> → <expected>  ✓/✗
   PreCompact:        <current options> → <expected>  ✓/✗
   SessionStart:      <current options> → <expected>  ✓/✗
   SessionEnd:        <current options> → <expected>  ✓/✗
   Setup:             <current options> → <expected>  ✓/✗
   TeammateIdle:      <current options> → <expected>  ✓/✗
   TaskCompleted:     <current options> → <expected>  ✓/✗
   ConfigChange:      <current options> → <expected>  ✓/✗
```

For each mismatch:
```
⚙️  <HookName> Options column outdated
   Current: <what the table says>
   Expected: <what it should say based on docs/changelog>
   Reason: <changelog version that introduced the change>
   Action: Update Options column in HOOKS-README.md table
```

### Section 12: Agent/Skill Frontmatter Hook Support

Compare the official docs "Hooks in skills and agents" section against our repo (which assumes only 3 agent hooks: PreToolUse, PostToolUse, Stop):
```
🤖 Agent Frontmatter Hook Support:
   Official docs says:         <"3 hooks" / "All hook events" / other>
   HOOKS-README.md says:       <current text — should say 3 hooks>  ✓/✗
   Presentation slide says:    <current text — should say 3 hooks>  ✓/✗
   SubagentStop conversion:    <Documented/Missing>  ✓/✗
```

If discrepancies found:
```
🤖 Agent frontmatter hook documentation outdated
   Official docs: <what the docs say>
   HOOKS-README.md: <what it currently says>
   Presentation: <what it currently says>
   Action: Update both HOOKS-README.md and presentation/index.html
```

### Summary: Action Items

List ALL required actions in priority order:

```
Priority Actions:
═════════════════════════════════════════════════════════════════════
 #  | Type              | Action
────┼───────────────────┼───────────────────────────────────────────
 1  | New Hook          | /add-new-hook <Name>
 2  | New Input Field   | Document <field> added to <Hook> in v<X>
 3  | Hook Options Table| Update Options column for <Hook> in HOOKS-README.md
 4  | Removed Hook      | Investigate <Name> removal
 5  | Config Drift      | Fix <description>
 6  | Version Update    | Update badges to vX.X.X
 7  | Can-Block Fix     | Fix can-block status for <Hook>
 8  | Matcher Docs      | Update matcher values for <Hook>
 9  | Schema Docs       | Document input schema for <Hook>
 10 | Hook Types Docs   | Document prompt/agent hook types
 11 | Env Vars Docs     | Document <variable>
 12 | Doc Update        | Update <file> <section>
 13 | Bug Fix           | Remove <workaround>
 14 | Presentation      | Update to <version>
 15 | Agent Hook Docs   | Update agent frontmatter hook support in HOOKS-README.md and presentation
═════════════════════════════════════════════════════════════════════
Total actions: <N>
```

**Priority #2 (New Input Field) means:** A new field was added to a hook's JSON input in the changelog. This MUST result in:
- A new row in README.md changelog table
- Updated Options column in the HOOKS-README.md hook table
- Updated presentation slide for the affected hook(s)

**Priority #3 (Hook Options Table) means:** An option was added, removed, or changed for a hook (e.g. `once` added, `timeout` changed, new input field). This MUST result in:
- Updated Options column in the HOOKS-README.md hook table
- If `once` or `timeout` changed: updated settings files (main, mac, linux, windows)

These are NOT optional "consider" items — they are required updates.

---

## Phase 5: Offer to Take Action

After presenting the report, ask the user:

> **I found <N> action items. Would you like me to:**
>
> 1. **Execute all actions** — I'll handle everything (new hooks via `/add-new-hook`, fixes, updates)
> 2. **Execute specific actions** — Tell me which numbers to execute
> 3. **Just save the report** — No changes, report only

### If the user chooses to execute:

- For **new hooks**: Use the `/add-new-hook <HookName>` command for each one (one at a time, in order)
- For **new input fields**: This requires updating THREE files:
  1. `README.md` — Add a changelog table row (e.g. "Added `last_assistant_message` to Stop/SubagentStop inputs | v2.1.47")
  2. `HOOKS-README.md` — Add the field to the Options column in the hook table AND to the hook description
  3. `presentation/index.html` — Update the affected hook slide(s) to mention the new field
- For **hook options table updates**: Edit the Options column in the HOOKS-README.md four-column table. If `once` or `timeout` changed, also update all 4 settings files (main, mac, linux, windows).
- For **removed/deprecated hooks**: Confirm with user before removing from all files
- For **version/count updates**: Edit the files directly
- For **matcher/schema documentation**: Update `HOOKS-README.md` with values from official docs
- For **can-block status fixes**: Update presentation slides
- For **hook types documentation**: Add section to `HOOKS-README.md`
- For **environment variable docs**: Add section to `HOOKS-README.md`
- For **other documentation updates**: Edit the files directly
- For **workaround removals**: Edit `hooks.py` and related files, then verify
- For **presentation updates**: Edit `presentation/index.html` directly
- For **agent hook doc updates**: Update `HOOKS-README.md` "Agent Frontmatter Hooks" section and `presentation/index.html` agent hooks slide. This project assumes only 3 agent hooks: PreToolUse, PostToolUse, Stop
- After all actions, re-run the verification to confirm everything is consistent

---

## CRITICAL RULES

1. **ALWAYS fetch from ALL sources** (changelog, hooks reference, AND hooks guide) — never skip any
2. **NEVER guess versions or dates** — always extract from the fetched data
3. **Read ALL local files** before starting the analysis — don't assume you know the current state
4. **Be thorough** — check every single file mentioned in Phase 2
5. **Be specific** — every action item must have a concrete, actionable description
6. **Prioritize correctly**: New hooks first, then new input fields, then config drift, then versions, then can-block fixes, then docs, then presentation. **NEVER dismiss new input fields as "informational"** — they are changelog-worthy changes that require README, HOOKS-README, and presentation updates.
7. **Don't auto-execute** — always present the report and ask before making changes
8. **For new hooks, ALWAYS use `/add-new-hook`** — never manually add hooks, the command handles all the files
9. **Check sound folders** — verify that every hook in `HOOK_SOUND_MAP` has a corresponding sound directory with both `.mp3` and `.wav` files
10. **Cross-reference everything** — the same hook count should appear in: settings files (x4), hooks.py, hooks-config.json, HOOKS-README.md, README.md badge, and presentation
11. **Always check the Options table** — the HOOKS-README.md four-column table (# | Hook | Description | Options) must stay in sync with the official docs. Any new input field, changed timeout, or added/removed `once` option must be reflected in the Options column
12. **Always check agent frontmatter hook support** — this project assumes only **3 agent hooks** (PreToolUse, PostToolUse, Stop). Compare the official docs "Hooks in skills and agents" section against what `HOOKS-README.md` and the presentation say. If the docs add new agent hooks, flag it but do not automatically expand beyond 3 hooks
