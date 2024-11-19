"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = tail = None

        def inorder(node):
            nonlocal head, tail
            if not node:
                return

            inorder(node.left)

            if tail:
                node.left = tail
                tail.right = node
            else:
                head = node
            tail = node

            inorder(node.right)

        if not root:
            return None
        inorder(root)
        head.left = tail
        tail.right = head
        return head