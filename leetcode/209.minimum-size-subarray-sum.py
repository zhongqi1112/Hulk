#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Two pointers
        Time complexity : O(n)
        Space complexity: O(1)
        """
        ans = float('inf') 
        left = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                ans = min(ans, (i-left+1))
                s -= nums[left]
                left += 1
        if ans == float('inf') :
            ans = 0
        return ans

# @lc code=end

