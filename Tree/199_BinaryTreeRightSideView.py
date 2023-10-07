class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightmost = None
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost.val)

        return res