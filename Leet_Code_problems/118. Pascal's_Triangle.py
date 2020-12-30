"""
118. Pascal's Triangle
Easy

2061

123

Add to List

Share
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Accepted
441,698
Submissions
815,480
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if 0 < j < i:
                    ans[i].append(ans[i-1][j-1] + ans[i-1][j])
                else:
                    ans[i].append(1)
        return ans