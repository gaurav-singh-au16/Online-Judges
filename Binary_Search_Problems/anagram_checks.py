"""
Anagram Checks
Given two strings s0 and s1, return whether they are anagrams of each other.

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where m is the length of s1
Example 1
Input
s0 = "listen"
s1 = "silent"
Output
True
Example 2
Input
s0 = "bedroom"
s1 = "bathroom"
Output
False
Solved
2,167
Attempted
2,428
Rate
89.26%
"""
class Solution:
    def solve(self, s0, s1):
        if sorted(s0) == sorted(s1):
            return True
        else:
            return False