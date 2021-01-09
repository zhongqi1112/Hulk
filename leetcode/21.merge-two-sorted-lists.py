#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        two pointers traverse two linkedlists to compare value
        time complexity : O(min(m, n))
        space complexity: O(m + n)
        """
        # create dummy head and the result will be the next of dummy head
        dummyHead = ListNode()
        # init the current node
        currentNode = dummyHead
        # create two pointers
        p1 = l1
        p2 = l2
        # repeat steps until one of linkedlists is none
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                currentNode.next = ListNode(p1.val)
                p1 = p1.next
            else:
                currentNode.next = ListNode(p2.val)
                p2 = p2.next
            currentNode = currentNode.next
        if p1 is None:
            currentNode.next = p2
        if p2 is None:
            currentNode.next = p1
        return dummyHead.next

        """
        Recursion
        """

        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        """

# @lc code=end

