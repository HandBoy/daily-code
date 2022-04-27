"""_summary_

Strings in Python are immutable. This means that they cannot be changed. 
If you try to change the contents of an existing string, 
you're liable to find an error that says something.

For example:
>>> string = "Banana"
>>> string[0] = "A"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 

"""


def change_alpha(text: str):
    list_of_char = list(text)
    begin_idx = 0
    last_idx = len(text) - 1

    while begin_idx < last_idx:
        if list_of_char[begin_idx].isalpha():
            if list_of_char[last_idx].isalpha():
                backup = list_of_char[begin_idx]
                list_of_char[begin_idx] = list_of_char[last_idx]
                list_of_char[last_idx] = backup

                begin_idx += 1
                last_idx -= 1
            else:
                last_idx -= 1
        else:
            begin_idx += 1

    return "".join(list_of_char)


if __name__ == "__main__":
    assert change_alpha("ab.cd") == "dc.ba"
    assert change_alpha("ab..cd") == "dc..ba"
    assert change_alpha("..a..") == "..a.."
    assert change_alpha("ab.-g-.cd") == "dc.-g-.ba"
    assert change_alpha("...ad") == "...da"
    assert change_alpha("..ad..") == "..da.."
    assert change_alpha("ad...") == "da..."
    assert change_alpha("aj40-l30-s") == "sl40-j30-a"
