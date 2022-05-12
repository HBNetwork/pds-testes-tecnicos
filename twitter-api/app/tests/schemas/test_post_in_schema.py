import pytest
from core.models import POST_CONTENT_LIMIT
from core.schemas import PostInSchema
from pydantic import ValidationError


def test_content_max_length():
    with pytest.raises(ValidationError):
        PostInSchema(content="A" * (POST_CONTENT_LIMIT + 1))
