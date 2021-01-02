"""
1512. Number of Good Pairs
Easy

771

69

Add to List

Share
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
Accepted
110,708
Submissions
125,975
"""
def numIdenticalPairs(nums):
    ans = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                ans += 1
    if ans == 0:
        return 0
    else:
        return ans
if __name__ == "__main__":
    nums = [1,1,1,1]
    print(numIdenticalPairs(nums))