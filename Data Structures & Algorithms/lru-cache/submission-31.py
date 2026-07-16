class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.post = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.post = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.post, nxt.prev = node, node
        node.post, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.post
        prev.post = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        temp = Node(key, value)
        self.cache[key] = temp
        self.insert(temp)
        if len(self.cache) > self.cap:
            lru = self.left.post
            self.remove(lru)
            del self.cache[lru.key]
