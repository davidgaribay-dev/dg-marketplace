---
name: worktree
description: Create Git worktrees for parallel development. Use when creating worktrees, setting up parallel Claude Code sessions, or working on multiple features simultaneously. Creates standardized worktree structure in adjacent directory.
---

# Git Worktree Creation

Creates a new Git worktree in `../<repo-name>-worktrees/<branch-name>` following best practices for running multiple Claude Code sessions in parallel.

## When to Use This

- Setting up parallel development environments
- Running multiple Claude Code agents on different features
- Working on multiple branches simultaneously without switching
- Creating isolated environments for testing or experimentation

## Quick Start

When the user asks to create a worktree, follow these steps:

1. Get the branch name from the user (if not provided, ask for it)
2. Execute the Python script located at the repository root: `create_worktree.py`
3. Report the results back to the user

Example:
```bash
python create_worktree.py feature/add-drums
```

## What This Does

1. Detects the current repository name and root path
2. Creates `../<repo-name>-worktrees/` directory (if it doesn't exist)
3. Creates new Git worktree with new branch at `../<repo-name>-worktrees/<branch-name>`
4. Copies important non-tracked files:
   - `.env*` files (all environment configurations)
   - `.claude/` directory (Claude Code settings and commands)
5. Provides instructions for next steps

## Script Reference

The worktree creation is handled by [scripts/create_worktree.py](scripts/create_worktree.py).

The script is implemented with:
- Type hints throughout for type safety
- Custom exception classes (GitOperationError, WorktreeCreationError)
- Proper logging infrastructure using Python's logging module
- Error handling with detailed error messages
- Path operations using pathlib for cross-platform compatibility

### Script Usage
```bash
python create_worktree.py <branch-name>
```

### Script Arguments
- `<branch-name>`: Name for the new branch and worktree directory (required)

### Valid Branch Names
- Must not be empty
- Must not start with `-`
- Should follow Git branch naming conventions
- Examples: `feature/add-auth`, `bugfix/login`, `drums`, `keyboards`

## Expected Output

```
Creating worktree for branch: <branch-name>
--------------------------------------------------
Repository: <repo-name>
Root path: <repo-root-path>
Worktrees directory: <worktrees-directory-path>
Created worktree at: <worktree-path>
Created branch: <branch-name>

Copying important files...
Copied .env
Copied .claude/

==================================================
Worktree creation complete!
==================================================

To start working:
  cd <worktree-path>

Or open in your editor:
  code <worktree-path>

To remove this worktree later:
  git worktree remove <branch-name>
```

## Common Workflows

### Creating Multiple Worktrees for Parallel Development

When a user wants to work on multiple features simultaneously:

1. Create worktree for first feature:
   ```bash
   python create_worktree.py feature/drums
   ```

2. Create worktree for second feature:
   ```bash
   python create_worktree.py feature/keyboards
   ```

3. Create worktree for third feature:
   ```bash
   python create_worktree.py feature/basses
   ```

Each worktree can have its own Claude Code session running independently.

### After Worktree Creation

After successfully creating a worktree, ask the user if they would like you to:
1. Help them open the worktree in their editor
2. Start working on a specific task in that worktree
3. Create additional worktrees for other features
4. Explain how to manage and merge worktrees

## Managing Worktrees

### List all worktrees:
```bash
git worktree list
```

### Remove a worktree:
```bash
git worktree remove <branch-name>
```

### Merge worktree changes back to main:
```bash
# From main branch
git merge <branch-name>
```

## Error Handling

The script uses custom exceptions for clear error reporting:

- GitOperationError: Raised when not in a git repository or git command fails
- WorktreeCreationError: Raised when worktree creation fails or already exists
- ValueError: Raised when branch name is invalid

All errors are logged using the logging module and exit with appropriate error codes.

If errors occur, relay them to the user and suggest solutions.

## Best Practices

- Location: Worktrees are created OUTSIDE the main repository to avoid nested repository issues
- Isolation: Each worktree is completely isolated with its own working directory
- Efficiency: Worktrees share the same Git object database (saves disk space)
- Parallel work: Perfect for running multiple Claude Code sessions on different features
- Clean up: Remember to remove worktrees when done to keep your workspace tidy
- Type safety: Script uses type hints for better IDE support and error catching
- Logging: All output uses Python's logging module for professional output management

## Requirements

- Must be in a Git repository
- Python 3 must be installed
- Git must be installed and available in PATH
