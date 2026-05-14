# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        for i in range(n):
            curr = curr.next

        track = dummy
        while curr.next:
            track = track.next
            curr = curr.next
        track.next = track.next.next
        return dummy.next