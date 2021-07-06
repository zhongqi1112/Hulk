#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # https://leetcode.com/problems/symmetric-tree
    # Updated: 07/06/2021

    # Recursive
    # Time complexity: O(n)
    # Space complexity:O(n)
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val \
            and self.isMirror(t1.right, t2.left) \
            and self.isMirror(t1.left, t2.right)


    # Iterative
    # Time complexity: O(n)
    # Space complexity:O(n)
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     q = list()
    #     q.append(root)
    #     q.append(root)
    #     while q:
    #         t1 = q.pop()
    #         t2 = q.pop()
    #         if not t1 and not t2: continue
    #         if not t1 or not t2: return False
    #         if t1.val != t2.val: return False
    #         q.append(t1.left)
    #         q.append(t2.right)
    #         q.append(t1.right)
    #         q.append(t2.left)
    #     return True

# @lc code=end

