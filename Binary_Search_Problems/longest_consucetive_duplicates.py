"""
Longest Consecutive Duplicate String
Given a lowercase alphabet string s, return the length of the longest substring with same characters.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "abbbba"
Output
4
Explanation
The longest substring is "bbbb".

Example 2
Input
s = "aaabbb"
Output
3
Solved
1,168
Attempted
1,351
Rate
86.46%
"""

def solve(s):
    ans = 0
    count = 0
    p1 = 0
    p2 = 1
    if len(s) == 0:
        return 0
    
    while p2 < len(s):
        if s[p1] != s[p2]:
            if ans < count:
                ans = count
                count = 0
            else:
                count = 0
            
            p1 += 1
            p2 += 1
        elif s[p1] == s[p2]:
            count += 1
            p1 += 1
            p2 += 1
    
    if ans < count:
        ans = count
        count = 0
    else:
        count = 0
    return ans+1
if __name__ == "__main__":
    s =  "aaabbbb"
    print(solve(s))