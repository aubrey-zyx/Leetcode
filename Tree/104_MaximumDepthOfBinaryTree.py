# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Iterative DFS
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        ans = 0
        while stack:
            node, depth = stack.pop()
            if node:
                ans = max(ans, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return ans

# BFS
class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level