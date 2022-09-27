from typing import List
from core.services import UserService

from core.models import User
from core.services import (
    CannotFollowYourself,
    FollowService,
    MaximumLimitPostsForToday,
    PostService,
    UserService,
)
from core.schemas import FollowingUserInSchema
from core.schemas import MessageSchema
from core.schemas import PostInSchema
from core.schemas import PostOutSchema
from core.schemas import QuotePostInSchema
from core.schemas import RepostInSchema
from core.schemas import UnfollowUserInSchema
from core.schemas import UserOutSchema
from ninja import NinjaAPI
from ninja.pagination import PageNumberPagination
from ninja.pagination import paginate

api = NinjaAPI(title="X")


@api.exception_handler(MaximumLimitPostsForToday)
def maximum_limit_posts_for_today(request, exc):
    return api.create_response(
        request,
        {"message": str(exc)},
        status=400,
    )

@api.exception_handler(CannotFollowYourself)
def cannot_follow_yourself(request, exc):
    return api.create_response(
        request,
        {"message": str(exc)},
        status=400,
    )

@api.exception_handler(User.DoesNotExist)
def user_not_found(request, exc):
    return api.create_response(
        request,
        {"message": "User not found."},
        status=404,
    )


@api.get(
    "/users/{user_id}",
    response={200: UserOutSchema, 404: MessageSchema},
    tags=["users"],
    url_name="user",
    summary="Get user information",
)
def user(request, user_id):
    user = User.objects.get(id=user_id)

    return UserOutSchema(
        id=user.id,
        username=user.username,
        joined_at=user.joined_at,
        following=user.following.count(),
        followers=user.followers.count(),
        posts=user.total_posts,
        is_following=UserService().is_following(request.user.id, user_id),
    )



@api.post(
    "/users/{user_id}/follow",
    response={200: None, 400: MessageSchema, 404: MessageSchema},
    tags=["users"],
    url_name="follow",
    summary="Follow a user",
)
def follow(request, user_id: int):
    payload = FollowingUserInSchema(user_id=user_id)
    User.objects.get(id=payload.user_id)
    FollowService().follow_user(request.user.id, payload.dict())


@api.post(
    "/users/{user_id}/unfollow",
    response={200: None, 404: MessageSchema},
    tags=["users"],
    url_name="unfollow",
    summary="Unfollow a user",
)
def unfollow(request, user_id: int):
    payload = UnfollowUserInSchema(user_id=user_id)
    User.objects.get(id=payload.user_id)
    FollowService().unfollow_user(request.user.id, payload.dict())


@api.get(
    "/users/{user_id}/posts",
    response={200: List[PostOutSchema]},
    tags=["users"],
    url_name="user_posts",
    summary="Get user posts",
)
@paginate(PageNumberPagination, page_size=5)
def user_posts(request, user_id: int):
    return UserService().posts_for(user_id)


@api.post(
    "/posts/",
    response={200: PostOutSchema, 400: MessageSchema, 422: None},
    tags=["posts"],
    url_name="posts",
    summary="Create post",
)
def create_post(request, payload: PostInSchema):
    return PostService().create_post(request.user.id, payload.dict())


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
    if query == "following":
        return PostService().following_posts(request.user.id)
    return PostService().all_posts()


@api.post(
    "/posts/{post_id}/repost",
    response={200: PostOutSchema, 400: MessageSchema, 422: None},
    tags=["posts"],
    url_name="repost",
    summary="Create repost",
)
def create_repost(request, post_id: int):
    payload = RepostInSchema(post_id=post_id)
    return PostService().create_repost(request.user.id, payload.dict())


@api.post(
    "/posts/{post_id}/quote",
    response={200: PostOutSchema, 400: MessageSchema, 422: None},
    tags=["posts"],
    url_name="quote",
    summary="Create quote post",
)
def create_quote_post(request, post_id: int, payload: QuotePostInSchema):
    payload.post_id = post_id
    return PostService().create_quote_post(request.user.id, payload.dict())
