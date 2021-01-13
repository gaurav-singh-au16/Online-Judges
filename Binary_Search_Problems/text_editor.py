"""
Text Editor
Given a string s representing characters typed into an editor, with "<-" representing a backspace, return the current state of the editor.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "abc<-z"
Output
"abz"
Explanation
The "c" got deleted by the backspace.

Example 2
Input
s = "<-x<-z<-"
Output
""
Explanation
All characters are deleted. Also note you can type backspace when the editor is empty as well.

Solved
564
Attempted
743
Rate
75.91%
"""

def solve(s):
    n = len(s)
    stack = []
    p1 = 0
    while p1 < n:
        if len(stack) == 0:
            stack.append(s[p1])
            p1 += 1
        elif s[p1] == "<":
            stack.pop(-1)
            p1 += 2
        else:
            stack.append(s[p1])
            p1 += 1
    ans = "".join(stack)
    return ans
if __name__ == "__main__":
    s = "abc<-z"
    print(solve(s))