import pytest
from core.models import User
from core.services import FollowService, CannotFollowYourself
from model_bakery import baker


@pytest.mark.django_db
def test_can_follow(user):
    other_user = baker.make(User)

    can = FollowService().can_follow(user.id, other_user.id)

    assert can is True


@pytest.mark.django_db
def test_cannot_follow_yourself(user):
    with pytest.raises(CannotFollowYourself):
        FollowService().can_follow(user.id, user.id)
