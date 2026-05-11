import os
import uuid
from collections.abc import Generator

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from clients.ethercalc_client import EtherCalcClient


@pytest.fixture(scope="session")
def base_url() -> str:
    load_dotenv()
    return os.getenv("BASE_URL", "https://ethercalc.net").rstrip("/")


@pytest.fixture(scope="session")
def api_client(base_url: str) -> EtherCalcClient:
    return EtherCalcClient(base_url)


@pytest.fixture
def generated_sheet_id() -> str:
    return f"test-{uuid.uuid4().hex}"


@pytest.fixture
def browser() -> Generator[webdriver.Chrome, None, None]:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()
