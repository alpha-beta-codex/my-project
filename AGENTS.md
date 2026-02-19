# Repository Guidelines

## Project Structure & Module Organization

This is a small Python CLI project. Layout:

- `main.py` CLI entry point
- `tests/` pytest tests
- `requirements.txt` runtime dependencies (may be empty)
- `requirements-dev.txt` development/test dependencies

Keep new modules grouped by feature and prefer flat, readable structures over deep nesting.

## Build, Test, and Development Commands

Target runtime: Python 3.12.10 on Windows 11 with PowerShell.

Common commands (from repo root):

- `python main.py --help` show CLI usage
- `python main.py --name "Ada"` run the CLI
- `python -m pytest` run tests

If you add scripts or a build step, document the exact command and expected output here.

## Coding Style & Naming Conventions

- Indentation: 4 spaces, no tabs
- Filenames: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`

If you introduce a formatter or linter (for example, `ruff` or `black`), add the tool and version plus the command to run it.

## Testing Guidelines

Tests use `pytest` and live under `tests/`. Name tests `test_<module>.py` and functions `test_<behavior>`. Prefer small tests that assert CLI output and exit codes. Run tests with `python -m pytest`.

## Commit & Pull Request Guidelines

No Git history exists in this workspace. If you initialize Git, use clear, imperative commit messages (for example, `Add CLI greeting`) and include in PRs:

- What changed and why
- How to test
- Screenshots only for UI changes

## Security & Configuration Tips

Do not commit secrets. Use `.env` for local values and keep it in `.gitignore`.