"""
Check Power of Two
Given an integer n greater than or equal to 0, return whether it is a power of two.

Constraints

0 ≤ n < 2 ** 31
Example 1
Input
n = 0
Output
False
Example 2
Input
n = 1
Output
True
Explanation
2^0 = 1

Example 3
Input
n = 2
Output
True
Explanation
2^1 = 2

Solved
1,548
Attempted
1,742
Rate
88.87%
Hint #1
"""
class Solution:
    def solve(self, n):
        for i in range(n):
            if 2**i == n:
                return True
            if 2**i > n:
                break
        return False
        