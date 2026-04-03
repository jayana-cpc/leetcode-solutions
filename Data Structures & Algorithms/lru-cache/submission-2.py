class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        lru = self.tail.prev
        lru.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = lru

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = node
        self.insert(node)

        if len(self.hm) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.hm[node.key]
        
