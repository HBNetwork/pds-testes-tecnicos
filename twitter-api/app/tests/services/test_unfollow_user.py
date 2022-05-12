import pytest
from core.models import User
from core.schemas import UnfollowUserInSchema
from core.services import CoreService
from model_bakery import baker


@pytest.mark.django_db
def test_unfollow(user):
    unfollowing_user = baker.make(User)
    user.following.add(unfollowing_user)
    payload = UnfollowUserInSchema(user_id=unfollowing_user.id)

    CoreService().unfollow_user(user.id, payload.dict())

    assert user.following.count() == 0
