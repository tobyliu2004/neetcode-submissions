# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        head2 = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = head2
            head2 = curr
            curr = temp
        
        first = head
        second = head2
        while second:
            next1 = first.next
            next2 = second.next
            first.next = second
            second.next = next1
            first = next1
            second = next2
