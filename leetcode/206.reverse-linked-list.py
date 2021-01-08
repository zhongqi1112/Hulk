#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Iteratively reversed linkedlist
        time complexity : O(n)
        space complexity: O(1) 
        """
        # init previous and currrent node
        prev = None
        curr = head
        while curr is not None:
            # save next node to template
            nextTemp = curr.next
            # next pointer point to previous node
            curr.next = prev
            # update current node to previous node
            prev = curr
            # update next temp node to current node
            curr = nextTemp
        # when we reach out to the end, curr is None, previous is the head
        return prev
# @lc code=end

