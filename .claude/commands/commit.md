---
description: Commit changes with auto-generated message showing command context, timestamp, and change count
argument-hint: [command name that produced these changes, e.g. changelog-tracker]
---

# Commit

Create a git commit with an auto-generated message in this format:

```
[/command-name][DD-Mon-YY HH:MM AM/PM] N changes detected
```

## Steps

1. **Get the command name** from `$ARGUMENTS`. If empty, ask the user what command or task produced these changes.

2. **Get the current timestamp** by running:
   ```
   date "+%d-%b-%y %I:%M %p"
   ```

3. **Count the changes** by running `git status --short` and counting the number of changed files (staged + unstaged + untracked).

4. **Show the user** the proposed commit message and the list of changed files. Ask for confirmation before committing.

5. **Stage and commit**:
   - Stage all relevant changed files (use `git add` with specific file paths — avoid `git add -A`)
   - Commit with the message: `[/$ARGUMENTS][<timestamp>] <N> changes detected`

## Example

If the user runs `/commit changelog-tracker` at 8:12 PM on Feb 20, 2025, and there are 12 changed files:

```
[/changelog-tracker][20-Feb-25 08:12 PM] 12 changes detected
```

## Rules

1. **Always show the commit message and file list** before committing — never auto-commit
2. **Never stage sensitive files** (.env, credentials, secrets)
3. **Use specific file paths** when staging — not `git add -A` or `git add .`
4. **Do not push** unless the user explicitly asks
5. The commit message is a single line — no body, no Co-Authored-By
