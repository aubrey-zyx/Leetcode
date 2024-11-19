# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def add_leaves(root):
            nonlocal res
            if not root.left and not root.right:
                res.append(root.val)
            else:
                if root.left:
                    add_leaves(root.left)
                if root.right:
                    add_leaves(root.right)

        if not root:
            return []
        res = []
        if root.left or root.right:
            res.append(root.val)

        # left boundry
        cur = root.left
        while cur:
            if cur.left or cur.right:
                res.append(cur.val)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right

        # leaves
        add_leaves(root)

        # right boundry
        cur = root.right
        stack = []
        while cur:
            if cur.left or cur.right:
                stack.append(cur.val)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        res.extend(stack[::-1])

        return res


class Solution2:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left, leaves, right = [], [], []

        def is_leaf(node):
            return not node.left and not node.right

        def is_root(flag):
            return flag == 0

        def is_left_boundary(flag):
            return flag == 1

        def is_right_boundary(flag):
            return flag == 2

        def left_child_flag(node, flag):
            if is_left_boundary(flag) or is_root(flag):
                return 1
            elif is_right_boundary(flag) and not node.right:
                return 2
            else:
                return 3

        def right_child_flag(node, flag):
            if is_right_boundary(flag) or is_root(flag):
                return 2
            elif is_left_boundary(flag) and not node.left:
                return 1
            else:
                return 3

        def preorder(node, flag):
            nonlocal left, leaves, right
            if not node:
                return []
            if is_leaf(node):
                leaves.append(node.val)
            elif is_left_boundary(flag) or is_root(flag):
                left.append(node.val)
            elif is_right_boundary(flag):
                right.append(node.val)
            preorder(node.left, left_child_flag(node, flag))
            preorder(node.right, right_child_flag(node, flag))

        preorder(root, 0)
        return left + leaves + right[::-1]