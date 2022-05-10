import pytest
from core.schemas import QuotePostInSchema
from pydantic import ValidationError


def test_comment_max_length():
    with pytest.raises(ValidationError):
        QuotePostInSchema(comment="1" * 778)
