class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]


# Scrolling array
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[n - 1]