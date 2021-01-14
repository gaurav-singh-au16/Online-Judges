"""
Vowels and Consonants Sort
Given a lowercase alphabet string s, return a string with all the vowels of s in sorted order followed by all the consonants of s in sorted order.

Note: vowels are ["a", "e", "i", "o", "u"] and consonants are all other characters.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "decalin"
Output
"aeicdln"
Explanation
Vowels are "eai" which when sorted is "aei"
Consonants are "dcln" which when sorted is "cdln"
Their concatenation is "aeicdln"
Solved
1,510
Attempted
1,643
Rate
91.91%
"""
def solve(s):
    vow = ""
    cons = ""
    for ch in s:
        if ch in "aeiou":
            vow +=  ch
        else:
            cons += ch
    a = sorted(vow)
    b = sorted(cons)
    ans = "".join(a)+"".join(b)
    return ans
if __name__ == "__main__":
    s = "decalin"
    print(solve(s))