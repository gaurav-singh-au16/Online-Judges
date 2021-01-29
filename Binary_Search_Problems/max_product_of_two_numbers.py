"""
Max Product of Two Numbers
Given a list of integers nums, find the largest product of two distinct elements.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [5, 1, 7]
Output
35
Explanation
35 is the largest product that can be made from 5 * 7

Example 2
Input
nums = [7, 1, 7]
Output
49
Explanation
49 is the largest product that can be made from 7 * 7. The values can be the same but they must be separate elements.

Example 3
Input
nums = [-5, 1, -7]
Output
35
Explanation
35 is the largest product that can be made from -5 * -7.

Solved
1,180
Attempted
1,483
Rate
79.57%
"""
class Solution:
    def solve(self, nums):
        a = min(nums)
        nums.remove(a)

        b = min(nums)
        nums.remove(b)

        nums.append(a)
        nums.append(b)

        x = max(nums)
        nums.remove(x)

        y = max(nums)
        
        if a*b > x*y:
            return a*b
        else:
            return x*y
        