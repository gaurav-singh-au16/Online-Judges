"""
Add One
Question 235 of 991
You are given a list of integers nums, representing a decimal number and nums[i] is between [0, 9].

For example, [1, 3, 9] represents the number 139.

Return the same list in the same representation except modified so that 1 is added to the number.

Constraints

n ≤ 100,000 where n is the length of nums.
Example 1
Input
nums = [1, 9, 1]
Output
[1, 9, 2]
Example 2
Input
nums = [9]
Output
[1, 0]
Solved
792
Attempted
965
Rate
82.08%
"""
def solve(nums):
    a = ""
    for i in range(len(nums)):
        a += str(nums[i])
    res = int(a)+1
    ans = []
    for ch in str(res):
        ans.append(int(ch))
    return ans
if __name__ == "__main__":
    nums = [1,9,1]
    print(solve(nums))