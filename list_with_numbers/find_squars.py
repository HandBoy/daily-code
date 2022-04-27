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
