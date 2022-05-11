import pytest
from core.schemas import QuotePostInSchema
from pydantic import ValidationError

POST_LIMIT = 777  # Importa lá do model do post

POST_OVER_LIMIT = POST_LIMIT + 1

def test_comment_max_length():
    with pytest.raises(ValidationError):
        QuotePostInSchema(comment="A" * POST_OVER_LIMIT)
