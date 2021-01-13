"""
Consecutive Duplicates
Given a string s, consisting of "X" and "Y"s, delete the minimum number of characters such that there's no consecutive "X" and no consecutive "Y".

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "YYYXYXX"
Output
"YXYX"
Explanation
One solution is to delete the first two "Y"s and the last "X".

Solved
734
Attempted
1,150
Rate
63.83%
"""
def solve(s):
    n = len(s)
    stack = []
    p1 = 0
    while p1 < n:
        if len(stack) == 0:
            stack.append(s[p1])
            p1 += 1
        elif s[p1] == stack[-1]:
            p1 += 1
        else:
            stack.append(s[p1])
            p1 += 1
    ans = "".join(stack)
    return ans

        
if __name__ == "__main__":
    s  = "YYYXYXX"
    print(solve(s))