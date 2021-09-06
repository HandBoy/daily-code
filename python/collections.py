"""
Differences and Applications of List, Tuple, Set and Dictionary in Python?

    List:   Receive differents types of value and your values are mutables.
    Tuple:  Is similar to a List but with one difference, it is imutable.
    Set:    Unordered  collection data, mutable and has no duplicate elements.
    Dict:   The keys are imutables and unique. The values are unordered.


"""

# List
list_one = ["one", "two", "three", 89, 5, 1.2]
list_one[0] = "eita"
print(list_one)
print(list_one[0])

# Tuple
tuple_one = ("one", "two", "three", 89, 5, 1.2)
# tuple_one[0] = "eita" TypeError: 'tuple' object does not support item assignment
print(tuple_one)
print(tuple_one[0])

# Set
set_one = set(list_one)
print(set_one)

# Dict
dict_one = {3: "Monday", 2: "Tuesday", 4: "Wednesday"}
print(dict_one)


a = {(1, 2): "abc"}


square_dict = {11: 121, 3: 9, 5: 25, 7: 49}


def find_square(the_num: int):
    """
    Updates the dict with the new squares..
    Args:
    The_num
    Returns:
    result(int): The square value
    """
    try:
        _result = None
        for _key, _value in square_dict.items():
            print(_key)
            if _key == the_num:
                _result = _value
                break

        if not _result:
            square_dict[the_num] = the_num ** 2
            _result = square_dict[the_num]
    except:
        pass

    return _result


def find_square2(the_num: int): 
    """
    Updates the dict with the new squares..
    Args:
    The_num
    Returns:
    result(int): The square value
    """
    if the_num in square_dict:
        return square_dict[the_num]

    result = the_num ** 2
    square_dict[the_num] = result

    return result



print("Result ", find_square(11))
print("Result ", find_square(2))
print(square_dict)
