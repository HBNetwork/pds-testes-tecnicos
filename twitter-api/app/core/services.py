from core import validators
from core.models import Post
from core.models import User


class CannotFollowYourself(Exception):
    def __str__(self):
        return "You can not follow yourself."


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

    def create_quote_post(self, user_id: int, data):
        validators.can_post(user_id)
        post = Post.objects.get(id=data.get("post_id"))
        quote_post = Post.objects.create(
            user_id=user_id,
            type=Post.Type.QUOTE,
            content=post.content,
            comment=data.get("comment"),
        )
        return quote_post


class FollowService:
    def can_follow(self, user_id: int, following_id: int):
        if user_id == following_id:
            raise CannotFollowYourself()
        return True

    def follow_user(self, user_id: int, data):
        self.can_follow(user_id, data.get("user_id"))
        user = User.objects.get(id=user_id)
        user.following.add(data.get("user_id"))

    def unfollow_user(self, user_id: int, data):
        user = User.objects.get(id=user_id)
        user.following.remove(data.get("user_id"))
