"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

import unittest

class Solution:
    def containsDuplicate(self, nums: list[int]) ->bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

class Test(unittest.TestCase):
    def test_containsDuplicate(self):
        self.assertEqual(True, Solution().containsDuplicate([1, 2, 3, 1]))
    def test_containsDuplicate2(self):
        self.assertEqual(False, Solution().containsDuplicate([1, 2, 3, 4]))
    def test_containsDuplicate3(self):
        self.assertEqual(True, Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == '__main__':
    unittest.main()