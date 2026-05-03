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
            fast = fast.next.next
            slow = slow.next

        second_list = slow.next
        slow.next = None

        curr = second_list
        head2 = None
        while curr:
            temp = curr.next
            curr.next = head2
            head2 = curr
            curr = temp
        
        first = head
        second = head2

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return 