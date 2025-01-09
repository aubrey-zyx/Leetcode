class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True