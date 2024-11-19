# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs_find_parent(node: TreeNode) -> None:
            if not node:
                return
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            dfs_find_parent(node.left)
            dfs_find_parent(node.right)

        dfs_find_parent(root)

        visited = set()
        visited.add(target)
        q = collections.deque()
        q.append(target)
        while k > 0 and q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in [parent.get(u, None), u.left, u.right]:
                    if v and v not in visited:
                        q.append(v)
                        visited.add(v)
            k -= 1

        res = [node.val for node in q]
        return res



class Solution2:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        res = []
        visited = set()

        def find_parent(node, parent):
            if node:
                parents[node] = parent
                find_parent(node.left, node)
                find_parent(node.right, node)

        def dfs(node, distance):
            if not node or node in visited:
                return
            visited.add(node)
            if distance == 0:
                res.append(node.val)
                return
            dfs(parents[node], distance - 1)
            dfs(node.left, distance - 1)
            dfs(node.right, distance - 1)

        find_parent(root, None)
        dfs(target, k)
        return res