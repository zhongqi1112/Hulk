#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Recursive
        # Time complexity: O(n)
        # Space complexity: O(h)
        # if not root: return None
        # right = self.invertTree(root.right)
        # left = self.invertTree(root.left)
        # root.left = right
        # root.right = left
        # return root


        # Iterative
        # Time complexity: O(n)
        # Space complexity: O(n)
        if not root: return None
        q = list()
        q.append(root)
        while q:
            current = q.pop()
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left: q.append(current.left)
            if current.right: q.append(current.right)
        return root


# @lc code=end

