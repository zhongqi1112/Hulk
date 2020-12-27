class Solution:
    def isPalindrome(self, s: str) -> bool:
        # https://leetcode.com/problems/valid-palindrome/
        # Updated: 12/24/2020
        
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list