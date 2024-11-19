# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q):
            if not node or node == p or node == q:
                return node
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        def dfs(node, target):
            if node == target:
                return True
            if not node:
                return False
            return dfs(node.left, target) or dfs(node.right, target)

        res = lca(root, p, q)
        if res == p:
            return p if dfs(p, q) else None
        elif res == q:
            return q if dfs(q, p) else None
        return res