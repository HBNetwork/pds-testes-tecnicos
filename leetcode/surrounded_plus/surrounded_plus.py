"""
Write a function that determines if all alpha characters in a string are surrounded 
(the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't 
surrounded by a plus sign. Otherwise the function should return true.
"""


def symbols(input_str: str) -> bool:

    # for idx, letter in enumerate(input_str):

    #     if letter.isalpha():
    #         if len(input_str) < 3 or idx - 1 < 0 or not input_str[idx - 1] == "+":
    #             return False

    #         for idx2, l in enumerate(input_str[idx + 1 :]):
    #             if l == "+":
    #                 if idx2 == len(input_str[idx + 1 :]) - 1:
    #                     return True
    #                 idx += idx2 + 1
    #                 break
                
    #             if l.isalpha():
    #                 if idx2 == len(input_str[idx + 1 :]) - 1:
    #                     return False
    #                 continue

    idx = 0

    while idx < len(input_str):
        if input_str[idx].isalpha() :
            if len(input_str) < 3:
                return False
            
            if not input_str[idx - 1] == "+":
                return False

            idx += 1

            if idx >= len(input_str):
                return False

            while idx < len(input_str):
                if input_str[idx] == "+":
                    break

                if input_str[idx].isalpha():
                    idx += 1
                    continue

                return False

        idx += 1

    return True

def main():
    
    assert symbols("") is True
    assert symbols("0") is True
    assert symbols("123") is True
    assert symbols("01%2-@") is True
    assert symbols("+a+") is True
    assert symbols("+1+") is True
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
    main()
    print("Success!")
