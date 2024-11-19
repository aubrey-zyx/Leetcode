# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        num = ''
        stack = []

        for c in s:
            if c.isdigit() or c == '-':
                num += c
            elif c == '(':
                if num:
                    node = TreeNode(int(num))
                    num = ''
                    stack.append(node)
            elif c == ')':
                node = TreeNode(int(num)) if num else stack.pop()
                num = ''
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

        return stack[-1] if stack else TreeNode(int(num))