class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if len(path) == k:
                res.append(path.copy())
                return
            if i > n:
                return
            path.append(i)
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        dfs(1, [])
        return res


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return res