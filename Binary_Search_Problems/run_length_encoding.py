"""
Run-Length Encoding
Given a string s, return its run-length encoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "aaaabbbccdaa"
Output
"4a3b2c1d2a"
Example 2
Input
s = "abcde"
Output
"1a1b1c1d1e"
Example 3
Input
s = "aabba"
Output
"2a2b1a"
Example 4
Input
s = "aaaaaaaaaa"
Output
"10a"
Solved
1,438
Attempted
1,745
Rate
82.41%
"""
class Solution:
    def solve(self, s):
        ans = ""
        res = ""
        cnt = 0
        for i in range(len(s)):
            if res == "":
                res = s[i]
                cnt += 1
            elif s[i] == res[-1]:
                cnt += 1
                res = s[i]
            elif i != res[-1]:
                ans += str(cnt)+ res
                res = s[i]
                cnt = 1
            if i == len(s)-1:
                ans += str(cnt) + res 

        return ans