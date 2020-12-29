class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-numbers-with-even-number-of-digits
        evenNumber = 0
        for n in nums:
            continues = True
            digits = 0
            while continues:
                if n / 10 > 0:
                    continues = True
                    digits = digits + 1
                    n = n // 10
                else:
                    continues = False
            if digits % 2 == 0:
                evenNumber = evenNumber + 1
        return evenNumber
    
        # return sum(len(str(i))%2==0 for i in nums)