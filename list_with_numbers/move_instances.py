"""
You're given an array of integers and an integer.
 Write a function that moves all instances of that integer in the array to the end of the array and returns the array. 
 The function doesn't need to maintain the order of the other integers. 

Sample Input: array = [2, 1, 2, 2, 2, 3, 4, 2] toMove = 2 
Sample Output: [1, 3, 4, 2, 2, 2, 2, 2) // the numbers 1, 3, and 4 could be ordered differently. 
"""


def solution(array, toMove):
    # write your code here
    end = len(array) - 1
    index = 0
    while index < end:
        if array[index] == toMove:
            if array[end] != toMove:
                backup = array[index]
                array[index] = array[end]
                array[end] = backup

            end -= 1
            continue

        index += 1

    return array


if __name__ == "__main__":
    assert solution([], 2) == []
    assert solution([1, 2, 3], 4) == [1, 2, 3]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    assert solution([4, 1, 2, 3], 4) == [3, 1, 2, 4]
    assert solution([1, 4, 2, 3], 4) == [1, 3, 2, 4]
    assert solution([1, 2, 4, 3], 4) == [1, 2, 3, 4]
    assert solution([4, 1, 2, 3, 4], 4) == [3, 1, 2, 4, 4]
    assert solution([2, 1, 2, 2, 2, 3, 4, 2], 2) == [4, 1, 3, 2, 2, 2, 2, 2]
