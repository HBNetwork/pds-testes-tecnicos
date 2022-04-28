"""
Write a function that determines if all alpha characters in a string 
  are surrounded (the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't
  surrounded by a plus sign. Otherwise the function should return true.
"""
def symbols(input_str: str) -> bool:
  plus = False
  foundalpha = False
  validInput = True
  for i, l in enumerate(input_str):
    if l == '+':
      if plus and foundalpha:
         foundalpha = False
         validInput = True
      plus = True
    elif l.isalpha():
      validInput = False
      foundalpha = True
    elif l != '+' and foundalpha:
      return False
   
  return validInput

 
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
