#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Time complexity: O(N)
        # Space complexity:O(n)
        if not root: return []
        rightside = []
        curr_level = []
        next_level = [root]
        while next_level:
            curr_level = next_level
            next_level = []
            while curr_level:
                node = curr_level.pop(0)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            rightside.append(node.val)
        return rightside
        
# @lc code=end

