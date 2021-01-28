#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two points is the common method to solve this problem and takes O(n) time and O(1) space
        binary search can take less time beside the worsest case, which is two numbers are in the center
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            middle = (left + right) // 2
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                if numbers[middle] + numbers[right] < target:
                    left = middle + 1
                else:
                    left = left + 1
            else:
                if numbers[left] + numbers[middle] > target:
                    right = middle - 1
                else:
                    right = right - 1
            
# @lc code=end

