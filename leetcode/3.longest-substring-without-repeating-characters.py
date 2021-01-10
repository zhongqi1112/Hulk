#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window optimized
        time complexity : O(n)
        space complexity: O(min(n, m))
        We need O(k) space for the sliding window, where k is the size of the Set.
        The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m. 
        """
        # init the longest length
        longestLength = 0
        # create left pointer of the window
        i = 0
        # create sliding window
        window = dict()
        # traverse the string until right pointer to the end of string
        for j in range(len(s)):
            # if the current item is in the window, update the left pointer
            if s[j] in window:
                i = max(window[s[j]], i)
            # update longest length
            longestLength = max(longestLength, j - i + 1)
            # add next index of current item to the window
            window[s[j]] = j + 1
        return longestLength
# @lc code=end

