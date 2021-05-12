#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursive Approach
        # result = []
        # if root:
        #     result += self.inorderTraversal(root.left)
        #     result.append(root.val)
        #     result += self.inorderTraversal(root.right)
        # return result

        # Iterating method using Stack
        result = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        # while root:
        #     stack.append(root)
        #     root = root.left
        #     while root == None and stack:
        #         temp = stack.pop()
        #         result.append(temp.val)
        #         root = temp.right
        return result

# @lc code=end

