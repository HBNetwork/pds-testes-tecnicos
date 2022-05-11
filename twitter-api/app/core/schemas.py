from datetime import datetime
from typing import Optional

from ninja import Schema
from pydantic import BaseModel
from pydantic import constr


class PostInSchema(Schema):
    content: constr(max_length=777)  # Importa de um único lugar


class PostOutSchema(Schema):
    id: int
    content: str
    created_at: datetime
    comment: str
    user_id: int
    type: str


class RepostInSchema(Schema):
    post_id: int


class QuotePostInSchema(Schema):
    post_id: Optional[int] = None
    comment: constr(max_length=777)


class UserOutSchema(Schema):
    id: int
    username: str
    joined_at: datetime
    following: int
    followers: int
    posts: int
    is_following: Optional[bool] = None


class FollowingUserInSchema(Schema):
    user_id: int


class UnfollowUserInSchema(Schema):
    user_id: int


class MessageSchema(BaseModel):
    message: str
