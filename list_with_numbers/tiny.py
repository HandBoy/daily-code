"""
You are given two arrays of integers a and b of the same length, and an integer k. 
We will be iterating through array a from left to right, and simultaneously through array b from right to left, 
and looking at pairs (x, y), where x is from a and y is from b. 
Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Input:
a: [1, 2, 3]
b: [1, 2, 3]
k: 31
"""


def solution(a, b, k):
    tiny = 0

    for x, y in zip(a, b[::-1]):
        value = f"{x}{y}"
        if int(value) < k:
            tiny += 1

    return tiny


if __name__ == "__main__":
    assert solution([1, 2, 3], [1, 2, 3], 31) == 2
