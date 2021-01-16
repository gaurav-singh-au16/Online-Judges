"""
High Frequency
Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 4, 1, 7, 1, 7, 1, 1]
Output
5
Example 2
Input
nums = [5, 5, 5, 5, 5, 5, 5]
Output
7
Example 3
Input
nums = [1, 2, 3, 4, 5, 6, 7]
Output
1
Solved
2,517
Attempted
2,783
Rate
90.45%
"""
class Solution:
    def solve(self, nums):
        d = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for key, value in d.items():
            if value > ans:
                ans = value
        return ans