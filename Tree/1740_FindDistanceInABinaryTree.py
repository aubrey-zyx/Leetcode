# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        lca = self.find_lca(root, p, q)
        return self.get_depth(lca, p) + self.get_depth(lca, q)

    def find_lca(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        left = self.find_lca(root.left, p, q)
        right = self.find_lca(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def get_depth(self, root, target, depth=0):
        if not root:
            return -1
        if root.val == target:
            return depth
        left_depth = self.get_depth(root.left, target, depth + 1)
        if left_depth != -1:
            return left_depth
        return self.get_depth(root.right, target, depth + 1)


class Solution2:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        lca = self.find_lca(root, p, q)
        queue = deque([lca])
        depth = 0
        distance = 0
        found_p = False
        found_q = False
        while queue and (not found_p or not found_q):
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val == p:
                    found_p = True
                    distance += depth
                if node.val == q:
                    found_q = True
                    distance += depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return distance

    def find_lca(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        left = self.find_lca(root.left, p, q)
        right = self.find_lca(root.right, p, q)
        if left and right:
            return root
        return left if left else right