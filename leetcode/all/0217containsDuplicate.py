class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # https://leetcode.com/problems/contains-duplicate/
        # Updated: 12/16/2020
        
        # numsSet = set(nums)
        # if len(numsSet) < len(nums):
        #     return True
        # else:
        #     return False
        return len(set(nums)) < len(nums)