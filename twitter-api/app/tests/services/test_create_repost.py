import pytest
from core.models import Post
from core.models import User
from core.schemas import RepostInSchema
from core.services import create_repost
from model_bakery import baker


@pytest.mark.django_db
def test_create(user):
    post = baker.make(Post, user=user)
    payload = RepostInSchema(post_id=post.id)

    create_repost(user.id, payload)

    assert Post.objects.count() == 2


@pytest.mark.django_db
def test_save_correctly(user):
    other_user = baker.make(User)
    post = baker.make(Post, user=other_user)
    payload = RepostInSchema(post_id=post.id)

    create_repost(user.id, payload)

    repost = Post.objects.last()
    assert repost.id != post.id
    assert repost.content == post.content
    assert repost.user_id != post.user_id


@pytest.mark.django_db
def test_return(user):
    post = baker.make(Post)
    payload = RepostInSchema(post_id=post.id)

    repost = create_repost(user.id, payload)

    assert isinstance(repost, Post)
