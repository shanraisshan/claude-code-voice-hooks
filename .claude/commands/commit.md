---
description: Commit changes with auto-generated message showing command context, timestamp, and change count
argument-hint: [command name that produced these changes, e.g. changelog-tracker]
---

# Commit

Create a git commit with an auto-generated message. The first line is a summary, followed by a numbered list of the actions/changes that were executed.

## Format

```
[/command-name][DD-Mon-YY HH:MM AM/PM] N changes

1. First change description
2. Second change description
...
```

**"N changes" refers to the number of actions/changes that were executed during the session** — NOT the number of git file changes. Look back through the conversation to find the actions that were taken (e.g., from a changelog-tracker report's action items, or from an add-new-hook workflow's steps).

## Steps

1. **Get the command name** from `$ARGUMENTS`. If empty, ask the user what command or task produced these changes.

2. **Get the current timestamp** by running:
   ```
   date "+%d-%b-%y %I:%M %p"
   ```

3. **Review the conversation** to identify all actions/changes that were executed. Summarize each as a short one-line description.

4. **Run `git status --short`** to see which files were changed.

5. **Show the user** the proposed commit message (title + numbered list) and the files to stage. Ask for confirmation before committing.

6. **Stage and commit**:
   - Stage all relevant changed files (use `git add` with specific file paths — avoid `git add -A`)
   - Commit using a HEREDOC for multi-line message

## Example

If `/commit changelog-tracker` is run after a session that executed 10 actions:

```
[/changelog-tracker][20-Feb-26 08:14 PM] 10 changes

1. Added stop_hook_active to Stop & SubagentStop Options
2. Added source to ConfigChange & SessionStart Options
3. Added reason to SessionEnd, trigger/custom_instructions to PreCompact
4. Added teammate_name/team_name to TaskCompleted Options
5. Removed stale workaround code block from HOOKS-README
6. Fixed PreToolUseRejected typo to SessionStart, SessionEnd
7. Updated presentation Slide 21 to show all 6 agent hooks
8. Removed empty plans/ sound folder
9. Added Decision Control Patterns and JSON Output Fields sections
10. Fixed $CLAUDE_SESSION_ID to session_id (via stdin JSON)
```

## Rules

1. **Always show the commit message and file list** before committing — never auto-commit
2. **Never stage sensitive files** (.env, credentials, secrets)
3. **Use specific file paths** when staging — not `git add -A` or `git add .`
4. **Do not push** unless the user explicitly asks
5. **Changes = actions executed**, not files changed
6. Keep each change description short (under 80 chars)
