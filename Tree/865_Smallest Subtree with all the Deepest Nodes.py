# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = {None: -1}

        def dfs_depth(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs_depth(node.left, node)
                dfs_depth(node.right, node)

        dfs_depth(root)

        max_depth = max(depth.values())

        def dfs_lca(node):
            if not node or depth.get(node, None) == max_depth:
                return node
            left = dfs_lca(node.left)
            right = dfs_lca(node.right)
            if left and right:
                return node
            return left if left else right

        return dfs_lca(root)


class Solution2:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            depth_l, lca_l = dfs(node.left)
            depth_r, lca_r = dfs(node.right)
            if depth_l > depth_r:
                return depth_l + 1, lca_l
            if depth_r > depth_l:
                return depth_r + 1, lca_r
            return depth_l + 1, node
        return dfs(root)[1]