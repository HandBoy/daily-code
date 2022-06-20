"""
Write a function that reverses a string. The input string is given as an array of characters s.

Do not use the .reverse() method

Input: s = ["h","e","l","l","o"] Output: ["o","l","l","e","h"]

"""


class Solution:
    def reverseString(self, s):
        result = []

        for idx in range(len(s) - 1, -1, -1):
            result.append(s[idx])

        return result


class SolutionInPlace:
    def reverseString(self, s):
        idx_a = 0
        idx_b = len(s) - 1

        while idx_a != idx_b:
            backup = s[idx_a]
            s[idx_a] = s[idx_b]
            s[idx_b] = backup

            idx_a += 1
            idx_b -= 1

        return s


if __name__ == "__main__":
    s = SolutionInPlace()

    assert s.reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert s.reverseString(["h", "e", "l"]) == ["l", "e", "h"]
