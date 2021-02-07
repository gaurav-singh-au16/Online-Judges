"""
List Min Replacement
Given a list of integers nums, replace every nums[i] with the smallest integer left of i. Replace nums[0] with 0.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [10, 5, 7, 9]
Output
[0, 10, 5, 5]
Explanation
nums[0] = 0 by definition
nums[1] = min(10)
nums[2] = min(5, 10)
nums[3] = min(7, 5, 10)
Solved
633
Attempted
1,047
Rate
60.46%
"""
class Solution:
    def solve(self, nums):
        ans = []
        mini = 0
        for i in range(len(nums)):
            if i == 0:
                ans.append(i)
                mini = nums[i]
            else:
                ans.append(mini)
                if nums[i] < mini:
                    mini = nums[i]
        return ans