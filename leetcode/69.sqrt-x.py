#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        use binary search iterate over the sorted set of integer numbers
        Time complexity : O(logn)
        Space complexity: O(1)
        """
        if x < 2:
             return x
        left = 2
        # square root is always smaller than x / 2
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end

