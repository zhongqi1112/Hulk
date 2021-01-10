#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # empty string is valid palindrome
        if len(s) == 0:
            return True
        # filter alphanumerica and convert to lowercase
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_chars = map(lambda ch: ch.lower(), filtered_chars)
        # convert char to list
        str_list = list(lowercase_chars)
        # determine whether or not there is a palindrome
        return str_list == str_list[::-1]

# @lc code=end

