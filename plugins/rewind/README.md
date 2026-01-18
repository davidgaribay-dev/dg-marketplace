# Rewind Plugin

Claude Code hook for ingesting conversation data into the Rewind API/Neo4j database.

## Features

- Runs on the Stop event to capture conversation data
- Pure Python 3 stdlib (no external dependencies)
- State tracking to avoid duplicate message ingestion
- Incremental processing (only new lines since last run)
- Never blocks Claude Code (returns 0 on any error)

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `REWIND_API_URL` | `http://localhost:8429` | Rewind API endpoint |
| `REWIND_HOOK_ENABLED` | `true` | Enable/disable the hook |
| `REWIND_HOOK_DEBUG` | `false` | Enable debug logging |

## Installation

1. Clone or copy this plugin to your Claude Code plugins directory
2. Configure the environment variables as needed
3. The hook will automatically run when Claude Code sessions end

## State Files

The hook maintains state in `~/.claude/state/rewind/`:
- `state.json` - Tracks processed transcript lines
- `hook.log` - Debug and error logs
