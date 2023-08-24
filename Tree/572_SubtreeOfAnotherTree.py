class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same_tree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)
        return False