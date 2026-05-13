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
    # Step: create a new EtherCalc page with an explicit room id.
    response = api_client.create_page(generated_sheet_id)

    # Add request and response details to Allure for easier CI failure analysis.
    allure.attach(
        f"{response.request.method} {response.request.url}",
        name="Request",
        attachment_type=allure.attachment_type.TEXT,
    )
    allure.attach(
        str(dict(response.headers)),
        name="Response headers",
        attachment_type=allure.attachment_type.TEXT,
    )
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.TEXT,
    )

    # Assert: EtherCalc should confirm page creation and return the created page id.
    assert response.status_code == 201, (
        f"Expected 201 Created, got {response.status_code}. "
        f"Request URL: {response.request.url}. Response body: {response.text}"
    )
    assert response.headers["Location"].endswith(f"/_/{generated_sheet_id}")
