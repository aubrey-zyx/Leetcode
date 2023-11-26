class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            inorder(root.right)

        self.k = k
        inorder(root)
        return self.res


# Iteratively
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right