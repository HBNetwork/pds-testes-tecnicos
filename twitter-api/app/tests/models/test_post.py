import pytest
from core.models import Post
from core.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError


@pytest.mark.django_db
def test_create():
    user = User.objects.create(username="username")
    Post.objects.create(content="my post", user=user)

    post = Post.objects.first()
    assert Post.objects.count() == 1
    assert post.created_at is not None
    assert post.type == Post.Type.DEFAULT


@pytest.mark.django_db
def test_content_max_length():
    user = User.objects.create(username="username")
    post = Post(content="1" * 778, user=user)

    with pytest.raises(ValidationError):
        post.full_clean()


@pytest.mark.django_db
def test_create_only_with_user():
    with pytest.raises(IntegrityError):
        Post.objects.create(content="my post")
