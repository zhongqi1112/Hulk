#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[left]
        # If the array is not rotated and the array is in ascending order
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            middle = (left + right) // 2
            # nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            # nums[mid - 1] > nums[mid] Hence, mid is the smallest
            elif nums[middle] < nums[middle - 1]:
                return nums[middle]
            # If mid element > first element of array this means that we need to look for the inflection point on the right of mid
            elif nums[middle] > nums[left]:
                left = middle + 1
            # If mid element < first element of array this that we need to look for the inflection point on the left of mid
            else:
                right = middle - 1

# @lc code=end
