#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Reverse Second Half In-place
        The only way we can avoid using O(n) extra space is by modifying the input in-place.
        time complexity : O(n)
        space complexity: O(1)
        """
        # if head is empty, it is palindrome
        if head is None:
            return True

        # Find the end of the first half.
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        first_half_end = slow

        # Reverse the second half.
        prev = None
        curr = first_half_end.next
        while curr is not None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        second_half_start = prev

        # Determine whether or not there is a palindrome.
        isPalindrome = True
        first_position = head
        second_position = second_half_start
        while first_position is not None and second_position is not None:
            if first_position.val != second_position.val:
                isPalindrome = False
            first_position = first_position.next
            second_position = second_position.next
        
        # Restore the list. (reverse the second half back)
        prev = None
        curr = second_half_start
        while curr is not None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        first_half_end.next = prev

        # Return the result.
        return isPalindrome
# @lc code=end

