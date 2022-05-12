import pytest
from core.models import POST_CONTENT_LIMIT
from core.schemas import QuotePostInSchema
from pydantic import ValidationError


def test_comment_max_length():
    with pytest.raises(ValidationError):
        QuotePostInSchema(comment="A" * (POST_CONTENT_LIMIT + 1))
