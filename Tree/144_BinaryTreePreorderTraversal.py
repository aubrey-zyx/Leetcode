class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(root):
            if not root:
                return None
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ans