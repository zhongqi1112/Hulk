#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            # this condition is important, it is the different from #33,
            # if nums[middle] == nums[left], then we can find the relative position of target
            elif nums[middle] == nums[left]:
                left = left + 1
                continue
            # pivot element is in second half
            # equal sign has to be here because middle point will be left element when even length
            elif nums[middle] > nums[left]:
                # if target is located in the non-rotated subarray
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # pivot element is in first half
            else:  # nums[middle] < nums[left]
                # if target is located in the non-rotated subarray
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return False
        
# @lc code=end
