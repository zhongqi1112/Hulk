# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # https://leetcode.com/problems/add-two-numbers/
        # https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
        # Updated: 12/15/2020
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        value = l1.val + l2.val
        if value < 10:
            resultNote = ListNode(value)
            resultNote.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            value -= 10
            resultNote = ListNode(value)
            resultNote.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
        
        return resultNote