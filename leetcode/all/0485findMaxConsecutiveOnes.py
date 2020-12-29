class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/max-consecutive-ones/
        
        maxLength = 0
        curLength = 0
        
        for n in nums:
            if n == 1:
                curLength = curLength + 1
            else:
                curLength = 0
            maxLength = max(curLength, maxLength)
        return maxLength