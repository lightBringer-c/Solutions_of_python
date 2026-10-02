"""

Code
Testcase
Testcase
Test Result
1480. Running Sum of 1d Array
Easy
Topics
premium lock icon
Companies
Hint
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

import unittest


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        current_sum = 0
        for num in nums:
            current_sum += num
            answer.append(current_sum)
        return answer

class TestSolution(unittest.TestCase):
    def test_running_sum(self):
        self.assertEqual(Solution().runningSum([1,2,3,4]), [1,3,6,10])
    def test_running_sum2(self):
        self.assertEqual(Solution().runningSum([1,1,1,1,1]), [1,2,3,4,5])
    def test_running_sum3(self):
        self.assertEqual(Solution().runningSum([3,1,2,10,1]), [3,4,6,16,17])

if __name__ == '__main__':
    unittest.main()