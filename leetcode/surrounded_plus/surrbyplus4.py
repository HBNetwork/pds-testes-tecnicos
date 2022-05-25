"""
Write a function that determines if all alpha characters in a string 
  are surrounded (the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't
  surrounded by a plus sign. Otherwise the function should return true.
"""

ZERO, ONE, TWO = 0, 1, 2


def symbols(s: str) -> bool:
    """Version 4 introducing the concept of states with explicit exits."""
    state = ZERO

    for char in s:
        if state == ZERO:
            if char == "+":
                state = ONE
            elif not char.isalpha():
                continue
            else:
                return False
        elif state == ONE:
            if char == "+":
                continue
            elif char.isalpha():
                state = TWO
            else:
                state = ZERO
        elif state == TWO:
            if char == "+":
                state = ONE
            elif char.isalpha():
                continue
            else:
                return False

    if state == TWO:
        return False

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
