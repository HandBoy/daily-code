from itertools import combinations

"""[summary]

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def any_equal_to(list_numbers: list, k: int) -> bool:
    num_set = set(list_numbers)  # Sort and remove duplicates

    if len(num_set) < 2:
        return False

    for i in num_set:
        if k - i in num_set:
            return True

    return False


def any_equal_to_with_for(list_numbers: list, k: int) -> bool:
    """
    0   1   2   3
    0   01  02  03
    1       12  13
    2           23
    3
    """
    for i in range(0, len(list_numbers)):
        for j in range(i + 1, len(list_numbers)):
            if list_numbers[i] + list_numbers[j] == k:
                return True

    return False


def any_equal_to_with_combinations(list_numbers, k):
    return any(((i + j) == k) for i, j in combinations(list_numbers, 2))


def main():
    assert any_equal_to([10, 15, 3, 7, 15], 17) is True
    assert any_equal_to([10, 15, 3, 7], 18) is True
    assert any_equal_to([10, 15, 3, 7], 19) is False
    assert any_equal_to([5], 10) is False

    assert any_equal_to_with_for([10, 15, 3, 7], 17) is True
    assert any_equal_to_with_for([10, 15, 3, 7], 18) is True
    assert any_equal_to_with_for([10, 15, 3, 7], 19) is False
    assert any_equal_to_with_for([5], 10) is False

    assert any_equal_to_with_combinations([10, 15, 3, 7], 17) is True
    assert any_equal_to_with_combinations([10, 15, 3, 7], 18) is True
    assert any_equal_to_with_combinations([10, 15, 3, 7], 19) is False
    assert any_equal_to_with_combinations([5], 10) is False

    print("Success!")


if __name__ == "__main__":
    main()
