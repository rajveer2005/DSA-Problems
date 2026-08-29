# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # n = 0
        # temp = head
        # while temp :
        #     n +=1
        #     temp = temp.next
        # temp = head            
        # for i in range(0,n//2):
        #     temp = temp.next
        # return temp

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        