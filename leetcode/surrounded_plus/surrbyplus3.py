"""
Write a function that determines if all alpha input_str[idx]acters in a string are surrounded 
(the input_str[idx]acters immediately before and after) by a plus sign.
Function should return false if any alpha input_str[idx]acter present in the string isn't 
surrounded by a plus sign. Otherwise the function should return true.
"""


def symbols(input_str: str) -> bool:
    """Working version 3 submitted by student."""
    idx = 0

    while idx < len(input_str):
        if input_str[idx].isalpha():
            if len(input_str) < 3:
                return False

            # Check the set of alphas start with plus
            if not input_str[idx - 1] == "+":
                return False

            idx += 1

            if idx >= len(input_str):
                return False

            # Verify with a set of alphas are surround by plus
            while idx < len(input_str):
                # Check the set of alphas end with plus
                if input_str[idx] == "+":
                    break

                if input_str[idx].isalpha():
                    idx += 1
                    continue

                return False

        idx += 1

    return True


def test_main():
    assert symbols("") is True
    assert symbols("0") is True
    assert symbols("123") is True
    assert symbols("01%2-@") is True
    assert symbols("+1+") is True
    assert symbols("+a+") is True
    assert symbols("+ab+") is True
    assert symbols("+ab++") is True
    assert symbols("+Z+Y+") is True
    assert symbols("+ab+a+") is True
    assert symbols("+a+b+7") is True
    assert symbols("+a+=5=+d+") is True
    assert symbols("12+ab+a+12") is True
    assert symbols("a") is False
    assert symbols("a+") is False
    assert symbols("+a") is False
    assert symbols("-a+") is False
    assert symbols("+a-") is False
    assert symbols("-a-") is False
    assert symbols("+ab1+") is False
    assert symbols("+a1b+") is False
    assert symbols("+1ab+") is False
    assert symbols("+ab+a") is False
    assert symbols("+a+b=") is False


if __name__ == "__main__":
    import pytest
    pytest.main(["-s", __file__])
