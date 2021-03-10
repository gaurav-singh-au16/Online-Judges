"""
ASCII String to Integer
You are given a string s containing digits from "0" to "9" and lowercase alphabet characters. Return the sum of the numbers found in s.

Constraints

1 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "11aa32bbb5"
Output
48
Explanation
Since 11 + 32 + 5 = 48.

Example 2
Input
s = "abc"
Output
0
Explanation
There's no digits so it defaults to 0.

Example 3
Input
s = "1a2b30"
Output
33
Explanation
Since 1 + 2 + 30 = 33.

Solved
1,404
Attempted
1,519
Rate
92.43%
"""

class Solution:
    def solve(self, s):
        number = []
        res = ""
        for ch in s:
            if ch in "0123456789":
                res += ch
            elif ch not in "0123456789" and res != "":
                number.append(int(res))
                res = ""
        if res != "":
            number.append(int(res))
        
        return sum(number)
            
        