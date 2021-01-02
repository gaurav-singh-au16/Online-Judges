"""
1281. Subtract the Product and Sum of Digits of an Integer
Easy

431

123

Add to List

Share
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
Accepted
117,936
Submissions
137,780
"""
def subtractProductAndSum(n):
    product = 1
    sum = 0
    a = str(n)
    for i in a:
        product *= int(i)
        sum += int(i)
    ans = product - sum
    return ans
if __name__ == "__main__":
    n = 4421
    print(subtractProductAndSum(n))