from core.models import Post
from core.models import User
from core.schemas import UserOutSchema


def user_data(user_id: int) -> UserOutSchema:
    user = User.objects.get(id=user_id)

    return UserOutSchema(
        id=user.id,
        username=user.username,
        joined_at=user.joined_at,
        following=user.following.count(),
        followers=user.followers.count(),
        posts=Post.objects.filter(user_id=user.id).count(),
    )


def posts(user_id: int, query: str = "all"):
    queryset = Post.objects.all()

    if query == "following":
        user = User.objects.get(id=user_id)
        queryset = queryset.filter(
            user_id__in=user.following.all().values("id")
        )

    queryset = queryset.order_by("-created_at")

    return queryset


def user_posts(user_id: int):
    return Post.objects.filter(user_id=user_id).order_by("-created_at")
