"""
1704. Determine if String Halves Are Alike
Easy

96

5

Add to List

Share
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
Accepted
16,129
Submissions
20,637
"""
def solve(s):   
    a = s[0:len(s)//2] 
    b = s[len(s)//2:]

    cnt1 = 0
    cnt2 = 0
    for i in a:
        if i in "aeiouAEIOU":
            cnt1 += 1
    for j in b:
        if j in "aeiouAEIOU":
            cnt2 += 1
    if cnt1 == cnt2:
        return True, a, b, cnt1, cnt2
    else:
        return False, a, b, cnt1, cnt2
if __name__ == "__main__":
    s = "textbook"
    print(solve(s))