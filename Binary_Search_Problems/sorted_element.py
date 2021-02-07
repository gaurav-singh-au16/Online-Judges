"""
Sorted Elements
Give a list of numbers nums, return the number of elements that are in the correct indices, if the list were to be sorted.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 7, 3, 4, 10]
Output
2
Explanation
Comparing nums and its sorted version we find that elements 1 and 10 are in their correct positions.

[1, 7, 3, 4, 10]
[1, 3, 4, 7, 10]
Solved
2,400
Attempted
2,603
Rate
92.21%
"""
class Solution:
    def solve(self, nums):
        res = sorted(nums)
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == res[i]:
                cnt += 1
        return cnt
            