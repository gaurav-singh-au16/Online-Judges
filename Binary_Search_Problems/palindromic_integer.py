"""
Palindromic Integer
Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?

Constraints

num < 2 ** 31
Example 1
Input
num = 121
Output
True
Example 2
Input
num = 20200202
Output
True
Example 3
Input
num = 43
Output
False
Solved
3,570
Attempted
3,846
Rate
92.83%
"""
class Solution:
    def solve(self, num):
        res = str(num)
        if res == res[::-1]:
            return True
        else:
            return False