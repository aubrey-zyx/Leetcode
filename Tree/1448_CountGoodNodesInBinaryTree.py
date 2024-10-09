# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            if not root:
                return 0
            res = 0
            if root.val >= max_val:
                res += 1
                max_val = root.val
            res += dfs(root.left, max_val) + dfs(root.right, max_val)
            return res

        return dfs(root, root.val)


class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                res += 1
                max_val = node.val

            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))

        return res