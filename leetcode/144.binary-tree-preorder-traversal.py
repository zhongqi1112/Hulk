#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursive Approach
        # result = []
        # if root:
        #     result.append(root.val)
        #     result += self.preorderTraversal(root.left)
        #     result += self.preorderTraversal(root.right)
        # return result

        # Iterating method using Stack
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return result

# @lc code=end

