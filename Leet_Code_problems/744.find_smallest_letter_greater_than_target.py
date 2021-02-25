"""
744. Find Smallest Letter Greater Than Target
Easy

574

678

Add to List

Share
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
Accepted
96,701
Submissions
212,103
Seen this question in a real interview before?

Yes

No
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = []
        for i in range(len(letters)):
            if ord(letters[i])>ord(target):
                res.append(ord(letters[i]))
                
        
        if len(res) != 0: 
            ans = min(res)
            return chr(ans)
        else:
            for i in range(len(letters)):
                res.append(ord(letters[i]))
            ans = min(res)
            return chr(ans)
                
                
       
                
            