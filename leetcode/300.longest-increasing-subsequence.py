#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dynamic Programming
        # Time complexity: O(n^2)
        # Space complexity:O(n)
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range (i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)


        # Improve With Binary Search
        # Time complexity: O(nlogn)
        # Space complexity:O(n)
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
# @lc code=end

