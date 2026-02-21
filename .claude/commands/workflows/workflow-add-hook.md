---
description: Add a new Claude Code hook event with sounds, config, settings, scripts, and docs
argument-hint: <HookEventName e.g. ConfigChange>
---

# Add New Hook

Add a new Claude Code hook event to the claude-code-voice-hooks project.

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
| `async` | Always `true` (all hooks in this project are async voice notifications) |

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

### `README.md`

- Update "supports all N hooks" count
- Add a new changelog table row at the TOP:
  ```
  | <today's date> | <N> | Added `<HookEventName>` | [v<version>](<changelog-link>) | |
  ```

### `presentation/index.html`

1. **Title slide:** Update version and date
2. **Slide 2:** Update hook counts ("N Hooks Explained", "all N hooks")
3. **Slide 3 (TOC):** Update title count, add new TOC item with correct `goToSlide(X)`
4. **Slide 4 (Lifecycle):** Add hook in appropriate lifecycle position
5. **New slide:** Create using the same HTML structure as existing hook slides — include hook number, can-block status, trigger description, how-to-trigger, matcher values (if applicable), use cases, and sound demo
6. **Shift slides:** Increment `data-slide` numbers and TOC `goToSlide(X)` references for all subsequent slides
7. **Summary slide:** Add hook to appropriate category card
8. **JavaScript:** Update `const totalSlides = N`

## Step 5: Verify

Count hooks across all files and print a summary:

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
```

---

## Critical Rules

1. **NEVER proceed past Step 1 if sound files don't exist** — always wait for the user
2. **Read each file before editing** — understand current state first
3. **ALL 4 settings files must be updated** — Windows uses `python` (not `python3`) and relative paths
4. **Keep `disableLogging` as the LAST entry** in hooks-config.json
5. **Only update `HOOK_SOUND_MAP`** — not `AGENT_HOOK_SOUND_MAP`
6. **Match existing code style exactly** — indentation, structure, formatting
7. **Update ALL presentation references** — counts, slides, TOC, lifecycle, summary, `totalSlides`

---

## Sources

The following URLs are fetched during execution:

| Source | URL |
|--------|-----|
| Hooks Reference | `https://code.claude.com/docs/en/hooks` |
| Hooks Guide | `https://code.claude.com/docs/en/hooks-guide` |
| Changelog | `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` |
