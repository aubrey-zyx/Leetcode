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


# Modified preorder and reverse
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]


# Two stacks
class Solution3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        main_stack, path_stack = [root], []
        res = []
        while main_stack:
            node = main_stack[-1]
            if path_stack and path_stack[-1] == node:
                res.append(node.val)
                main_stack.pop()
                path_stack.pop()
            else:
                path_stack.append(node)
                if node.right:
                    main_stack.append(node.right)
                if node.left:
                    main_stack.append(node.left)
        return res


# One stack
class Solution4:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        prev = None
        res = []
        node = root
        while stack or node:
            # Traverse to the leftmost node
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                # If no right child or the right child was already processed
                if not node.right or node.right == prev:
                    res.append(node.val)
                    stack.pop()
                    prev = node
                    node = None  # Ensure we don't traverse again from this node
                else:
                    node = node.right
        return res