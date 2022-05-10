import pytest
from core import selects
from core.models import User
from model_bakery import baker


@pytest.mark.django_db
def test_is_following(user):
    following_user = baker.make(User)
    user.following.add(following_user)

    assert selects.is_following(user.id, following_user.id) is True


@pytest.mark.django_db
def test_is_not_following(user):
    following_user = baker.make(User)

    assert selects.is_following(user.id, following_user.id) is False
