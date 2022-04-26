import pytest
from contains_duplicate import has_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(nums, expected):
    assert expected == has_duplicate(nums)
