from core import validators
from core.models import Post
from core.models import User
from core.schemas import FollowingUserInSchema
from core.schemas import QuotePostInSchema
from core.schemas import UnfollowUserInSchema


class CoreService:
    def create_post(self, user_id: int, data):
        validators.can_post(user_id)
        post = Post.objects.create(**data, user_id=user_id)
        return post

    def create_repost(self, user_id: int, data):
        validators.can_post(user_id)
        post = Post.objects.get(id=data.get("post_id"))
        repost = Post.objects.create(
            user_id=user_id,
            type=Post.Type.REPOST,
            content=post.content,
        )
        return repost


def create_quote_post(user_id: int, payload: QuotePostInSchema):
    post = Post.objects.get(id=payload.post_id)
    quote_post = Post.objects.create(
        user_id=user_id,
        type=Post.Type.QUOTE,
        content=post.content,
        comment=payload.comment,
    )
    return quote_post


def follow_user(user_id: int, payload: FollowingUserInSchema):
    user = User.objects.get(id=user_id)
    user.following.add(payload.user_id)


def unfollow_user(user_id: int, payload: UnfollowUserInSchema):
    user = User.objects.get(id=user_id)
    user.following.remove(payload.user_id)
