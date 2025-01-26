class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


# Space Optimization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)

        prev = [0] * (n + 1)
        for i in reversed(range(m)):
            cur = [0] * (n + 1)
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    cur[j] = prev[j + 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j + 1])
            prev = cur
        return prev[0]