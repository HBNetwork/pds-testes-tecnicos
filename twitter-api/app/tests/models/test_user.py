import pytest
from core.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError


@pytest.mark.django_db
def test_create():
    User.objects.create(username="username")

    user = User.objects.first()
    assert User.objects.count() == 1
    assert user.username == "username"
    assert user.joined_at is not None


@pytest.mark.django_db
def test_username_max_length():
    user = User(username="ahugeusernamehere")

    with pytest.raises(ValidationError):
        user.full_clean()
        assert User.objects.count() == 0


@pytest.mark.django_db
def test_only_alphanumerics():
    user = User(username="------")

    with pytest.raises(ValidationError):
        user.full_clean()
        assert User.objects.count() == 0


@pytest.mark.django_db
def test_username_is_unique():
    User.objects.create(username="username")

    with pytest.raises(IntegrityError):
        User.objects.create(username="username")
