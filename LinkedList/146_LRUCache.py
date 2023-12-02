class DListNode:
    def __init__(self, key=0, value=0):
        self.key, self.val = key, value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # map key to node
        self.capacity = capacity
        # left = LRU, right = Most Recently Used
        self.left, self.right = DListNode(), DListNode()
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # insert node at right
    def insert(self, node):
        pre, nxt = self.right.prev, self.right
        pre.next = nxt.prev = node
        node.prev, node.next = pre, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            # remove from list and delete the LRU from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# OrderedDict
class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.cap:
            self.popitem(last=False)


# Just use dict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1:
            self.cache.pop(key)
            self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            first_key = next(iter(self.cache))
            self.cache.pop(first_key)