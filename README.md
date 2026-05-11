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

Pytest is configured to save Allure result files to `allure-results/`.

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

At the initial stage, marker commands may collect zero tests until test files are added.

## Allure Reports

The Python adapter is installed from `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

Test runs automatically generate Allure result files in `allure-results/` because `pytest.ini` contains:

```ini
addopts = --alluredir=allure-results
```

Run tests and open the report:

```powershell
python -m pytest
allure serve allure-results
```

To use `allure serve`, install Allure Commandline separately and make sure the `allure` command is available in PATH.

Check Java first:

```powershell
java -version
```

If Java is not installed, install JDK 17:

```powershell
winget install EclipseAdoptium.Temurin.17.JDK
```

Install Allure Commandline with Scoop:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install allure
```

Or install Allure Commandline with npm if Node.js is already installed:

```powershell
npm install -g allure-commandline
```

Check that Allure is available:

```powershell
allure --version
```

After installing Java or Allure Commandline, restart PowerShell or the PyCharm terminal if the command is not found.

## GitHub Actions

CI is configured in `.github/workflows/ci.yml`.

The workflow runs on:

- push to any branch
- pull request to `master`
- manual run from the GitHub Actions tab

CI steps:

- install Python 3.11
- install dependencies from `requirements.txt`
- run Ruff
- run all tests with `python -m pytest`
- upload `allure-results/` as a workflow artifact

## Common Fixtures

Common pytest fixtures are defined in `conftest.py` and are available in tests without explicit imports.

- `base_url` - base URL of the tested EtherCalc instance. It is loaded from `BASE_URL` in `.env`; default value is `https://ethercalc.net`.
- `api_client` - configured `EtherCalcClient` instance for API tests.
- `generated_sheet_id` - unique test sheet id generated with `uuid`, so tests do not conflict with each other.
- `browser` - Selenium Chrome browser instance. The browser is opened before a UI test and closed after it.

Example:

```python
def test_open_sheet(browser, base_url, generated_sheet_id):
    browser.get(f"{base_url}/{generated_sheet_id}")

    assert generated_sheet_id in browser.current_url
```

## API Client

API tests should use `EtherCalcClient` through the `api_client` fixture instead of calling `requests` directly in tests.

Available client methods (from https://github.com/audreyt/ethercalc/blob/main/API.md):

- `create_page(sheet_id)`
- `get_page_content(sheet_id)`
- `get_cells(sheet_id)`
- `get_cell(sheet_id, cell)`
- `export_csv(sheet_id)`
- `export_json(sheet_id)`
- `export_html(sheet_id)`

Example:

```python
def test_export_csv(api_client, generated_sheet_id):
    api_client.create_page(generated_sheet_id)

    csv_content = api_client.export_csv(generated_sheet_id)

    assert isinstance(csv_content, str)
```

