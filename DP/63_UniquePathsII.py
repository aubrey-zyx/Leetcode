class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if not obstacleGrid[r][c]:
                    if r == c == 0:
                        dp[r][c] = 1
                    else:
                        left = dp[r][c - 1] if c > 0 else 0
                        up = dp[r - 1][c] if r > 0 else 0
                        dp[r][c] = left + up
        return dp[-1][-1]


# Scrolling array
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 0 if obstacleGrid[0][0] else 1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c - 1]
        return dp[-1]