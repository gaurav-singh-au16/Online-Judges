"""
34. Find First and Last Position of Element in Sorted Array
Medium

4592

181

Add to List

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 10
"""
def searchRange(nums, target):
    if target not in nums:
        return([-1, -1])

    n = nums.index(target)
    j = n
    for x in range(n+1, len(nums)):
        if nums[x]==target:
            j = x
        else:
            break
    return([n, j])

if __name__ == "__main__":
    
    print(searchRange(nums = [5,7,7,8,8,10], target = 8))