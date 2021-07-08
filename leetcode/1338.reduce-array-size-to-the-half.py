#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#

# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Time complexity: O(nlogn)
        # Space complexity:O(n)
        counts = collections.Counter(arr)
        counts = [count for number, count in counts.most_common()]
        total_removed = 0
        set_size = 0
        for count in counts:
            total_removed += count
            set_size += 1
            if total_removed >= len(arr) // 2:
                break
        return set_size
# @lc code=end

