class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/two-sum/
        # https://www.geeksforgeeks.org/enumerate-in-python/
        # Updated: 12/15/2020
        
        seen = {}
        for count, item in enumerate(nums):
            complement = target - item
            if complement in seen:
                return [seen[complement], count]
            else:
                seen[item] = count
                