class ListNode:
    def __init__(self, key = 0, value = 0):
        self.val = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.right.prev = self.left
        self.left.next = self.right

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        node = ListNode(key, value)
        self.add(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
