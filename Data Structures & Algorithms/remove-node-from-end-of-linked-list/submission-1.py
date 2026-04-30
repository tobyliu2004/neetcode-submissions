# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # advance right n steps
        for i in range(n):
            right = right.next
        
        # move both until right hits the end
        while right:
            left = left.next
            right = right.next
        
        # left is now just before the node to remove
        left.next = left.next.next
        
        return dummy.next
