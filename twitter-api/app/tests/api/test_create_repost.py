import pytest
from core.models import Post
from core.services import MaximumLimitPostsForToday
from django.urls import reverse
from model_bakery import baker


def make_url(post_id):
    return reverse("api-1.0.0:repost", kwargs={"post_id": post_id})


@pytest.mark.django_db
def test_repost(client_authenticated):
    post = baker.make(Post)

    resp = client_authenticated.post(make_url(post.id))

    assert resp.status_code == 200
    assert Post.objects.count() == 2


@pytest.mark.django_db
def test_bad_request(client_authenticated, user):
    posts = baker.make(Post, user=user, _quantity=5)

    resp = client_authenticated.post(make_url(posts[0].id))

    assert resp.status_code == 400
    assert resp.json()["message"] == str(MaximumLimitPostsForToday())
