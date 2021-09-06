"""[summary]
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def produtc_list(list_of_numbers):
    product_list = []
    for i in range(0, len(list_of_numbers)):
        prod = 1
        for j in range(0, len(list_of_numbers)):
            if i != j:
                print(list_of_numbers[j])
                prod *= list_of_numbers[j]

        product_list.append(prod)

    return product_list


def main():
    assert produtc_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert produtc_list([3, 2, 1]) == [2, 3, 6]
    print("Success!")


if __name__ == "__main__":
    main()
