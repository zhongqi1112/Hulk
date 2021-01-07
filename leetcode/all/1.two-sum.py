#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for count, item in enumerate(nums):
            complement = target - item
            if complement in seen:
                return [seen[complement], count]
            else:
                seen[item] = count
# @lc code=end

