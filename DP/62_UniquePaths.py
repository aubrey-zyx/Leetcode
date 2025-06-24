class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        return dp[-1][-1]


# Scrolling array
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[n - 1]