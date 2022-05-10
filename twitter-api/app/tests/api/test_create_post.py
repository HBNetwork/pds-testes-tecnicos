import pytest
from core.models import Post
from core.validators import MaximumLimitPostsForToday
from django.urls import reverse
from model_bakery import baker

URL = reverse("api-1.0.0:posts")


@pytest.mark.django_db
def test_create(client_authenticated, faker):
    resp = client_authenticated.post(
        URL,
        data={
            "content": faker.text(),
        },
        content_type="application/json",
    )

    assert resp.status_code == 200
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_data(client_authenticated, faker, user):
    content = faker.text()
    resp = client_authenticated.post(
        URL,
        data={"content": content},
        content_type="application/json",
    )

    post = Post.objects.first()
    data = resp.json()
    assert data["id"] == post.id
    assert data["content"] == content
    assert data["comment"] == ""
    assert data["user_id"] == user.id
    assert data["type"] == "DE"


@pytest.mark.django_db
def test_wrong_data(client_authenticated):
    resp = client_authenticated.post(
        URL,
        content_type="application/json",
    )

    assert resp.status_code == 422


@pytest.mark.django_db
def test_cannot_post(client_authenticated, faker, user):
    baker.make(Post, user=user, _quantity=5)
    resp = client_authenticated.post(
        URL,
        data={"content": faker.text()},
        content_type="application/json",
    )

    assert resp.status_code == 400
    assert resp.json()["message"] == str(MaximumLimitPostsForToday())
