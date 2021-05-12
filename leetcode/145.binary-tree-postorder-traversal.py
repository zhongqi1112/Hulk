#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursive Approach
        # result = []
        # if root:
        #     result += self.postorderTraversal(root.left)
        #     result += self.postorderTraversal(root.right)
        #     result.append(root.val)
        # return result

        # Iterating method using Stack
        if not root:
            return []
        result = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    # For post-order traversal, need to first visit left then right before node is "done", so add them in reverse order to the stack.
                    # By changing the order here we could achieve pre- or in-order as well.
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result 

# @lc code=end

