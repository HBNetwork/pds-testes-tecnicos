import pytest
from core.models import Post
from core.services import MaximumLimitPostsForToday
from django.urls import reverse
from model_bakery import baker


def make_url(post_id):
    return reverse("api-1.0.0:quote", kwargs={"post_id": post_id})


@pytest.mark.django_db
def test_quote(client_authenticated, faker):
    post = baker.make(Post)

    resp = client_authenticated.post(
        make_url(post.id),
        data={"comment": faker.text()},
        content_type="application/json",
    )

    assert resp.status_code == 200
    assert Post.objects.count() == 2


@pytest.mark.django_db
def test_data(client_authenticated, faker):
    post = baker.make(Post)
    comment = faker.text()

    resp = client_authenticated.post(
        make_url(post.id),
        data={"comment": comment},
        content_type="application/json",
    )

    data = resp.json()
    assert data["comment"] == comment
    assert data["type"] == "QU"


@pytest.mark.django_db
def test_bad_request(client_authenticated, user, faker):
    posts = baker.make(Post, user=user, _quantity=5)

    resp = client_authenticated.post(
        make_url(posts[0].id),
        data={"comment": faker.text()},
        content_type="application/json",
    )

    assert resp.status_code == 400
    assert resp.json()["message"] == str(MaximumLimitPostsForToday())


@pytest.mark.django_db
def test_wrong_data(client_authenticated):
    post = baker.make(Post)

    resp = client_authenticated.post(
        make_url(post.id),
        content_type="application/json",
    )

    assert resp.status_code == 422
