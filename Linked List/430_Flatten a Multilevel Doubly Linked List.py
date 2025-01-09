"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        stack = []
        while node:
            if node.child:
                if node.next:
                    stack.append(node.next)
                node.child.prev = node
                node.next = node.child
                node.child = None
            elif not node.next and stack:
                node.next = stack.pop()
                node.next.prev = node
            node = node.next
        return head


class Solution2:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            if cur.child:
                nxt = cur.next
                child = cur.child

                cur.next = child
                child.prev = cur
                cur.child = None

                while child.next:
                    child = child.next
                if nxt:
                    child.next = nxt
                    nxt.prev = child
            cur = cur.next
        return head