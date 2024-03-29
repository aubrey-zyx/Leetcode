class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(root):
            if not root:
                return None
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)

        postorder(root)
        return ans