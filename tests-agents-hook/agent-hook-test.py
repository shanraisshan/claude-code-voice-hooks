#!/usr/bin/env python3
"""Simple logger to test which agent frontmatter hooks actually trigger."""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

# Hardcode log path next to this script for reliability
SCRIPT_DIR = Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR.parent / "agent-hook-test.log"

try:
    # Read stdin JSON (same way hooks.py does it)
    stdin_data = ""
    try:
        stdin_data = sys.stdin.read().strip()
    except Exception:
        pass

    # Parse event name from stdin JSON
    hook_event = "no-stdin"
    if stdin_data:
        try:
            parsed = json.loads(stdin_data)
            hook_event = parsed.get("hook_event_name", "missing-field")
        except Exception:
            hook_event = "parse-error"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    entry = {
        "timestamp": timestamp,
        "hook_event": hook_event,
        "cwd": os.getcwd(),
        "claude_project_dir": os.environ.get("CLAUDE_PROJECT_DIR", "NOT_SET"),
        "stdin_len": len(stdin_data)
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

except Exception as e:
    # Last resort: write error to a fallback location
    fallback = Path("/tmp/agent-hook-test-error.log")
    with open(fallback, "a") as f:
        f.write(f"{datetime.now()}: {e}\n")
