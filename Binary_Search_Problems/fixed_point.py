"""
Fixed Point
Given a list of unique integers nums sorted in ascending order, return the minimum i such that nums[i] == i. If there's no solution, return -1.

This should be done in \mathcal{O}(log(n))O(log(n)) time.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [-5, -2, 0, 3, 4]
Output
3
Explanation
Both nums[3] == 3 and nums[4] == 4 but 3 is smaller.

Example 2
Input
nums = [-5, -4, 0]
Output
-1
Explanation
There's no i such that nums[i] = i.

Solved
814
Attempted
915
Rate
88.97%
"""
class Solution:
    def solve(self, nums):
        ans = []
        for i in range(len(nums)):
            if i == nums[i]:
                ans.append(i)
        if len(ans) == 0:
            return -1
        else:
            return min(ans)
            