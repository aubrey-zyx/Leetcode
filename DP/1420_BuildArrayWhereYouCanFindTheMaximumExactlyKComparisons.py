class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0

        dp = [[[0] * (m + 1) for _ in range(k + 1)] for __ in range(n + 1)]
        mod = 10 ** 9 + 7

        for c in range(1, m + 1):
            dp[1][1][c] = 1
        for a in range(2, n + 1):
            for b in range(1, min(k, a) + 1):
                for c in range(1, m + 1):
                    dp[a][b][c] = dp[a - 1][b][c] * c
                    for cc in range(1, c):
                        dp[a][b][c] += dp[a - 1][b - 1][cc]
                    dp[a][b][c] %= mod

        return sum(dp[n][k][c] for c in range(1, m + 1)) % mod