"""
Write a function that determines if all alpha characters in 
a string are surrounded (the characters immediately before
and after) by a plus sign.
Function should return false if any alpha character present 
in the string isn't surrounded by a plus sign.
Otherwise the function should return true.
"""
import pdb

def symbols(input_str: str) -> bool:
    surrounded = True
    found_plus = False
    has_alpha = False

    if not input_str:
      return surrounded
       
    #pdb.set_trace()
    it = iter(input_str)
    letter = next(it, '')
    #pdb.set_trace()
    while(letter):
      if letter == '+':
        if check_surround(it):
          return True
        else:
          return False

      if letter.isalpha():
        surrounded = False
        break

      letter = next(it, '')
    
    return surrounded

def check_surround(it):
  #pdb.set_trace()
  letter = next(it, '')
  has_alpha = False
  while(letter):
    if letter.isalpha():
      letter = next(it, '')
      has_alpha = True
      continue
    
    if letter == '+':
      return True

    letter = next(it, '')

  if has_alpha:
    return False

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
    # assert symbols("+ab+a") is False
    # assert symbols("+a+b=") is False

    print("Success!")


if __name__ == "__main__":
    main()

    # for index, letter in list(enumerate(input_str)):
    #   if  letter == "+":
    #     if letter.isalpha():
    #         if input_str[index-1] == "+" and input_str[index+1] == "+":
    #           surrounded = True
    #         else:
    #           return False