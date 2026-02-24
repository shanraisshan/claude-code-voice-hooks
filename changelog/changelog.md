# Workflow Changelog History

## Status Legend

| Status | Meaning |
|--------|---------|
| ✅ COMPLETE (reason) | Action was taken and resolved successfully |
| ❌ INVALID (reason) | Finding was incorrect, not applicable, or intentional |
| ✋ ON HOLD (reason) | Action deferred — waiting on external dependency or user decision |

---

## [2026-02-20 08:14 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Doc Fix | `agent_type` version attribution — README said v2.1.43, changelog disagrees | ✅ COMPLETE (marked as ~v2.1.43, unconfirmed) |
| 2 | MEDIUM | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's 6 | ✅ COMPLETE (added update note to HOOKS-README and README) |
| 3 | LOW | Hook Options Table | `notification_type`, `message`, `title` missing from Notification Options column | ✅ COMPLETE (added to HOOKS-README) |
| 4 | LOW | Hook Types/Env | Additional `CLAUDE_HOOK_*` env vars from blog sources | ❌ INVALID (false positive — not in official docs) |
| 5 | LOW | New Hook | `OpenInEditor` hook existence | ❌ INVALID (false positive — does not exist in official docs) |

---

## [2026-02-20 11:15 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Hook Options Table | UserPromptSubmit Options column missing `prompt` input field in HOOKS-README | ✅ COMPLETE (added `prompt` to Options column) |
| 2 | LOW | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's tested 6; needs re-testing | ✅ COMPLETE (reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153)) |

---

## [2026-02-20 11:57 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (already reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153); pending response) |

---

## [2026-02-21 06:41 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeCreate — new in v2.1.50 for agent worktree isolation VCS setup | ✅ COMPLETE (added — all 18 hooks consistent across files) |
| 2 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeRemove — new in v2.1.50 for agent worktree isolation VCS teardown | ✅ COMPLETE (added — all 18 hooks consistent across files) |
| 3 | LOW | Hook Options Table | Add `tool_response` to PostToolUse Options column in HOOKS-README | ✅ COMPLETE (added to HOOKS-README) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream bug reported at [#27153](https://github.com/anthropics/claude-code/issues/27153); pending their fix) |

---

## [2026-02-21 07:57 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Presentation | Add can-block/cannot-block badge to WorktreeCreate and WorktreeRemove slides — all other 16 hook slides had this badge | ✅ COMPLETE (added "Cannot Block" badge to both slides) |
| 2 | LOW | Documentation | README.md changelog table missing v2.1.47 `last_assistant_message` — no action needed, table is for new hook additions only | ❌ INVALID (not applicable — editorial choice) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream bug reported; pending their fix) |
| 4 | LOW | Presentation | Setup hook not shown in lifecycle diagram — fires separately via --init/--maintenance | ✅ COMPLETE (added Setup to lifecycle diagram with separate trigger section) |
| 5 | LOW | Workflow | Updated workflow-add-hook to require can-block badge on every new hook slide and update summary can-block list | ✅ COMPLETE (added explicit instructions to workflow) |

---

## [2026-02-21 08:13 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | Add `WorktreeCreate` and `WorktreeRemove` to "Not in Official Docs" table in HOOKS-README — they exist in changelog (v2.1.50) but are absent from official hooks reference | ✅ COMPLETE (added both rows to table) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |
| 3 | LOW | Workflow | Updated workflow-add-hook to include "Not in Official Docs" table step when adding changelog-only hooks | ✅ COMPLETE (added instruction to HOOKS-README section) |

---

## [2026-02-21 09:10 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |

---

## [2026-02-22 02:30 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | WorktreeCreate can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list | ✅ COMPLETE (changed to "Can Block" + added to summary list) |
| 2 | HIGH | Doc Fix | HOOKS-README "Not in Official Docs" table stale — WorktreeCreate and WorktreeRemove ARE now in official docs (17 hooks listed, not 15) | ✅ COMPLETE (removed stale rows, updated count to 17) |
| 3 | MEDIUM | New Input Field | WorktreeCreate missing `name` input field in HOOKS-README Options column | ✅ COMPLETE (added `name` to Options column) |
| 4 | MEDIUM | New Input Field | WorktreeRemove missing `worktree_path` input field in HOOKS-README Options column | ✅ COMPLETE (added `worktree_path` to Options column) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |

---

## [2026-02-23 01:08 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading | ❌ INVALID (intentional wording) |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ✅ COMPLETE (added Per-Hook Matcher Reference table) |
| 3 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ✅ COMPLETE (v2.1.33 confirmed correct) |
| 4 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ✅ COMPLETE (added Common Input Fields section) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 10:02 AM PKT] Claude Code v2.1.51

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | ~~MEDIUM~~ | ~~Documentation~~ | ~~HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading~~ | ❌ INVALID (intentional wording) |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ✅ COMPLETE (added to HOOKS-README) |
| 3 | MEDIUM | Hook Types/Env | HOOKS-README prompt/agent hook exclusion list only mentions TeammateIdle — should list all 9 command-only events | ✅ COMPLETE (updated exclusion list) |
| 4 | ~~MEDIUM~~ | ~~Config Drift~~ | ~~Windows settings use relative path — windows hooks won't work regardless~~ | ❌ INVALID (intentional platform difference) |
| 5 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ✅ COMPLETE (researched and fixed) |
| 6 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ✅ COMPLETE (added section) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 02:18 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Matcher/Schema | Specify SubagentStart/SubagentStop matcher values (Bash, Explore, Plan, custom) in HOOKS-README — currently says "Agent name string" | ✅ COMPLETE (updated to specific values) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 03:37 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Matcher/Schema | Add WorktreeCreate to HOOKS-README Decision Control Patterns table (stdout path + non-zero exit fails creation) | ✅ COMPLETE (added row to Decision Control Patterns table in HOOKS-README) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |
