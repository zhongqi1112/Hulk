#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # Time complexity: O(n)
        # Space complexity:O(1)
        best_sum = float('-inf')
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum
# @lc code=end

