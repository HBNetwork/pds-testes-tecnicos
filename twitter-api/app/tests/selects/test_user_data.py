import pytest
from core.models import Post
from core.models import User
from core.selects import user_data
from model_bakery import baker


@pytest.mark.django_db
def test_data(user):
    payload = user_data(user.id)

    assert payload.id == user.id
    assert payload.username == user.username
    assert payload.following == user.following.count()
    assert payload.followers == user.following.count()
    assert payload.joined_at == user.joined_at
    assert payload.posts == 0


@pytest.mark.django_db
def test_posts_count(user):
    other_user = baker.make(User)
    baker.make(Post, user=other_user, _quantity=3)
    baker.make(Post, user=user, _quantity=5)

    payload = user_data(user.id)

    assert payload.posts == 5
