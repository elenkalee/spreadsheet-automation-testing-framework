import allure
import pytest


@allure.epic("EtherCalc")
@allure.feature("Pages API")
@allure.story("Create page")
@allure.title("Create page with custom room id")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
@pytest.mark.smoke
def test_create_page_returns_created_status_and_location(
    api_client,
    generated_sheet_id,
):
    response = api_client.create_page(generated_sheet_id)

    assert response.status_code == 201
    assert response.headers["Location"].endswith(f"/_/{generated_sheet_id}")
