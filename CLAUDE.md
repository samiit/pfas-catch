use context7

# CLAUDE.md

This file provides personalized guidance for Claude Code (claude.ai/code) when working with Python projects for this user.

## General Python Projects Overview

These guidelines apply broadly to all of your Python projects regardless of framework or tooling, designed to keep code clean, maintainable, and consistent.

## Development Environment

- Use Python 3.12+ for all projects (take advantage of modern language features and typing improvements).
- Use your preferred package manager and virtual environment tooling consistently (e.g., uv, pipenv, poetry, or venv).
- Maintain isolated virtual environments for each project for dependency management.

## Common Commands (Adapt as Needed)

```bash
# Install dependencies (example)
uv sync

# Add new dependencies to local virtualenv
uv add <package>

# Activate virtual environment (if applicable)
source .venv/bin/activate

# Run your application script
uv run python main.py
/markdown

## Code Style and Best Practices

### Clean Code Principles

 • Write self-documenting code with clear, descriptive variable and function names.
 • Define small functions focused on a single responsibility.
 • Prefer explicit and straightforward code over clever or implicit constructs.
 • Names should reveal intent clearly.

### DRY (Don't Repeat Yourself)

 • Identify common functionality and extract it into reusable functions, classes, or modules.
 • Use constants for repeated literals or magic values.
 • Avoid duplicated logic; centralize common behavior.

### Type Hints (Python 3.12+ Style)

 • Use built-in generics without importing from typing where possible:
    • list[str] instead of List[str]
    • dict[str, int] instead of Dict[str, int]
    • set[int] instead of Set[int]
    • tuple[str, ...] instead of Tuple[str, ...]
    • Use union with |, e.g., str | None instead of Optional[str]
 • Only import from typing when necessary (Protocol, TypeVar, Generic).
 • Never relax type hints to an extent that we have to use `Any`, ever!!! Whenever you feel you need to make a function input or output a dict, you should create proper types for it even if it just a Literal

### Control Flow

 • Use guard clauses and early returns to reduce nesting.
 • Avoid multiple nested conditionals by extracting complex boolean expressions into well-named functions.
 • Example:
   python
   def is_valid_user(user):
       return user.is_active and user.email_verified and user.has_permission()

   if not is_valid_user(user):
       return
   /python

### Loop Handling

 • Extract complex loop logic into separate helper functions for clarity and testing.
 • Use list/dict comprehensions where appropriate for concise looping.

### Indentation and Nesting

 • Keep nesting shallow (recommended max 2-3 levels).
 • Prefer flat code structure over deeply nested code blocks.
 • Use early returns and function extraction to reduce indentation levels.

### Error Handling

 • Avoid over-catching exceptions; let unexpected exceptions propagate for debugging.
 • Catch exceptions only when recovery or meaningful fallback is possible.

### Comments and Documentation

 • Favor clear code over comments; add comments sparingly when the intent or rationale is not obvious.
 • Document public interfaces, classes, and functions with concise docstrings.

## Project Structure (General Recommendations)

 • Organize source code under a package folder.
 • Keep tests in a separate tests/ directory.
 • Use a modern project configuration file (e.g., pyproject.toml) to manage dependencies and tooling.
 • Use version control roots and ignore virtual environments and build artifacts.

## Example Project Layout

text
project-root/
├── src_project/          # Python package source code
│   ├── __init__.py
│   └── main.py
├── tests/                # Test suite
│   └── test_main.py
├── .venv/                # Virtual environment (ignored in VCS)
├── pyproject.toml        # Build and dependency config
├── README.md
└── .gitignore
/text

## Framework-Integration Test

Add a simple integration test script framework_integration_test.py to verify that your environment and main dependencies are correctly installed and working.

python
"""
Framework-integration-test for Python projects using `uv` as the default package manager.

This script tests:
- Basic Python 3.12+ features and type hints
- Core dependency (pydantic) functionality if installed

Usage with uv:
```bash
# Ensure dependencies are synced
uv sync

# Run the integration test within the uv-managed venv
uv run python framework_integration_test.py
/python

Adapt this test to include other key libraries/frameworks in your projects. """

# Example 1: Basic Python and type hinting test

def greet(name: str | None = None) -> str: if not name: return "Hello, World!" return f"Hello, {name}!"

def test_greet(): assert greet() == "Hello, World!" assert greet("Claude") == "Hello, Claude!"

# Example 2: Pydantic integration test

try: from pydantic import BaseModel, ValidationError


 class User(BaseModel):
     id: int
     name: str | None

 def test_pydantic_model():
     user = User(id=1, name="Alice")
     assert user.id == 1
     assert user.name == "Alice"
     try:
         User(id="bad_id")
     except ValidationError:
         pass
     else:
         assert False, "ValidationError was not raised"

 test_pydantic_model()
 print("Pydantic integration test passed.")


except ImportError: print("Pydantic not installed - skipping pydantic integration test.")

# Run all tests when executed as script

if name == "main": test_greet() print("Basic Python environment and type hinting test passed.")

text

---

## Git Guidelines

### CRITICAL RULES - NEVER BREAK THESE:

 • **NEVER** use `git add -A` or `git add .` - these are dangerous and can add unintended files
 • **ALWAYS** add files explicitly by name: `git add specific_file.py`
 • **ALWAYS** check `git status` and `git diff --staged` before committing
 • **NEVER** commit without reviewing exactly what is being staged

### Safe Git Workflow:
```bash
# Check what's changed
git status

# Add specific files only
git add path/to/specific_file.py
git add another/specific_file.py

# Review what will be committed
git diff --staged

# Commit with descriptive message
git commit -m "feat: add specific feature with clear description"
```

## Final Notes

- Adapt tooling commands according to the specific project package manager (`uv` recommended by default).
- Prioritize readability and maintainability over micro-optimizations.
- Leverage Python 3.12+ features for modern, idiomatic code.
- Use this guide to maintain consistency and quality across all your Python projects.

## Common Development Practices

 • Always uv run python

use context7
<ch:aliases>
ch   → Main helper: ch [category] [command]
chp  → Project overview (run first in new projects)
chs  → Search tools: find-code, find-file, search-imports
chg  → Git ops: quick-commit, pr-ready, diff

</ch:aliases>

<ch:categories>
project|p         → Project analysis
docker|d          → Container ops: ps, logs, shell, inspect
git|g             → Git workflows
search|s          → Code search (needs: ripgrep)
ts|node           → TypeScript/Node.js (needs: jq)
multi|m           → Multi-file ops (uses: bat)
env|e             → Environment checks
api               → API testing (needs: jq, httpie)
interactive|i     → Interactive tools (needs: fzf, gum)
context|ctx       → Context generation
code-relationships|cr → Dependency analysis
code-quality|cq   → Quality checks

</ch:categories>

<ch:key-commands>
# Start with project overview
chp

# Use helpers not raw commands
chs find-code "pattern"      # not grep
ch m read-many f1 f2 f3      # not multiple cats
chg quick-commit "msg"       # not git add && commit
ch i select-file             # interactive file picker
ch ctx for-task "desc"       # generate focused context
ch api test /endpoint        # test APIs

</ch:key-commands>

<ch:required-tools>
ripgrep → search-tools.sh
jq      → project-info.sh, ts-helper.sh, api-helper.sh
fzf     → interactive selections
bat     → syntax highlighting
gum     → interactive prompts
delta   → enhanced diffs

</ch:required-tools>

<ch:paths>
Scripts: ~/.claude/scripts/
Commands: ~/.claude/commands/

</ch:paths>
