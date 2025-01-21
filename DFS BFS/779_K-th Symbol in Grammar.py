class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k, root):
            if n == 1:
                return root
            total = 2 ** (n - 1)
            if k > total / 2:
                next_root = 1 if root == 0 else 0
                return dfs(n - 1, k - total / 2, next_root)
            else:
                next_root = 0 if root == 0 else 1
                return dfs(n - 1, k, next_root)

        return dfs(n, k, 0)


class Solution2:
    def kthGrammar(self, n: int, k: int) -> int:
        def recursion(n, k):
            if n == 1:
                return 0
            total = 2 ** (n - 1)
            if k > total // 2:
                return 1 - recursion(n, k - total // 2)
            return recursion(n - 1, k)

        return recursion(n, k)