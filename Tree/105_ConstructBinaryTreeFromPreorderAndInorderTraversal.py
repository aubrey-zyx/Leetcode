# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        root_idx = 0

        def build(l, r):
            nonlocal root_idx
            if l > r:
                return None
            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            root_idx += 1
            root.left = build(l, inorder_idx[root_val] - 1)
            root.right = build(inorder_idx[root_val] + 1, r)
            return root

        return build(0, len(preorder) - 1)


# Iterative
class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0

        for i in range(1, len(preorder)):
            pre_val = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorder_idx]:
                node.left = TreeNode(pre_val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx += 1
                node.right = TreeNode(pre_val)
                stack.append(node.right)

        return root