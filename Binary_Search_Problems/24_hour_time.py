"""
24-Hour Time
Given a string s, representing a 12-hour clock time with am/pm, return its 24-hour equivalent.

Example 1
Input
s = "05:30pm"
Output
"17:30"
Example 2
Input
s = "03:00am"
Output
"03:00"
Example 3
Input
s = "12:00pm"
Output
"12:00"
Example 4
Input
s = "12:00am"
Output
"00:00"
Example 5
Input
s = "11:59pm"
Output
"23:59"
Solved
747
Attempted
890
Rate
83.94%
"""

def solve(s):
    res = ""
    res += s[0]+s[1]
    ans = ""
    if "12" in res and "pm" in s:
        return res+s[2]+s[3]+s[4]
    elif "12" in res and "am" in s:
        return "00"+s[2]+s[3]+s[4]
    else:
        if "pm" in s and "12" not in res:
            ans = int(res) + 12
            return str(ans)+s[2]+s[3]+s[4]
        else:
            return res +s[2]+s[3]+s[4]
    
if __name__ == "__main__":
    s = "05:30pm"
    print(solve(s))