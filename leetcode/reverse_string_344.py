"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

import unittest

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

class TestSolution(unittest.TestCase):
    def test_reverseString(self):
        s = ["h","e","l","l","o"]
        Solution().reverseString(s)
        self.assertEqual(s, ["o","l","l","e","h"])
    def test_reverseString2(self):
        s = ["H","a","n","n","a","h"]
        Solution().reverseString(s)
        self.assertEqual(s, ["h","a","n","n","a","H"])

if __name__ == '__main__':
    unittest.main()