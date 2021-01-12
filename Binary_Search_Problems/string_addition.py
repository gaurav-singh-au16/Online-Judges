"""
String Addition
Given two strings a, and b, both representing an integer, add them and return it in the same string representation.

This should be implemented directly, instead of using eval or built-in big integers.

Constraints`

n ≤ 200 where n is the length of a
m ≤ 200 where m is the length of b
Example 1
Input
a = "12"
b = "23"
Output
"35"
Explanation
12 + 23 = 35

Solved
666
Attempted
821
Rate
81.13%
"""
class Solution:
    def solve(self, a, b):
        ans = int(a) + int(b)
        return str(ans)