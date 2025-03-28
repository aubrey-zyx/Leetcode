# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            nonlocal root_idx
            if left > right:
                return None
            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            root_idx += 1
            root.left = build(left, inorder_idx[root_val] - 1)
            root.right = build(inorder_idx[root_val] + 1, right)
            return root

        root_idx = 0
        inorder_idx = {}
        for i, val in enumerate(inorder):
            inorder_idx[val] = i
        return build(0, len(preorder) - 1)