#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict (hashtable)
        seen = {}
        # go through the list once
        for count, item in enumerate(nums):
            complement = target - item
            if complement in seen:
                indices = [seen[complement], count]
                return indices
            else:
                seen[item] = count

# @lc code=end

