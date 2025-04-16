import json
import pytest
from companies.models import Company
from companies.tests.api_tests_pytest.setup_tests import companies_url

pytestmark = pytest.mark.django_db


def test_zero_companies_should_return_empty_list(client, companies_url):
    """Test to ensure an empty list is returned when no companies exist."""
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_exists_should_succeed(client, companies_url):
    """Test to ensure one company is returned correctly."""
    expected_company_name = "Amazon"
    test_company = Company.objects.create(name=expected_company_name)

    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]

    assert response.status_code == 200
    assert response_content["name"] == expected_company_name
    assert response_content["status"] == "Hiring"
    assert response_content["application_link"] == ""
    assert response_content["notes"] == ""
