"""
Write a function that determines if all alpha characters in a string are surrounded (the characters immediately before and after) by a plus sign.
Function should return false if any alpha character present in the string isn't surrounded by a plus sign. Otherwise the function should return true.
"""
from ast import Return
import pdb
import re
import unittest


# def symbols(input_str: str) -> bool:
#     surrounded = True
#     found_plus = False
#     has_alpha = False

#     if not input_str:
#         return surrounded

#     # pdb.set_trace()
#     it = iter(input_str)
#     letter = next(it, "")
#     # pdb.set_trace()
#     while letter:
#         if letter == "+":
#             if check_around(it):
#                 return True
#             else:
#                 return False

#         if letter.isalpha():
#             surrounded = False
#             break

#         letter = next(it, "")

#     return surrounded

class NotAround(Exception):
	pass


def symbols_regex(input_str: str):
    return re.findall("\+\w+\+", input_str)


def check_around(idx, input):
	while idx < len(input):
		if not input[idx].isalpha():
			break
		idx += 1

	if idx >= len(input):
		raise NotAround()

	if input[idx] == "+":
		return idx
	
	raise NotAround()


def symbols(input_str: str) -> bool:
	idx = 0
	size = len(input_str)

	while idx < size:
		if not input_str[idx].isalpha():
			idx += 1
			continue
		
		try:
			if not (idx-1 and input_str[idx-1] == "+"):
				return False

		except NotAround:
			return False
	
	return True


class CheckAround(unittest.TestCase):
    def test_surround(self):
        self.assertIsInstance(check_around(1, "+a+"), int)
        self.assertIsInstance(check_around(1, "+ab+"), int)
        self.assertIsInstance(check_around(1, "+acb+"), int)
        self.assertIsInstance(check_around(1, "+acb+a+"), int)

    def test_not_around(self):
        self.assertRaises(NotAround, check_around, 1, "+a")
        self.assertRaises(NotAround, check_around, 1, "+a1a+")


class Symbols(unittest.TestCase):
	def test_not_around(self):
		self.assertFalse(symbols("a"))
		self.assertFalse(symbols("1a"))
		self.assertFalse(symbols("-a+"))
# def main():
    # assert symbols("12+ab+a+12") is True
    # assert symbols("") is True
    # assert symbols("0") is True
    # assert symbols("+a+") is True
    # assert symbols("+1+") is True
    # assert symbols("123") is True
    # assert symbols("+ab+") is True
    # assert symbols("+ab++") is True
    # assert symbols("+Z+Y+") is True
    # assert symbols("+a+b+7") is True
    # assert symbols("+a+=5=+d+") is True

    # assert symbols("a") is False
    # assert symbols("a+") is False
    # assert symbols("+a") is False
    # assert symbols("+a-") is False
    # assert symbols("-a+") is False
    # assert symbols("-a-") is False
    # assert symbols("+ab+a") is False
    # assert symbols("+a+b=") is False


if __name__ == "__main__":
	unittest.main(exit=False)
	print("Success!")

    # for index, letter in list(enumerate(input_str)):
    #   if  letter == "+":
    #     if letter.isalpha():
    #         if input_str[index-1] == "+" and input_str[index+1] == "+":
    #           surrounded = True
    #         else:
    #           return False
