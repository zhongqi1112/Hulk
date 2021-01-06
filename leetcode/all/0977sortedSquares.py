class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/squares-of-a-sorted-array/
        squares = [n**2 for n in nums]
        squares.sort()
        return squares
    
        # return sorted(list(map(lambda n: n**2, nums)))