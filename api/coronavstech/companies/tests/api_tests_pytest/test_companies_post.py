import json
import pytest
from companies.models import Company
from companies.tests.api_tests_pytest.setup_tests import companies_url

pytestmark = pytest.mark.django_db


def test_create_company_without_arguments_should_fail(client, companies_url):
    """Test creating a company without required fields should fail."""
    response = client.post(companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client, companies_url):
    """Test creating a company with an already existing name should fail."""
    Company.objects.create(name="apple")

    response = client.post(companies_url, data={"name": "apple"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_all_fields_should_be_default(
    client, companies_url
):
    """Test creating a company with only a name and default values for other fields."""
    response = client.post(companies_url, data={"name": "test company name"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content["name"] == "test company name"
    assert response_content["status"] == "Hiring"
    assert response_content["application_link"] == ""
    assert response_content["notes"] == ""


def test_create_company_with_layoffs_status_should_succeed(client, companies_url):
    """Test creating a company with the 'Layoffs' status should succeed."""
    response = client.post(
        companies_url, data={"name": "test company name", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content["status"] == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client, companies_url):
    """Test creating a company with an invalid status should fail."""
    response = client.post(
        companies_url, data={"name": "test company name", "status": "WrongStatus"}
    )
    assert response.status_code == 400
    assert "WrongStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)
