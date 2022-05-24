from django.db import models
from django.core.validators import RegexValidator

POST_CONTENT_LIMIT = 777

alphanumeric = RegexValidator(
    r"^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
)


class User(models.Model):
    username = models.CharField(
        max_length=14,
        validators=[alphanumeric],
        unique=True,
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    # Fields required by django
    is_anonymous = False
    is_authenticated = True

    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
    )

    @property
    def total_posts(self):
        return self.post_set.count()


class Post(models.Model):
    class Type(models.TextChoices):
        DEFAULT = "DE", "Default"
        REPOST = "RE", "Repost"
        QUOTE = "QU", "Quote"

    content = models.CharField(max_length=POST_CONTENT_LIMIT)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.DEFAULT,
    )
