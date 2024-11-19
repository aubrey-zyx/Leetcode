# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        null_node = False
        while queue:
            node = queue.popleft()
            if not node:
                null_node = True
            else:
                if null_node:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True


# DFS
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def count_nodes(root):
            if not root:
                return 0
            return 1 + count_nodes(root.left) + count_nodes(root.right)

        def dfs(node, i, n):
            if not node:
                return True
            if i >= n:
                return False
            return dfs(node.left, 2 * i + 1, n) and dfs(node.right, 2 * i + 2, n)

        return dfs(root, 0, count_nodes(root))