import pytest
from core.models import User
from model_bakery import baker


@pytest.fixture
def user():
    return baker.make(User)


@pytest.fixture
def client_authenticated(client, user):
    client.force_login(user=user)
    return client
