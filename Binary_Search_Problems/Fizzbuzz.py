"""
FizzBuzz
Given an integer n, return a list of integers from 1 to n as strings except for multiples of 3 use “Fizz” instead of the integer and for the multiples of 5 use “Buzz”. For integers which are multiples of both 3 and 5 use “FizzBuzz”.

Constraints

0 ≤ n ≤ 100,000
Example 1
Input
n = 15
Output
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
Solved
2,821
Attempted
3,057
Rate
92.29%
"""
class Solution:
    def solve(self, n):
        ans = []
        for i in range(1, n+1):
            if i%3==0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i%3 == 0:
                ans.append("Fizz")
            elif i%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans