import pytest
from core.models import Post
from core.models import User
from django.urls import reverse
from model_bakery import baker

URL = reverse("api-1.0.0:posts")


@pytest.mark.django_db
def test_get(client_authenticated):
    resp = client_authenticated.get(URL)

    assert resp.status_code == 200


@pytest.mark.django_db
def test_all(client_authenticated):
    baker.make(Post, _quantity=50)

    resp = client_authenticated.get(URL)

    assert resp.status_code == 200
    assert len(resp.json()["items"]) == 10
    assert resp.json()["count"] == 50


@pytest.mark.django_db
def test_following(client_authenticated, user):
    other_user = baker.make(User)
    user.following.add(other_user)
    baker.make(Post, _quantity=10, user=other_user)
    baker.make(Post, _quantity=10)

    resp = client_authenticated.get(f"{URL}?query=following")

    assert resp.status_code == 200
    assert len(resp.json()["items"]) == 10
    assert resp.json()["count"] == 10
