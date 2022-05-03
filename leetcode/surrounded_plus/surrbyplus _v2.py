"""
Write a function that determines if all alpha characters in a string 
  are surrounded (the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't
  surrounded by a plus sign. Otherwise the function should return true.
"""


def symbols(input_str: str) -> bool:
    onValidation = False

    if len(input_str) < 3:
        for l in input_str:
            if l.isalpha():
                return False
        return True

    for i, l in enumerate(input_str):
        if onValidation:
            if l.isalpha():
                continue
            elif l == "+":
                onValidation = False
                continue

            return False

        if l.isalpha():
            if i == len(input_str) - 1:
                return False
            elif input_str[i - 1] == "+":
                onValidation = True
            else:
                return False

    return True


def main():
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

    print("Success!")


if __name__ == "__main__":
    main()
