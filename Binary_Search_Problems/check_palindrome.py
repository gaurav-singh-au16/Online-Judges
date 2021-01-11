"""
Check Palindrome
Given a string s, return whether it is a palindrome.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "racecar"
Output
True
Example 2
Input
s = "evilolive"
Output
True
Example 3
Input
s = "palindrome"
Output
False
Solved
3,441
Attempted
3,677
Rate
93.59%
"""
class Solution:
    def solve(self, s):
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False