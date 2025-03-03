class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder_list = []

        def preorder(root):
            if root:
                preorder_list.append(root)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        for i in range(1, len(preorder_list)):
            prev, cur = preorder_list[i - 1], preorder_list[i]
            prev.left = None
            prev.right = cur


class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def recursion(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            left_tail = recursion(node.left)
            right_tail = recursion(node.right)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            return right_tail if right_tail else left_tail

        recursion(root)


class Solution3:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                rightmost = root.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = root.right
                root.right = root.left
                root.left = None
            root = root.right