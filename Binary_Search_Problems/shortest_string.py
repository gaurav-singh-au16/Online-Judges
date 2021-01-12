"""
Shortest String
Given a string s consisting only of "1"s and "0"s, you can delete any two adjacent letters if they are different.

Return the length of the smallest string that you can make if you're able to perform this operation as many times as you want.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "11000"
Output
1
Explanation
After deleting "10" we get "100" and we can delete another "10" to get "0" which has a length of 1.

Solved
611
Attempted
774
Rate
78.95%
"""
class Solution:
    def solve(self, s):
        stack = []
        p1 = 0
        n = len(s)
        while p1 < n:
            if len(stack) == 0:
                stack.append(s[p1])
                p1 += 1
            elif stack[-1] == s[p1]:
                stack.append(s[p1])
                p1 += 1
            elif stack[-1] != s[p1]:
                stack.pop(-1)
                p1 += 1
        return len(stack) 