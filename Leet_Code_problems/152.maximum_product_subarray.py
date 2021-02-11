"""
152. Maximum Product Subarray
Medium

6153

205

Add to List

Share
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
Accepted
442,762
Submissions
1,353,714
"""
def maxProduct(nums):
    left = 0
    right = 0
    maxsum = float("-inf")
    for i in range(len(nums)):
        left = (left or 1) * nums[i]
        right = (right or 1) * nums[-i-1]
        maxsum = max(maxsum, left, right)
    return maxsum
if __name__ == '__main__':
    nums = [-2,0,-1]
    print(maxProduct(nums))
    
