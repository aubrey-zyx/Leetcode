"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set()
        for node in tree:
            for child in node.children:
                seen.add(child.val)
        for node in tree:
            if node.val not in seen:
                return node


class Solution2:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total = 0
        for node in tree:
            total += node.val
            for child in node.children:
                total -= child.val
        for node in tree:
            if node.val == total:
                return node