---
description: Review changes, generate commit message, commit and push with approval gates
model: haiku
allowed-tools: Bash(git:*)
---

# Interactive Git Commit and Push Workflow

Execute this multi-step workflow with approval gates at each critical point.

## Step 1: Review Changed Files

First, show me what files have changed:

Execute git status to see modified, added, deleted files.
Execute git diff HEAD to show the complete diff of all unstaged changes.
Execute git diff --cached to show any staged changes.

Present the changes in a clear, organized format.

## Step 2: User Approval - Review Changes

STOP and ask the user: "Do these changes look correct? Should we proceed to generating a commit message?"

Wait for explicit user confirmation before continuing.
If the user says no or requests changes, ask what they would like to do differently.
Only proceed to Step 3 after receiving affirmative confirmation.

## Step 3: Generate Commit Message Using Best Practices

Based on the changes shown above, generate a commit message following these industry best practices:

### Conventional Commits Format

Type(scope): Subject line

Body paragraph explaining the what and why (not how)

Footer with breaking changes and issue references

### Commit Types (use the most appropriate):
- feat: New feature for the user
- fix: Bug fix for the user
- docs: Documentation only changes
- style: Formatting, missing semicolons, etc (no code change)
- refactor: Code change that neither fixes a bug nor adds a feature
- perf: Code change that improves performance
- test: Adding missing tests or correcting existing tests
- build: Changes to build system or external dependencies
- ci: Changes to CI configuration files and scripts
- chore: Other changes that don't modify src or test files
- revert: Reverts a previous commit

### Subject Line Rules:
- Use imperative mood ("add feature" not "added feature")
- Do not capitalize first letter
- No period at the end
- Maximum 50 characters
- Be specific and descriptive

### Body Rules (if needed):
- Wrap at 72 characters per line
- Explain what and why vs how
- Separate from subject with blank line
- Use bullet points for multiple changes
- Reference issue numbers

### Footer Rules:
- BREAKING CHANGE: description (if applicable)
- Closes #123, Fixes #456 (reference issues)

### Examples of Good Commit Messages:

```
feat(auth): add OAuth2 login flow

Implement OAuth2 authentication to support Google and GitHub login.
This replaces the previous email/password only authentication.

- Add OAuth2 client configuration
- Create callback handlers for providers
- Update user model to store OAuth tokens
- Add provider selection UI

Closes #234
```

```
fix(api): prevent race condition in user creation

Add mutex lock around user creation to prevent duplicate entries
when multiple requests arrive simultaneously.

Fixes #456
```

```
docs: update API documentation for v2 endpoints

Add comprehensive examples for all v2 API endpoints including
request/response formats and error codes.
```

Present the proposed commit message following these conventions.

## Step 4: User Approval - Commit Message

STOP and ask the user: "Do you approve this commit message, or would you like me to modify it?"

Wait for explicit user confirmation.
If the user suggests changes, incorporate them and present the updated message.
Only proceed to Step 5 after the user approves the final commit message.

## Step 5: Execute Commit

Execute git add -A to stage all changes (or use git add with specific files if user specified).
Execute git commit with the approved message using proper formatting (use -m for subject, additional -m for body).
Show the result of the commit operation.

## Step 6: User Approval - Ready to Push

STOP and ask the user: "The commit is complete. Are you ready to push to the remote repository?"

Show the current branch name and remote tracking information.
Wait for explicit user confirmation.
If the user says no, explain that they can push later with git push.
Only proceed to Step 7 if the user confirms they want to push.

## Step 7: Execute Push

Execute git push to push the commit to the remote repository.
Show the result of the push operation.

## Step 8: Final Confirmation

Display a summary:
- Commit hash and message
- Branch pushed to
- Remote repository name
- Number of files changed

Confirm that the workflow completed successfully.

## Important Guidelines

- At each STOP point, you must explicitly ask the user for approval before continuing
- Never skip approval gates
- If any git command fails, stop immediately and report the error
- Be clear about what action you are about to take before taking it
- Show command output so the user can verify each step succeeded
- Follow conventional commits format strictly
- Write commit messages in imperative mood
- Keep subject lines under 50 characters
- Wrap body text at 72 characters
