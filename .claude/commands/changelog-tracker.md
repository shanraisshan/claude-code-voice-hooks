---
description: Track Claude Code changelog and find what needs updating in this repo
argument-hint: [number of versions to check, default 10]
---

# Changelog Tracker

You are a coordinator for the claude-code-voice-hooks project. Your job is to launch two research agents in parallel, wait for their results, merge findings, and present a unified report.

**Versions to check:** `$ARGUMENTS` (default: 10 if empty or not a number)

This is a **read-then-report** workflow. Launch agents, merge results, and produce a report. Only take action if the user approves.

---

## Phase 0: Launch Both Agents in Parallel

**Immediately** spawn both agents using the Task tool **in the same message** (parallel launch):

### Agent 1: changelog-tracker-agent

Spawn using `subagent_type: "changelog-tracker-agent"`. Give it this prompt:

> Research the claude-code-voice-hooks project for changelog drift. Check the last $ARGUMENTS versions (default: 10).
>
> Fetch these 3 external sources:
> 1. Hooks Reference: https://code.claude.com/docs/en/hooks
> 2. Hooks Guide: https://code.claude.com/docs/en/hooks-guide
> 3. Changelog: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
>
> Then read all local repository files (settings, hooks.py, config, README, HOOKS-README, install settings, presentation) and analyze differences. Return a structured findings report covering missing hooks, configuration drift, version mismatches, hook behavior changes, bug fixes, matcher accuracy, presentation staleness, and agent frontmatter hooks.

### Agent 2: claude-code-guide

Spawn using `subagent_type: "claude-code-guide"`. Give it this prompt:

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

Both agents run independently and will return their findings.

---

## Phase 1: Read Previous Changelog Entries

**Before merging findings**, read the file `workflow-changelog/workflow-changelog.md` to get the last 10 changelog entries. Each entry is separated by `---`. Parse the priority actions from those previous entries so you can compare them against the current findings. This lets you identify:
- **Recurring items** — issues that appeared before and are still unresolved
- **Newly resolved items** — issues from previous runs that are now fixed
- **New items** — issues that appear for the first time in this run

---

## Phase 2: Merge Findings & Generate Report

**Wait for both agents to complete.** Once you have:
- **changelog-tracker-agent findings** — detailed repo analysis with local file reads, external doc fetches, and drift detection
- **claude-code-guide findings** — independent research on latest Claude Code hooks, features, and changes

Cross-reference the two. The changelog-tracker-agent provides repo-specific drift analysis, while the claude-code-guide agent may surface things it missed (e.g. very recent changes, undocumented features, or context from web searches). Flag any contradictions between the two for the user to resolve.

Also compare the current findings against the previous changelog entries (from Phase 1). For each priority action, mark it as:
- `NEW` — first time this issue appears
- `RECURRING` — appeared in a previous run and is still unresolved (include which run date it first appeared)
- `RESOLVED` — appeared in a previous run but is now fixed (include resolution date)

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
13. **claude-code-guide Agent Findings** — Unique insights from the agent that weren't captured by the changelog-tracker-agent. Only include findings that add new information. If there are contradictions between the two agents, flag them for the user to resolve. Do NOT list "confirmed agreements" — if both agents found the same thing, that's expected and not worth reporting.

End with a prioritized **Action Items** summary table. Each item must include a `Status` column showing `NEW`, `RECURRING (first seen: <date>)`, or `RESOLVED`:

```
Priority Actions:
#  | Type              | Action                                    | Status
1  | New Hook          | /add-new-hook <Name>                      | NEW
2  | New Input Field   | Document <field> added to <Hook> in v<X>  | NEW
3  | Hook Options Table| Update Options column for <Hook>          | RECURRING (first seen: 2026-02-20)
4  | Removed Hook      | Investigate <Name> removal                | NEW
5  | Config Drift      | Fix <description>                         | NEW
6  | Version Update    | Update badges to vX.X.X                   | NEW
7  | Can-Block Fix     | Fix can-block status for <Hook>           | NEW
8  | Matcher/Schema    | Update documentation for <Hook>           | NEW
9  | Hook Types/Env    | Document missing items                    | RECURRING (first seen: 2026-02-15)
10 | Presentation      | Update to <version>                       | NEW
11 | Agent Hook Docs   | Update frontmatter hook support           | NEW
12 | Bug Fix           | Remove <workaround>                       | RESOLVED
```

Also include a **Resolved Since Last Run** section listing any items from the previous run that are no longer issues.

---

## Phase 2.5: Append Summary to workflow-changelog/workflow-changelog.md

**This phase is MANDATORY — always execute it before presenting the report to the user.**

Read the existing `workflow-changelog/workflow-changelog.md` file, then **append** (do NOT overwrite) a new entry at the end. The entry format must be exactly:

```markdown
---

## [<YYYY-MM-DD HH:MM AM/PM PKT>] Claude Code v<VERSION>

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH/MED/LOW | <type> | <action description> | NEW/RECURRING/RESOLVED |
| ... | ... | ... | ... | ... |
```

**Rules for appending:**
- Always append — never overwrite or replace previous entries
- The date and time is when the command is executed in Pakistan Standard Time (PKT, UTC+5); get it by running `TZ=Asia/Karachi date "+%Y-%m-%d %I:%M %p PKT"`. The version comes from agent findings
- If `workflow-changelog/workflow-changelog.md` doesn't exist or is empty, create it with `# Changelog Tracker History` then the first entry
- Each entry is separated by `---`
- **Only include items with HIGH, MEDIUM, or LOW priority** — omit NONE priority items (things that need no action)

---

## Phase 3: Offer to Take Action

After presenting the report (and confirming the workflow-changelog/workflow-changelog.md was updated), ask the user:

1. **Execute all actions** — Handle everything (new hooks via `/add-new-hook`, fixes, updates)
2. **Execute specific actions** — User picks which numbers to execute
3. **Just save the report** — No changes

When executing:
- **New hooks**: Use `/add-new-hook <HookName>` (one at a time, in order)
- **New input fields**: Update README.md changelog table, HOOKS-README.md Options column + description, and presentation slides
- **Hook options changes**: Edit HOOKS-README.md Options column; if `once`/`timeout` changed, also update all 4 settings files
- **Removed hooks**: Confirm with user before removing
- **Agent hook docs**: Update HOOKS-README.md and presentation (this project supports 6 agent hooks, not all 16)
- After all actions, re-run verification to confirm consistency

---

## Critical Rules

1. **Launch BOTH agents in parallel** in a single message — never sequentially
2. **Wait for both agents** before generating the report
3. **Never guess** versions or dates — use data from the agents
4. **New input fields are HIGH PRIORITY** — they require README, HOOKS-README, and presentation updates. Never dismiss them as "informational"
5. **For new hooks, ALWAYS use `/add-new-hook`** — never manually add hooks
6. **Cross-reference counts** — the same hook count must appear in: settings (x4), hooks.py, hooks-config.json, HOOKS-README.md, README.md badge, and presentation
7. **Don't auto-execute** — always present the report first
8. **Agent hooks** — this project supports 6 agent hooks (PreToolUse, PostToolUse, PermissionRequest, PostToolUseFailure, Stop, SubagentStop). Not all 16 hooks fire in agent sessions.
9. **ALWAYS append to workflow-changelog/workflow-changelog.md** — Phase 2.5 is mandatory. Never skip it. Never overwrite previous entries.
10. **Compare with previous runs** — read the last 10 entries from workflow-changelog/workflow-changelog.md and mark each action item as NEW, RECURRING, or RESOLVED.
