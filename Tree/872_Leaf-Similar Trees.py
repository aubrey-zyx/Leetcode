# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preorder(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            preorder(root.left, leaves)
            preorder(root.right, leaves)
        
        leaves1, leaves2 = [], []
        preorder(root1, leaves1)
        preorder(root2, leaves2)
        return leaves1 == leaves2