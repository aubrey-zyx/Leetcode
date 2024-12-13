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


class Solution2:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def get_num(s, i):
            positive = True
            if s[i] == "-":
                positive = False
                i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            return num if positive else -num, i

        def dfs(s, i):
            if i == len(s):
                return None, i

            # Calculate the root first
            value, i = get_num(s, i)
            node = TreeNode(value)

            # If any data left, check for the first subtree, which will be the left child
            if i < len(s) and s[i] == "(":
                node.left, i = dfs(s, i + 1)

            # Right child
            if node.left and i < len(s) and s[i] == "(":
                node.right, i = dfs(s, i + 1)

            return node, i + 1 if i < len(s) and s[i] == ")" else i

        return dfs(s, 0)[0]