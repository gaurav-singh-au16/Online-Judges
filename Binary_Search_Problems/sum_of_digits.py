"""
Given a positive integer num, return the sum of its digits.

Bonus: Can you do it without using strings?

Constraints

0 ≤ num < 2 ** 31
Example 1
Input
num = 123
Output
6
Explanation
Since 6 = 1 + 2 + 3

Example 2
Input
num = 50
Output
5
Explanation
Since 5 = 5 + 0

Solved
4,027
Attempted
4,507
Rate
89.35%
"""
def solve(num):
    a = str(num)
    ans = 0
    for i in a:
        ans += int(i)
    return ans

if __name__ == "__main__":
    num = 123
    print(solve(num))