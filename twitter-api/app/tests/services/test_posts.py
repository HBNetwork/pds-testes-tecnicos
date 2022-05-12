from datetime import timedelta

import pytest
from core.models import Post
from core.models import User
from core.services import PostService
from django.utils import timezone
from model_bakery import baker


@pytest.mark.django_db
def test_all(user):
    baker.make(Post, _quantity=10)

    posts = PostService().all_posts()

    assert len(posts) == 10


@pytest.mark.django_db
def test_dont_select_without_following(user):
    other_user = baker.make(User)
    baker.make(Post, _quantity=10, user=other_user)

    posts = PostService().following_posts(user.id)

    assert len(posts) == 0


@pytest.mark.django_db
def test_select_following(user):
    other_user = baker.make(User)
    baker.make(Post, _quantity=10, user=other_user)
    user.following.add(other_user.id)

    posts = PostService().following_posts(user.id)

    assert len(posts) == 10


@pytest.mark.django_db
def test_order_by(user):
    now = timezone.now()
    three_hours_ago = now - timedelta(hours=3)
    two_hours_ago = now - timedelta(hours=2)
    post3 = baker.make(Post, created_at=two_hours_ago)
    post2 = baker.make(Post, created_at=three_hours_ago)
    post1 = baker.make(Post, created_at=now)

    posts = PostService().all_posts()

    assert posts[0] == post1
    assert posts[1] == post2
    assert posts[2] == post3
