"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        pre, cur = head, head.next
        insert = False
        while True:
            if pre.val <= insertVal <= cur.val:
                # Case 1: insertVal sits between the minimal and maximal values
                insert = True
            elif pre.val > cur.val:
                # Case 2: insertVal goes beyond the minimal and maximal values
                if insertVal >= pre.val or insertVal <= cur.val:
                    insert = True

            if insert:
                pre.next = Node(insertVal, cur)
                return head

            pre, cur = cur, cur.next
            if pre == head:
                break

        # Case 3: the list contains uniform values
        pre.next = Node(insertVal, cur)
        return head