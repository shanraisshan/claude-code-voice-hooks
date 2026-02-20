---
description: Track Claude Code changelog and find what needs updating in this repo
argument-hint: [number of versions to check, default 10]
---

# Changelog Tracker

You are a tracker agent for the claude-code-voice-hooks project. Analyze the last N versions from the Claude Code changelog and determine what changes need to be made in this repo.

**Versions to check:** `$ARGUMENTS` (default: 10 if empty or not a number)

This is a **read-then-report** workflow. Fetch sources, read local files, compare, and produce a report. Only take action if the user approves.

---

## Phase 0: Launch claude-code-guide Agent (in parallel with Phase 1 & 2)

**Immediately** spawn a `claude-code-guide` agent using the Task tool (`subagent_type: "claude-code-guide"`) to run **in parallel** with your own Phase 1 and Phase 2 work. This agent has specialized knowledge about Claude Code features, hooks, and recent changes.

Give the agent this prompt:

> Research the latest Claude Code hooks system. I need you to find:
> 1. The complete list of all currently supported hook events (e.g. PreToolUse, PostToolUse, Stop, etc.) with their descriptions
> 2. Any new hooks or hook changes introduced in recent Claude Code versions
> 3. New hook input fields, matcher values, or configuration options added recently
> 4. Any new hook types (command, prompt, agent) or new environment variables
> 5. Changes to agent/skill frontmatter hook support
> 6. Any bug fixes related to hooks
> 7. New features in Claude Code that relate to hooks (e.g. new tool names for matchers, new subagent types)
>
> Be thorough — search the web, fetch docs, and provide concrete version numbers and details for everything you find.

This agent runs independently and will return its findings. You will merge its results with your own analysis in Phase 4.

---

## Phase 1: Fetch External Data (in parallel)

Fetch all three sources using WebFetch simultaneously (run these **at the same time** as the Phase 0 agent):

1. **Hooks Reference** — Extract the complete list of officially supported hooks, matcher support, hook options, input schemas, decision control patterns, can-block status, and experimental features.
2. **Hooks Guide** — Extract hook types (`command`, `prompt`, `agent`), matcher values with examples, hook location scopes, environment variables (`CLAUDE_PROJECT_DIR`, `CLAUDE_ENV_FILE`, `CLAUDE_PLUGIN_ROOT`, `CLAUDE_CODE_REMOTE`), and security considerations.
3. **Changelog** — Extract the last N version entries with version numbers, dates, and all hook-related changes (new hooks, behavior changes, new input fields, bug fixes, breaking changes, new options).

---

## Phase 2: Read Local Repository State (in parallel)

Read ALL of the following:

| File | What to check |
|------|---------------|
| `.claude/settings.json` | Hook configurations |
| `.claude/hooks/scripts/hooks.py` | `HOOK_SOUND_MAP`, `AGENT_HOOK_SOUND_MAP`, docstring counts |
| `.claude/hooks/config/hooks-config.json` | Disable toggles |
| `.claude/hooks/HOOKS-README.md` | Documentation, hook table (Options column), matcher values, agent frontmatter section |
| `README.md` | Badge versions, hook count, changelog table |
| `install/settings-mac.json` | Mac settings |
| `install/settings-linux.json` | Linux settings |
| `install/settings-windows.json` | Windows settings |
| `presentation/index.html` | Slides, version, hook count, lifecycle diagram, `totalSlides` |

Also list directories in `.claude/hooks/sounds/` to verify sound folders exist for each hook.

---

## Phase 3: Analysis

Compare external data against local repo state. Check for:

### Missing Hooks
Compare official docs hook list against `HOOK_SOUND_MAP`. Flag any missing hooks with the version that introduced them.

### Configuration Drift
For each existing hook, verify it exists in ALL 4 settings files, `hooks-config.json`, `HOOK_SOUND_MAP`, sound folders (`.mp3` + `.wav`), `HOOKS-README.md`, and the presentation.

### Version & Count Accuracy
Verify the README badge version/count, `HOOKS-README.md` heading count, `hooks.py` docstring count, changelog table, and presentation version/count all match reality.

### Hook Behavior Changes (HIGH PRIORITY)
Identify from the changelog: new input fields (e.g. `last_assistant_message`), new matcher values, changed behavior/timing, new options, and deprecations. **New input fields are major changes** requiring updates to README changelog table, HOOKS-README Options column, and presentation slides.

### Bug Fixes & Workarounds
Check if known issues (e.g. SubagentStop vs Stop bug, GitHub Issue #19220) have been fixed. Flag removable workarounds.

### Matcher Values & Can-Block Status
Verify `HOOKS-README.md` and presentation correctly document matcher values and can-block status for each hook per the official docs.

### Hook Options Table (HOOKS-README.md)
Cross-reference the Options column in the four-column table against official docs. Any new input field, changed timeout, or added/removed `once` option must be reflected.

### Hook Input Schemas
Verify input schema documentation covers common fields (`session_id`, `transcript_path`, `cwd`, etc.) and hook-specific fields.

### Hook Types & Environment Variables
Check if `HOOKS-README.md` documents all three hook types and all environment variables from the official docs.

### Removed/Deprecated Hooks
Cross-reference repo hooks against official docs. Flag any hooks in the repo that no longer appear in official docs.

### Agent/Skill Frontmatter Hooks
This project assumes only **3 agent hooks**: PreToolUse, PostToolUse, Stop. Compare against official docs and flag discrepancies.

### Presentation Accuracy
Verify title slide version, hook counts, TOC, individual hook slides, lifecycle diagram, summary slide, and `totalSlides` variable.

---

## Phase 4: Merge Findings & Generate Report

**Before generating the report**, wait for the `claude-code-guide` agent from Phase 0 to complete. Once you have both:
- **Your own analysis** (from Phases 1-3 using WebFetch + local file reads)
- **Agent findings** (from the claude-code-guide agent's independent research)

Cross-reference the two. The agent may surface things you missed (e.g. very recent changes, undocumented features, or context from web searches). Likewise, your local file analysis will catch repo-specific drift the agent can't see.

Produce a structured report with these sections:

1. **New Hooks to Add** — Missing hooks with version and `/add-new-hook` command
2. **Configuration Drift** — Inconsistencies across files with specific fixes
3. **Version & Count Mismatches** — Table showing current vs expected for each location
4. **Documentation Updates** — Outdated docs with changelog version references
5. **Bug Fixes & Workaround Status** — Known issues with fix status
6. **New Features to Consider** — Relevant new features from changelog
7. **Matcher & Schema Accuracy** — Per-hook verification status
8. **Hook Types & Environment Variables** — Documentation coverage status
9. **Removed/Deprecated Hooks** — Hooks in repo but not in docs
10. **Presentation Updates** — Staleness across all presentation elements
11. **Hook Options Table** — Per-hook Options column accuracy
12. **Agent Frontmatter Hooks** — 3-hook assumption verification
13. **claude-code-guide Agent Findings** — Unique insights from the agent that weren't captured by your own analysis. If the agent found something you missed, add it here. If the agent confirms your findings, note the agreement. If there are contradictions, flag them for the user to resolve.

End with a prioritized **Action Items** summary table:

```
Priority Actions:
#  | Type              | Action
1  | New Hook          | /add-new-hook <Name>
2  | New Input Field   | Document <field> added to <Hook> in v<X>
3  | Hook Options Table| Update Options column for <Hook>
4  | Removed Hook      | Investigate <Name> removal
5  | Config Drift      | Fix <description>
6  | Version Update    | Update badges to vX.X.X
7  | Can-Block Fix     | Fix can-block status for <Hook>
8  | Matcher/Schema    | Update documentation for <Hook>
9  | Hook Types/Env    | Document missing items
10 | Presentation      | Update to <version>
11 | Agent Hook Docs   | Update frontmatter hook support
12 | Bug Fix           | Remove <workaround>
```

---

## Phase 5: Offer to Take Action

After presenting the report, ask the user:

1. **Execute all actions** — Handle everything (new hooks via `/add-new-hook`, fixes, updates)
2. **Execute specific actions** — User picks which numbers to execute
3. **Just save the report** — No changes

When executing:
- **New hooks**: Use `/add-new-hook <HookName>` (one at a time, in order)
- **New input fields**: Update README.md changelog table, HOOKS-README.md Options column + description, and presentation slides
- **Hook options changes**: Edit HOOKS-README.md Options column; if `once`/`timeout` changed, also update all 4 settings files
- **Removed hooks**: Confirm with user before removing
- **Agent hook docs**: Update HOOKS-README.md and presentation (this project assumes only 3 agent hooks)
- After all actions, re-run verification to confirm consistency

---

## Critical Rules

1. **Fetch ALL 3 sources** — never skip any
2. **Never guess** versions or dates — extract from fetched data
3. **Read ALL local files** before analyzing
4. **New input fields are HIGH PRIORITY** — they require README, HOOKS-README, and presentation updates. Never dismiss them as "informational"
5. **For new hooks, ALWAYS use `/add-new-hook`** — never manually add hooks
6. **Cross-reference counts** — the same hook count must appear in: settings (x4), hooks.py, hooks-config.json, HOOKS-README.md, README.md badge, and presentation
7. **Don't auto-execute** — always present the report first
8. **Agent hooks assumption** — this project assumes only 3 agent hooks (PreToolUse, PostToolUse, Stop). Flag but don't auto-expand

---

## Sources

The following URLs are fetched during execution:

| Source | URL |
|--------|-----|
| Hooks Reference | `https://code.claude.com/docs/en/hooks` |
| Hooks Guide | `https://code.claude.com/docs/en/hooks-guide` |
| Changelog | `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` |
