# Claude Code Voice Hooks 🔊 Ding Dong
[supports all 15 hooks](https://github.com/shanraisshan/claude-code-voice-hooks/blob/main/.claude/hooks/HOOKS-README.md#hook-events-overview---official-15-hooks)

<p align="center">
  <img src="!/claude-speaking.svg" alt="Claude Code mascot speaking" width="168" height="108">
</p>

plays #ding 🔊 on PreToolUse and #dong 🔊 on PostToolUse

Providing voice feedback to your Claude Code agent! Get instant audio notifications for tool usage, prompts, git commits, and session events.

# [Demo Video + Presentation](https://youtu.be/6_y3AtkgjqA)

<p>
  <a href="https://youtu.be/6_y3AtkgjqA"><img src="!/pill-youtube-red.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="presentation/index.html"><img src="!/pill-slides.svg" alt="Slides" height="36"></a>
</p>

![thumbnail](!/thumbnail3.jpg)

## Installation

<p>
  <a href="install/README-mac.md"><img src="!/pill-mac.svg" alt="Mac" height="36"></a>&nbsp;
  <a href="install/README-linux.md"><img src="!/pill-linux.svg" alt="Linux" height="36"></a>&nbsp;
  <a href="install/README-windows.md"><img src="!/pill-windows.svg" alt="Windows" height="36"></a>
</p>

## Common Errors

If you don't follow the prerequisites, you will see the following error on claude code start

```
SessionStart:startup hook error
```

## Changelog

- **v3.2** (Feb 6, 2026): Added `TeammateIdle` and `TaskCompleted` hooks (15 hooks total)
- **v3.1** (Jan 30, 2026): Added `async` and `once` hook options — hooks now run in background without blocking Claude Code, with `once` option for session lifecycle events
- **v3** (Jan 19, 2026): Added `Setup` hook (13 hooks) — runs when Claude Code executes the /setup command for project initialization
- **v2** (Nov 26, 2025): Added `PermissionRequest` and `SubagentStart` hooks (12 hooks) — introduced in [Claude Code v2.0.43](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2043) and [v2.0.45](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2045) ■ [Demo 2](https://youtu.be/JFPJtMNV8Qw)
- **v1** (Nov 5, 2025): Initial release with 10 hooks ■ [Demo 1](https://youtu.be/vgfdSUbz_b0)

## Links

<p>
  <a href="https://www.youtube.com/watch?v=vgfdSUbz_b0"><img src="!/pill-youtube.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="https://www.linkedin.com/posts/shanraisshan_claudecode-aicoding-voicehooks-activity-7393305703697805312-4gl0"><img src="!/pill-linkedin.svg" alt="LinkedIn" height="36"></a>&nbsp;
  <a href="https://www.reddit.com/r/ClaudeCode/comments/1otaf7f/i_just_made_claude_code_speak_using_hooks/"><img src="!/pill-reddit.svg" alt="Reddit" height="36"></a>&nbsp;
  <a href="https://x.com/shanraisshan/status/1987817251966513620"><img src="!/pill-x.svg" alt="X" height="36"></a>&nbsp;
  <a href="https://medium.com/@shanraisshan/claude-code-just-got-a-voice-%25EF%25B8%258F-51008157305b"><img src="!/pill-medium.svg" alt="Medium" height="36"></a>
</p>
