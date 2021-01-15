"""
Repeated Addition
Given a positive integer n, sum all of its digits to get a new number. Repeat this operation until it's less than 10.

Example 1
Input
n = 8835
Output
6
Explanation
8 + 8 + 3 + 5 = 24
2 + 4 = 6
Solved
1,065
Attempted
1,202
Rate
88.61%
"""
class Solution:
    def solve(self, n):
        n_str = str(n)
        res = []
        for ch in n_str:
            res.append(int(ch))
        
        total = str(sum(res))
        ans = []
        for i in total:
            ans.append(int(i))
        
        if sum(ans) >= 10:
            re = str(sum(ans))
            final = []
            for j in re:
                final.append(int(j))
            return sum(final)

        else:
            return sum(ans)
            
