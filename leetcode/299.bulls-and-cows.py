#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # HashMap: Two Passes
        # Time complexity: O(n)
        # Space complexity:O(1)
        h = Counter(secret)
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch == secret[idx]:
                bulls += 1
                cows -= int(h[ch] <= 0)
            else:
                cows += int(h[ch] > 0)
            h[ch] -= 1
        return "{}A{}B".format(bulls, cows)
# @lc code=end

