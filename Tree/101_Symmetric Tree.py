# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (
                t1.val == t2.val
                and self.isMirror(t1.right, t2.left)
                and self.isMirror(t1.left, t2.right)
        )


# Iterative with queue
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root.left, root.right])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True