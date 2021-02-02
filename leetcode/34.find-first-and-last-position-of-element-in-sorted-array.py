#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result =[-1, -1]
        left = 0
        ## we need to change right because the condition is changed
        right = len(nums)
        # find the leftmost index
        while left < right:
            middle = (left + right) // 2
            ## this condition is different from rightmost
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        ## if we can not find leftmost index
        if left == len(nums) or nums[left] != target:
            return result
        else:
            result[0] = left
        # find the rightmost index
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            else:
                left = middle + 1
        ## we need to substract 1 becase left will jump over the last target
        result[1] = left - 1
        return result
# @lc code=end

