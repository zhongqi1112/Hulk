#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursion with Memoization
        # Time complexity: O(n)
        # Space complexity:O(n)
        """
        self.memo = {}
        self.nums = nums
        
        return self.robFrom(0)
    
    def robFrom(self, i):
        # No more houses left to examine.
        if i >= len(self.nums):
            return 0
        
        # Return cached value.
        if i in self.memo:
            return self.memo[i]
        
        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1), self.robFrom(i + 2) + self.nums[i])
        
        # Cache for future use.
        self.memo[i] = ans
        return ans
        """

        # Dynamic Programming
        # Time complexity: O(n)
        # Space complexity:O(n)
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
        return maxRobbedAmount[0] 
# @lc code=end

