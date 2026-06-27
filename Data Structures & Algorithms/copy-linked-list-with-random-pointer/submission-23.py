"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        same = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, cur.random)
            same[cur] = copy
            cur = cur.next
        
        curr = head
        while curr:
            copy = same[curr]
            copy.next = same[curr.next]
            copy.random = same[curr.random]
            curr = curr.next
        return same[head]