"""
Merging Two Sorted Lists
Given two sorted lists of integers, merge them into one large sorted list.

Example 1
Input
lst0 = [5, 10, 15]
lst1 = [3, 8, 9]
Output
[3, 5, 8, 9, 10, 15]
Solved
2,971
Attempted
3,186
Rate
93.26%
"""
class Solution:
    def solve(self, lst0, lst1):
        ans = []
        p1 = 0
        p2 = 0
        while p1 < len(lst0) and p2 < len(lst1):
            if lst0[p1] > lst1[p2]:
                ans.append(lst1[p2])
                p2 += 1
            else:
                ans.append(lst0[p1])
                p1 += 1
               
        while p2 < len(lst1):
            ans.append(lst1[p2])
            p2 += 1
        while p1 < len(lst0):
            ans.append(lst0[p1])
            p1 += 1
        return ans
        