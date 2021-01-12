"""
A Unique String
Given a lowercase alphabet string s, determine whether it has all unique characters.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "abcde"
Output
True
Explanation
All characters only occur once

Example 2
Input
s = "aab"
Output
False
Explanation
There's two as

Example 3
Input
s = ""
Output
True
Explanation
All characters occur once (of which there are none)

Solved
3,077
Attempted
3,296
Rate
93.36%
"""
class Solution:
    def solve(self, s):
        ans = ""
        if s == "":
            return True
        for ch in s:
            if ch not in ans:
                ans += ch
            elif ch in ans:
                return False
        if ans == s:
            return True

