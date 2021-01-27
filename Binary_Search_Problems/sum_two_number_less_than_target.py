"""
Sum of Two Numbers Less Than Target
Given a list of integers nums and an integer target, return the sum of the largest pair of numbers in nums whose sum is less than target. You can assume that there is a solution.

Constraints

2 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [5, 1, 2, 3]
target = 4
Output
3
Explanation
Sum of the largest pair of numbers less than 4 is 1 + 2 = 3.

Solved
247
Attempted
379
Rate
65.18%
"""
class Solution:
    def solve(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] < target:
                    ans.append(nums[i]+nums[j])
        return max(ans)
