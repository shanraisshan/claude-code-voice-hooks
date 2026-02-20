---
description: Add a new Claude Code hook event with sounds, config, settings, scripts, and docs
argument-hint: <HookEventName e.g. ConfigChange>
---

# Add New Hook Command

You are adding a new Claude Code hook event to the claude-code-voice-hooks project. The user will provide the hook event name as an argument: `$ARGUMENTS`

## IMPORTANT: Read these rules carefully before doing anything

1. The hook event name is **PascalCase** (e.g. `ConfigChange`, `PreToolUse`, `SessionStart`)
2. The **sound folder name** is the hook event name lowercased with no separators (e.g. `configchange`, `pretooluse`, `sessionstart`)
3. The **sound file names** follow the same lowercase pattern: `<foldername>.mp3` and `<foldername>.wav`
4. You must update **ALL** of the following files — no exceptions

## Step 0: Validate the hook event name

- If `$ARGUMENTS` is empty or not provided, ask the user: "What is the hook event name? (e.g. ConfigChange, PreToolUse)"
- The hook name must be PascalCase (first letter uppercase). If it looks wrong, confirm with the user.
- Derive the lowercase version: e.g. `ConfigChange` -> `configchange`

## Step 1: Check for sound files in `.claude/hooks/sounds/<lowercase>/`

Before doing ANY file modifications, check if the sound directory and files exist:

**Expected path:** `.claude/hooks/sounds/<lowercase>/`
**Expected files:** `<lowercase>.mp3` AND `<lowercase>.wav`

Example for `ConfigChange`:
```
.claude/hooks/sounds/configchange/
  configchange.mp3
  configchange.wav
```

### If the directory or sound files do NOT exist:

1. Create the directory: `.claude/hooks/sounds/<lowercase>/`
2. Tell the user:
   ```
   I've created the sound directory at: .claude/hooks/sounds/<lowercase>/

   Please add your sound files to this directory:
     - <lowercase>.mp3
     - <lowercase>.wav

   TTS generation tip: Use https://elevenlabs.io/ with voice "Samara X"
   Suggested phrase: "<Hook Event Name spaced>" (e.g. "Config Change")

   I'll wait for you to add the files. Let me know when they're ready!
   ```
3. **STOP HERE.** Do NOT proceed to any other steps. Wait for the user to confirm the files are added.

### If the sound files exist:

Confirm to the user: "Found sound files for `<HookName>`. Proceeding with all updates..."
Then continue to Step 2.

## Step 2: Research the hook from official sources

Before editing files, you MUST fetch these two resources to gather hook details:

1. **Hooks documentation:** Fetch `https://code.claude.com/docs/en/hooks` — find the hook's description, whether it supports matchers, and any special requirements
2. **Changelog:** Fetch `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` — find which Claude Code version introduced this hook (search for the hook name)

Use WebFetch to retrieve both resources in parallel. Extract:
- A one-line description of what the hook does
- The Claude Code version that introduced it (e.g. `v2.1.49`)
- Whether it requires experimental features or special flags

**NEVER ask the user for the version or description — always look it up yourself.**

## Step 3: Determine hook properties

Before editing files, decide the hook properties by analyzing the hook name and the documentation fetched in Step 2:

### Timeout
- Default: `5000` (5 seconds)
- Use `30000` (30 seconds) only for hooks that involve heavy initialization (like `Setup`)
- Ask the user if unsure, but default to `5000`

### `once: true`
- Add `"once": true` ONLY for session-lifecycle hooks that should fire once per session
- Existing hooks with `once: true`: `SessionStart`, `SessionEnd`, `PreCompact`
- Ask the user: "Should this hook run only once per session? (like SessionStart/SessionEnd)"
- Default to `false` (don't add the property) if the user says no or is unsure

### `async: true`
- Always `true` for this project (all hooks are async voice notifications)

## Step 4: Update all files

You MUST update ALL of the following files. Read each file first, then edit.

### 4a: `.claude/settings.json` (main project settings)

Add the new hook entry. Insert it in the correct position (alphabetical or after the last existing hook, matching the current order).

Pattern (macOS/Linux — uses `python3` and `${CLAUDE_PROJECT_DIR}`):
```json
"<HookEventName>": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
        "timeout": <timeout>,
        "async": true,
        <"once": true,  -- only if applicable>
        "statusMessage": "<HookEventName>"
      }
    ]
  }
]
```

### 4b: `install/settings-mac.json`

Exact same content as `.claude/settings.json` (uses `python3` and `${CLAUDE_PROJECT_DIR}`).

### 4c: `install/settings-linux.json`

Exact same content as `.claude/settings.json` (uses `python3` and `${CLAUDE_PROJECT_DIR}`).

### 4d: `install/settings-windows.json`

Same structure but uses `python` (no `3`) and relative path (no `${CLAUDE_PROJECT_DIR}`):
```json
"<HookEventName>": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python .claude/hooks/scripts/hooks.py",
        "timeout": <timeout>,
        "async": true,
        <"once": true,  -- only if applicable>
        "statusMessage": "<HookEventName>"
      }
    ]
  }
]
```

### 4e: `.claude/hooks/config/hooks-config.json`

Add a new disable toggle BEFORE the `"disableLogging"` line (keep `disableLogging` last):
```json
"disable<HookEventName>Hook": false
```

### 4f: `.claude/hooks/scripts/hooks.py`

Update the `HOOK_SOUND_MAP` dictionary. Add the new entry in the correct position:
```python
"<HookEventName>": "<lowercase>",
```

Also update the docstring at the top of the file:
- Update the hook count: "Supports all N Claude Code hooks" (increment from current number)

### 4g: `.claude/hooks/HOOKS-README.md`

1. Update the heading: "Official N Hooks" (increment the count)
2. Add the new hook to the numbered list with a description from the hooks documentation fetched in Step 2.
3. Update the shared configuration example JSON block to include the new `disable<HookEventName>Hook` entry
4. If the hook requires special conditions (like experimental features), add a note

### 4h: `README.md`

1. Update the first line that says "supports all N hooks" — increment the count
2. Add a new row to the Changelog table at the TOP (most recent first):
   ```
   | <today's date>, 2026 | <N> | Added `<HookEventName>` | [v<version>](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#<version-anchor>) | |
   ```
   - Use today's date
   - Use the Claude Code version found in the changelog (Step 2)

### 4i: `presentation/index.html`

This is the slide deck for the project. It MUST be updated to include the new hook. Read the file first, then make ALL of the following changes:

1. **Title slide (slide 1):** Update the version text (e.g. "As of Claude Code v2.1.XX | <date>") to the new version and today's date
2. **Slide 2 (What You'll Learn):** Update hook counts in both places — "N Hooks Explained" and "all N hooks with audio feedback"
3. **Slide 3 (Table of Contents):**
   - Update the title: "The N Hooks"
   - Update the subtitle version and date
   - Add a new TOC item for the new hook at the end of the `toc-list` div, with the next number and correct `onclick="goToSlide(X)"` pointing to the new slide
4. **Slide 4 (Lifecycle diagram):** Add the new hook in the appropriate position in the lifecycle flow. Use the hook description from Step 2 to determine where it fits.
5. **New hook slide:** Create a new slide for the hook using the same HTML structure as existing hook slides. Include:
   - Hook number and name with `hook-title` div
   - Whether it can block (use `can-block` or `cannot-block` span) — determine from docs fetched in Step 2
   - `trigger-box` with "When It Triggers" description
   - `how-to-trigger` with instructions on how to trigger it
   - `matcher-values` if the hook supports matchers (from docs)
   - Use cases section with 3-4 relevant use cases
   - `sound-demo` at the bottom with the sound file name
   - Set the correct `data-slide` number
6. **Shift existing slides:** All slides after the new hook slide must have their `data-slide` numbers incremented by 1. Also update all `onclick="goToSlide(X)"` references in the TOC that point to shifted slides.
7. **Summary slide (last slide):** Add the new hook to the appropriate category card in the `info-grid`
8. **JavaScript:** Update `const totalSlides = N;` to the new total

**IMPORTANT:** Maintain the exact same HTML structure, CSS classes, and indentation as existing slides. Look at the slide immediately before the new one as a template.

## Step 5: Verify all changes

After completing all edits, verify by listing what was changed:

1. Count hooks in `.claude/settings.json` — should match new total
2. Count hooks in `install/settings-mac.json` — should match
3. Count hooks in `install/settings-linux.json` — should match
4. Count hooks in `install/settings-windows.json` — should match
5. Count entries in `HOOK_SOUND_MAP` in `hooks.py` — should match
6. Count disable flags in `hooks-config.json` — should match (excluding `disableLogging`)
7. Count hooks listed in `HOOKS-README.md` — should match
8. Verify sound files exist in `.claude/hooks/sounds/<lowercase>/`
9. Count hook slides in `presentation/index.html` — should match new total
10. Verify `totalSlides` in presentation JS matches actual slide count

Print a summary table:

```
Hook Addition Summary: <HookEventName>
========================================
Sound folder:     .claude/hooks/sounds/<lowercase>/ ✓
Sound files:      <lowercase>.mp3, <lowercase>.wav ✓
settings.json:    Updated (N hooks) ✓
settings-mac:     Updated (N hooks) ✓
settings-linux:   Updated (N hooks) ✓
settings-windows: Updated (N hooks) ✓
hooks-config:     Updated (N toggles) ✓
hooks.py:         Updated (N mappings) ✓
HOOKS-README:     Updated (N hooks) ✓
README.md:        Updated changelog ✓
presentation:     Updated (N slides, hook #X added) ✓
```

## CRITICAL REMINDERS

- NEVER proceed past Step 1 if sound files don't exist. Always wait for the user.
- ALWAYS read each file before editing to understand current state.
- Keep the exact same JSON structure/indentation as existing entries.
- The 4 settings files (main, mac, linux, windows) must ALL be updated.
- Windows uses `python` (not `python3`) and relative paths (no `${CLAUDE_PROJECT_DIR}`).
- `hooks-config.json`: keep `disableLogging` as the LAST entry.
- `hooks.py`: only update `HOOK_SOUND_MAP`, not `AGENT_HOOK_SOUND_MAP` (agent hooks are separate).
- Match the existing code style exactly — no extra whitespace, comments, or formatting changes.
- `presentation/index.html`: update ALL count references, add a new slide, shift subsequent slide numbers, and update `totalSlides` in JS.
