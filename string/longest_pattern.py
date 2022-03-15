import unittest
"""
Write a function that takes a string and returns the longest case-insensitive pattern in that string.
A pattern is an alphabetically ascending sequence of at least two characters. 
If no pattern is found an empty string will be returned. 
If two or more patterns are found with the same length return the first.

For example:
- "acwxyzabghwxyo" will return "wxyz"
- "azbycxdwev" will return the empty string
- "abcaeabcaeabcdabcd" will return "abcd"
"""

class Solution:
    def find_longest_pattern(self, input):
        result = ""
        pattern = ""
        last = ""

        it = iter(input)
        letter = next(it, None)

        while letter:
            last = letter
            letter = next(it, None)

            if letter and ord(last)+1 == ord(letter):
                if pattern:
                    pattern += letter
                else:
                    pattern = last+letter
                continue
                
            if len(result) < len (pattern):
                result = pattern
            
            pattern = ""
           
        return result


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_with_empty_string(self):
        self.assertEqual(self.solution.find_longest_pattern(""), "")
    
    def test_with_minimal_pattern(self):
        self.assertEqual(self.solution.find_longest_pattern("abd"), "ab")

    def test_without_pattern(self):
        self.assertEqual(self.solution.find_longest_pattern("azbycxdwev"), "")
    
    def test_with_pattern_in_the_beggining(self):
        self.assertEqual(self.solution.find_longest_pattern("wxyzacabghwxyo"), "wxyz")

    def test_with_pattern_in_the_middle(self):
        self.assertEqual(self.solution.find_longest_pattern("acabgwxyzhwxyo"), "wxyz")

    def test_with_pattern_in_the_end(self):
        self.assertEqual(self.solution.find_longest_pattern("acabghwxyowxyz"), "wxyz")
    
    def test_with_two_diff_pattern_with_the_same_len(self):
        self.assertEqual(self.solution.find_longest_pattern("wwwabcawwwghi"), "abc")
    
    def test_with_duplicate_pattern(self):
        self.assertEqual(
            self.solution.find_longest_pattern("abcaeabcaeabcdabcd"), "abcd"
        )
    
    
    
if __name__ == '__main__':
    unittest.main()
