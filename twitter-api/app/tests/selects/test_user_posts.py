from datetime import timedelta

import pytest
from core import selects
from core.models import Post
from core.models import User
from django.utils import timezone
from model_bakery import baker


@pytest.mark.django_db
def test_posts(user):
    baker.make(Post, user=user, _quantity=10)

    posts = selects.user_posts(user.id)

    assert len(posts) == 10


@pytest.mark.django_db
def test_filter_user(user):
    other_user = baker.make(User)
    baker.make(Post, user=other_user, _quantity=10)

    posts = selects.user_posts(user.id)

    assert len(posts) == 0


@pytest.mark.django_db
def test_order_by(user):
    now = timezone.now()
    three_hours_ago = now - timedelta(hours=3)
    two_hours_ago = now - timedelta(hours=2)
    post3 = baker.make(Post, user=user, created_at=two_hours_ago)
    post2 = baker.make(Post, user=user, created_at=three_hours_ago)
    post1 = baker.make(Post, user=user, created_at=now)

    posts = selects.user_posts(user.id)

    assert posts[0] == post1
    assert posts[1] == post2
    assert posts[2] == post3
