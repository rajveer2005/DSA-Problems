# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Fix the current connection
        front = head.next          # The node that comes after current
        front.next = head          # Make it point back to current
        head.next = None           # Remove current's forward connection
        
        return new_head
        