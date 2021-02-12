"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        res = sorted(nums)
        
        ans = 0
        if len(res) % 2 == 0:
            idx = len(res)//2
            ans = (res[idx] + res[idx-1]) / 2
        else:
            idx = len(res)//2
            ans = res[idx]
        return ans