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
        if not head:
            return
        d = dict()
        node = head
        while node:
            d[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            if node.next:
                d[node].next = d[node.next]
            if node.random:
                d[node].random = d[node.random]
            node = node.next
        return d[head]


class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        # Create new nodes after every node
        node = head
        while node:
            new_node = Node(node.val, node.next, None)
            node.next = new_node
            node = new_node.next

        # Set new nodes' random
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # Separate two lists
        node = head
        dummy = Node(-1, None, None)
        cur = dummy
        while node:
            cur.next = node.next
            cur = cur.next
            node.next = cur.next
            node = node.next

        return dummy.next