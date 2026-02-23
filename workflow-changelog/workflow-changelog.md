# Workflow Changelog History

---

## [2026-02-20 08:14 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Doc Fix | `agent_type` version attribution — README said v2.1.43, changelog disagrees | ✅ marked as ~v2.1.43 (unconfirmed) |
| 2 | MEDIUM | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's 6 | ✅ added update note to HOOKS-README and README |
| 3 | LOW | Hook Options Table | `notification_type`, `message`, `title` missing from Notification Options column | ✅ added to HOOKS-README |
| 4 | LOW | Hook Types/Env | Additional `CLAUDE_HOOK_*` env vars from blog sources | ✖️ false positive — not in official docs |
| 5 | LOW | New Hook | `OpenInEditor` hook existence | ✖️ false positive — does not exist in official docs |

---

## [2026-02-20 11:15 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Hook Options Table | UserPromptSubmit Options column missing `prompt` input field in HOOKS-README | ✅ added `prompt` to Options column |
| 2 | LOW | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's tested 6; needs re-testing | ✅ reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153) |

---

## [2026-02-20 11:57 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ RESOLVED — already reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153); pending response |

---

## [2026-02-21 06:41 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeCreate — new in v2.1.50 for agent worktree isolation VCS setup | ✅ added — all 18 hooks consistent across files |
| 2 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeRemove — new in v2.1.50 for agent worktree isolation VCS teardown | ✅ added — all 18 hooks consistent across files |
| 3 | MEDIUM | Version Update | Update all version badges from v2.1.49 → v2.1.50, hook count from 16 → 18 across README, HOOKS-README, presentation, hooks.py | ✅ updated — badge now shows v2.1.50 (Feb 21, 2026) |
| 4 | LOW | Hook Options Table | Add `tool_response` to PostToolUse Options column in HOOKS-README | ✅ added to HOOKS-README |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ RESOLVED — upstream bug reported at [#27153](https://github.com/anthropics/claude-code/issues/27153); pending their fix |

---

## [2026-02-21 07:57 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Presentation | Add can-block/cannot-block badge to WorktreeCreate and WorktreeRemove slides — all other 16 hook slides had this badge | ✅ added "Cannot Block" badge to both slides |
| 2 | LOW | Documentation | README.md changelog table missing v2.1.47 `last_assistant_message` — no action needed, table is for new hook additions only | ✖️ not applicable — editorial choice |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ RESOLVED — upstream bug reported; pending their fix |
| 4 | LOW | Presentation | Setup hook not shown in lifecycle diagram — fires separately via --init/--maintenance | ✅ added Setup to lifecycle diagram with separate trigger section |
| 5 | LOW | Workflow | Updated workflow-add-hook to require can-block badge on every new hook slide and update summary can-block list | ✅ added explicit instructions to workflow |

---

## [2026-02-21 08:13 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | Add `WorktreeCreate` and `WorktreeRemove` to "Not in Official Docs" table in HOOKS-README — they exist in changelog (v2.1.50) but are absent from official hooks reference | ✅ added both rows to table |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ RESOLVED — upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there |
| 3 | LOW | Workflow | Updated workflow-add-hook to include "Not in Official Docs" table step when adding changelog-only hooks | ✅ added instruction to HOOKS-README section |

---

## [2026-02-21 09:10 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ RESOLVED — upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there |

---

## [2026-02-22 02:30 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | WorktreeCreate can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list | ✅ fixed — changed to "Can Block" + added to summary list |
| 2 | HIGH | Doc Fix | HOOKS-README "Not in Official Docs" table stale — WorktreeCreate and WorktreeRemove ARE now in official docs (17 hooks listed, not 15) | ✅ fixed — removed stale rows, updated count to 17 |
| 3 | MEDIUM | New Input Field | WorktreeCreate missing `name` input field in HOOKS-README Options column | ✅ added `name` to Options column |
| 4 | MEDIUM | New Input Field | WorktreeRemove missing `worktree_path` input field in HOOKS-README Options column | ✅ added `worktree_path` to Options column |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ RESOLVED — upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there |

---

## [2026-02-23 01:08 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading | ⚠️ NEEDS INVESTIGATION |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ⚠️ NEEDS INVESTIGATION |
| 3 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ⚠️ NEEDS INVESTIGATION |
| 4 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ⚠️ NEEDS INVESTIGATION |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ⚠️ NEEDS INVESTIGATION |
