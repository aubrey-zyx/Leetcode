class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        def dfs(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            for j in range(i, n):
                if dp[i][j]:
                    cur.append(s[i: j + 1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res