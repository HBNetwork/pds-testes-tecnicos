from datetime import timedelta

import pytest
from core.models import Post
from core.validators import can_post
from core.validators import MaximumLimitPostsForToday
from django.utils import timezone
from model_bakery import baker


@pytest.mark.django_db
def test_can_post(user):
    assert can_post(user.id) is True


@pytest.mark.django_db
def test_cannot_post(user):
    baker.make(Post, user=user, _quantity=5)

    with pytest.raises(MaximumLimitPostsForToday):
        can_post(user.id)


@pytest.mark.django_db
def test_just_today(user):
    yesterday = timezone.now() - timedelta(days=1)
    baker.make(Post, user=user, _quantity=4)
    post = baker.make(Post, user=user, created_at=yesterday)
    post.created_at = yesterday
    post.save()

    can = can_post(user.id)

    assert can is True
