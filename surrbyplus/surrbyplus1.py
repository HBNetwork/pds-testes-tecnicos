"""
Write a function that determines if all alpha characters in a string 
  are surrounded (the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't
  surrounded by a plus sign. Otherwise the function should return true.
"""
def symbols(input_str: str) -> bool:
  onValidation = False

  if len(input_str) < 3:
    return not any(l.isalpha() for l in input_str)
  for i, l in enumerate(input_str):
    if onValidation:
      if l.isalpha():
        continue
      elif l == '+':
        onValidation = False
        continue
      return False

    if l.isalpha():
      if i == len(input_str) - 1 or input_str[i - 1] != '+':
        return False
      else:
        onValidation = True
  return True

 
def main():
   assert symbols("12+ab+a+12") is True
   assert symbols("") is True
   assert symbols("0") is True
   assert symbols("+a+") is True
   assert symbols("+1+") is True
   assert symbols("123") is True
   assert symbols("+ab+") is True
   assert symbols("+ab++") is True
   assert symbols("+Z+Y+") is True
   assert symbols("+a+b+7") is True
   assert symbols("+a+=5=+d+") is True
   assert symbols("a") is False
   assert symbols("a+") is False
   assert symbols("+a") is False
   assert symbols("+a-") is False
   assert symbols("-a+") is False
   assert symbols("-a-") is False
   assert symbols("+ab+a") is False
   assert symbols("+a+b=") is False
   assert symbols("+ab1+") is False
 
   print("Success!")
 
 
if __name__ == "__main__":
   main()
