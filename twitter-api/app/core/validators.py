from core import models
from django.core.validators import RegexValidator
from django.utils import timezone


class MaximumLimitPostsForToday(Exception):
    def __str__(self):
        return "You have reached the maximum number for creating posts today."


alphanumeric = RegexValidator(
    r"^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
)


def can_post(user_id: int):
    now = timezone.now()

    count = models.Post.objects.filter(
        user_id=user_id,
        created_at__day=now.day,
        created_at__month=now.month,
        created_at__year=now.year,
    ).count()

    if count >= 5:
        raise MaximumLimitPostsForToday("...")

    return True
