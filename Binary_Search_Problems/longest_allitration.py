"""
Longest Alliteration
Given a list of lowercase alphabet strings words, return the length of the longest contiguous sublist where all words share the same first letter.

Constraints

0 ≤ n ≤ 100,000 where n is the length of words
Example 1
Input
words = ["she", "sells", "seashells", "he", "sells", "clams"]
Output
3
Explanation
["she", "sells", "seashells"] all share the first letter s.

Solved
761
Attempted
911
Rate
83.54%
Hint #1
"""
class Solution:
    def solve(self, words):
        ans = 0
        res = 0
        wrd = ""
        if len(words) == 1:
            return 1
        for i in words:
            if wrd != i[0] and ans <= res:
                ans = res
                res = 0
            if res == 0:
                wrd = i[0]
                res += 1
                
            elif wrd == i[0]:
                res += 1
            else:
                wrd = i[0]
                res = 1
            if len(words)-1 and ans <= res:
                ans = res
            
        return ans
