#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        # Recursion
        # Time complexity: O(n)
        # Space complexity: O(n)
        if not root: return ""
        if not root.left and not root.right: return str(root.val)
        if not root.right: return str(root.val) + "(" + self.tree2str(root.left) + ")"
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" \
            + self.tree2str(root.right) + ")"
# @lc code=end

