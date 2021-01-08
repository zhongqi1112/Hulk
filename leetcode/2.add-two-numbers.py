#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iteratively add
        time complexity : O(max(m, n))
        space complexity: O(max(m, n))
        """

        """
        # create dummy head and the result will be the next of dummy head
        dummyHead = ListNode()
        # init the current node
        currentNode = dummyHead
        # copy two pointers
        p1 = l1
        p2 = l2
        # init carrying
        carrying = 0
        # repeat steps until both of linkedlists are none
        while p1 is not None or p2 is not None:
            # get the sum of two values
            if p1 is None:
                value = p2.val + carrying
                p2 = p2.next
            elif p2 is None:
                value = p1.val + carrying
                p1 = p1.next
            else:
                value = p1.val + p2.val + carrying
                p1 = p1.next
                p2 = p2.next
            # get carrying
            carrying = 0 if value < 10 else 1
            # update value
            value %= 10
            # update current node
            currentNode.next = ListNode(value)
            currentNode = currentNode.next
        # if we need to add the carrying to result, such as 9 + 9
        if carrying == 1:
            currentNode.next = ListNode(carrying)
        return dummyHead.next
        """

        """
        Recursion
        time complexity : O(min(m, n))
        space complexity: O(min(m, n))
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        value = l1.val + l2.val
        if value < 10:
            currentNode = ListNode(value)
            currentNode.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            currentNode = ListNode(value % 10)
            currentNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
        return currentNode

# @lc code=end

