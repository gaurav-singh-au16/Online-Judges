"""
Odd Number of Digits
Given a list of positive integers nums, return the number of integers that have odd number of digits.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 800, 2, 10, 3]
Output
4
Explanation
[1, 800, 2, 3] have odd number of digits.

Solved
2,724
Attempted
2,976
Rate
91.54%
"""
class Solution:
    def solve(self, nums):
        res = []
        count = 0
        for i in range(len(nums)):
            res.append(str(nums[i]))
        for j in res:
            if len(j) % 2 != 0:
                count += 1
        return count