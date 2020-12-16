class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/majority-element/
        # Updated: 12/15/2020
        
        nums.sort()
        return nums[len(nums)//2]