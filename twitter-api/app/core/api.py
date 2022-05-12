from typing import List

from core import selects
from core.models import User
from core.services import (
    CannotFollowYourself,
    FollowService,
    MaximumLimitPostsForToday,
    PostService,
)
from core.schemas import FollowingUserInSchema
from core.schemas import MessageSchema
from core.schemas import PostInSchema
from core.schemas import PostOutSchema
from core.schemas import QuotePostInSchema
from core.schemas import RepostInSchema
from core.schemas import UnfollowUserInSchema
from core.schemas import UserOutSchema
from django.http import Http404
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.pagination import PageNumberPagination
from ninja.pagination import paginate

api = NinjaAPI(title="Posterr")


@api.get(
    "/users/{user_id}",
    response={200: UserOutSchema, 404: MessageSchema},
    tags=["users"],
    url_name="user",
    summary="Get user information",
)
def user(request, user_id):
    try:
        data = selects.user_data(user_id)
        data.is_following = selects.is_following(request.user.id, user_id)
        return data
    except User.DoesNotExist:
        return 404, {"message": "User not found."}


@api.post(
    "/users/{user_id}/follow",
    response={200: None, 400: MessageSchema, 404: MessageSchema},
    tags=["users"],
    url_name="follow",
    summary="Follow a user",
)
def follow(request, user_id: int):
    try:
        payload = FollowingUserInSchema(user_id=user_id)
        get_object_or_404(User, id=payload.user_id)
        FollowService().follow_user(request.user.id, payload.dict())
    except CannotFollowYourself as e:
        return 400, {"message": str(e)}
    except Http404:
        return 404, {"message": "User not found."}


@api.post(
    "/users/{user_id}/unfollow",
    response={200: None, 404: MessageSchema},
    tags=["users"],
    url_name="unfollow",
    summary="Unfollow a user",
)
def unfollow(request, user_id: int):
    try:
        payload = UnfollowUserInSchema(user_id=user_id)
        get_object_or_404(User, id=user_id)
        FollowService().unfollow_user(request.user.id, payload.dict())
    except Http404:
        return 404, {"message": "User not found."}


@api.get(
    "/users/{user_id}/posts",
    response={200: List[PostOutSchema]},
    tags=["users"],
    url_name="user_posts",
    summary="Get user posts",
)
@paginate(PageNumberPagination, page_size=5)
def user_posts(request, user_id: int):
    return selects.user_posts(user_id)


@api.post(
    "/posts/",
    response={200: PostOutSchema, 400: MessageSchema, 422: None},
    tags=["posts"],
    url_name="posts",
    summary="Create post",
)
def create_post(request, payload: PostInSchema):
    try:
        return PostService().create_post(request.user.id, payload.dict())
    except MaximumLimitPostsForToday as e:
        return 400, {"message": str(e)}


@api.get(
    "/posts/",
    response={200: List[PostOutSchema]},
    tags=["posts"],
    url_name="posts",
    summary="Get posts",
)
@paginate(PageNumberPagination, page_size=10)
def posts(request, query: str = "all"):
    """
    Valid queries are:
    - **all** - Get all posts.
    - **following** - Get posts for people you are following.
    """
    return selects.posts(request.user.id, query)


@api.post(
    "/posts/{post_id}/repost",
    response={200: PostOutSchema, 400: MessageSchema, 422: None},
    tags=["posts"],
    url_name="repost",
    summary="Create repost",
)
def create_repost(request, post_id: int):
    try:
        payload = RepostInSchema(post_id=post_id)
        return PostService().create_repost(request.user.id, payload.dict())
    except MaximumLimitPostsForToday as e:
        return 400, {"message": str(e)}


@api.post(
    "/posts/{post_id}/quote",
    response={200: PostOutSchema, 400: MessageSchema, 422: None},
    tags=["posts"],
    url_name="quote",
    summary="Create quote post",
)
def create_quote_post(request, post_id: int, payload: QuotePostInSchema):
    try:
        payload.post_id = post_id
        return PostService().create_quote_post(request.user.id, payload.dict())
    except MaximumLimitPostsForToday as e:
        return 400, {"message": str(e)}
