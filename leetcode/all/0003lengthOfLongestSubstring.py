class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # https://leetcode.com/problems/longest-substring-without-repeating-characters/
        # Updated: 12/16/2020
        
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}
        
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j-i+1)
            mp[s[j]] = j + 1
        
        return ans
        