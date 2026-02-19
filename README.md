# Simple Python CLI

## Setup

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

## Run

```powershell
python main.py --name "Ada"
```

Optional flag:

- `--shout` prints the greeting in uppercase.
- `--v` prints the script version number.

Example:

```powershell
python main.py --name "Ada" --shout
```

```powershell
python main.py --v
```

## Test

```powershell
python -m pytest
```
