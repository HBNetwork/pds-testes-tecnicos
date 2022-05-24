import pytest
from core.models import User
from core.schemas import FollowingUserInSchema
from core.services import FollowService
from model_bakery import baker


@pytest.mark.django_db
def test_follow(user):
    following_user = baker.make(User)
    payload = FollowingUserInSchema(user_id=following_user.id)

    FollowService().follow_user(user.id, payload.dict())

    assert user.following.count() == 1
    assert user.following.first() == following_user
