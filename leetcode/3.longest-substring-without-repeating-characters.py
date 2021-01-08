#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longestLength = 0
        i = 0
        seen = dict()
        for j in range(len(s)):
            if s[j] in seen:
                # starting position will be the first repeat index + 1
                if j - i > longestLength:
                    longestLength = j - i
                i = seen[s[j]] + 1
                seen.pop(s[j])
                seen[s[j]] = j
            else:
                # add item to seen
                seen[s[j]] = j
        if longestLength == 0:
            longestLength = len(s)
        return longestLength
# @lc code=end

