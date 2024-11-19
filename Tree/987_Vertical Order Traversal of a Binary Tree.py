# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ht = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            if node:
                ht[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        res = []
        for c in range(min_col, max_col + 1):
            res.append([v for r, v in sorted(ht[c])])
        return res


class Solution2:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ht = defaultdict(list)
        min_col = max_col = 0

        def dfs(node, row, col):
            if node:
                nonlocal min_col, max_col
                ht[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []
        for c in range(min_col, max_col + 1):
            res.append([v for r, v in sorted(ht[c])])
        return res