# Spreadsheet Automation Testing Framework

PET project for automated testing with Python, pytest, Selenium, requests, webdriver-manager, and python-dotenv.

## Setup on a Fresh Environment

1. Clone the repository and open the project folder:

```powershell
git clone <https://github.com/elenkalee/spreadsheet-automation-testing-framework.git>
cd spreadsheet-automation-testing-framework
```

2. Create a virtual environment:

```powershell
python -m venv .venv
```

3. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, allow scripts for the current user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

4. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

5. Check that the dependencies are installed correctly:

```powershell
python -m pip check
python -c "import pytest, requests, selenium, webdriver_manager, dotenv; print('Dependencies are installed')"
```

6. Run tests:

```powershell
python -m pytest
```

## Pytest Markers

Available markers are configured in `pytest.ini`:

- `api` - API tests
- `ui` - UI tests
- `e2e` - end-to-end tests
- `smoke` - smoke tests
- `regression` - regression tests

Run tests by marker:

```powershell
python -m pytest -m api
python -m pytest -m ui
python -m pytest -m smoke
```

