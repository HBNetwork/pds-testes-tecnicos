import pytest
from core.models import Post
from core.models import User
from django.urls import reverse
from model_bakery import baker


def make_url(user_id):
    return reverse("api-1.0.0:user_posts", kwargs={"user_id": user_id})


@pytest.mark.django_db
def test_get(client_authenticated, user):
    resp = client_authenticated.get(make_url(user.id))

    assert resp.status_code == 200


@pytest.mark.django_db
def test_pagination(client_authenticated, user):
    baker.make(Post, user=user, _quantity=10)

    resp = client_authenticated.get(make_url(user.id))

    assert len(resp.json()["items"]) == 5
    assert resp.json()["count"] == 10


@pytest.mark.django_db
def test_filter_user(client_authenticated, user):
    other_user = baker.make(User)
    baker.make(Post, user=other_user, _quantity=10)

    resp = client_authenticated.get(make_url(user.id))

    assert len(resp.json()["items"]) == 0
    assert resp.json()["count"] == 0
