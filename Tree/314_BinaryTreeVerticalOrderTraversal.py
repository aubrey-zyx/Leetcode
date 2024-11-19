# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_nodes = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            if node:
                column_nodes[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [column_nodes[c] for c in range(min_col, max_col + 1)]


# DFS
class Solution2:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_nodes = defaultdict(list)
        min_col = max_col = 0

        def dfs(node, row, col):
            if node:
                nonlocal min_col, max_col
                column_nodes[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []
        for c in range(min_col, max_col + 1):
            column_nodes[c].sort(key=lambda x: x[0])
            res.append([val for row, val in column_nodes[c]])
        return res