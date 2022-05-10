import pytest
from core.schemas import PostInSchema
from pydantic import ValidationError


def test_content_max_length():
    with pytest.raises(ValidationError):
        PostInSchema(content="1" * 778)
