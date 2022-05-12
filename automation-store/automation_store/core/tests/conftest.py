import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client_api():
    return APIClient()
