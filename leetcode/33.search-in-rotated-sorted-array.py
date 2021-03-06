#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The idea is that we add some additional condition checks in the normal binary search in order to better narrow down the scope of the search.
        Time complexity : O(logN)
        Space complexity: O(1)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            # pivot element is in second half
            # equal sign has to be here because middle point will be left element when even length
            elif nums[middle] >= nums[left]:
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
        return -1
        
# @lc code=end

