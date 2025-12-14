# Claude Code Marketplace

A curated collection of Claude Code plugins for Git workflows and developer productivity.

## 🚀 Quick Start

### Add this marketplace

```bash
/plugin marketplace add davidgaribay-dev/claude-code-marketplace
```

### Browse and install

```bash
/plugin                                              # Browse available plugins
/plugin install worktree@claude-code-marketplace    # Install specific plugin
```

## 📦 Available Plugins

### Commands

#### `/git-commit-push`
Interactive git workflow with approval gates for reviewing changes, generating conventional commit messages, and pushing to remote. Uses industry best practices for commit message formatting.

**Install**: `/plugin install git-commit-push@claude-code-marketplace`

### Skills

#### `worktree`
Create Git worktrees for parallel development. Creates standardized worktree structure in adjacent directory for working on multiple features simultaneously. Ideal for running multiple Claude Code sessions in parallel.

**Install**: `/plugin install worktree@claude-code-marketplace`

## 💡 Why Use This Marketplace?

- **🎯 Git-Focused**: Specialized plugins for Git workflows and productivity
- **✅ Best Practices**: Conventional commits, approval gates, and industry standards
- **🔧 Developer Tools**: Worktree management for parallel development
- **📦 Granular Control**: Install only what you need, no bloat

## 🛠️ Local Development & Testing

### Validate the marketplace

```bash
claude plugin validate .
```

### Test locally

```bash
/plugin marketplace add .
/plugin install worktree@claude-code-marketplace
```

### List configured marketplaces

```bash
/plugin marketplace list
```

## 🤝 Contributing

Contributions welcome! Please open an issue or PR on [GitHub](https://github.com/davidgaribay-dev/claude-code-marketplace).

### Project Structure

```
.
├── .claude/
│   ├── commands/
│   │   └── git-commit-push.md
│   └── skills/
│       └── worktree/
│           ├── SKILL.md
│           └── scripts/
│               └── create_worktree.py
├── .claude-plugin/
│   └── marketplace.json
└── README.md
```

### Adding New Plugins

1. Create your plugin/skill in the appropriate directory
2. Add an entry to `.claude-plugin/marketplace.json`:

```json
{
  "name": "your-plugin-name",
  "source": "./path/to/plugin",
  "description": "What your plugin does",
  "category": "productivity",
  "tags": ["tag1", "tag2"],
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "strict": false
}
```

3. Validate and test:

```bash
claude plugin validate .
/plugin marketplace add .
/plugin install your-plugin-name@claude-code-marketplace
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

## 👤 Author

**David Garibay** ([@davidgaribay-dev](https://github.com/davidgaribay-dev))
Email: me@davidgaribay.dev

---

**Repository**: [github.com/davidgaribay-dev/claude-code-marketplace](https://github.com/davidgaribay-dev/claude-code-marketplace)
