#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time complexity : O(nlogn)
        Space complexity: O(logn)

        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
# @lc code=end

