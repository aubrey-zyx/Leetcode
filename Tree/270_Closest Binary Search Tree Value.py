# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(root):
            nonlocal nodes
            if not root:
                return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)

        nodes = []
        inorder(root)
        return min(nodes, key=lambda x: abs(target - x))


class Solution2:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        cur = root
        while cur:
            closest = min(closest, cur.val, key=lambda x: (abs(target - x), x))
            if target < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return closest