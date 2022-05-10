import pytest
from core.models import User
from django.urls import reverse
from model_bakery import baker


def make_url(user_id):
    return reverse("api-1.0.0:unfollow", kwargs={"user_id": user_id})


@pytest.mark.django_db
def test_unfollow(client_authenticated):
    other_user = baker.make(User)

    resp = client_authenticated.post(make_url(other_user.id))

    assert resp.status_code == 200


@pytest.mark.django_db
def test_not_found(client_authenticated, faker):
    resp = client_authenticated.post(make_url(faker.pyint()))

    assert resp.status_code == 404
    assert resp.json()["message"] == "User not found."


@pytest.mark.django_db
def test_unfollow_db(client_authenticated, user):
    other_user = baker.make(User)
    user.following.add(other_user.id)

    client_authenticated.post(make_url(other_user.id))

    assert user.following.count() == 0
