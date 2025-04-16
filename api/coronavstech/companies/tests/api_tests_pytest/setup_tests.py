import pytest
from django.urls import reverse
from rest_framework.test import APIClient

# Mapping of URLs for better extendability
URLS = {"companies": reverse("companies-list")}


@pytest.fixture
def client():
    """Fixture for the API client."""
    return APIClient()


@pytest.fixture
def companies_url():
    """Fixture for the companies URL."""
    return URLS["companies"]
