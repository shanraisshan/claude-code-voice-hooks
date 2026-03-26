---
description: Add a new Claude Code hook event with sounds, config, settings, scripts, and docs
argument-hint: <HookEventName e.g. ConfigChange>
---

# Add New Hook

Add a new Claude Code hook event to the claude-code-hooks project.

**Hook event name:** `$ARGUMENTS` (if empty, ask the user)

**Naming rules:**
- Hook name is **PascalCase** (e.g. `ConfigChange`, `PreToolUse`)
- Sound folder/files use **lowercase** with no separators (e.g. `configchange`, `pretooluse`)

---

## Step 0: Validate

If `$ARGUMENTS` is empty, ask the user for the hook event name. Confirm it's PascalCase. Derive the lowercase version.

## Step 1: Check Sound Files (BLOCKING)

Check if `.claude/hooks/sounds/<lowercase>/` exists with `<lowercase>.mp3` and `<lowercase>.wav`.

- **If missing:** Create the directory, tell the user to add sound files (suggest ElevenLabs with voice "Samara X"), and **STOP. Do NOT proceed until the user confirms files are added.**
- **If present:** Continue to Step 2.

## Step 2: Research the Hook

Fetch all three sources in parallel using WebFetch:
1. **Hooks Reference** — Find the hook's description, matcher support, can-block status, and special requirements
2. **Hooks Guide** — Find hook types, matcher values with examples, environment variables, and additional usage details
3. **Changelog** — Find which Claude Code version introduced this hook

**Never ask the user for version or description — always look it up.**

## Step 3: Determine Hook Properties

| Property | Rule |
|----------|------|
| `timeout` | Default `5000`. Use `30000` only for heavy init hooks (like `Setup`) |
| `once` | Only for session-lifecycle hooks (like `SessionStart`, `SessionEnd`, `PreCompact`). Ask user if unsure, default to `false` |
| `async` | Always `true` (all hooks in this project are async sound notifications) |

## Step 4: Update All Files

Read each file first, then edit. **ALL files must be updated — no exceptions.**

### Settings files (4 files)

Add the hook entry in correct position. Structure:

```json
"<HookEventName>": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
        "timeout": <timeout>,
        "async": true,
        "statusMessage": "<HookEventName>"
      }
    ]
  }
]
```

Add `"once": true` only if applicable.

| File | Notes |
|------|-------|
| `.claude/settings.json` | `python3` + `${CLAUDE_PROJECT_DIR}` |
| `install/settings-mac.json` | Same as above |
| `install/settings-linux.json` | Same as above |
| `install/settings-windows.json` | Uses `python` (no `3`) + relative path `.claude/hooks/scripts/hooks.py` (no `${CLAUDE_PROJECT_DIR}`) |

### `.claude/hooks/config/hooks-config.json`

Add `"disable<HookEventName>Hook": false` **before** the `"disableLogging"` line (keep `disableLogging` last).

### `.claude/hooks/scripts/hooks.py`

- Add `"<HookEventName>": "<lowercase>"` to `HOOK_SOUND_MAP` (NOT `AGENT_HOOK_SOUND_MAP`)
- Update the docstring hook count

### `.claude/hooks/HOOKS-README.md`

- Update heading count ("Official N Hooks")
- Add the hook to the numbered list with description from docs
- Update the shared config JSON block with new `disable<HookEventName>Hook` entry
- **If the hook is NOT listed in the [Official Hooks Reference](https://code.claude.com/docs/en/hooks)** (i.e. it only appears in the changelog), add a row to the "Not in Official Docs" table with the hook name, version, changelog quote, and a note that it's excluded from the official reference page

### `README.md`

- Update the **Version badge** timestamp to the current PKT time. Run `TZ=Asia/Karachi date "+%b %d, %Y %-I:%M %p PKT"` to get it, then URL-encode and replace the date in the `[![Version](...)]` badge on line 2. Also update the version number in the badge if it changed.
- Update "supports all N hooks" count
- Add a new changelog table row at the TOP:
  ```
  | <today's date> | <N> | Added `<HookEventName>` | [v<version>](<changelog-link>) | |
  ```

### `.claude/agents/claude-code-test-agent.md`

- Add the new hook to the agent's frontmatter `hooks:` section using the same pattern as existing hooks (echo hook name + timestamp to `tests-agents-hook/agent-hook-fired.log`, `timeout: 5000`, `async: true`). Use `timeout: 30000` only for `Setup`.
- Update the description line's hook count ("Tests all N Claude Code hooks")
- Add the hook to the "All N Hooks Configured" list with a one-line description
- Add the hook to the "Hook Trigger Summary" output format list
- Update all "N" hook count references in the agent body

### Demo files (3 files)

The `demo/` directory has its own hook setup that mirrors the main project. All three files must be updated:

#### `demo/.claude/settings.json`

Add the hook entry using the same structure as existing entries:

```json
"<HookEventName>": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/demo-hooks.py",
        "timeout": <timeout>,
        "async": true,
        "statusMessage": "<HookEventName>"
      }
    ]
  }
]
```

Add `"once": true` only if applicable. Use `"async": false` only for WorktreeCreate/WorktreeRemove-style hooks. Use timeout `30000` only for Setup.

#### `demo/.claude/hooks/scripts/demo-hooks.py`

- Add `"<HookEventName>": "<lowercase>"` to `HOOK_SOUND_MAP`
- Update the docstring hook count ("Handles all N Claude Code hooks")

#### `demo/hooks-lifecycle.html`

Update both the **flowchart SVG** and the **prompt cards**:

**Flowchart (right panel SVG):**
- Add a new `<g class="hook-group" data-hook="<HookEventName>">` element in the appropriate lifecycle position
- Use `hook-rect-side` + `hook-text-side` classes for side-panel hooks (async/external events like Notification, ConfigChange, Elicitation, etc.)
- Use regular `hook-rect` + `hook-text` classes for main-flow hooks
- Include a `<text class="fire-count">` element for the fire counter
- Add connecting arrows (`arrow-line`) or dashed connectors (`connector-dashed`) as appropriate
- Adjust Y coordinates of subsequent elements if inserting in the middle of the flow
- Update the `viewBox` height if the chart grows taller

**Prompt cards (left panel) — MANDATORY, never skip:**
Every hook MUST appear in at least one prompt card with a **real trigger prompt** that shows how to fire the hook. Either:
- Add `<span class="hook-tag"><HookEventName></span>` to an existing card's `.prompt-hooks` div if the hook fits that scenario, OR
- Create a new `<div class="prompt-card" data-card-hooks="<HookEventName>">` with:
  - A numbered step in `.prompt-step` (increment from the last card number)
  - Hook tags in `.prompt-hooks`
  - **A concrete command or prompt that triggers the hook** in `.prompt-code` with copy buttons. Every card MUST have a runnable command (shell `$` prefix) or a Claude prompt (`>` prefix) that actually fires the hook. If the hook requires special setup (e.g. env vars, flags), show the full command including setup.
- **Numbering rule:** Left column = cards 1 through N, right column = cards N+1 through M. The grid fills left-right by row, so HTML source order alternates: left-1, right-1, left-2, right-2, etc. When adding a card, increment the last number and place it in the correct HTML position to maintain the alternating pattern.
- Renumber subsequent prompt cards if inserting in the middle

**Branding text:**
- Update the "22 supported" text in `.right-branding-text` to the new count

### `presentation/index.html`

1. **Title slide:** Update version and date
2. **Slide 2:** Update hook counts ("N Hooks Explained", "all N hooks", and "currently supports N hooks (as of vX.X.XX)" in the use-case span)
3. **Slide 3 (TOC):** Update title count, add new TOC item with correct `goToSlide(X)`
4. **Slide 4 (Lifecycle):** Add hook in appropriate lifecycle position
5. **New slide:** Create using the same HTML structure as existing hook slides — include hook number, **can-block/cannot-block badge** (`<span class="can-block">Can Block</span>` or `<span class="cannot-block">Cannot Block</span>` in the `hook-title` div), trigger description, how-to-trigger, matcher values (if applicable), use cases, and sound demo. **Every hook slide MUST have a can-block badge — never omit it.**
6. **Shift slides:** Increment `data-slide` numbers and TOC `goToSlide(X)` references for all subsequent slides
7. **Summary slide:** Add hook to appropriate category card. **If the hook can block**, also add it to the "Hooks That Can Block Execution" `matcher-values` div at the bottom of the summary slide.
8. **JavaScript:** Update `const totalSlides = N`

## Step 5: Update CLAUDE.md

Read `CLAUDE.md` at the project root and update any stale values:
- Hook count (e.g. "currently **19**" → new count)
- Agent hook count/list (only if this hook fires in agent sessions)
- `once: true` hook list (only if this hook uses `once: true`)
- Slide count / `totalSlides`

## Step 6: Verify

**After all edits, re-read every modified file and confirm the new hook name appears.** This is critical — do NOT rely on the edit tool succeeding; grep each file for the hook name.

Run these verifications:
1. `grep -c "<HookEventName>" .claude/settings.json` — must return ≥1
2. `grep -c "<HookEventName>" install/settings-mac.json` — must return ≥1
3. `grep -c "<HookEventName>" install/settings-linux.json` — must return ≥1
4. `grep -c "<HookEventName>" install/settings-windows.json` — must return ≥1
5. `grep -c "<HookEventName>" demo/.claude/settings.json` — must return ≥1
6. `grep -c "<HookEventName>" demo/.claude/hooks/scripts/demo-hooks.py` — must return ≥1
7. `grep -c "<HookEventName>" demo/hooks-lifecycle.html` — must return ≥1
8. `grep -c "data-card-hooks=.*<HookEventName>" demo/hooks-lifecycle.html` — must return ≥1 (prompt card check)

Count hooks across all files and print a summary. **All counts must match the expected new total — if ANY count is wrong, fix it before finishing.**

```
Hook Addition Summary: <HookEventName>
========================================
Sound folder:     ✓/✗
Sound files:      ✓/✗
settings.json:    N hooks ✓/✗
settings-mac:     N hooks ✓/✗
settings-linux:   N hooks ✓/✗
settings-windows: N hooks ✓/✗
hooks-config:     N toggles ✓/✗
hooks.py:         N mappings ✓/✗
HOOKS-README:     N hooks ✓/✗
README.md:        changelog ✓/✗
presentation:     N slides ✓/✗
test-agent:       N hooks ✓/✗
demo/settings:    N hooks ✓/✗
demo/hooks.py:    N mappings ✓/✗
demo/lifecycle:   flowchart + card ✓/✗
```

**If any line shows ✗, stop and fix it before declaring done.**

---

## Critical Rules

1. **NEVER proceed past Step 1 if sound files don't exist** — always wait for the user
2. **Read each file before editing** — understand current state first
3. **ALL 5 settings files must be updated** — Windows uses `python` (not `python3`) and relative paths; demo uses `demo-hooks.py`
4. **Keep `disableLogging` as the LAST entry** in hooks-config.json
5. **Only update `HOOK_SOUND_MAP`** — not `AGENT_HOOK_SOUND_MAP` (in both `hooks.py` and `demo-hooks.py`)
6. **Match existing code style exactly** — indentation, structure, formatting
7. **Update ALL presentation references** — counts, slides, TOC, lifecycle, summary, `totalSlides`
8. **Update ALL demo files** — `demo/.claude/settings.json`, `demo-hooks.py` HOOK_SOUND_MAP + docstring, and `hooks-lifecycle.html` flowchart SVG + prompt cards + branding count

---

## Sources

The following URLs are fetched during execution:

| Source | URL |
|--------|-----|
| Hooks Reference | `https://code.claude.com/docs/en/hooks` |
| Hooks Guide | `https://code.claude.com/docs/en/hooks-guide` |
| Changelog | `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` |
