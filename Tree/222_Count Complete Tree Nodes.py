# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, root):
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d

    def exists(self, idx, d, root):
        l, r = 0, 2 ** d - 1
        for _ in range(d):
            m = l + (r - l) // 2
            if idx <= m:
                root = root.left
                r = m
            else:
                root = root.right
                l = m + 1
        return root is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = self.get_depth(root)
        if d == 0:
            return 1
        l, r = 1, 2 ** d - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.exists(m, d, root):
                l = m + 1
            else:
                r = m - 1
        return (2 ** d - 1) + l