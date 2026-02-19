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

## Test

```powershell
python -m pytest
```