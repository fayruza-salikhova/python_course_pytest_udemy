import json
from companies.models import Company
from companies.tests.api_tests.setup_tests import BasicCompanyApiTestCase


class TestGetCompanies(BasicCompanyApiTestCase):
    def test_zero_companies_should_return_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        expected_company_name = "Amazon"
        test_company = Company.objects.create(name=expected_company_name)
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        print(json.dumps(json.loads(response.content), indent=4))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), expected_company_name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")
        test_company.delete()
