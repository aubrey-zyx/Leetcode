# BFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []

        queue = deque([(root, None, 0)])
        while queue:
            node, parent, depth = queue.popleft()
            if node.val == x or node.val == y:
                res.append((parent, depth))
                if len(res) == 2:
                    break
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        node_x, node_y = res
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]


# DFS
class Solution2:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []

        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((parent, depth))
                if len(res) == 2:
                    return
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        node_x, node_y = res
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]