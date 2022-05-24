import pytest
from core.models import Post
from core.schemas import PostInSchema
from core.services import PostService


@pytest.mark.django_db
def test_create(user, faker):
    payload = PostInSchema(content=faker.text())

    PostService().create_post(user.id, payload.dict())

    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_save_correctly(user, faker):
    payload = PostInSchema(content=faker.text())

    PostService().create_post(user.id, payload.dict())

    post = Post.objects.first()
    assert post.user.id == user.id
    assert post.content == payload.content


@pytest.mark.django_db
def test_return(user, faker):
    payload = PostInSchema(content=faker.text())

    post = PostService().create_post(user.id, payload.dict())

    assert isinstance(post, Post)
