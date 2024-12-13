# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)
        res = cur = TreeNode()
        for v in vals:
            cur.right = TreeNode(v)
            cur = cur.right
        return res.right


class Solution2:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            nonlocal cur
            if not node:
                return
            inorder(node.left)
            node.left = None
            cur.right = node
            cur = node
            inorder(node.right)

        res = cur = TreeNode()
        inorder(root)
        return res.right