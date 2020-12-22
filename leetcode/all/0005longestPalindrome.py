class Solution:
    def longestPalindrome(self, s: str) -> str:
        # https://leetcode.com/problems/longest-palindromic-substring/solution/
        # Updated: 12/17/2020
        
        if len(s) <= 1:
            return s
        
        start = end = 0
        for i in range(len(s)):
            max_len_1 = self.expandAroundCenter(s, i, i + 1)
            max_len_2 = self.expandAroundCenter(s, i, i)
            max_len = max(max_len_1, max_len_2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end+1]
        
    def expandAroundCenter(self, s: 'list', left: 'int', right: 'int') -> 'int':
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    # Input:
    s = "babad"
    # Output: "bab"
    # Note: "aba" is also a valid answer.
    result = Solution().longestPalindrome(s)
    print(result)
