class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


# Use BFS to keep track of each node's parent and depth
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = defaultdict(TreeNode)
        parent[root] = None
        depth = defaultdict(int)
        depth[root] = 0

        queue = deque()
        queue.append((root, 0))

        while queue:
            node, dep = queue.popleft()
            left, right = node.left, node.right
            if left:
                parent[left] = node
                depth[left] = dep + 1
                queue.append((left, dep + 1))
            if right:
                parent[right] = node
                depth[right] = dep + 1
                queue.append((right, dep + 1))

        # Assuming p's depth is larger than q's depth, move p up to the same level as q.
        # Then move p and q up simultaneously.
        p, q = (p, q) if depth[p] >= depth[q] else (q, p)
        for _ in range(abs(depth[p] - depth[q])):
            p = parent[p]
        while p != q:
            p = parent[p]
            q = parent[q]

        return p