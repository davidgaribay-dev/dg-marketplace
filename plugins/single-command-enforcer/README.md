# Single Command Enforcer

A Claude Code plugin that blocks command chaining in Bash tool calls, requiring each command to be approved individually.

## What it does

This PreToolUse hook intercepts Bash tool calls and blocks commands containing:

- **Command chaining operators**: `&&`, `||`, `;`
- **Command substitution**: `$()`, backticks
- **Process substitution**: `<()`, `>()`

## Why use it

When Claude runs multiple commands chained together, you only get one approval prompt for the entire chain. This plugin forces each command to be separate, giving you granular control to approve or reject each one.

## Installation

```bash
/plugin install single-command-enforcer@dg-marketplace
```

## Example

Without this plugin, Claude might run:
```bash
cd /tmp && rm -rf important_files && echo "done"
```

With this plugin, Claude must run each command separately:
```bash
cd /tmp
# (requires approval)
rm -rf important_files
# (requires approval)
echo "done"
# (requires approval)
```
