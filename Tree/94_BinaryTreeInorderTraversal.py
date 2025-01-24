# Recursively
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(root):
            nonlocal ans
            if not root:
                return None
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        return ans


# Iteratively
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans