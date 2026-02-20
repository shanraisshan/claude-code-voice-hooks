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
