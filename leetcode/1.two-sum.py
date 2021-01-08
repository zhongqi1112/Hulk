#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Traverse list once, finding the complement for each item
        time complexity : O(n)
        space complexity: O(n)
        """
        # create a dict (hashtable), seen, key is the item and value is index
        seen = {}
        # go through the list once
        # converge list to dict, key is the index, value is the item
        for i, item in enumerate(nums):
            # get complement for current item
            complement = target - item
            # if the the complement of current item is in the seen, return ideices of complement and current item
            if complement in seen:
                indices = [seen[complement], i]
                return indices
            # otherwise, add item as key and index as value into seen dict
            else:
                seen[item] = i
# @lc code=end

