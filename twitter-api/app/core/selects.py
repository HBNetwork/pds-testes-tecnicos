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
