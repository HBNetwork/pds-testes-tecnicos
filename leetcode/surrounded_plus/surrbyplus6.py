"""
Write a function that determines if all alpha characters in a string 
  are surrounded (the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't
  surrounded by a plus sign. Otherwise the function should return true.
"""

NORMAL, PLUS, ALPHA, ERROR = 0, 1, 2, 3


def symbols(s: str) -> bool:
    """Version 5 removing redundant exits to enforce the transition to error
    state."""
    state = NORMAL

    for char in s:
        if state == NORMAL:
            if char == "+":
                state = PLUS
            elif char.isalpha():
                state = ERROR
        elif state == PLUS:
            if char.isalpha():
                state = ALPHA
            elif char != "+":
                state = NORMAL
        elif state == ALPHA:
            if char == "+":
                state = PLUS
            elif not char.isalpha():
                state = ERROR
        elif state == "ERROR":
            break

    return state not in (ALPHA, ERROR)


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
