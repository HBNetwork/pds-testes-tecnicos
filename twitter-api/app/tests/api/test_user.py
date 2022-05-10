import pytest
from core.models import User
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from model_bakery import baker


def make_url(user_id):
    return reverse("api-1.0.0:user", kwargs={"user_id": user_id})


@pytest.mark.django_db
def test_get(client, user):
    resp = client.get(make_url(user.id))

    assert resp.status_code == 200


@pytest.mark.django_db
def test_data(client, user):
    resp = client.get(make_url(user.id))

    data = resp.json()
    assert data["id"] == user.id
    assert data["username"] == user.username
    assert data["following"] == user.following.count()
    assert data["followers"] == user.followers.count()
    assert data["posts"] == 0
    assert parse_datetime(data["joined_at"]).replace(
        microsecond=0
    ) == user.joined_at.replace(microsecond=0)
    assert data["is_following"] is False


@pytest.mark.django_db
def test_not_found(client, faker):
    resp = client.get(make_url(faker.pyint()))

    assert resp.status_code == 404
    assert resp.json()["message"] == "User not found."


@pytest.mark.django_db
def test_is_following(client_authenticated, user):
    other_user = baker.make(User)
    user.following.add(other_user)

    resp = client_authenticated.get(make_url(other_user.id))

    assert resp.json()["is_following"] is True
