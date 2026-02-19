# AGENTS.md — Repository Guidelines for Codex

## Project overview
- This project is a small Python CLI script.
- **Target runtime:** Python 3.12.10.
- **Environment:** Windows 11 + PowerShell.
- Keep changes minimal, readable, and focused

## Structure
- `main.py` is the CLI entry point.
- `tests/` contains pytest unit tests (e.g., `tests/test_main.py`).
- `requirements.txt` is for runtime dependencies (may be empty).
- `requirements-dev.txt` is for developer tooling (e.g., `pytest`).

## Compatibility & behavior (must-follow)
- **Do not break existing behavior; keep backward compatibility.**
- If you change any user-facing behavior (CLI output, arguments, defaults), **update `README.md`** accordingly.

## Development commands (PowerShell)
- Create venv: `py -m venv .venv`
- Activate venv: `.\.venv\Scripts\Activate.ps1`
- Install runtime deps: `py -m pip install -r requirements.txt`
- Install dev deps: `py -m pip install -r requirements-dev.txt`
- Run CLI: `py main.py`
- Run tests: `py -m pytest -q`

## Coding style
- Use 4-space indentation.
- Use `snake_case` for functions/variables and `PascalCase` for classes.
- Keep CLI args/flags short and descriptive (e.g., `--name`).

## Testing guidelines (must-follow)
- Use `pytest`.
- **Add/maintain tests when you add or change a feature.**
- Keep tests deterministic and focused on observable CLI behavior.

## “Project helper files” (keep in sync)
When you make changes, also update any relevant helper files:
- `README.md` (usage, examples, behavior changes)
- `requirements*.txt` (deps)
- `tests/` (coverage for new/changed behavior)
- `.gitignore` / `.gitattributes` (repo hygiene, line endings) — only if needed

## Security & repo hygiene
- Keep secrets out of the repo; use env vars or a local `.env` if needed.
- Do not commit `.venv/`, `__pycache__/`, or `*.pyc`.

## Working agreement for Codex runs (must-follow)
- Prefer a short plan before making changes.
- **At the end, show a `/diff` summary and explain exactly how to run the tests.**