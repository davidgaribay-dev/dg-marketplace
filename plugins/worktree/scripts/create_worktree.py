#!/usr/bin/env python3
"""
Git Worktree Creation Script

Creates a new Git worktree in a standardized location with proper structure.
Usage: python create_worktree.py <branch-name>
"""

import sys
import logging
import subprocess
import shutil
from pathlib import Path
from typing import NoReturn


logger = logging.getLogger(__name__)


class GitOperationError(Exception):
    """Raised when a git operation fails."""
    pass


class WorktreeCreationError(Exception):
    """Raised when worktree creation fails."""
    pass


def _execute_git_command(*args: str) -> str:
    """Execute a git command and return stdout."""
    result = subprocess.run(
        ['git', *args],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()


def _get_git_toplevel() -> Path:
    try:
        return Path(_execute_git_command('rev-parse', '--show-toplevel'))
    except subprocess.CalledProcessError as e:
        raise GitOperationError("Not in a git repository") from e


def get_repo_name() -> str:
    return _get_git_toplevel().name


def get_repo_root() -> Path:
    return _get_git_toplevel()


def create_worktrees_directory(repo_root: Path, repo_name: str) -> Path:
    worktrees_dir = repo_root.parent / f"{repo_name}-worktrees"
    worktrees_dir.mkdir(exist_ok=True)
    return worktrees_dir


def create_worktree(worktrees_dir: Path, branch_name: str) -> Path:
    worktree_path = worktrees_dir / branch_name

    if worktree_path.exists():
        raise WorktreeCreationError(f"Worktree already exists at {worktree_path}")

    try:
        subprocess.run(
            ['git', 'worktree', 'add', '-b', branch_name, str(worktree_path)],
            check=True,
            capture_output=True
        )
        logger.info("Created worktree at: %s", worktree_path)
        logger.info("Created branch: %s", branch_name)
    except subprocess.CalledProcessError as e:
        raise WorktreeCreationError(f"Failed to create worktree: {e.stderr.decode()}") from e

    return worktree_path


def _copy_file_if_exists(source: Path, dest: Path) -> bool:
    if source.exists():
        shutil.copy2(source, dest)
        return True
    return False


def _copy_directory_if_exists(source: Path, dest: Path) -> bool:
    if source.exists():
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(source, dest)
        return True
    return False


def copy_untracked_artifacts(repo_root: Path, worktree_path: Path) -> None:
    env_files = ('.env', '.env.local', '.env.development', '.env.production')
    config_directories = ('.claude',)

    for file_name in env_files:
        if _copy_file_if_exists(repo_root / file_name, worktree_path / file_name):
            logger.info("Copied %s", file_name)

    for dir_name in config_directories:
        if _copy_directory_if_exists(repo_root / dir_name, worktree_path / dir_name):
            logger.info("Copied %s/", dir_name)


def validate_branch_name(branch_name: str) -> None:
    if not branch_name or branch_name.startswith('-'):
        raise ValueError("Invalid branch name")


def log_usage_instructions(worktree_path: Path, branch_name: str) -> None:
    separator = "=" * 50
    message = f"""
{separator}
Worktree creation complete!
{separator}

To start working:
  cd {worktree_path}

Or open in your editor:
  code {worktree_path}

To remove this worktree later:
  git worktree remove {branch_name}
"""
    logger.info(message)


def exit_with_error(message: str, exit_code: int = 1) -> NoReturn:
    logger.error(message)
    sys.exit(exit_code)


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )


def main() -> None:
    _configure_logging()

    if len(sys.argv) != 2:
        logger.info("Usage: python create_worktree.py <branch-name>")
        logger.info("Example: python create_worktree.py feature/add-drums")
        sys.exit(1)

    branch_name = sys.argv[1]

    try:
        validate_branch_name(branch_name)

        logger.info("Creating worktree for branch: %s", branch_name)
        logger.info("-" * 50)

        repo_root = get_repo_root()
        repo_name = get_repo_name()

        logger.info("Repository: %s", repo_name)
        logger.info("Root path: %s", repo_root)

        worktrees_dir = create_worktrees_directory(repo_root, repo_name)
        logger.info("Worktrees directory: %s", worktrees_dir)

        worktree_path = create_worktree(worktrees_dir, branch_name)

        logger.info("\nCopying important files...")
        copy_untracked_artifacts(repo_root, worktree_path)

        log_usage_instructions(worktree_path, branch_name)

    except (ValueError, GitOperationError, WorktreeCreationError) as e:
        exit_with_error(str(e))
    except Exception as e:
        exit_with_error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
