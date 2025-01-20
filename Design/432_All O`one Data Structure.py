class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)

            nxt = node.next
            if nxt == self.tail or nxt.freq != freq + 1:
                new = Node(freq + 1)
                new.keys.add(key)
                new.prev, new.next = node, nxt
                node.next = nxt.prev = new
                self.map[key] = new
            else:
                nxt.keys.add(key)
                self.map[key] = nxt

            if not node.keys:
                self.remove(node)
        else:
            first = self.head.next
            if first == self.tail or first.freq > 1:
                new = Node(1)
                new.keys.add(key)
                new.prev, new.next = self.head, first
                self.head.next = first.prev = new
                self.map[key] = new
            else:
                first.keys.add(key)
                self.map[key] = first

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            del self.map[key]
        else:
            pre = node.prev
            if pre == self.head or pre.freq != freq - 1:
                new = Node(freq - 1)
                new.keys.add(key)
                new.prev, new.next = pre, node
                pre.next = node.prev = new
                self.map[key] = new
            else:
                pre.keys.add(key)
                self.map[key] = pre

        if not node.keys:
            self.remove(node)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()