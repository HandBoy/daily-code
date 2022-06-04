"""
Task 3 
You're given a string of available characters and a string representing a document that you need to generate. 
Write a function: solution(characters, document) that determines if you can generate the document using the available characters.
If you can generate the document, your function should return True; otherwise it should return False 

For example, if you're given characters = 'abcabc' and document = ' aabbccc ', 
you cannot generate the document because you're missing one c so function should return False. 

Notes: The document that you need to create may contain any characters, including special characters, numbers and spaces. 

"""


def solution(characters: str, document: str):

    for char in document:
        if char not in characters:
            return False

        characters = characters.replace(char, "", 1)

    return True


if __name__ == "__main__":
    assert solution("abc", "") == True
    assert solution("abc", "cba") == True
    assert solution("helloworldO", "hello") == True

    assert solution("abcabc", "aabbccc") == False
    assert solution("abc", "aaaaaaa") == False
    assert solution("abc", "d") == False
    assert solution("abc", "dabc") == False
    assert solution("abc", "abcd") == False
    assert solution("aheaollabbhb", "hello wOrld") == False
