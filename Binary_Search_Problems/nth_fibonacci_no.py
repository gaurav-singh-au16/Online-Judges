"""
Nth Fibonacci Number
The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.

Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

Constraints

n ≤ 30
Example 1
Input
n = 1
Output
1
Explanation
This is the base case and the first fibonacci number is defined as 1.

Example 2
Input
n = 6
Output
8
Explanation
Since 8 is the 6th fibonacci number: 1, 1, 2, 3, 5, 8.

Example 3
Input
n = 7
Output
13
Explanation
Since 13 is the seventh number: 1, 1, 2, 3, 5, 8, 13

Solved
2,779
Attempted
3,007
Rate
92.42%
"""
def solve(n):
        
    dp = [0]* 10
    dp[0] = 0
    dp[1] = 1
    for i in range(n+1):
        if i !=0 and i !=1:
            dp[i] = dp[i-2]+dp[i-1]
    return dp[n]
if __name__ == "__main__":
    n = 3
    print(solve(n))


