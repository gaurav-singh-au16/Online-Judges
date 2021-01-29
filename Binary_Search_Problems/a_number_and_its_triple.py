"""
A Number and Its Triple
Given a list of integers nums, return whether there's two numbers such that one is a triple of another.

Constraints

n ≤ 100,000 where n is the length of nums.
Example 1
Input
nums = [2, 3, 10, 7, 6]
Output
True
Explanation
6 is a triple of 2

Example 2
Input
nums = [3, 4, 5]
Output
False
Explanation
There's no 9, 12, or 15.

Example 3
Input
nums = [0, 2, 0]
Output
True
Explanation
0 is a triple of 0

Solved
469
Attempted
792
Rate
59.22%
Topics
"""
class Solution:
    def solve(self, nums):
        n = len(nums)
        p1 = 0
        if len(nums) == 1:
            return False
        while p1 < n:
            a = nums[p1]*3
            x = nums.pop(p1)
            if a in nums:
                return True
            else:
                nums.insert(p1, x)
                p1 += 1
                
        return False
            
