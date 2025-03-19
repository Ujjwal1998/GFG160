class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, cap):
        # code here
        self.cap = cap
        self.mp = {}
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def _insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # Function to return value corresponding to the key.
    def get(self, key):
        # code here
        if key in self.mp:
            node = self.mp[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    # Function for storing key-value pair.
    def put(self, key, value):
        # code here
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            newNode = DLLNode(key, value)
            if len(self.mp) >= self.cap:
                last = self.tail.prev
                self._remove(last)
                del self.mp[last.key]
            self._insert(newNode)
            self.mp[key] = newNode
