class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.buckets = [Bucket() for _ in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].insert(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].delete(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.buckets[idx].exists(key)


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def exists(self, value):
        cur = self.head.next
        while cur:
            if cur.val == value:
                return True
            cur = cur.next
        return False

    def insert(self, value):
        if self.exists(value):
            return
        node = Node(value, self.head.next)
        self.head.next = node

    def delete(self, value):
        pre, cur = self.head, self.head.next
        while cur:
            if cur.val == value:
                pre.next = cur.next
                return
            pre, cur = cur, cur.next

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)