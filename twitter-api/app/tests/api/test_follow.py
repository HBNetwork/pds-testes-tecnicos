import pytest
from core.models import User
from django.urls import reverse
from model_bakery import baker


def make_url(user_id):
    return reverse("api-1.0.0:follow", kwargs={"user_id": user_id})


@pytest.mark.django_db
def test_follow(client_authenticated):
    other_user = baker.make(User)

    resp = client_authenticated.post(make_url(other_user.id))

    assert resp.status_code == 200


@pytest.mark.django_db
def test_cannot_follow_yourself(client_authenticated, user):
    resp = client_authenticated.post(make_url(user.id))

    assert resp.status_code == 400
    assert resp.json()["message"] == "You can not follow yourself."


@pytest.mark.django_db
def test_not_found(client_authenticated, faker):
    resp = client_authenticated.post(make_url(faker.pyint()))

    assert resp.status_code == 404
    assert resp.json()["message"] == "User not found."


@pytest.mark.django_db
def test_follow_db(client_authenticated, user):
    other_user = baker.make(User)
    assert user.following.count() == 0

    client_authenticated.post(make_url(other_user.id))

    assert user.following.count() == 1
