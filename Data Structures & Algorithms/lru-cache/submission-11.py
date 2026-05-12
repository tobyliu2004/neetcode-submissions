class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev = prev
        prev.next = nxt

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.next = nxt
        prev.next = nxt.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)