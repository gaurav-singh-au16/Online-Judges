"""
Largest Gap
Given a list of integers nums, return the largest difference of two consecutive integers in the sorted version of nums.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [4, 1, 2, 8, 9, 10]
Output
4
Explanation
The largest gap is between 4 and 8.

Solved
1,829
Attempted
1,962
Rate
93.23%
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        gap = 0
        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p2] -nums[p1] > gap:
                gap = nums[p2] - nums[p1]
                p1 += 1
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return gap 
